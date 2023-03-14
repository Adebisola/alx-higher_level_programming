#!/usr/bin/node

exports.nbOccurences = function(list, searchElement) {
    let count = 0;
    for (let i = 0; i < list.length; i++) {
        let num = list[i];
        if (num === searchElement) {
            count += 1;
            console.log(count);
        }
    }
}