var passport = require('passport');
var _ = require('lodash');
var async = require('async');
var crypto = require('crypto');
var passport = require('passport');
var User = require('../schema/user.js');
var Sequelize = require('sequelize');
/*
 * GET /login
 * Login page.
 */
exports.getLogin = function(request, response) {
  //console.log(req);
  if (request.user) return response.redirect('/');
  response.render('pages/login');
};

/**
 * POST /login
 * Sign in using email and password.
 */
exports.postLogin = function(req, res, next) {


  passport.authenticate('local', function(err, user, info) {
    if (err) return next(err);
    if (!user) {
      req.flash('errors', { msg: info.message });
      console.log("invalid");
      return res.redirect('/login');
    }
    req.logIn(user, function(err) {
      if (err) return next(err);
      req.flash('success', { msg: 'Success! You are logged in.' });
      res.redirect(req.session.returnTo || '/');
    });
  })(req, res, next);
};

/**
 * GET /logout
 * Log out.
 */
exports.logout = function(request, response) {
  req.logout();
  res.redirect('/');
};

/**
 * GET /signup
 * Signup page.
 */
exports.getSignup = function(request, response) {
  //if (req.user) return res.redirect('/');
  response.render('pages/signup');
  console.log('get ');
};

/**
 * POST /signup
 * Create a new local account.
 */
exports.postSignup = function(req, res, next) {

console.log('here1');

User.findOne({where: {username:req.body.username}})
  .then(function(existingUser){
      if(existingUser) {
          req.flash('errors', { msg: 'Account with that email address already exists.' });
          console.log("nope");
          return res.redirect('/signup');
        }
  });

var user = User.create({
    username: req.body.username,
    password: req.body.password,
});

};


/*** GET PROFILE ***/

