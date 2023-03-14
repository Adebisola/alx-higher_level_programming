const stack = [];
exports.logMe = function (item) {
  stack.push(item);
  console.log(stack.indexOf(item) + ': ' + item);
};
