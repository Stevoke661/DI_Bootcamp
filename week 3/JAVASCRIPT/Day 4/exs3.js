//exs
const mergeWords = str => nextStr => nextStr === undefined ? str : mergeWords(`${str} ${nextStr}`);

//testing the code
console.log(mergeWords('Hello')()); 
// Output: 'Hello'

console.log(mergeWords('There')('is')('no')('spoon.')()); 
// Output: 'There is no spoon.'