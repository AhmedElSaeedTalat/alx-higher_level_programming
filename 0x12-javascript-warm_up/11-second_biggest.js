#!/usr/bin/node
let val;
let val2;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  val = parseInt(process.argv[2]);
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > val) {
      val = process.argv[i];
    }
  }
  if (val !== process.argv[2]) {
    val2 = process.argv[2];
  } else {
    val2 = process.argv[3];
  }
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > val2 && process.argv[i] !== val) {
      val2 = process.argv[i];
    }
  }
  console.log(val2);
}
