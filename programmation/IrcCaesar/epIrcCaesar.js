var irc = require('irc');
var client = new irc.Client('irc.worldnet.net', 'dfghjklertyui', {
    channels: ['#nc-irc-challs'],
});
client.say("NickServ ", "identify dfghjklertyui");
client.addListener('error', function(message) {
    console.log('error: ', message);
});
client.addListener('message', function (from, to, message) {
    console.log(from + ' => ' + to + ': ' + message);
});
client.join("#nc-irc-challs", function(){
    console.log("Je suis connecté !");
    client.say('#nc-irc-challs', "I'm a bot!");
})
