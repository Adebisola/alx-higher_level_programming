#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments.
if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
