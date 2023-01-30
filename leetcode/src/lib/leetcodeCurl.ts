import {LeetcodeResponse, ProblemSetQuestionListResponse, QuestionNodeResponse, QuestionResponse} from "./types";
import {execSync} from "child_process";
import {Browser, Builder} from "selenium-webdriver";
import * as chrome from "selenium-webdriver/chrome";
import {shell} from "./fsUtils";

class LeetcodeCurl {
  cmd = "curl";
  baseUrl = "https://leetcode.com/graphql/"
  headers = [
    "-H 'authority: leetcode.com'",
    "-H 'accept: */*'",
    "-H 'accept-language: en-US,en;q=0.9'",
    "-H 'authorization;'",
    "-H 'content-type: application/json'",
    "-H 'origin: https://leetcode.com'",
    "-H 'sec-ch-ua: \"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"'",
    "-H 'sec-ch-ua-mobile: ?0'",
    "-H 'sec-ch-ua-platform: \"macOS\"'",
    "-H 'sec-fetch-dest: empty'",
    "-H 'sec-fetch-mode: cors'",
    "-H 'sec-fetch-site: same-origin'",
    "-H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'",
  ];
  flags = ['-s', '--compressed'];
  private readonly csrfToken: string;

  constructor(csrfToken: string) {
    this.csrfToken = csrfToken;
    this.headers = this.headers.concat([
      `-H 'x-csrftoken: ${this.csrfToken}' `,
      `-H 'cookie: NEW_PROBLEMLIST_PAGE=1; csrftoken=${this.csrfToken}'`,
    ])
  }

  curl(cmd: string) {
    return shell(cmd)
  }

  private getCurl(dataRaw: string, headers = this.headers, flags = this.flags) {
    return this.curl(`${this.cmd} '${this.baseUrl}' \\\n ${headers.join(' \\\n')} ${flags.join(' ')} --data-raw '${dataRaw}'`);
  }

  getProblemSetQuestionList(page: number = 1): LeetcodeResponse<ProblemSetQuestionListResponse> {
    // must quote then paste the data to escape the \n
    const dataRaw = `{\"query\":\"\\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\\n  problemsetQuestionList: questionList(\\n    categorySlug: $categorySlug\\n    limit: $limit\\n    skip: $skip\\n    filters: $filters\\n  ) {\\n    total: totalNum\\n    questions: data {\\n      acRate\\n      difficulty\\n      freqBar\\n      frontendQuestionId: questionFrontendId\\n      isFavor\\n      paidOnly: isPaidOnly\\n      status\\n      title\\n      titleSlug\\n      topicTags {\\n        name\\n        id\\n        slug\\n      }\\n      hasSolution\\n      hasVideoSolution\\n    }\\n  }\\n}\\n    \",\"variables\":{\"categorySlug\":\"\",\"skip\":${50*(page-1)},\"limit\":50,\"filters\":{}}}`;
    const res = this.getCurl(dataRaw, this.headers.concat([
      `-H 'referer: https://leetcode.com/problemset/all/${page === 1 ? '' : '?page=' + page}'`
    ]));
    return <LeetcodeResponse<ProblemSetQuestionListResponse>>JSON.parse(res);
  }

