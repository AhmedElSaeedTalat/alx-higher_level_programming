#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
