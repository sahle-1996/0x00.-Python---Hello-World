#!/usr/bin/node
/* 8 (adv). Return sorted list of character names from a movie (sync). */

const request = require('request');
const movieId = process.argv[2];

const apiUrl = `http://swapi.dev/api/films/${movieId}`;
const charactersMap = {};

request(apiUrl, (err, res, data) => {
  if (err) {
    throw err;
  }
  const characters = JSON.parse(data).characters;
  let completed = 0;
  
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        throw error;
      }
      const character = JSON.parse(body);
      charactersMap[character.url] = character.name;
      completed++;
      
      if (completed === characters.length) {
        characters.forEach(url => {
          console.log(charactersMap[url]);
        });
      }
    });
  });
});
