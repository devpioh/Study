const local = require('./localStrategy');
const kakao = require('./kakaoStrategy');
const { User } = require('../models');


module.exports = (passport) => 
{
    passport.serializeUser((user, done) => { done(null, user.id); });
    
    passport.deserializeUser(async (id, done) => 
    {
        //User.findOne({ where: { id } }).then(user=> doen(null, user)).catch(err=>done(err));
        try
        {
            const user = await User.findOne({
                where: {id},
                include: [{
                    model: User,
                    attributes: ['id', 'nick'],
                    as: 'Followers',
                },
                {
                    model: User,
                    attributes: ['id', 'nick'],
                    as: 'Followings',
                }],
            });

            done(null, user);
        }
        catch(err)
        {
            console.error(err);
            done(err);
        }
    });

    local(passport);
    kakao(passport);
};
