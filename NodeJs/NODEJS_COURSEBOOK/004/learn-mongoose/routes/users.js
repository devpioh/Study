var express = require('express');
var User = require('../schemas/user');

var router = express.Router();

router.get( '/', async (req, res, next) => 
{
  try
  {
    const users = await User.find({});
    res.json(users);
  }
  catch(error)
  {
    console.error(error);
    next(error);
  }
});

router.post('/', async (req, res, next) => 
{
  try
  {
    // const user = new User({
    //   name: req.body.name,
    //   age: req.body.age,
    //   married: req.body.married,  
    // });

    // const result = await user.save();
    // console.log(result);
    // res.status(201).json(result);


    const user = await User.create({
      name: req.body.name,
      age: req.body.age,
      married: req.body.married,
    });
    
    console.log(user);
    res.status(201).json(user);
  }
  catch(error)
  {
    console.error(error);
    next(error);
  }
});



module.exports = router;
