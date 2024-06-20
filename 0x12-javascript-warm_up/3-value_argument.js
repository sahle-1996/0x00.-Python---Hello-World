#!/usr/bin/node
const args = process.argv.slice(2);
const len = args.length;

len === 0 ? console.log('No argument') : console.log(args.join(' '));
