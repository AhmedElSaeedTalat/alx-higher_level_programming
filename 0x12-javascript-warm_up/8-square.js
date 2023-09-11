#!/usr/bin/node
let square = '';
let iteration;
if (parseInt(process.argv[2])) {
  iteration = process.argv[2];
  for (let i = 0; i < iteration; i++) {
    square += 'X';
  }
  for (let i = 0; i < iteration; i++) {
    console.log(square);
  }
} else {
  console.log('Missing size');
}
