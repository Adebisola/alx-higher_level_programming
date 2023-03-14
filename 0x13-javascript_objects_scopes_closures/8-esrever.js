#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    const elem = list[i];
    newList.push(elem);
  }
  return newList;
};
