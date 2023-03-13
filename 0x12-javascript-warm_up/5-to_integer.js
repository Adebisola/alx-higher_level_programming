#!/usr/bin/node
// a script that prints a number if first argument can be converted to an integer
const myArgs = parseInt(process.argv[2]);
if (myArgs) {
  console.log("My number is " + myArgs);
} else {
  console.log('Not a number')
}
