var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', (req, res, next) => {
  //res.send('respond with a resource');
  next();
}, (req, res, next) => {
  console.log('1');
  next('route');
}, (req, res, next) => {
  console.log('2');
  next();
}, (req, res, next) => {
  console.log('3');
  next();
});

// router.get('/', (req, res) => {
//   console.log('I am Work!');
//   res.render('index', {title:'Express'});
// });

router.get('/:id',(req, res) =>
{
  console.log(req.params, req.query);
  // res.write( 'params : ' + String(req.params));
  // res.end('query : '+ String(req.query));
});

module.exports = router;
