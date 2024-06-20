#!/usr/bin/node

const sum = (a, b) => a + b;

const args = process.argv.slice(2).map(Number);

console.log(sum(...args));
