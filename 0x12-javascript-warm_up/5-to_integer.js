#!/usr/bin/node

const value = parseFloat(process.argv[2]);
const integer = Number.isNaN(value) ? NaN : Math.trunc(value);

console.log(Number.isNaN(integer) ? 'Not a number' : `My number: ${integer}`);
