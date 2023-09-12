#!/usr/bin/node
const converter = (base) => {
  return function (number) {
    return number.toString(base);
  };
};
module.exports = { converter };
