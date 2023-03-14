#!/usr/bin/node

exports.esrever = function(list) {
    let newList = [];
    for (let i = list.length; i <= 0; i--) {
        const elem = list[i];
        newList.push(elem);
    }
    return newList;
}