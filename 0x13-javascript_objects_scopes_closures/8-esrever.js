#!/usr/bin/node
const esrever = (list) => {
  const length = list.length;
  const reversed = [];
  for (let i = length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
module.exports = { esrever };
