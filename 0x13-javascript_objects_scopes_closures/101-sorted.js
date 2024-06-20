#!/usr/bin/node

const dict = require('./101-data').dict;

const newObj = {};

for (const key in dict) {
  const value = dict[key];
  if (newObj[value]) {
    newObj[value].push(key);
  } else {
    newObj[value] = [key];
  }
}

console.log(newObj);
