<?php
require_once('context.php');
$retour = file_get_contents("http://www.newbiecontest.org/epreuves/prog/prog9/epreuve9.php", false, $context);
print_r($retour);
// PERSONNES
preg_match('@<hr width="90%" />(.*)\..*<br><br>@s', $retour, $m);
$textes = explode('. ', trim($m[1]));
$personnes = array();
foreach ($textes as $texte) {
	preg_match("@([a-zA-Z0-]*) a un processeur de ([0-9.]* [M,G]Hz) et dispose de ([0-9]* Mo [S,D]DRAM.*)@s", $texte, $infos);
	// var_dump($infos);
	array_push($personnes, array('nom'=>$infos[1], 'proc'=>$infos[2], 'ram'=>$infos[3]));
}
// var_dump($personnes);

// CONFIG RAM
preg_match("@(<tr align='center'>.*);\)@s", $retour, $a);
$texteRam = $a[1];
$texteRam = str_replace("	<td>", "", $texteRam);
$texteRam = str_replace("</td align='center'>", "", $texteRam);
$texteRam = str_replace("</td>", "", $texteRam);
$texteRam = str_replace("\n</tr>", "", $texteRam);
$textesRam = explode("<tr align='center'>", $texteRam);
$nomRams = array();
$prixRams = array();
foreach ($textesRam as $t) {
	$t = trim($t);
	if(empty($t) || strlen($t)>50){
		continue;
	}
	preg_match("@(.*)\s(.*)@", $t, $m);
	array_push($nomRams, $m[1]);
	array_push($prixRams, intval($m[2]));
}
var_dump($nomRams);
var_dump($prixRams);

// CONFIG PROC
preg_match("@Tarifs des processeurs.*Prix \(en euros\)(.*)</table>@s", $retour, $a);
$texteProc = $a[1];
$texteProc = str_replace("	<td>", "", $texteProc);
$texteProc = str_replace("</td align='center'>", "", $texteProc);
$texteProc = str_replace("</td>", "", $texteProc);
$texteProc = str_replace("\n</tr>", "", $texteProc);
$texteProc = explode("<tr align='center'>", $texteProc);
$nomProcs = array();
$prixProcs = array();
foreach ($texteProc as $t) {
	$t = trim($t);
	if(empty($t) || strlen($t)>50){
		continue;
	}
	if(preg_match("@^(.*)\s(.*)$@", $t, $m)){
		array_push($nomProcs, $m[1]);
		array_push($prixProcs, intval($m[2]));
	}
}
var_dump($nomProcs);
var_dump($prixProcs);


$max = array('nom'=>'', 'prix'=>0);
foreach($personnes as $p){
	echo $p['nom'];
	$prixProc = $prixProcs[array_search($p['proc'],$nomProcs)];
	$prixRam = $prixRams[array_search($p['ram'],$nomRams)];
	$total = $prixProc + $prixRam;
	echo 'proc('.$prixProc.')ram('.$prixRam.')tot('.$total.')';
	if($total > $max['prix']){
		$max['prix'] = $total;
		$max['nom'] = $p['nom'];
	}
	echo '<br/>';
}
var_dump($max);

// exit();
echo file_get_contents('http://www.newbiecontest.org/epreuves/prog/prog9/verifpr9.php?prenom='.$max['nom'].'&prix='.$max['prix'], false, $context);
