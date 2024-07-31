#!/usr/bin/node
/* 2. Display the status code of a GET request. */

const request = require('request');
const targetUrl = process.argv[2];

request.get(targetUrl, (err, res) => {
  if (err) {
    throw err;
  }
  console.log('code:', res.statusCode);
});
