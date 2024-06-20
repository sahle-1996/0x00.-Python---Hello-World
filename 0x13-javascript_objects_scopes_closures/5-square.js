#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    this.width = w > 0 ? w : 0;
    this.height = h > 0 ? h : 0;
  }
}

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }
}

module.exports = Square;
