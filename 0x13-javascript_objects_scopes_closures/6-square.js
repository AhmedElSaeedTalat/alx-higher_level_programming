#!/usr/bin/node
const Sq = require('./5-square.js');
class Square extends Sq {
  charPrint (c) {
    let square = '';
    for (let i = 0; i < this.width; i++) {
      if (c == null) {
        square += 'X';
      } else {
        square += c;
      }
    }
    for (let i = 0; i < this.height; i++) {
      console.log(square);
    }
  }
}
module.exports = Square;
