import exp = require("constants");


export interface TopicTag {
  name: string;
  id: string;
  slug: string;
}

export interface Question {
  acRate: number;
  difficulty: string;
  freqBar: null
  frontendQuestionId: string;
  isFavor: boolean
  paidOnly: boolean
  status: null
  title: string;
  titleSlug: string;
  topicTags: Array<TopicTag>
  hasSolution: boolean;
  hasVideoSolution: boolean;
}
export interface CodeSnippetNode {
  lang: string;
  langSlug: string;
  code: string;
  __typename: string;
}
interface ArticleNode {
  "id": "1486",
  "canSeeDetail": true,
  "paidOnly": false,
  "hasVideoSolution": false,
  "paidOnlyVideo": true,
  "__typename": "ArticleNode"
}
interface ChallengeQuestionNode {
  "id": "1090",
  "date": "2022-10-13",
  "incompleteChallengeCount": 13,
  "streakCount": 0,
  "type": "DAILY",
  "__typename": "ChallengeQuestionNode"
}
export interface QuestionNode {
  "questionId": "237",
  "questionFrontendId": "237",
  "boundTopicId": null,
  "title": "Delete Node in a Linked List",
  "titleSlug": "delete-node-in-a-linked-list",
  // this is the important stuff
  "content": "<p>There is a singly-linked list <code>head</code> and we want to delete a node <code>node</code> in it.</p>\n\n<p>You are given the node to be deleted <code>node</code>. You will <strong>not be given access</strong> to the first node of <code>head</code>.</p>\n\n<p>All the values of the linked list are <strong>unique</strong>, and it is guaranteed that the given node <code>node</code> is not the last node in the linked list.</p>\n\n<p>Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:</p>\n\n<ul>\n\t<li>The value of the given node should not exist in the linked list.</li>\n\t<li>The number of nodes in the linked list should decrease by one.</li>\n\t<li>All the values before <code>node</code> should be in the same order.</li>\n\t<li>All the values after <code>node</code> should be in the same order.</li>\n</ul>\n\n<p><strong>Custom testing:</strong></p>\n\n<ul>\n\t<li>For the input, you should provide the entire linked list <code>head</code> and the node to be given <code>node</code>. <code>node</code> should not be the last node of the list and should be an actual node in the list.</li>\n\t<li>We will build the linked list and pass the node to your function.</li>\n\t<li>The output will be the entire list after calling your function.</li>\n</ul>\n\n<p>&nbsp;</p>\n<p><strong class=\"example\">Example 1:</strong></p>\n<img alt=\"\" src=\"https://assets.leetcode.com/uploads/2020/09/01/node1.jpg\" style=\"width: 400px; height: 286px;\" />\n<pre>\n<strong>Input:</strong> head = [4,5,1,9], node = 5\n<strong>Output:</strong> [4,1,9]\n<strong>Explanation: </strong>You are given the second node with value 5, the linked list should become 4 -&gt; 1 -&gt; 9 after calling your function.\n</pre>\n\n<p><strong class=\"example\">Example 2:</strong></p>\n<img alt=\"\" src=\"https://assets.leetcode.com/uploads/2020/09/01/node2.jpg\" style=\"width: 400px; height: 315px;\" />\n<pre>\n<strong>Input:</strong> head = [4,5,1,9], node = 1\n<strong>Output:</strong> [4,5,9]\n<strong>Explanation: </strong>You are given the third node with value 1, the linked list should become 4 -&gt; 5 -&gt; 9 after calling your function.\n</pre>\n\n<p>&nbsp;</p>\n<p><strong>Constraints:</strong></p>\n\n<ul>\n\t<li>The number of the nodes in the given list is in the range <code>[2, 1000]</code>.</li>\n\t<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>\n\t<li>The value of each node in the list is <strong>unique</strong>.</li>\n\t<li>The <code>node</code> to be deleted is <strong>in the list</strong> and is <strong>not a tail</strong> node.</li>\n</ul>\n",
  "translatedTitle": null,
  "translatedContent": null,
  "isPaidOnly": false,
  "canSeeQuestion": true,
  "difficulty": "Medium",
  "likes": 1433,
  "dislikes": 445,
  "isLiked": null,
  // TODO convert these string objects to types
  "similarQuestions": "[{\"title\": \"Remove Linked List Elements\", \"titleSlug\": \"remove-linked-list-elements\", \"difficulty\": \"Easy\", \"translatedTitle\": null}]",
  // this is the important stuff
  "exampleTestcases": "[4,5,1,9]\n5\n[4,5,1,9]\n1",
  "categoryTitle": "Algorithms",
  "contributors": [],
  "topicTags": Array<TopicTag>,
  "companyTagStats": null;
  // this is the important stuff
  "codeSnippets": CodeSnippetNode;
  "stats": "{\"totalAccepted\": \"964.2K\", \"totalSubmission\": \"1.3M\", \"totalAcceptedRaw\": 964183, \"totalSubmissionRaw\": 1286919, \"acRate\": \"74.9%\"}",
  "hints": [],
  "solution": ArticleNode;
  "status": null,
  // this is the important stuff
  "sampleTestCase": "[4,5,1,9]\n5",
  "metaData": "{\n  \"name\": \"deleteNode\",\n  \"params\": [\n    {\n      \"name\": \"head\",\n      \"type\": \"ListNode\"\n    },\n    {\n      \"name\": \"node\",\n      \"type\": \"integer\"\n    }\n  ],\n  \"return\": {\n    \"type\": \"void\"\n  },\n  \"output\": {\n    \"paramindex\": 0\n  },\n  \"manual\": true,\n  \"languages\": [\n    \"cpp\",\n    \"java\",\n    \"python\",\n    \"c\",\n    \"csharp\",\n    \"javascript\",\n    \"ruby\",\n    \"swift\",\n    \"golang\",\n    \"python3\",\n    \"scala\",\n    \"kotlin\",\n    \"php\",\n    \"typescript\"\n  ]\n}",
  "judgerAvailable": true,
  "judgeType": "large",
  "mysqlSchemas": [],
  "enableRunCode": true,
  "enableTestMode": false,
  "enableDebugger": true,
  "envInfo": "{\"cpp\": [\"C++\", \"<p>Compiled with <code> clang 11 </code> using the latest C++ 17 standard.</p>\\r\\n\\r\\n<p>Your code is compiled with level two optimization (<code>-O2</code>). <a href=\\\"https://github.com/google/sanitizers/wiki/AddressSanitizer\\\" target=\\\"_blank\\\">AddressSanitizer</a> is also enabled to help detect out-of-bounds and use-after-free bugs.</p>\\r\\n\\r\\n<p>Most standard library headers are already included automatically for your convenience.</p>\"], \"java\": [\"Java\", \"<p><code> OpenJDK 17 </code>. Java 8 features such as lambda expressions and stream API can be used. </p>\\r\\n\\r\\n<p>Most standard library headers are already included automatically for your convenience.</p>\\r\\n<p>Includes <code>Pair</code> class from https://docs.oracle.com/javase/8/javafx/api/javafx/util/Pair.html.</p>\"], \"python\": [\"Python\", \"<p><code>Python 2.7.12</code>.</p>\\r\\n\\r\\n<p>Most libraries are already imported automatically for your convenience, such as <a href=\\\"https://docs.python.org/2/library/array.html\\\" target=\\\"_blank\\\">array</a>, <a href=\\\"https://docs.python.org/2/library/bisect.html\\\" target=\\\"_blank\\\">bisect</a>, <a href=\\\"https://docs.python.org/2/library/collections.html\\\" target=\\\"_blank\\\">collections</a>. If you need more libraries, you can import it yourself.</p>\\r\\n\\r\\n<p>For Map/TreeMap data structure, you may use <a href=\\\"http://www.grantjenks.com/docs/sortedcontainers/\\\" target=\\\"_blank\\\">sortedcontainers</a> library.</p>\\r\\n\\r\\n<p>Note that Python 2.7 <a href=\\\"https://www.python.org/dev/peps/pep-0373/\\\" target=\\\"_blank\\\">will not be maintained past 2020</a>. For the latest Python, please choose Python3 instead.</p>\"], \"c\": [\"C\", \"<p>Compiled with <code>gcc 8.2</code> using the gnu11 standard.</p>\\r\\n\\r\\n<p>Your code is compiled with level one optimization (<code>-O1</code>). <a href=\\\"https://github.com/google/sanitizers/wiki/AddressSanitizer\\\" target=\\\"_blank\\\">AddressSanitizer</a> is also enabled to help detect out-of-bounds and use-after-free bugs.</p>\\r\\n\\r\\n<p>Most standard library headers are already included automatically for your convenience.</p>\\r\\n\\r\\n<p>For hash table operations, you may use <a href=\\\"https://troydhanson.github.io/uthash/\\\" target=\\\"_blank\\\">uthash</a>. \\\"uthash.h\\\" is included by default. Below are some examples:</p>\\r\\n\\r\\n<p><b>1. Adding an item to a hash.</b>\\r\\n<pre>\\r\\nstruct hash_entry {\\r\\n    int id;            /* we'll use this field as the key */\\r\\n    char name[10];\\r\\n    UT_hash_handle hh; /* makes this structure hashable */\\r\\n};\\r\\n\\r\\nstruct hash_entry *users = NULL;\\r\\n\\r\\nvoid add_user(struct hash_entry *s) {\\r\\n    HASH_ADD_INT(users, id, s);\\r\\n}\\r\\n</pre>\\r\\n</p>\\r\\n\\r\\n<p><b>2. Looking up an item in a hash:</b>\\r\\n<pre>\\r\\nstruct hash_entry *find_user(int user_id) {\\r\\n    struct hash_entry *s;\\r\\n    HASH_FIND_INT(users, &user_id, s);\\r\\n    return s;\\r\\n}\\r\\n</pre>\\r\\n</p>\\r\\n\\r\\n<p><b>3. Deleting an item in a hash:</b>\\r\\n<pre>\\r\\nvoid delete_user(struct hash_entry *user) {\\r\\n    HASH_DEL(users, user);  \\r\\n}\\r\\n</pre>\\r\\n</p>\"], \"csharp\": [\"C#\", \"<p><a href=\\\"https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-10\\\" target=\\\"_blank\\\">C# 10 with .NET 6 runtime</a></p>\"], \"javascript\": [\"JavaScript\", \"<p><code>Node.js 16.13.2</code>.</p>\\r\\n\\r\\n<p>Your code is run with <code>--harmony</code> flag, enabling <a href=\\\"http://node.green/\\\" target=\\\"_blank\\\">new ES6 features</a>.</p>\\r\\n\\r\\n<p><a href=\\\"https://lodash.com\\\" target=\\\"_blank\\\">lodash.js</a> library is included by default.</p>\\r\\n\\r\\n<p>For Priority Queue / Queue data structures, you may use <a href=\\\"https://github.com/datastructures-js/priority-queue\\\" target=\\\"_blank\\\">datastructures-js/priority-queue</a> and <a href=\\\"https://github.com/datastructures-js/queue\\\" target=\\\"_blank\\\">datastructures-js/queue</a>.</p>\"], \"ruby\": [\"Ruby\", \"<p><code>Ruby 3.1</code></p>\\r\\n\\r\\n<p>Some common data structure implementations are provided in the Algorithms module: https://www.rubydoc.info/github/kanwei/algorithms/Algorithms</p>\"], \"swift\": [\"Swift\", \"<p><code>Swift 5.5.2</code>.</p>\"], \"golang\": [\"Go\", \"<p><code>Go 1.17.6</code>.</p>\\r\\n\\r\\n<p>Support <a href=\\\"https://godoc.org/github.com/emirpasic/gods\\\" target=\\\"_blank\\\">https://godoc.org/github.com/emirpasic/gods</a> library.</p>\"], \"python3\": [\"Python3\", \"<p><code>Python 3.10</code>.</p>\\r\\n\\r\\n<p>Most libraries are already imported automatically for your convenience, such as <a href=\\\"https://docs.python.org/3/library/array.html\\\" target=\\\"_blank\\\">array</a>, <a href=\\\"https://docs.python.org/3/library/bisect.html\\\" target=\\\"_blank\\\">bisect</a>, <a href=\\\"https://docs.python.org/3/library/collections.html\\\" target=\\\"_blank\\\">collections</a>. If you need more libraries, you can import it yourself.</p>\\r\\n\\r\\n<p>For Map/TreeMap data structure, you may use <a href=\\\"http://www.grantjenks.com/docs/sortedcontainers/\\\" target=\\\"_blank\\\">sortedcontainers</a> library.</p>\"], \"scala\": [\"Scala\", \"<p><code>Scala 2.13.7</code>.</p>\"], \"kotlin\": [\"Kotlin\", \"<p><code>Kotlin 1.3.10</code>.</p>\"], \"php\": [\"PHP\", \"<p><code>PHP 8.1</code>.</p>\\r\\n<p>With bcmath module</p>\"], \"typescript\": [\"Typescript\", \"<p><code>TypeScript 4.5.4, Node.js 16.13.2</code>.</p>\\r\\n\\r\\n<p>Your code is run with <code>--harmony</code> flag, enabling <a href=\\\"http://node.green/\\\" target=\\\"_blank\\\">new ES2020 features</a>.</p>\\r\\n\\r\\n<p><a href=\\\"https://lodash.com\\\" target=\\\"_blank\\\">lodash.js</a> library is included by default.</p>\"]}",
  "libraryUrl": null,
  "adminUrl": null,
  "challengeQuestion": ChallengeQuestionNode,
  "__typename": "QuestionNode"
}

export interface ProblemsetQuestionList {
  total: number;
  questions: Array<Question>;
}

export interface ProblemSetQuestionListResponse {
  problemsetQuestionList: ProblemsetQuestionList;
}
export interface QuestionResponse {
  question: ProblemsetQuestionList;
}
export interface QuestionNodeResponse {
  question: QuestionNode;
}

export interface LeetcodeResponse<T> {
  data: T;
}


