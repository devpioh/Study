const cluster = require('cluster');
const http = require('http');
const numCPUs = require('os').cpus().length;


if( cluster.isMaster )
{
    console.log(`master process id : ${process.pid}`);
    // build worker cpu count

    for( let i = 0; i < numCPUs; i++ )
    {
        cluster.fork();
    }
    
    // end of worker
    cluster.on('exit', (worker, code, signal) => {
        console.log(`end worker number ${worker.process.pid}`);
        cluster.fork();
    });
}
else
{
    // waiting worker from port
    http.createServer((req, res) => {
        res.write('<h1>Hello Node!</h1>');
        res.end('<p>Hello Cluster!</p>');

        setTimeout(() => {
            process.exit(1);
        }, 1000);

    }).listen(8085);

    console.log(`work to number ${process.pid}`);
}


