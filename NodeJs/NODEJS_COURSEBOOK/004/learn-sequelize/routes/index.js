var express = require('express');
const user = require('../models/user');
var User = require('../models').User;

var router = express.Router();

router.get('/', async (req, res, next) =>
{
    try
    {
      const users = await User.findAll();

      //console.log( users );
      res.render('sequelize', { users });
    }
    catch(error)
    {
      console.error(error);
      next(error);
    }
});

module.exports = router;
