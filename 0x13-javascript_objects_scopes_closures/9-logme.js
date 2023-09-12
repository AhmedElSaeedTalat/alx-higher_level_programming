#!/usr/bin/node
let counter = 0;
const logMe = (item) => {
  console.log(counter + ': ' + item);
  counter += 1;
};
module.exports = { logMe };
