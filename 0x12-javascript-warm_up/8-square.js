#!/usr/bin/node
// A script that prints a square.
const size = parseInt(process.argv[2]);
if (size) {
  for (let r = 0; r < size; r++) {
    let row = '';
    for (let c = 0; c < size; c++) row += 'X';
    console.log(row);
  }
} else {
  console.log('Missing size');
}
