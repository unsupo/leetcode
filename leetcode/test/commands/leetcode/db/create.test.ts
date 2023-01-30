import {expect, test} from '@oclif/test'

describe('leetcode:db:create', () => {
  test
  .stdout()
  .command(['leetcode:db:create'])
  .it('runs hello', ctx => {
    expect(ctx.stdout).to.contain('hello world')
  })

  test
  .stdout()
  .command(['leetcode:db:create', '--name', 'jeff'])
  .it('runs hello --name jeff', ctx => {
    expect(ctx.stdout).to.contain('hello jeff')
  })
})
