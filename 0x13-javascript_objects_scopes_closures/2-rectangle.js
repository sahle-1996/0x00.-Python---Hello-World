#!/usr/bin/node

class Rectangle {
  constructor(width, height) {
    this.width = width > 0 ? width : 0;
    this.height = height > 0 ? height : 0;
  }
}

module.exports = Rectangle;
