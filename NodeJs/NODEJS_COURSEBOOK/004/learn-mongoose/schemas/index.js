const mongoose = require('mongoose');

module.exports = () =>
{
    const connect = () =>
    {
        if(process.env.NODE_ENV !== 'production')
        {
            mongoose.set('debug', true);
        }

        mongoose.connect( 'mongodb://[id]:[password]@localhost:27017/admin',
        {
            dbName: 'nodejs',
        },
        (error) => 
        {
            if(error)
                console.error( 'error!! connection mongodb', error );
            else
                console.log('success!! connection mongodb');
        });
    };

    connect();
    mongoose.connection.on('error', (error) =>
    {
       console.error('connection error mongodb', error);         
    });
    mongoose.connection.on('disconnected', () => 
    {
        console.error( 'disconnected mongodb... try reconnect...');
        connect();
    });

    require('./user');
    require('./comment');
};