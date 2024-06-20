#!/usr/bin/node

const getFactorial = (n) => n > 1 ? n * getFactorial(n - 1) : 1;

const number = parseInt(process.argv[2]);

console.log(isNaN(number) ? 1 : getFactorial(number));