  /*
  // forget about this:  -H 'cookie: csrftoken=GsUTDalYpz0uFoKEttjfUPSMmwry0mLgpyfZFePBXAOrZxFISAhqDqF8Eg1kO1lB; NEW_PROBLEMLIST_PAGE=1; __stripe_mid=2212bd6b-d0fa-4758-9c91-a1da169e7ff1b09819; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjAyODI5MCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMGI5MWZjNTIzN2VhMThiODFkNjI1MjNkMTg0NjBlODFjZDc1ZjlhYSIsImlkIjoyMDI4MjkwLCJlbWFpbCI6InVuc3Vwb0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6InVuc3VwbyIsInVzZXJfc2x1ZyI6InVuc3VwbyIsImF2YXRhciI6Imh0dHBzOi8vczMtdXMtd2VzdC0xLmFtYXpvbmF3cy5jb20vczMtbGMtdXBsb2FkL2Fzc2V0cy9kZWZhdWx0X2F2YXRhci5qcGciLCJyZWZyZXNoZWRfYXQiOjE2NjU2MTEzNTQsImlwIjoiMjQuMTAuMTgzLjE1MyIsImlkZW50aXR5IjoiYTA1ZGYwMDdlZmNlZmUyODk0MTRjZDZkMGUxMGU3MTciLCJzZXNzaW9uX2lkIjoyODYwODM4OCwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.Bqkwpw1K0qu4-7gQDoO-nngCSBLwg_JqrD2MotLFapg; c_a_u=dW5zdXBv:1oj4Ay:TJ6H--wFqkPUazF8xwO8jG16uEg' \
  // can i ignore this? below
  -H 'x-newrelic-id: UAQDVFVRGwEAXVlbBAg=' \
  $
  */
  getProblem(problemSlug: string): LeetcodeResponse<QuestionNodeResponse> {
    const dataRaw = `{"operationName":"questionData","variables":{"titleSlug":"${problemSlug}"},"query":"query questionData($titleSlug: String\u0021) {\\n  question(titleSlug: $titleSlug) {\\n    questionId\\n    questionFrontendId\\n    boundTopicId\\n    title\\n    titleSlug\\n    content\\n    translatedTitle\\n    translatedContent\\n    isPaidOnly\\n    canSeeQuestion\\n    difficulty\\n    likes\\n    dislikes\\n    isLiked\\n    similarQuestions\\n    exampleTestcases\\n    categoryTitle\\n    contributors {\\n      username\\n      profileUrl\\n      avatarUrl\\n      __typename\\n    }\\n    topicTags {\\n      name\\n      slug\\n      translatedName\\n      __typename\\n    }\\n    companyTagStats\\n    codeSnippets {\\n      lang\\n      langSlug\\n      code\\n      __typename\\n    }\\n    stats\\n    hints\\n    solution {\\n      id\\n      canSeeDetail\\n      paidOnly\\n      hasVideoSolution\\n      paidOnlyVideo\\n      __typename\\n    }\\n    status\\n    sampleTestCase\\n    metaData\\n    judgerAvailable\\n    judgeType\\n    mysqlSchemas\\n    enableRunCode\\n    enableTestMode\\n    enableDebugger\\n    envInfo\\n    libraryUrl\\n    adminUrl\\n    challengeQuestion {\\n      id\\n      date\\n      incompleteChallengeCount\\n      streakCount\\n      type\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}`;
    const res = this.getCurl(dataRaw, this.headers.concat([
      `-H 'referer: https://leetcode.com/problems/${problemSlug}/'`
    ]));
    return <LeetcodeResponse<QuestionNodeResponse>>JSON.parse(res);
  }
  // could get discussion and get article with solution.  uses questionId with question slug in referrer
  /*
-H 'referer: https://leetcode.com/problems/delete-node-in-a-linked-list/discuss/?currentPage=1&orderBy=most_votes&query=' \
--data-raw $'{"operationName":"questionTopicsList","variables":{"orderBy":"most_votes","query":"","skip":0,"first":15,"tags":[],"questionId":"237"},"query":"query questionTopicsList($questionId: String\u0021, $orderBy: TopicSortingOption, $skip: Int, $query: String, $first: Int\u0021, $tags: [String\u0021]) {\\n  questionTopicsList(questionId: $questionId, orderBy: $orderBy, skip: $skip, query: $query, first: $first, tags: $tags) {\\n    ...TopicsList\\n    __typename\\n  }\\n}\\n\\nfragment TopicsList on TopicConnection {\\n  totalNum\\n  edges {\\n    node {\\n      id\\n      title\\n      commentCount\\n      viewCount\\n      pinned\\n      tags {\\n        name\\n        slug\\n        __typename\\n      }\\n      post {\\n        id\\n        voteCount\\n        creationDate\\n        isHidden\\n        author {\\n          username\\n          isActive\\n          nameColor\\n          activeBadge {\\n            displayName\\n            icon\\n            __typename\\n          }\\n          profile {\\n            userAvatar\\n            __typename\\n          }\\n          __typename\\n        }\\n        status\\n        coinRewards {\\n          ...CoinReward\\n          __typename\\n        }\\n        __typename\\n      }\\n      lastComment {\\n        id\\n        post {\\n          id\\n          author {\\n            isActive\\n            username\\n            __typename\\n          }\\n          peek\\n          creationDate\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    cursor\\n    __typename\\n  }\\n  __typename\\n}\\n\\nfragment CoinReward on ScoreNode {\\n  id\\n  score\\n  description\\n  date\\n  __typename\\n}\\n"}' \
   */
  // discuss topic tags same inputs as above
  /*
-H 'referer: https://leetcode.com/problems/delete-node-in-a-linked-list/discuss/?currentPage=1&orderBy=most_votes&query=' \
--data-raw $'{"operationName":"discussQuestionTopicTags","variables":{"selectedTags":[],"questionId":"237"},"query":"query discussQuestionTopicTags($tagType: String, $questionId: String\u0021, $selectedTags: [String\u0021]) {\\n  discussQuestionTopicTags(tagType: $tagType, questionId: $questionId, selectedTags: $selectedTags) {\\n    ...TopicTag\\n    __typename\\n  }\\n}\\n\\nfragment TopicTag on DiscussTopicTagNode {\\n  id\\n  name\\n  slug\\n  numTopics\\n  __typename\\n}\\n"}' \
   */
  // get the particular article takes in the data.questionTopicsList.edges[n].node.id as topicId, data.questionTopicsList.edges[n].node.title as title and questionSlug
  /*
-H 'referer: https://leetcode.com/problems/delete-node-in-a-linked-list/discuss/65455/1-3-lines-C%2B%2BJavaPythonCCJavaScriptRuby' \
--data-raw $'{"operationName":"DiscussTopic","variables":{"topicId":65455},"query":"query DiscussTopic($topicId: Int\u0021) {\\n  topic(id: $topicId) {\\n    id\\n    viewCount\\n    topLevelCommentCount\\n    subscribed\\n    title\\n    pinned\\n    tags\\n    hideFromTrending\\n    post {\\n      ...DiscussPost\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\\nfragment DiscussPost on PostNode {\\n  id\\n  voteCount\\n  voteStatus\\n  content\\n  updationDate\\n  creationDate\\n  status\\n  isHidden\\n  coinRewards {\\n    ...CoinReward\\n    __typename\\n  }\\n  author {\\n    isDiscussAdmin\\n    isDiscussStaff\\n    username\\n    nameColor\\n    activeBadge {\\n      displayName\\n      icon\\n      __typename\\n    }\\n    profile {\\n      userAvatar\\n      reputation\\n      __typename\\n    }\\n    isActive\\n    __typename\\n  }\\n  authorIsModerator\\n  isOwnPost\\n  __typename\\n}\\n\\nfragment CoinReward on ScoreNode {\\n  id\\n  score\\n  description\\n  date\\n  __typename\\n}\\n"}' \
   */

}

let lc: LeetcodeCurl;


const getWebDriver = async () => {
  return new Builder().forBrowser(Browser.CHROME)
    .setChromeOptions(new chrome.Options().headless())
    .build();
}

export const leetcodeCurl = async (): Promise<LeetcodeCurl> => {
  if (!lc) {
    const driver = await getWebDriver();
    await driver.get('https://leetcode.com/problemset/all/');
    const cookies = await driver.manage().getCookies();
    await driver.quit();
    // TODO determine expiry on csrftoken and persist it until expired
    const csrfToken = cookies.filter(c => c.name === 'csrftoken').concat()[0].value;
    lc = new LeetcodeCurl(csrfToken);
  }
  return lc;
}
