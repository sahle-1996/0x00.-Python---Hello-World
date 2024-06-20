#!/usr/bin/node

const count = parseInt(process.argv[2]);
const repeatMessage = (times) => {
  for (let i = 0; i < times; i++) console.log('C is fun');
};

isNaN(count) ? console.log('Missing number of occurrences') : repeatMessage(count);
