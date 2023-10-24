#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  function checkId (id) {
    return id === 'https://swapi-api.alx-tools.com/api/people/18/';
  }
  const counterList = [];
  for (let i = 0; i < data.results.length; i++) {
    if (data.results[i].characters.filter(checkId).length !== 0) {
      counterList.push(data.results[i].characters.filter(checkId));
    }
  }
  console.log(counterList.length);
});
