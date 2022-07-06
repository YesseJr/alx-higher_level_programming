#!/usr/bin/node
  const request = require('request');
  request('http://swapi.co/api/films/' + process.argv[2], function (err, resp, body) {
    if (err) {
      console.log(err);
    } else if (resp.statusCode === 200 && resp.headers['content-type'] === 'application/json') {
      console.log(JSON.parse(body).title);
    }
  });if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body['title']);
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
