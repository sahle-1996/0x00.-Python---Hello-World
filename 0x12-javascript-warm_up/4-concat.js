#!/usr/bin/node

const args = require('process').argv.slice(2);

console.log(args[0] ? `${args[0]} is ${args[1] || 'undefined'}` : 'Insufficient arguments');
