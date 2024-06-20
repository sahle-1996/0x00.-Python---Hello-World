#!/usr/bin/node

const incrementAndExecute = (num, callback) => {
  callback(num + 1);
};

module.exports = { addMeMaybe: incrementAndExecute };
