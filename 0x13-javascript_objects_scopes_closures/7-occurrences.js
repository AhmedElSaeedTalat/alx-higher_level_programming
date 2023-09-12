#!/usr/bin/node
const nbOccurences = (list, searchElement) => {
  let counter = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      counter += 1;
    }
  }
  return counter;
};
module.exports = { nbOccurences };
