#!/usr/bin/node

const SquareP = require('./5-square.js');

module.exports = class Square extends SquareP {
  charPrint(c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
