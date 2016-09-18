<?php
require_once('context.php');
$retour = file_get_contents("http://www.newbiecontest.org/epreuves/prog/prog3_1.php", false, $context) ;
$k = preg_split("/ /", $retour);
$a = $k[5];
var_dump($a);
$retour = file_get_contents("http://www.newbiecontest.org/epreuves/prog/prog3_2.php", false, $context) ;
$k = preg_split("/ /", $retour);
$b = $k[5];
var_dump($b);
$y = sqrt($a)*$b;
$y = intval($y);
var_dump($y);
echo file_get_contents('http://www.newbiecontest.org/epreuves/prog/verifpr3.php?solution='.$y, false, $context);
