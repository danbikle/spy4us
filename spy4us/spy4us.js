if (Meteor.isClient) {

  Template.body.onRendered(function() {
    var myv1 = $('pre#pre_ff1').html();
    Session.set('ff1csv',myv1);
  });

  Template.body.helpers({
    myCollection: function() {
      return Session.get('ff1csv');
    }
  });

  // counter starts at 0
  Session.setDefault('counter', 0);

  Template.hello.helpers({
    counter: function () {
      return Session.get('counter');
    }
  });

  Template.hello.events({
    'click button': function () {
      // increment the counter when button is clicked
      Session.set('counter', Session.get('counter') + 1);
    }
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
