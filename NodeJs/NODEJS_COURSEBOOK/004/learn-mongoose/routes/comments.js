const express = require('express');
const Comment = require('../schemas/comment');

var router = express.Router();

router.get( '/:id', async (req, res, next) =>
{
    try
    {
        const comments = await Comment.find({ commenter: req.params.id }).populate('commenter');
        
        console.log(comments);
        res.json(comments);
    }
    catch(error)
    {
        console.error(error);
        next(error);
    }
});

router.post( '/', async (req, res, next) => 
{
    try
    {
        // 할당 및 save() 동시...
        const comment = await Comment.create({
            commenter: req.body.id,
            comment: req.body.comment,
        }); 

        const result = await Comment.populate( comment, { path: 'commenter'} );
        res.status(201).json(result);
    }
    catch(error)
    {
        console.error(error);
        next(error);
    }
});

router.patch('/:id', async (req, res, next) =>
{
    try
    {
        const result = await Comment.update({_id: req.params.id}, {comment: req.body.comment});
        res.json(result);
    }
    catch(error)
    {
        console.error(error);
        next(error);
    }
});

router.delete( '/:id', async (req, res, next) => 
{
    try
    {
        const result = await Comment.remove({_id: req.params.id});
        res.json(result);
    }
    catch(error)
    {
        console.error(error);
        next(error);
    }
});

module.exports = router;