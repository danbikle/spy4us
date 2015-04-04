if (Meteor.isClient) {

  Template.hello.onRendered(function() {
    var myh1 = $('pre#pre_ff1');
    var myh2 = myh1.html()     ;
    var myp1 = Papa.parse(myh2);
    var myp2 = myp1.data       ;
    Session.set('ff1csv',myp2) ;
    myh1.hide();

  });

  // counter starts at 0
  Session.setDefault('counter', 0);

  Template.hello.helpers({
    myCollection: function() {return Session.get('ff1csv'); },
    counter:      function() {return Session.get('counter');}
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
