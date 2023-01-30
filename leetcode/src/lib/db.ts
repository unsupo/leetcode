import {DataTypes, Sequelize} from "sequelize";
import {ProblemsetQuestionList, Question, QuestionNode} from "./types";

export class DB {
  sequelize: Sequelize;
  QuestionTopicTag: any;
  Question: any;
  TopicTag: any;
  QuestionNode: any;
  private isSynced: boolean = false;


  constructor(/*props could be sequilize props*/) {
    this.sequelize = new Sequelize({
      dialect: "sqlite",
      storage: "leetcode.sqlite"
    });
    this.createModels();
  }
  private createModels(){
    const Question = this.sequelize.define('Question', {
      acRate: DataTypes.NUMBER,
      difficulty: DataTypes.STRING,
      freqBar: DataTypes.STRING,
      frontendQuestionId: {
        type: DataTypes.STRING,
        primaryKey: true,
      },
      isFavor: DataTypes.BOOLEAN,
      paidOnly: DataTypes.BOOLEAN,
      status: DataTypes.STRING,
      title: {
        type: DataTypes.STRING,
        unique: 'compositeIndex'
      },
      titleSlug: {
        type: DataTypes.STRING,
        unique: 'compositeIndex'
      },
      // topicTags: Array < TopicTag >,
      hasSolution: DataTypes.STRING,
      hasVideoSolution: DataTypes.STRING
    });
    const QuestionNode = this.sequelize.define('QuestionNode', {
      // "questionId": "237", // are these ever with questionFrontendId not the same? // autogen
      "questionFrontendId": { // TODO add this back
        type: DataTypes.STRING,
        unique: 'compositeIndex'
      }, // this will be set when the relationship is set below
      "boundTopicId": DataTypes.STRING,
      // "title": "Delete Node in a Linked List", // same as in questionId
      // "titleSlug": "delete-node-in-a-linked-list",// same as in questionId
      "content": DataTypes.STRING,
      "translatedTitle": DataTypes.STRING,
      "translatedContent": DataTypes.STRING,
      // "isPaidOnly": DataTypes.BOOLEAN,// same as in questionId (paidOnly) // TODO can i remove these dupe props in the query from curl?
      "canSeeQuestion": DataTypes.BOOLEAN,
      // "difficulty": "Medium", // same as in questionId
      "likes": DataTypes.NUMBER,
      "dislikes": DataTypes.NUMBER,
      "isLiked": DataTypes.BOOLEAN,
      // TODO convert these string objects to relationships (ie a SimilarQuestions Table which this slug and all of these slugs are defined)  (low priority)
      "similarQuestions": DataTypes.STRING,
      // this is the important stuff
      "exampleTestcases": DataTypes.STRING,
      "categoryTitle": DataTypes.STRING,
      // TODO this should be a relationship to a contributors table (empty usually so not a priority)
      "contributors": DataTypes.STRING,
      // "topicTags": Array<TopicTag>, // this can obtained from the the questions relationship
      "companyTagStats": DataTypes.STRING,
      // this is the important stuff
      // TODO this should be a relationship to a code snippets table instead i'll just have it has a json string (not much to sort by here so not huge priority)
      "codeSnippets": DataTypes.STRING,
      // TODO this should be a relationship to a stats table (low priority)
      "stats": DataTypes.STRING,
      // TODO this should be a relationship to a hints table (empty usually so not a priority)
      "hints": DataTypes.STRING,
      // TODO this should be a relationship to a solutions table (more sortable so might be higher priorty)
      "solution": DataTypes.STRING,
      "status": DataTypes.STRING,
      // this is the important stuff
      "sampleTestCase": DataTypes.STRING,
      // TODO this should be a relationship to a metaData table (low priority)
      "metaData": DataTypes.STRING,
      "judgerAvailable": DataTypes.BOOLEAN,
      "judgeType": DataTypes.STRING,
      // TODO this should be a relationship to a mysqlSchemas table (empty usually so not a priority)
      "mysqlSchemas": DataTypes.STRING,
      "enableRunCode": DataTypes.BOOLEAN,
      "enableTestMode": DataTypes.BOOLEAN,
      "enableDebugger": DataTypes.BOOLEAN,
      // TODO this should be a relationship to a envInfo table (this is probably the same)
      "envInfo": DataTypes.STRING,
      "libraryUrl": DataTypes.STRING,
      "adminUrl": DataTypes.STRING,
      // TODO this should be a relationship to a challengeQuestion table
      "challengeQuestion": DataTypes.STRING,
      // "__typename": "QuestionNode"
    });
    const TopicTag = this.sequelize.define('TopicTag', {
      name: DataTypes.STRING,
      id: {
        type: DataTypes.STRING,
        primaryKey: true,
      },
      slug: DataTypes.STRING,
    });
    const QuestionTopicTag = this.sequelize.define('QuestionTopicTag', {});
    Question.hasOne(QuestionNode, {foreignKey: 'questionId'});
    Question.belongsToMany(TopicTag, {through: QuestionTopicTag});
    TopicTag.belongsToMany(Question, {through: QuestionTopicTag});
    QuestionTopicTag.belongsTo(TopicTag);
    QuestionTopicTag.belongsTo(Question);
    Question.hasMany(QuestionTopicTag);
    TopicTag.hasMany(QuestionTopicTag);
    this.QuestionTopicTag = QuestionTopicTag;
    this.Question = Question;
    this.TopicTag = TopicTag;
    this.QuestionNode = QuestionNode;
  }

