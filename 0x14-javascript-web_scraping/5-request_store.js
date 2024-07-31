#!/usr/bin/node
/* 5. Retrieve website content and save it to a file. */

const request = require('request');
const fs = require('fs');

const [url, filePath] = process.argv.slice(2);

request(url, (err, response, body) => {
  if (err) {
    throw err;
  }
  fs.writeFile(filePath, body, 'utf8', (writeErr) => {
    if (writeErr) {
      throw writeErr;
    }
  });
});
