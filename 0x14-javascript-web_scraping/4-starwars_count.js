#!/usr/bin/node
/* 4. Count the number of movies featuring Antilles. */

const request = require('request');
const apiUrl = process.argv[2];

let movieCount = 0;
request.get(apiUrl, (err, res, body) => {
  if (err) {
    throw err;
  }
  const films = JSON.parse(body).results;
  films.forEach(film => {
    film.characters.forEach(character => {
      if (character.includes('18/')) {
        movieCount++;
      }
    });
  });
  console.log(movieCount);
});
