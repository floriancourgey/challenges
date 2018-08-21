<?php
$titre = "localhost";
$regex = "@(([0-9]{1,2}/){4,}[0-9]{1,2})@";
require_once('context.php');
$retour = get("epreuves/prog/prog14.php");
echo $retour;
$xxx = 0;
$firstTime = true;
$nbParties = 0;
do{

	e("===========================================================");
	e("======================== TOUR ".(2*$xxx+1)." PARTIE ".($nbParties+1)."============================");
	e("===========================================================");
	preg_match_all($regex, $retour, $m);
	if($firstTime){
		$tirage = $m[0][0];
		$firstTime = false;
	} else {
		$tirage = $m[0][1];
	}
	if(!is_string($tirage)){
		e("Erreur dans le tirage(".$tirage);
		break;
	}
	e('tirage : '.$tirage);
	$tasDec = explode('/', $tirage);
	$nbTas = count($tasDec);
	// conversion tasDec en entier
	for ($i=0; $i < $nbTas; $i++) { 
		$tasDec[$i] = intval($tasDec[$i]);
	}
	// recherche du plus grand entier du tas
	$max = 0;
	$max2 = 0;
	foreach ($tasDec as $value) {
		if($value > $max){
			$max2 = $max;
			$max = $value;
		} else if($value>$max2){
			$max2 = $value;
		}
	}
	$tailleMax = strlen(decbin($max));

	// si on arrive à la fin
	if($max2 == 1 || $max2 == 0){
		e("1(".$max.")2(".$max2.")");
		// on compte le nombre de tas non nul
		$nbTasNonNul = 0;
		for ($i=0; $i < $nbTas; $i++) { 
			if($tasDec[$i] != 0){
				$nbTasNonNul++;
			}
		}
		// si c'est pair, j'enlève le premier non nul
		if($nbTasNonNul%2 == 0){
			e("CHANGEMENT DE STRAT, j'enlève le premier non nul");
			for ($i=0; $i < $nbTas; $i++) { 
				if($tasDec[$i] != 0){
					$noTas=$i;
					$noPions=$tasDec[$i];
					break;
				}
			}
		}
		// sinon, j'enlève n-1 au premier tas != 1
		else {
			e("CHANGEMENT DE STRAT, j'enlève n-1 au premier >1");
			for ($i=0; $i < $nbTas; $i++) {
				if($tasDec[$i] > 1){
					$noTas=$i;
					$noPions=$tasDec[$i]-1;
					break;
				}
			}
		}
	}
	// sinon
	else {
		// calcul de la somme
		$pstGagnante = false;
		$memoire = 0;
		$noTas=1;
		$noPions=1;
		// pour chacun des tas
		for ($m=0; $m<$nbTas && !$pstGagnante ; $m++) {
			// j'enlève X
			$memoire = $tasDec[$m];
			for ($n=0; $n<$memoire  && !$pstGagnante ; $n++) {
				if($tasDec[$m] == 0){
					break;
				}
				$tasDec[$m]--;
				// e('tasDec :');
				// var_dump($tasDec);
				// je convertis en binaire
				// pour chacun des tas, conversion en binaire
				$tasBin = array();
				foreach ($tasDec as $dec) {
					$s = decbin($dec);
					while(strlen($s) < $tailleMax){
						$s = '0'.$s;
					}
					array_push($tasBin, $s);
				}
				// e('tasBin :');
				// var_dump($tasBin);

				// et je cherche si je suis gagnant
				$pstGagnante = true;
				$s = "";
				for ($i=0; $i < $tailleMax; $i++) { 
					$sDec = 0;
					foreach ($tasBin as $bin) {
						$sDec += intval($bin[$i]);
					}
					$s .= $sDec;
					if($sDec % 2 != 0){
						$pstGagnante = false;
						break;
					}
				}
				if($pstGagnante){
					$noTas=$m;
					$noPions=$n+1;
				}
				$bool = ($pstGagnante)?"true":"false";
				// e('tas('.$m.')valTas('.$tasDec[$m].')Somme('.$s.')gagnant('.$bool.')');
			}
			if($pstGagnante){
				e('tas('.$m.')valTas('.$tasDec[$m].')Somme('.$s.')gagnant('.$bool.')');
			}
			$tasDec[$m] = $memoire;
		}
		var_dump($s);
		var_dump($pstGagnante);
	}
	var_dump($tasDec);
	e('noTas('.$noTas.')noPions('.$noPions.')');
	// exit();
	$xxx++;
	$url = "epreuves/prog/prog14.php?numtas=".($noTas+1)."&nbpions=".$noPions;
	e("url(".$url);
	e("===========================================================");
	e("======================== TOUR ".(2*$xxx)."============================");
	e("===========================================================");
	$retour = get($url);
	echo $retour;
	if(preg_match('@Vous avez gagné !@', $retour)){
		$xxx = 0;
		$retour = get("epreuves/prog/prog14.php");
		echo $retour;
		$firstTime = true;
		$nbParties++;
		if($nbParties > 3){
			break;
		}
	}
}while($xxx < 50);


function e($s){
	echo $s.'<br/>';
}