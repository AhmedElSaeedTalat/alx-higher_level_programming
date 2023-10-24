#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  for (let i = 0; i < data.characters.length; i++) {
    request(data.characters[i], function (error, response, body) {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
