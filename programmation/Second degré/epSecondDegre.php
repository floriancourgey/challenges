<?php
require_once('context.php');
$retour = file_get_contents(URL, false, $context);
$retour=preg_split("@:<br />@", $retour)[1];
var_dump($retour);
preg_match("/(.{1,2})x² [+,-] (.{1,2})x [+,-] (.{1,2}) = 0/", $retour, $m);
var_dump($m);
$a = $m[1];
$b = $m[2];
$c = $m[3];
$delta = $b*$b - 4*$a*$c;
$x1 = ($b - sqrt($delta))/(2*$a);
$x2 = ($b + sqrt($delta))/(2*$a);
$y = ($x1 > $x2) ? $x1 : $x2;
$y = number_format($y, 2);
// exit();
echo file_get_contents(URL.$y, false, $context);
