import {expect, test} from '@oclif/test'

describe('leetcode:create', () => {
  test
  .stdout()
  .command(['leetcode:create'])
  .it('runs hello', ctx => {
    expect(ctx.stdout).to.contain('hello world')
  })

  test
  .stdout()
  .command(['leetcode:create', '--name', 'jeff'])
  .it('runs hello --name jeff', ctx => {
    expect(ctx.stdout).to.contain('hello jeff')
  })
})
