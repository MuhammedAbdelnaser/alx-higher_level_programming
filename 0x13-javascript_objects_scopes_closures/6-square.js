#!/usr/bin/node
const SquareMain = require('./5-square');

class Square extends SquareMain {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let sum = '';
      for (let i = 0; i < this.width; i++) {
        sum += c;
      }
      console.log(sum);
    }
  }
}
module.exports = Square;
