import {LeetcodeResponse} from "./types";

export class Curl {
  headers = [
    "-H 'authority: leetcode.com' \\",
    "-H 'accept: */*' \\",
    "-H 'accept-language: en-US,en;q=0.9' \\",
    "-H 'authorization;' \\",
    "-H 'content-type: application/json' \\",
    "-H 'cookie: NEW_PROBLEMLIST_PAGE=1; csrftoken=${csrfToken}' \\",
    "-H 'origin: https://leetcode.com' \\",
    "-H 'referer: https://leetcode.com/problemset/all/${page === 1 ? '' : '?page=' + page}' \\",
    "-H 'sec-ch-ua: \"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"' \\",
    "-H 'sec-ch-ua-mobile: ?0' \\",
    "-H 'sec-ch-ua-platform: \"macOS\"' \\",
    "-H 'sec-fetch-dest: empty' \\",
    "-H 'sec-fetch-mode: cors' \\",
    "-H 'sec-fetch-site: same-origin' \\",
    "-H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' \\",
    "-H 'x-csrftoken: ${csrfToken}' ",
  ]


<LeetcodeResponse>JSON.parse(this.curl(`curl -s 'https://leetcode.com/graphql/' \\
  --data-raw '{"query":"\\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\\n  problemsetQuestionList: questionList(\\n    categorySlug: $categorySlug\\n    limit: $limit\\n    skip: $skip\\n    filters: $filters\\n  ) {\\n    total: totalNum\\n    questions: data {\\n      acRate\\n      difficulty\\n      freqBar\\n      frontendQuestionId: questionFrontendId\\n      isFavor\\n      paidOnly: isPaidOnly\\n      status\\n      title\\n      titleSlug\\n      topicTags {\\n        name\\n        id\\n        slug\\n      }\\n      hasSolution\\n      hasVideoSolution\\n    }\\n  }\\n}\\n    ","variables":{"categorySlug":"","skip":${(page - 1) * 50},"limit":50,"filters":{}}}' \\
  --compressed`));

}
