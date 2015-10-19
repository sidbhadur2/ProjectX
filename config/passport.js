var _ = require('lodash');
var passport = require('passport');
var LocalStrategy = require('passport-local').Strategy;
var secrets = require('../secrets');
var User = require('../schema/user.js');

passport.serializeUser(function(user, done) {
  done(null, user);
});

passport.deserializeUser(function(user, done) {
  User.findById(user.id).then(function(){
    done(null, user);
  });
  });

/**
 * Sign in using Email and Password.
 */
passport.use(new LocalStrategy(
  function(username, password, done) {
    User.find({ where: { username: username }}).then(function(user) {
      if (!user) {
        done(null, false, { message: 'Unknown user' });
      } else if (password != user.password) {
        done(null, false, { message: 'Invalid password'});
      } else {
        done(null, user);
      }
    }).error(function(err){
      done(err);
    });
  }
));