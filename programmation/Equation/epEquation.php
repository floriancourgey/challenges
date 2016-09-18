<?php
require_once('context.php');
$retour = file_get_contents("http://www.newbiecontest.org/epreuves/prog/prog4.php", false, $context);
$equation = preg_split("/ /", $retour)[0];
// $match = array();
var_dump($equation);
preg_match("/racine\((.{1,2})\)\*(.{1,2})&sup2;\+(...)/", $equation, $match);
var_dump($match);
$y = sqrt($match[1])*pow($match[2],2)+$match[3];
// echo "équation racine(".$match.")*".;
$y = intval($y);
var_dump($y);
echo file_get_contents('http://www.newbiecontest.org/epreuves/prog/verifpr4.php?solution='.$y, false, $context);
