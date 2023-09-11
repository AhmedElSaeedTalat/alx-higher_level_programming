#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const val1 = parseInt(process.argv[2]);
const val2 = parseInt(process.argv[3]);
console.log(add(val1, val2));
