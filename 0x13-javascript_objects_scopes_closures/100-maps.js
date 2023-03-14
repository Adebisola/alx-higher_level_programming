#!/usr/bin/node
// A script that imports an array and computes a new array.
const myList = require('./100-data.js').list;
const newList = myList.map((item, index) => item * index);
console.log(myList);
console.log(newList);
