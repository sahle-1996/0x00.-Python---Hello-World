#!/usr/bin/node

const fac = (num) => (num <= 1 || isNaN(num)) ? 1 : num * fac(num - 1);

const num = parseInt(process.argv[2]);

console.log(fac(num));
