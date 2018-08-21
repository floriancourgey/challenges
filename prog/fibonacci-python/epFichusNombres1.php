<?php
$time = microtime();

$dico = file_get_contents("epFichusNombres.txt");
// var_dump($dico);
$index = 0;
$liste = array();
for($i=0 ; $i<3951 ; $i++){
	// echo $dico[$i];
	if(ord($dico[$i]) == 10){
		// echo '<br/>';
		$index++;
		continue;
	} else {
		if(!isset($liste[$index])){
			$liste[$index] = '';
		}
		$liste[$index] .= $dico[$i];
	}
}

require_once('context.php');
$retour = get("epreuves/prog/frok-fichus_nb/prog_1.php");
// echo $retour;
preg_match_all("@([0-9]{6,7})@", $retour, $m);
$anagrammes = $m[1];
// var_dump($anagrammes);


// pour chaque anagramme
$anagrammesDecodes = array();
foreach ($anagrammes as $anagramme) {
	// on regarde dans toute la liste du dico
	foreach ($liste as $value) {
		// check meme taille
	 	$taille = strlen($anagramme);
		if(strlen($value) != $taille){
			continue;
		}
		$flag = true;
		// on regarde si tous les chiffres existent
		for($i=0 ; $i<$taille ; $i++){
			// chiffre
			$chiffre = $value[$i];
			// nb fois qu'il apparait dans le dico
			$nbDico = preg_match_all("@".$value[$i]."@", $value);
			$nbAna = preg_match_all("@".$value[$i]."@", $anagramme);
			if($nbAna != $nbDico){
				$flag = false;
				break;
			}
			// if(preg_match_all("@".$value[$i]."@", $anagramme) == 0){
			// 	$flag = false;
			// 	break;
			// }
			// if(strpos($anagramme, $value[$i]) === FALSE){
			// 	$flag = false;
			// 	break;
			// }
		}
		//
		if($flag){
			array_push($anagrammesDecodes, $value);
			// echo $anagramme.' en '.$value.'<br/>';
			break;
		}
	}
}


// var_dump($anagrammesDecodes);



// $curl_instance=curl_init();
// curl_setopt($curl_instance, CURLOPT_URL, URL) ;
// curl_setopt($curl_instance, CURLOPT_POST, count($anagrammes));
// curl_setopt($curl_instance, CURLOPT_POSTFIELDS, $fields_string);
// curl_setopt($curl_instance, CURLOPT_COOKIE, "Cookie=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2255733%22%3Bi%3A1%3Bs%3A40%3A%229d7f3bfccaa88609c97b73c31412f1e409c9d541%22%3Bi%3A2%3Bi%3A1612301728%3Bi%3A3%3Bi%3A0%3B%7D") ;
// curl_setopt($curl_instance, CURLOPT_RETURNTRANSFER, 1);
// $retour = curl_exec ($curl_instance);
$retour = post("epreuves/prog/frok-fichus_nb/verif_1.php", $anagrammesDecodes);

preg_match('@est: (.*)\.@', $retour, $m);
if(isset($m[1]))
	$login = $m[1];
else
	exit($retour);
echo 'Le login est '.$login.'<br/>';

?>