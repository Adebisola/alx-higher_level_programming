const myArgs = parseInt(process.argv[2]);
if (myArgs) {
    console.log("My number is " + myArgs);
} else {
    console.log('Not a number')
}