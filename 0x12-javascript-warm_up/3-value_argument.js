#!/usr/bin/node
const [, , arg] = process.argv;
console.log(arg === undefined ? 'No argument' : arg);
