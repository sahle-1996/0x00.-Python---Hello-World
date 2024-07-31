#!/usr/bin/node
/* 1. Write a string to a file. */

const fs = require('fs');
const [filePath, content] = process.argv.slice(2);

fs.writeFile(filePath, content, 'utf8', (error) => {
  if (error) {
    console.error(error);
  }
});
