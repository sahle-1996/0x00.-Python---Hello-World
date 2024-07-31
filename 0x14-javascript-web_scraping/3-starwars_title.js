#!/usr/bin/node
/* 3. Print the title of a Star Wars movie based on given argument. */

const request = require('request');
const filmId = process.argv[2];

const apiUrl = `http://swapi.dev/api/films/${filmId}`;
request.get(apiUrl, (err, res, body) => {
  if (err) {
    throw err;
  }
  const movie = JSON.parse(body);
  console.log(movie.title);
});
