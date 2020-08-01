const http = require('http');
const fs = require('fs');

const users = {};

http.createServer((req, res) => {
    if( 'GET' === req.method ) {
        if('/' === req.url) {
            return fs.readFile('./restFront.html', (err, data) => {
                if(err) {
                    throw err;
                }
                res.end(data);
            });
        }
        else if('/about' === req.url) {
            return fs.readFile('./about.html', (err, data) => {
                if(err) {
                    throw err;
                }
                res.end(data);
            });
        }
        else if('/users' === req.url) {
            return res.end(JSON.stringify(users));
        }

        return fs.readFile(`.${req.url}`, (err, data) => {
            if(err) {
                res.writeHead(404, 'NOT FOUND');
                return res.end('NOT FOUND');
            }
            return res.end(data);
        });
    }
    else if( 'POST' === req.method ) {
        if('/users' === req.url) {
            let body = '';
            req.on('data', (data) => {
               body += data; 
            });

            return req.on('end', () => {
                console.log('POST BODY:', body);
                const { name } = JSON.parse(body);
                const id = Date.now();
                users[id] = name;

                res.writeHead(201);
                res.end('Success Register');
            });
        }
    }
    else if( 'PUT' === req.method ) {
        if(req.url.startsWith('/users/')) {
            const key = req.url.split('/')[2];
            let body = '';
            req.on('data', (data) => {
                body += data;
            });

            return req.on('end', () =>  {
                console.log('PUT BODY:', body);
                users[key] = JSON.parse(body).name;
                return res.end(JSON.stringify(users));
            });
        }
    }
    else if( 'DELETE' === req.method ) {
        if(req.url.startsWith('/users/')) {
            const key = req.url.split('/')[2];
            delete users[key];

            return res.end(JSON.stringify(users));
        }   
    }
    res.writeHead(404, 'NOT FOUND');
    return res.end('NOT FOUND');
}).listen(8085, () => {
    console.log('Waiting Server from 8085 Port');
});
