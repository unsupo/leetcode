// import parser from 'fast-xml-parser';
import * as os from 'os';
import {resolve} from 'path';
import {promisify} from 'util';
import * as fs from "fs";
import * as path from "path";
import {execSync} from "child_process";

// const archiver = require('archiver');

// function incrementFileName(filePath: string): string {
//     const dirName = path.dirname(filePath);
//     const name = path.basename(filePath).split('.').slice(0, -1).join('.');
//     const ex = path.extname(filePath);
//     let i = 0;
//     while (true) {
//         const fName = `${dirName}/${name}${i++ === 0 ? "" : i}${ex}`;
//         if (!fs.fileExistsSync(fName))
//             return fName;
//     }
// }
export const shell = (cmd: string) => execSync(cmd, {encoding: 'utf-8'});
export function remove(filePath: string) {
  try {
    if (fs.lstatSync(filePath).isDirectory())
      fs.unlinkSync(filePath);
    else
      fs.unlinkSync(filePath);
  } catch (e) {
    // @ts-ignore
    if (e.message.indexOf('no such') < 0)
      throw e;
  }
}
export const cleanFilePath = (filePath: string) => filePath.replace('~', os.homedir());
export const readFileSync = (filepath: string) => fs.readFileSync(cleanFilePath(filepath));

export function cleanName(name: string) {
  return name.replace('@', 'AT').replace('.', 'DOT');
}

export function mkdirSync(name: string) {
  try {
    fs.mkdirSync(name, {recursive: true});
  } catch (e) {
    /*DO NOTHING don't care if file already exists*/
  }
  return name;
}

export function copyFileSync(source: string, target: string) {
  let targetFile = target;
  // If target is a directory, a new file with the same name will be created
  if (fs.existsSync(target))
    if (fs.lstatSync(target).isDirectory())
      targetFile = path.join(target, path.basename(source));
  fs.writeFileSync(targetFile, fs.readFileSync(source));
}

export function copyFolderRecursiveSync(source: string, target: string) {
  let files = [];
  // Check if folder needs to be created or integrated
  const targetFolder = path.join(target, path.basename(source));
  if (!fs.existsSync(targetFolder))
    fs.mkdirSync(targetFolder);
  // Copy
  if (fs.lstatSync(source).isDirectory()) {
    files = fs.readdirSync(source);
    files.forEach(file => {
      const curSource = path.join(source, file);
      if (fs.lstatSync(curSource).isDirectory())
        copyFolderRecursiveSync(curSource, targetFolder);
      else
        copyFileSync(curSource, targetFolder);
    });
  }
}
export async function getFiles(dir: string): Promise<any> {
  const readdir = promisify(fs.readdir);
  const stat = promisify(fs.stat);
  const subdirs = await readdir(dir);
  // @ts-ignore
  const files = await Promise.all(subdirs.map(async subdir => {
    const res = resolve(dir, subdir);
    return (await stat(res)).isDirectory() ? getFiles(res) : res;
  }));
  return files.reduce((a: string | any[], f: any) => a.concat(f), []);
}

export function formatBytes(bytes: number, decimals = 2) {
  if (bytes === 0) return '0 Bytes';

  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];

  const i = Math.floor(Math.log(bytes) / Math.log(k));

  return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}
