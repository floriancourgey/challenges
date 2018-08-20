<?php
require_once('context.php');
$retour = file_get_contents(URL, false, $context) ;
var_dump($retour);
preg_match("/'(.*)' <br/", $retour, $texte);
preg_match("/clef est : '(.*)'/", $retour, $cle);
$texte = $texte[1];
var_dump($texte);
$cle = $cle[1];
var_dump($cle);
var_dump(strlen($texte));
var_dump(strlen($cle));
$y = '';
for ($i=0; $i<strlen($texte); $i++){
	$y .= chr(ord($texte[$i])-$cle);
}
// exit();
var_dump($y);
echo file_get_contents(URL.$y, false, $context);
