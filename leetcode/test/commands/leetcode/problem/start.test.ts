import {expect, test} from '@oclif/test'

describe('leetcode:problem:start', () => {
  test
  .stdout()
  .command(['leetcode:problem:start'])
  .it('runs hello', ctx => {
    expect(ctx.stdout).to.contain('hello world')
  })

  test
  .stdout()
  .command(['leetcode:problem:start', '--name', 'jeff'])
  .it('runs hello --name jeff', ctx => {
    expect(ctx.stdout).to.contain('hello jeff')
  })
})
