#!/usr/bin/node
// Star War API interview question implemented using nodejs

const request = require('request');
const FILMID = process.argv[2];

// Star war root or base url
const URL_BASE = 'https://swapi-api.hbtn.io/api/films';

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(error);
      }
    });
  });
}

// Using the function, doRequest to make a call

async function main (filmID) {
  const res = await doRequest(`${URL_BASE}/${filmID}`);
  for (const e of res.characters) {
    const pj = await doRequest(e);
    console.log(pj.name);
  }
}

main(FILMID);