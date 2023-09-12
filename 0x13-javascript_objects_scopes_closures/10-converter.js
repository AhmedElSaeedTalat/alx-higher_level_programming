#!/usr/bin/node
const converter = (base) => {
  return function (number) {
    if (base === 10) {
      return number;
    }
    return number.toString(base);
  };
};
module.exports = { converter };
