#!/usr/bin/node

const sum = (x, y) => x + y;

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

console.log(sum(a, b));
