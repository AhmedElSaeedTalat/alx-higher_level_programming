#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  let counter = 0;
  const dict = {};
  for (let i = 1; i <= data[data.length - 1].userId; i++) {
    for (let y = 0; y < data.length; y++) {
      if (data[y].userId === i && data[y].completed === true) {
        counter += 1;
      }
    }
    dict[String(i)] = counter;
    counter = 0;
  }
  console.log(dict);
});
