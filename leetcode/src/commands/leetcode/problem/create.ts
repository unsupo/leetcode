import {CliUx, Command, Flags} from '@oclif/core'
import {shell} from "../../../lib/fsUtils";
import {DB} from "../../../lib/db";
import {CodeSnippetNode, Question, QuestionNode, TopicTag} from "../../../lib/types";
import {Op} from "sequelize";
import { NodeHtmlMarkdown } from 'node-html-markdown'
import * as fs from "fs";


export default class LeetcodeProblemCreate extends Command {
  static description = 'describe the command here'

  static examples = [
    '<%= config.bin %> <%= command.id %>',
  ]

  // static flags = {
  //   // flag with a value (-n, --name=VALUE)
  //   name: Flags.string({char: 'n', description: 'name to print'}),
  //   // flag with no value (-f, --force)
  //   force: Flags.boolean({char: 'f'}),
  // }
  //
  // static args = [{name: 'file'}]

  /**
   * Create a leetcode problem
   * if no params set, use the db to create the next javascript problem with the highest acceptance
   * if the db doesn't exist or there are no more problems in the db attempt to use curl to find a
   *    problem from the site if still no problems then halt
   * params can be:
   *    db          - to obtain data from (none (go to website and find problem), sqlite3 default, postgres, ect)
   *    tag         - tag or tags to filter by
   *    difficulty  - difficulty to filter by
   *    isPaidOnly  - default is false (so no paid problems will be downloaded)
   *    // possibly other filters (dislike to like ratio, )
   *    name        - don't pick one for me, use the name provided
   *    id          - don't pick one for me, use the id provided
   *    language    - default javascript, create a folder for the problem, language.  Create a readme, problem.ext, tests
   *    problemdir  - directory where the problems will be created
   */
  public async run(): Promise<void> {
    // const {args, flags} = await this.parse(LeetcodeProblemCreate)
    //
    // const name = flags.name ?? 'world'
    // this.log(`hello ${name} from /Users/jarndt/dev/leetcode/leetcode/src/commands/leetcode/problem/create.ts`)
    // if (args.file && flags.force) {
    //   this.log(`you input --force and --file: ${args.file}`)
    // }
    // TODO add the flags specified in description
    // make problem directory using stub if not exist, language dir if not exist
    const language = 'Python3'; //'JavaScript';
    const name = undefined; //'build-array-from-permutation';
    const problemDir = '..'
    const db = new DB();
    let questionNodeTags;
    if(!name) {
      const s = shell(`ls ${problemDir}`).split('\n');
      // TODO check if language is different
      // get a list of all problems and remove them from select query
      questionNodeTags = await db.Question.findOne({
        where: {paidOnly: false, titleSlug: {[Op.notIn]: s}},
        include: [{model: db.QuestionNode, where: {categoryTitle: {[Op.not]: "Database"}}}, db.TopicTag],
        order: [['acRate', 'DESC']]
      });
    }else
      questionNodeTags = await db.Question.findOne({
        where: {titleSlug: name},
        include: [db.QuestionNode, db.TopicTag]
      });
    const question = <Question>questionNodeTags.dataValues;
    const tags = questionNodeTags.TopicTags.map((t: any)=><TopicTag>(t.dataValues));
    const questionNode = <QuestionNode>questionNodeTags.QuestionNode.dataValues;
    // const question = q.dataValues;
    const problemStub = question.titleSlug;
    const dir = `${problemDir}/${problemStub}`
    // const languages = shell(`ls ${dir}`).split('\n');
    // if(languages.includes(language))

    // TODO format this markdown better for example put examples in code blocks
    let markDown = NodeHtmlMarkdown.translate(questionNode.content); //.replace(/\n/g,'\n<br/>');
    let outputs;
    try {
      // @ts-ignore
      outputs = markDown.split(/\*\*Example.*:\*\*/).splice(1).map(m => m.match(/(?<=\*\*Output:\*\* ).*/)[0]);
    }catch (e){
      // @ts-ignore
      outputs = markDown.split(/\*\*Example.*:\*\*/).splice(1).map(m => m.match(/(?<=\*\*Output\*\*\n).*/)[0]);
    }
    // TODO python turns null into None subrectangle-queries
    // TODO typical class named Solution is SubrectangleQueries for subrectangle-queries
    const inputs = questionNode.exampleTestcases.split('\n');
    const like = `<button><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M7 19v-8H4v8h3zM7 9c0-.55.22-1.05.58-1.41L14.17 1l1.06 1.05c.27.27.44.65.44 1.06l-.03.32L14.69 8H21c1.1 0 2 .9 2 2v2c0 .26-.05.5-.14.73l-3.02 7.05C19.54 20.5 18.83 21 18 21H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h3zm2 0v10h9l3-7v-2h-9l1.34-5.34L9 9z"></path></svg><span>${questionNode.likes}</span></button>`;
    const dislike = `<button><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M17 3v12c0 .55-.22 1.05-.58 1.41L9.83 23l-1.06-1.05c-.27-.27-.44-.65-.44-1.06l.03-.32.95-4.57H3c-1.1 0-2-.9-2-2v-2c0-.26.05-.5.14-.73l3.02-7.05C4.46 3.5 5.17 3 6 3h11zm-2 12V5H6l-3 7v2h9l-1.34 5.34L15 15zm2-2h3V5h-3V3h3a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-3v-2z"></path></svg><span>${questionNode.dislikes}</span></button>`
    const difficulty = `<span style="color:${question.difficulty === "Easy"?'green':'red'}">${question.difficulty}</span>`;
    const link = `https://leetcode.com/problems/${question.titleSlug}/`;
    markDown = `# [${question.frontendQuestionId}. ${question.title}](${link})\n${difficulty}   ${like}   ${dislike}  Acc: ${question.acRate}\n---\n${questionNode.categoryTitle}\n\nTags:\n- ${tags.map((t: TopicTag)=>t.name).join('\n- ')}\n\n`+
      markDown+`\n\n**Hints:**\n- ${JSON.parse(questionNode.hints+"").join('\n- ')}\n\n*Generated by [leetcode generator](https://github.com/unsupo/leetcode)*`
    const codeSnippets =<Array<CodeSnippetNode>> JSON.parse(questionNode.codeSnippets+"");
    const code = modifyForLang(codeSnippets.filter(c=>c.lang===language)[0].code+'\n', language); // TODO get input/output and pass it to a generate test case method
    const tests = generateTestCode(language, JSON.parse(questionNode.metaData), inputs, outputs);
    shell(`mkdir -p ${dir}/${language}`);
    fs.writeFileSync(`${dir}/README.md`,markDown);
    fs.writeFileSync(`${dir}/${language}/${question.titleSlug}.${getExtension(language)}`,code+'\n'+tests);
    CliUx.ux.log(`Created problem: ${dir}/${language}`);
    // TODO look at problem add-two-integers and shuffle-the-array it gives two inputs and tests doesn't support this yet
    // I group the inputs as an array and use the spread operator (python is *)
  }
}
function getExtension(language: string) {
  switch (language) {case "C++": return ""
    case "Java": return "java"
    case "Python": return "py"
    case "Python3": return "py"
    case "C": return "c"
    case "C#": return "cs"
    case "JavaScript": return "js"
    case "Ruby": return "rb"
    case "Swift": return "swift"
    case "Go": return "go"
    case "Scala": return "sc"
    case "Kotlin": return "kt"
    case "Rust": return "rs"
    case "PHP": return "php"
    case "TypeScript": return "ts"
    case "Racket": return "rkt"
    case "Erlang": return "erl"
    case "Elixir": return "ex"
    case "Dart": return "dart"
  }
}
interface Param {
  name: string;
  type: string;
}
interface Return {
  type: string;
}
interface Metadata {
  "name": string,
  "params": Array<Param>,
  "return": Param
}
function generateTestCode(language: string, metadata: Metadata, inputs: string[], outputs: string[]) {
  const INPUT = "<!INPUTS!>", OUTPUT = "<!OUTPUTS!>", METHOD = "<!METHOD!>"
  switch (language) {
    case "C++": return ""
    case "Java": return "java" // java not quite as simple since you can't just append it to the end of the file, might need a refactor
    case "Python":
    case "Python3": return (`input=[${INPUT}]\n` + // TODO python3 needs to import from typing import List and pass
      `output=[${OUTPUT}]\n` +  // TODO python converts null to None and capitalizes booleans
      'for i in range(len(output)):\n' +
      `    r = Solution().${METHOD}(input[i])\n` + // TODO class names aren't always Solution see subrectangle-queries
      '    if str(r) != str(output[i]):\n' + // str wrapper is for checking type so we don't return a double when it wants an int
      '        raise Exception(\'Failed: \'+str(input[i])+\' ---- Got: \'+str(r)+\' !== \'+str(output[i]))\n' +
      '    print(\'Passed input: \'+str(input[i]))').replace(INPUT,inputs.join(',').replace('null','None')).replace(OUTPUT,outputs.join(',').replace('null','None')).replace(METHOD,metadata.name);
    // TODO find a regex for non quoted null and boolean and replace those
    case "C": return "c"
    case "C#": return "cs"
    case "JavaScript": return (`const inputs = [${INPUT}]\n` +
      `const outputs = [${OUTPUT}]\n` +
      'inputs.forEach((input,i)=>{\n' +
      `  const r = ${METHOD}(input);\n` +
      '  if(JSON.stringify(r)!==JSON.stringify(outputs[i]))\n' +
      '    throw new Error(\'Failed: \'+input+\' ---- Got: \'+JSON.stringify(r)+\' !== \'+JSON.stringify(outputs[i]));\n' +
      '  else console.log(\'Passed input: \'+input);\n' +
      '});').replace(INPUT,inputs.join(',')).replace(OUTPUT,outputs.join(',')).replace(METHOD,metadata.name);
    case "Ruby": return "rb"
    case "Swift": return "swift"
    case "Go": return "go"
    case "Scala": return "sc"
    case "Kotlin": return "kt"
    case "Rust": return "rs"
    case "PHP": return "php"
    case "TypeScript": return "ts"
    case "Racket": return "rkt"
    case "Erlang": return "erl"
    case "Elixir": return "ex"
    case "Dart": return "dart"
  }
}

/**
 * Take in code and output any code modification ie python needs to import List and Optional sometimes
 * @param code
 * @param language
 */
function modifyForLang(code: string, language: string) {
  switch (language) {
    case "C++": return code
    case "Java": return code // java not quite as simple since you can't just append it to the end of the file, might need a refactor
    case "Python":
    case "Python3":
      if(code.indexOf("Optional") > -1)
        code="from typing import Optional\n"+code
      if(code.indexOf("TreeNode") > -1)
        code="from util import TreeNode\n"+code
      if(code.indexOf("List") > -1)
        code="from typing import List\n"+code
      return code
    case "C": return code
    case "C#": return code
    case "JavaScript": return code
    case "Ruby": return code
    case "Swift": return code
    case "Go": return code
    case "Scala": return code
    case "Kotlin": return code
    case "Rust": return code
    case "PHP": return code
    case "TypeScript": return code
    case "Racket": return code
    case "Erlang": return code
    case "Elixir": return code
    case "Dart": return code
  }
}
