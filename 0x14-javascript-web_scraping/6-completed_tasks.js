#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dict = {};
  for (let i = 0; i < data.length; i++) {
    if (dict[data[i].userId] && data[i].completed === true) {
      dict[data[i].userId] += 1;
    } else if (!dict[data[i].userId] && data[i].completed === true) {
      dict[data[i].userId] = 1;
    }
  }
  console.log(dict);
});
