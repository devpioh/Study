//import { http } from 'http';
//import { fs } from 'fs';
const http = require('http');
const fs = require('fs');


http.createServer((req, res) => {
    fs.readFile('./first_web.html', (err, data) => {
        if(err)
        {
            throw err;
        }
        res.end(data);
    });
}).listen(8081, () => {
    console.log('Waiting Server from 8081');
});
