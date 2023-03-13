//#!/usr/bin/node
// A script that prints the first argument passed to it
if (typeof process.argv === undefined) {
    console.log('No argument')
} else {
    console.log(process.argv[2])
}