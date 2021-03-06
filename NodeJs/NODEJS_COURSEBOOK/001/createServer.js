//import { http } from 'http';
const http = require('http');

const server = http.createServer((req, res) => {
    res.write('<h1>Hello Node!</h1>');
    res.end('<p>Hello Server</p>');
});

server.listen(8080);

server.on('listening', () => {
    console.log('waiting server from 8080 port');
});

server.on('error', (error) => {
    console.error(error);
});

