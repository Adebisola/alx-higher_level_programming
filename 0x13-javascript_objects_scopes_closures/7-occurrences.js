#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    const num = list[i];
    if (num === searchElement) {
      count++;
    }
  }
  return count;
};
