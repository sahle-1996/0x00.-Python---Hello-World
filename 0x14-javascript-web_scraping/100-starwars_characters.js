#!/usr/bin/node
/* 7 (adv). Fetch and display names of all characters in a specified movie. */

const request = require('request');
const movieId = process.argv[2];

const apiEndpoint = `http://swapi.dev/api/films/${movieId}`;

request(apiEndpoint, (err, response, body) => {
  if (err) {
    throw err;
  }
  const characters = JSON.parse(body).characters;
  characters.forEach(characterUrl => {
    request(characterUrl, (error, res, data) => {
      if (error) {
        throw error;
      }
      console.log(JSON.parse(data).name);
    });
  });
});
