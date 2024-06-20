#!/usr/bin/node
const [,, firstArg, secondArg] = process.argv;
console.log(firstArg ? `${firstArg} is ${secondArg}` : 'Missing arguments');
