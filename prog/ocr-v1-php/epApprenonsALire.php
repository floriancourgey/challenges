<!-- nb lignes : 13 -->
<!-- nb colonnes : 8*6 -->
<?php

$s = file_get_contents("epApprenonsALire.txt");
$lettresConfig = array();
$ligneActuel = 0;
$lettre = '';
// var_dump($s);
for ($i=0; $i < strlen($s); $i++) { 
	$c = $s[$i];
	// echo $c;

	// si retour à la ligne
	if($c == "\r"){
		$ligneActuel++;
		if($ligneActuel > 13){
			$ligneActuel = 0;
		}
		continue;
		// echo '<br/>';
	}
	if($c == "\n"){
		continue;
	}
	
	// echo '<br/>';

	// définition index lettre
	if($ligneActuel == 0){
		$lettre = $c;
		// echo $lettre;
		$lettresConfig[$lettre] = array();
	} 
	// ajout dans la string
	else {
		if(!isset($lettresConfig[$lettre][$ligneActuel-1])){
			$lettresConfig[$lettre][$ligneActuel-1] = '';
		}
		$lettresConfig[$lettre][$ligneActuel-1] .= $c;
	}

}
// var_dump($lettresConfig);
// exit();
?>



<html>
<head>
<style type="text/css">
html{
	font-family: "Courier New", Courier, monospace;
}
</style>
</head>
</html>
<?php
function String2Hex($string){
    $hex='';
    for ($i=0; $i < strlen($string); $i++){
        $hex .= dechex(ord($string[$i]));
    }
    return $hex;
}
$nom = "epApprenonsALire.png";
require_once('context.php');
$retour = file_get_contents(URL, false, $context);
$binary = @hex2bin(String2Hex($retour));
file_put_contents($nom, $retour);
$file = imagecreatefrompng($nom);
echo  '<img src="'.$nom.'" alt="Smiley face" height="200" width="400">';
$largeur = getimagesize($nom)[0];
$hauteur = getimagesize($nom)[1];
echo '<br/>';

$commence = false;
$indexLigneCommencee = 0;
$fini = false;
$lettres = array();
// recherche du texte
for ($i=0; $i<$hauteur&&!$fini ; $i++) { 
	for ($j=0; $j<$largeur&&!$fini; $j++) {
		$val = imagecolorat($file,$j,$i);
		// echo $val;
		// début du message
		if($commence==false && $val==1){
			// echo 'commence<br/>';
			$commence = true;
			$indexLigneCommencee = $i;
		}
		// if($commence)
	}
	if($commence && $indexLigneCommencee+9==$i){
		// echo '<br/>FINI';
		$fini = true;
	}
	// echo '<br/>';
}
// élimination du texte au dessus, en dessous
$lignes = array();
for ($i=$indexLigneCommencee; $i<$indexLigneCommencee+13 ; $i++) {
	$ligneCommencee = false;
	$ligne = "";
	for ($j=0; $j<$largeur; $j++) {
		$val = imagecolorat($file,$j,$i);
		if((!$ligneCommencee && $val==1) || $ligneCommencee){
			$ligneCommencee = true;
			$ligne .= $val;
			// echo $val;
		}
	}
	array_push($lignes, $ligne);
	// echo '<br/>';
}
// élimination du texte à gauche
$maxJ = 0;
for ($i=0; $i < 13; $i++) {
	$j = strlen($lignes[$i]);
	if($j > $maxJ){
		$maxJ = $j;
	}
}
for ($i=0; $i < 13; $i++) {
	while(strlen($lignes[$i]) <= $maxJ){
		$lignes[$i] = '0'.$lignes[$i];
	}
}
// élimination du texte à droite
for ($i=0; $i < 13; $i++) {
	$lignes[$i] = substr($lignes[$i], 0, 8*6);
}

// créa lettres
$lettres = array();
for ($i=0; $i < 13; $i++) {
	$ligne = $lignes[$i];
	$ligneLettre = "";
	for ($j=0, $k=0; $j < 8*6; $j++) { 
		$ligneLettre .= $ligne[$j];
		if(($j+1)%8 == 0 && $j!=0){
			if(!isset($lettres[$k])){
				$lettres[$k] = array();
			}
			array_push($lettres[$k], $ligneLettre);
			$k++;
			$ligneLettre = '';
		}
	}
}

// élimination des espaces à droite
for ($j=0; $j < count($lettres); $j++) { 
// for ($j=0; $j < 1; $j++) { 
	$lettre = $lettres[$j];
	$min = 99;
	$max = 0;
	foreach ($lettre as $ligneLettre) {
		$pos = intval(strrpos($ligneLettre, '1'));
		if($pos>$max){
			$max = $pos;
		}
		$pos = intval(strpos($ligneLettre, '1'));
		// var_dump($pos);
		if($pos<$min){
			$min = $pos;
		}
	}
	for ($i=0; $i < count($lettre); $i++) { 
		// echo 'de '.$min.' a '.$max.'<br/>';
		// echo $lettre[$i].'<br/>';
		$lettres[$j][$i] = substr($lettre[$i], $min+1, $max);
		// echo $lettre[$i].'<br/>';
	}
}

// var_dump($lettres);
$y = '';

// pour chaque lettre
foreach ($lettres as $lettre) {
	// echo 'NOUVELLE LETTRE == <br/>';
	// pour chaque lettre config
	foreach ($lettresConfig as $key=>$lettreConfig){
		$flag = true;
		// echo 'nv lettre config '.$key.'<br/>';
		// on lit les lignes des lettres
		for ($i=0; $i < 13; $i++) { 
			// si diff, on break
			// echo $lettre[$i].'|'.$lettreConfig[$i].((strcmp($lettre[$i], $lettreConfig[$i]) != 0)?' different':' identique').'<br/>';
			if(strcmp($lettre[$i], $lettreConfig[$i]) != 0){
				$flag = false;
				break;
			} 
			// echo 'ligne OK<br/>';
		}
		if($flag){
			// echo 'lettre OK<br/>';
			break;
		}
	}
	if(!$flag){
		echo 'XXX<br/>';
		for ($j=0; $j < count($lettre); $j++) {
			echo $lettre[$j];
			echo '<br/>';
		}
	} else {
		$y .= $key;
	}
}


// echo coloré
foreach ($lettres as $lettre) {
	foreach ($lettre as $ligneLettre) {
		for ($j=0; $j < strlen($ligneLettre); $j++) { 
			$v = $ligneLettre[$j];
			if($v==0){
				echo '<span style="background-color: black;">_</span>';
			} else {
				echo '<span style="background-color: yellow;">_</span>';
			}
		}
		echo '<br/>';
	}
}
for ($i=0; $i < count($lignes); $i++) {
	for ($j=0; $j < strlen($lignes[$i]); $j++) { 
		$v = $lignes[$i][$j];
		if($v==0){
			echo '<span style="background-color: black;">_</span>';
		} else {
			echo '<span style="background-color: yellow;">_</span>';
		}
	}
	echo '<br/>';
}
var_dump( $y);
if(strlen($y) == 6)
// exit();
echo file_get_contents(URL.$y, false, $context);
