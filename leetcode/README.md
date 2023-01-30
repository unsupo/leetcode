Leetcode Problems
=================

The idea is to download leetcode problems to solve it locally before submitting it.

You can also save iterations and things you learned along the way.

Create a repository of notes and progress.

By default it will download a problem you don't have sorted by acceptance.

You can change this with parameters.

It should also put the start time, you should not exceed 10m for easy, 20m and 30m for hard.
If you do exceed the time limit, look for the solution and learn what you can, then remember to
come back to it and see if you can solve it in the time limit.


[![oclif](https://img.shields.io/badge/cli-oclif-brightgreen.svg)](https://oclif.io)
[![Version](https://img.shields.io/npm/v/oclif-hello-world.svg)](https://npmjs.org/package/oclif-hello-world)
[![CircleCI](https://circleci.com/gh/oclif/hello-world/tree/main.svg?style=shield)](https://circleci.com/gh/oclif/hello-world/tree/main)
[![Downloads/week](https://img.shields.io/npm/dw/oclif-hello-world.svg)](https://npmjs.org/package/oclif-hello-world)
[![License](https://img.shields.io/npm/l/oclif-hello-world.svg)](https://github.com/oclif/hello-world/blob/main/package.json)

<!-- toc -->
* [Usage](#usage)
* [Commands](#commands)
<!-- tocstop -->
# Usage
<!-- usage -->
```sh-session
$ npm install -g leetcode
$ leetcode COMMAND
running command...
$ leetcode (--version)
leetcode/0.0.0 darwin-arm64 node-v18.10.0
$ leetcode --help [COMMAND]
USAGE
  $ leetcode COMMAND
...
```
<!-- usagestop -->
# Commands
<!-- commands -->
* [`leetcode hello PERSON`](#leetcode-hello-person)
* [`leetcode hello world`](#leetcode-hello-world)
* [`leetcode help [COMMAND]`](#leetcode-help-command)
* [`leetcode plugins`](#leetcode-plugins)
* [`leetcode plugins:install PLUGIN...`](#leetcode-pluginsinstall-plugin)
* [`leetcode plugins:inspect PLUGIN...`](#leetcode-pluginsinspect-plugin)
* [`leetcode plugins:install PLUGIN...`](#leetcode-pluginsinstall-plugin-1)
* [`leetcode plugins:link PLUGIN`](#leetcode-pluginslink-plugin)
* [`leetcode plugins:uninstall PLUGIN...`](#leetcode-pluginsuninstall-plugin)
* [`leetcode plugins:uninstall PLUGIN...`](#leetcode-pluginsuninstall-plugin-1)
* [`leetcode plugins:uninstall PLUGIN...`](#leetcode-pluginsuninstall-plugin-2)
* [`leetcode plugins update`](#leetcode-plugins-update)

## `leetcode hello PERSON`

Say hello

```
USAGE
  $ leetcode hello [PERSON] -f <value>

ARGUMENTS
  PERSON  Person to say hello to

FLAGS
  -f, --from=<value>  (required) Who is saying hello

DESCRIPTION
  Say hello

EXAMPLES
  $ oex hello friend --from oclif
  hello friend from oclif! (./src/commands/hello/index.ts)
```

_See code: [dist/commands/hello/index.ts](https://github.com/jarndt-ltm/leetcode/blob/v0.0.0/dist/commands/hello/index.ts)_

## `leetcode hello world`

Say hello world

```
USAGE
  $ leetcode hello world

DESCRIPTION
  Say hello world

EXAMPLES
  $ leetcode hello world
  hello world! (./src/commands/hello/world.ts)
```

## `leetcode help [COMMAND]`

Display help for leetcode.

```
USAGE
  $ leetcode help [COMMAND] [-n]

ARGUMENTS
  COMMAND  Command to show help for.

FLAGS
  -n, --nested-commands  Include all nested commands in the output.

DESCRIPTION
  Display help for leetcode.
```

_See code: [@oclif/plugin-help](https://github.com/oclif/plugin-help/blob/v5.1.14/src/commands/help.ts)_

## `leetcode plugins`

List installed plugins.

```
USAGE
  $ leetcode plugins [--core]

FLAGS
  --core  Show core plugins.

DESCRIPTION
  List installed plugins.

EXAMPLES
  $ leetcode plugins
```

_See code: [@oclif/plugin-plugins](https://github.com/oclif/plugin-plugins/blob/v2.1.1/src/commands/plugins/index.ts)_

## `leetcode plugins:install PLUGIN...`

Installs a plugin into the CLI.

```
USAGE
  $ leetcode plugins:install PLUGIN...

ARGUMENTS
  PLUGIN  Plugin to install.

FLAGS
  -f, --force    Run yarn install with force flag.
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Installs a plugin into the CLI.

  Can be installed from npm or a git url.

  Installation of a user-installed plugin will override a core plugin.

  e.g. If you have a core plugin that has a 'hello' command, installing a user-installed plugin with a 'hello' command
  will override the core plugin implementation. This is useful if a user needs to update core plugin functionality in
  the CLI without the need to patch and update the whole CLI.

ALIASES
  $ leetcode plugins add

EXAMPLES
  $ leetcode plugins:install myplugin 

  $ leetcode plugins:install https://github.com/someuser/someplugin

  $ leetcode plugins:install someuser/someplugin
```

## `leetcode plugins:inspect PLUGIN...`

Displays installation properties of a plugin.

```
USAGE
  $ leetcode plugins:inspect PLUGIN...

ARGUMENTS
  PLUGIN  [default: .] Plugin to inspect.

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Displays installation properties of a plugin.

EXAMPLES
  $ leetcode plugins:inspect myplugin
```

## `leetcode plugins:install PLUGIN...`

Installs a plugin into the CLI.

```
USAGE
  $ leetcode plugins:install PLUGIN...

ARGUMENTS
  PLUGIN  Plugin to install.

FLAGS
  -f, --force    Run yarn install with force flag.
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Installs a plugin into the CLI.

  Can be installed from npm or a git url.

  Installation of a user-installed plugin will override a core plugin.

  e.g. If you have a core plugin that has a 'hello' command, installing a user-installed plugin with a 'hello' command
  will override the core plugin implementation. This is useful if a user needs to update core plugin functionality in
  the CLI without the need to patch and update the whole CLI.

ALIASES
  $ leetcode plugins add

EXAMPLES
  $ leetcode plugins:install myplugin 

  $ leetcode plugins:install https://github.com/someuser/someplugin

  $ leetcode plugins:install someuser/someplugin
```

## `leetcode plugins:link PLUGIN`

Links a plugin into the CLI for development.

```
USAGE
  $ leetcode plugins:link PLUGIN

ARGUMENTS
  PATH  [default: .] path to plugin

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Links a plugin into the CLI for development.

  Installation of a linked plugin will override a user-installed or core plugin.

  e.g. If you have a user-installed or core plugin that has a 'hello' command, installing a linked plugin with a 'hello'
  command will override the user-installed or core plugin implementation. This is useful for development work.

EXAMPLES
  $ leetcode plugins:link myplugin
```

## `leetcode plugins:uninstall PLUGIN...`

Removes a plugin from the CLI.

```
USAGE
  $ leetcode plugins:uninstall PLUGIN...

ARGUMENTS
  PLUGIN  plugin to uninstall

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Removes a plugin from the CLI.

ALIASES
  $ leetcode plugins unlink
  $ leetcode plugins remove
```

## `leetcode plugins:uninstall PLUGIN...`

Removes a plugin from the CLI.

```
USAGE
  $ leetcode plugins:uninstall PLUGIN...

ARGUMENTS
  PLUGIN  plugin to uninstall

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Removes a plugin from the CLI.

ALIASES
  $ leetcode plugins unlink
  $ leetcode plugins remove
```

## `leetcode plugins:uninstall PLUGIN...`

Removes a plugin from the CLI.

```
USAGE
  $ leetcode plugins:uninstall PLUGIN...

ARGUMENTS
  PLUGIN  plugin to uninstall

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Removes a plugin from the CLI.

ALIASES
  $ leetcode plugins unlink
  $ leetcode plugins remove
```

## `leetcode plugins update`

Update installed plugins.

```
USAGE
  $ leetcode plugins update [-h] [-v]

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Update installed plugins.
```
<!-- commandsstop -->
