#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  let counter = 0;
  for (let i = 0; i < data.results.length; i++) {
    for (let y = 0; y < data.results[i].characters.length; y++) {
      if (data.results[i].characters[y].endsWith('/18/')) {
        counter += 1;
      }
    }
  }
  console.log(counter);
});
