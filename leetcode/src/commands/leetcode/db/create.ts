import {CliUx, Command} from '@oclif/core'
import {Question, QuestionNode} from "../../../lib/types";
import {DB} from "../../../lib/db";
import {leetcodeCurl} from "../../../lib/leetcodeCurl";
import * as pLimit from 'p-limit';
import {Op} from "sequelize";


export default class LeetcodeDbCreate extends Command {
  static description = 'describe the command here'

  static examples = [
    '<%= config.bin %> <%= command.id %>',
  ]

  static flags = {
    // flag with a value (-n, --name=VALUE)
    // name: Flags.string({char: 'n', description: 'name to print'}),
    // flag with no value (-f, --force)
    // force: Flags.boolean({char: 'f'}),
  }

  // static args = [{name: 'file'}]

  async run() {
    const leetcode = (await leetcodeCurl());
    const db = new DB();
    let dbTotal = 0;
    try {
      dbTotal = await db.Question.count();
    } catch (e) {

    }
    CliUx.ux.log('Getting all leetcode problem')
    CliUx.ux.action.start('Getting 1st leetcode problem set');
    // is there a way to avoid getting the first problem so have the total?
    const problemSetQuestionList = leetcode.getProblemSetQuestionList().data.problemsetQuestionList;
    CliUx.ux.action.stop('Done');
    const total = Math.ceil(problemSetQuestionList.total / 50);
    if (dbTotal < problemSetQuestionList.total) {
      CliUx.ux.action.start('Getting the rest of the leetcode problem set');
      const res = <Array<Array<Question>>>await Promise.all([...Array(total).keys()].map(i => Promise.resolve(leetcode.getProblemSetQuestionList(i + 2).data.problemsetQuestionList.questions)))
      CliUx.ux.action.stop('Done');
      problemSetQuestionList.questions = problemSetQuestionList.questions.concat(res.flat());
      // adds all problems to the db along with their tags
      await db.insertBaseQuestionIntoDB(problemSetQuestionList);
    }
    // now get all problem details
    await db.createDB();
    let foundQuestionNodes = [];
    try {
      foundQuestionNodes = (await db.QuestionNode.findAll()).map((n:any)=>(<QuestionNode>n.dataValues).questionId);
    } catch (e) {
      console.debug(e);
    }
    const limit = pLimit(10); // 5 works // 10 untested (the issue is how many will leetcode let me get concurrently)
    const questions = await db.Question.findAll({where: {frontendQuestionId: {[Op.notIn]: foundQuestionNodes}}});
    const allQuestionPromises = questions.map((d: { dataValues: Question; }) => limit(async () => {
      const q = leetcode.getProblem(d.dataValues.titleSlug);
      try {
        await db.insertProblemNodeIntoDB(q.data.question);
      } catch (e) {
        return e;
      }
      return q;
    }));
    await Promise.all(allQuestionPromises);
    // console.log();
  }
}

