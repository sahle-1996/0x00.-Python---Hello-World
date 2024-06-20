#!/usr/bin/node

const repeatFunction = (count, callback) => {
  while (count > 0) {
    callback();
    count--;
  }
};

module.exports = { callMeMoby: repeatFunction };
