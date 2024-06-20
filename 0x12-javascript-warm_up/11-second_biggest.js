#!/usr/bin/node

const { argv } = require('process');
const numbers = argv.slice(2).map(Number);
const sorted = numbers.filter(n => !isNaN(n)).sort((a, b) => b - a);
console.log(sorted.length > 1 ? sorted[1] : 0);
