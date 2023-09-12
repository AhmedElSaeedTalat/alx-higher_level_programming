#!/usr/bin/node
const converter = (base) => {
  function myConverter (number) {
    return number.toString(base);
  }
  return myConverter;
};
module.exports = { converter };
