#!/usr/bin/node
/* 0. Open and print contents of a file, print error object if any. */

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});
