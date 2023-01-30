import {expect, test} from '@oclif/test'

describe('leetcode:db:problem', () => {
  test
  .stdout()
  .command(['leetcode:db:problem'])
  .it('runs hello', ctx => {
    expect(ctx.stdout).to.contain('hello world')
  })

  test
  .stdout()
  .command(['leetcode:db:problem', '--name', 'jeff'])
  .it('runs hello --name jeff', ctx => {
    expect(ctx.stdout).to.contain('hello jeff')
  })
})
