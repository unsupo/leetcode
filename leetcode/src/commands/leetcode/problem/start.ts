import {CliUx, Command, Flags} from '@oclif/core'
import cli from 'cli-ux'
import * as notifier from 'node-notifier'
import {rejects} from "assert";
import * as fs from "fs";



export default class LeetcodeProblemStart extends Command {
  static description = 'describe the command here'

  static examples = [
    '<%= config.bin %> <%= command.id %>',
  ]

  static flags = {
    // flag with a value (-n, --name=VALUE)
    // name: Flags.string({char: 'n', description: 'name of problem slug'}),
  }

  static args = [{name: 'file'}]

  // This will start a timer for this problem which will notify you when the time is up.  either specify problem name or be in directory of problem
  // easy gets 10m, medium get 20m and hard gets 30m
  public async run(): Promise<void> {
    // const {args, flags} = await this.parse(LeetcodeProblemStart)

    // const name = flags.name
    const d = new Date();
    try {
      CliUx.ux.log('Type any key if successfully submitted to leetcode to stop the countdown');
      const anyKey = CliUx.ux.anykey();
      const r = await customSettingExample(10, anyKey);
      if(r)
        notifier.notify({
          title: 'Times Up!',
          message: 'Time has expired for problem'
        });
    }catch (e){
      const ed = new Date();
      fs.writeFileSync('time.txt','start: '+d.toISOString()+', end: '+ed.toISOString()+", total time: "+(ed.getMilliseconds()-d.getMilliseconds()));
    }
  }
}
async function payloadValueExample() {
  console.log('Example 3: bar with payload values')
  const bar = cli.progress({
    format: '[{bar}] {percentage}% | ETA: {eta}s | {value}/{total} | Speed: {speed}',
  })

  // initialize the bar -  defining payload token "speed" with the default value "N/A"
  bar.start(200, 0, {
    speed: 'N/A',
  })
  // the bar value - will be linear incremented
  let value = 0
  const speedData: any = []
  return new Promise<void>(resolve => {
    const timer = setInterval(function () {
      // increment value
      value++

      // example speed data
      speedData.push(Math.random() * 2 + 5)
      const currentSpeedData = speedData.splice(-10)

      // update the bar value
      bar.update(value, {
        speed: (currentSpeedData.reduce((a: any, b: any) => {
          return a + b
        }, 0) / currentSpeedData.length).toFixed(2) + 'mb/s',
      })

      if (value >= bar.getTotal()) {
        // stop timer
        clearInterval(timer)

        bar.stop()
        resolve()
      }
    }, 20)
  })
}

// @ts-ignore
async function customSettingExample(time: number, stopper): Promise<boolean> {
  // console.log('Example 2: bar with custom settings')
  const bar = cli.progress({
    barCompleteChar: '\u2588',
    barIncompleteChar: '\u2591',
    format: `|| {bar} || {percentage}% | ETA: {eta}s | {value}/{total} seconds`,
    fps: 100,
    stream: process.stdout,
    barsize: 30,
  })
  bar.start(time*60, 0) // stop when time in seconds is reached
  let value = 0
  return new Promise<boolean>((resolve, reject) => {
    const timer = setInterval(async () => {
      value += 1.

      // update the bar value
      bar.update(value)
      const t = {};
      const s = await Promise.race([stopper, t]);
      if (value >= bar.getTotal() || s !== t) {
        // stop timer
        clearInterval(timer)

        bar.stop()
        if(s)
          reject(false)
        resolve(true)
      }
    }, 1000) // update every second
  })
}

async function defaultSettingExample() {
  // create new progress bar using default values
  console.log('Example 1: bar with default values')
  return new Promise<void>(resolve => {
    const bar = cli.progress()
    bar.start()
    let value = 0
    const timer = setInterval(() => {
      value++

      // update the bar value
      bar.update(value)
      if (value >= bar.getTotal()) {
        // stop timer
        clearInterval(timer)

        bar.stop()
        resolve()
      }
    }, 20)
  })
}
