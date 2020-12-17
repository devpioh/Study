const KaKaoStrategy = require('passport-kakao').Strategy;
const { User } = require('../models');

module.exports = (passport) =>
{
    passport.use( new KaKaoStrategy(
    {
        clientID: process.env.KAKAO_ID,
        callbackURL: '/auth/kakao/callback',
    },
    async (accessTocken, refreshToken, profile, done) =>
    {
        try
        {
            console.log('kakao profile => ', profile);

            const exUser = await User.findOne({ where: {snsId: profile.id, provider: 'kakao'} });

            if(exUser)
                done(null, exUser);
            else
            {
                const newUser = await User.create(
                {
                    email: profile._json && profile._json.kaccount_email,
                    nick: profile.displayName,
                    snsId: profile.id,
                    provider: 'kakao',
                });
                done(null, newUser);
            }
        }
        catch(err)
        {
            console.error(err);
            done(err);
        }
    }));
};