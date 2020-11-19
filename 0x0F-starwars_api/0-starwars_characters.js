#!/usr/bin/node

const URL = 'https://swapi-api.hbtn.io/api/';
const request = require('request');
const idMovie = process.argv[2];

async function getRequest (url) {
  return new Promise(function (resolve, reject) {
    request.get(url, function (err, resp, body) {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

(async function main () {
  try {
    const movie = await getRequest(URL + 'films/' + idMovie);
    if (typeof (movie) === 'object') {
      for (const characterURL of movie.characters) {
        const character = await getRequest(characterURL);
        if (typeof (character) === 'object') {
          console.log(character.name);
        }
      }
    }
  } catch (error) {

  }
})();
