#!/usr/bin/node

/*
Get characters from Star Wars Movie
*/

const request = require('request');
const idMovie = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films' + idMovie;

const getName = async (ch) => {
  return new Promise((resolve, reject) => {
    request(ch, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        const jsonBody = JSON.parse(body);
        resolve(jsonBody.name);
      }
    });
  });
};

const getMovie = async () => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        const jsonBody = JSON.parse(body);
        resolve(jsonBody.characters);
      }
    });
  });
};

(async () => {
  return getMovie();
})().then(async (movies) => {
  if (typeof (movies) === 'object') {
    for (const ch of movies) {
      const name = await getName(ch);
      if (typeof (movies) === 'object') {
        console.log(name);
      }
    }
  }
});
