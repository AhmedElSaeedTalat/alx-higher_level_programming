#!/usr/bin/node
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
let val;
if (parseInt(process.argv[2])) {
  val = parseInt(process.argv[2]);
  console.log(factorial(val));
} else {
  console.log(1);
}
