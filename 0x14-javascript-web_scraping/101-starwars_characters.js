#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/', function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  for (let i = 0; i < data.results.length; i++) {
    if (i === Number(process.argv[2]) - 1) {
      for (let y = 0; y < data.results[i].characters.length; y++) {
        request(data.results[i].characters[y], function (error, response, body) {
          if (error) {
            console.log(error);
          }
          console.log(JSON.parse(body).name);
        });
      }
      break;
    }
  }
});
