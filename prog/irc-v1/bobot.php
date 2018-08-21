<?PHP
set_time_limit(0);
error_reporting(E_ALL);

// example use of the boboirc class 

// define your variables
$host = "irc.worldnet.net";
$port=6667;
$nick="dabobot"; // change to something unique. this aint gonna try twice.
$ident="mybot";
$chan="#nc-irc-challs";
$realname = "ima bobot";


echo "including irc class...\r\n";
require_once('class.boboirc.php');

echo "initiating irc class and connecting...\r\n";
$ircbot = new boboirc($nick, $ident, $realname, $host, $port);

echo "joining channel..\r\n";
$ircbot->joinChan($chan); 

echo "entering loop..\r\n";
$ircbot->loop();

echo "disconnected. \r\n";




?> 