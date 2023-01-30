import {expect, test} from '@oclif/test'

describe('leetcode:problem:create', () => {
  test
  .stdout()
  .command(['leetcode:problem:create'])
  .it('runs hello', ctx => {
    expect(ctx.stdout).to.contain('hello world')
  })

  test
  .stdout()
  .command(['leetcode:problem:create', '--name', 'jeff'])
  .it('runs hello --name jeff', ctx => {
    expect(ctx.stdout).to.contain('hello jeff')
  })
})