  public async createDB() {
    if(this.isSynced)
      return;
    this.createModels();
    try {
      await this.sequelize.sync();
      this.isSynced = true;
    } catch (e) {
      console.log(e);
    }
  }

  async insertBaseQuestionIntoDB(problemSetQuestionList: ProblemsetQuestionList) {
    await this.createDB();
    try {
      const allQuestions = problemSetQuestionList.questions.map((q: any) => {
        return {...q}
      });
      const unique = [...new Map(allQuestions.map(item => [item.titleSlug, item])).values()];
      await this.Question.bulkCreate(unique, {include: [this.TopicTag]});
    } catch (e) {
      console.debug(e);
    }
    try {
      const allTopics = problemSetQuestionList.questions.map(q => q.topicTags.map(t => {
        return {...t}
      })).flat();
      const unique = [...new Map(allTopics.map(item => [item.id, item])).values()];
      await this.TopicTag.bulkCreate(unique);
    } catch (e) {
      console.debug(e);
    }
    try {
      await this.Question.sync();
      await this.TopicTag.sync();
      const questiontopics = problemSetQuestionList.questions.map(q =>
        q.topicTags.map(t => {
          return {QuestionFrontendQuestionId: q.frontendQuestionId, TopicTagId: t.id}
        })
      ).flat();
      const unique = [...new Map(questiontopics.map(item => [item.QuestionFrontendQuestionId + item.TopicTagId, item])).values()];
      await this.QuestionTopicTag.bulkCreate(unique);
    } catch (e) {
      console.debug(e);
    }
  }
  async insertProblemNodeIntoDB(question: QuestionNode){
    await this.createDB();
    const obj = {...question};
    // @ts-ignore
    obj['contributors'] = JSON.stringify(question.contributors);
    // @ts-ignore
    obj['codeSnippets'] = JSON.stringify(question.codeSnippets);
    // @ts-ignore
    obj['hints'] = JSON.stringify(question.hints);
    // @ts-ignore
    obj['solution'] = JSON.stringify(question.solution);
    // @ts-ignore
    obj['mysqlSchemas'] = JSON.stringify(question.mysqlSchemas);
    // @ts-ignore
    obj['challengeQuestion'] = JSON.stringify(question.challengeQuestion);
    obj['questionId'] = question.questionFrontendId;
    try {
      await this.QuestionNode.create(obj);
    } catch (e) {
      console.log(e);
    }
  }
}
