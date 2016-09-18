<?php
function e($t){
	echo $t.'<br/>';
}
require_once('context.php');
$retour = file_get_contents("http://www.newbiecontest.org/epreuves/prog/progsudoku.php", false, $context);
$retour = trim(preg_replace('/\s+/', ' ', $retour));
print_r($retour);
preg_match_all("/<td class=\"chiffe1?\">([0-9])<\/td>/", $retour, $m);
$tableau = htmlToObject($m[1]);

do{
	// pour chaque case du tableau
	for($i=0 ; $i<9 ; $i++){
		for($j=0 ;$j<9 ; $j++){
			$case = $tableau[$i][$j];
			// si elle est vide
			if($case->valeur == 0){
				// e('case['.$i.','.$j.'] vide');
				// 
				// ELIMINATION PAR LIGNE COLONNE
				// 
				// on regarde sur toute sa colonne
				$potentiel = $case->potentiel;
				// e('sur la colonne');
				for($k=0 ; $k<9 ; $k++){
					if($tableau[$k][$j]->valeur != 0){
						if(in_array($tableau[$k][$j]->valeur, $potentiel)){
							// e($tableau[$k][$j]->valeur.' en '.($k).','.($j));
							unset($potentiel[array_search($tableau[$k][$j]->valeur, $potentiel)]);
						}
					}
				}
				// puis toute sa ligne
				// e('sur la ligne');
				for($k=0 ; $k<9 ; $k++){
					if($tableau[$i][$k]->valeur != 0){
						if(in_array($tableau[$i][$k]->valeur, $potentiel)){
							// e($tableau[$i][$k]->valeur.' en '.($k).','.($j));
							unset($potentiel[array_search($tableau[$i][$k]->valeur, $potentiel)]);
						}
					}
				}
				// 
				// ELIMINATION PAR CARRE
				// 
				// pour chaque ligne du carré
				for($y=0 ; $y<3 ; $y++){
					// pour chaque colonne du carré
					for($z=0 ; $z<3 ; $z++){
						$case_testee = $tableau[$y+3*$case->carre_vertical][$z+3*$case->carre_horizontal];
						if(in_array($case_testee->valeur, $potentiel)){
							// e($case_testee->valeur.' en '.($y+3*$case->carre_vertical).','.($z+3*$case->carre_horizontal));
							unset($potentiel[array_search($case_testee->valeur, $potentiel)]);
						}
					}
				}
				

				$case->potentiel = $potentiel;
				// e('potentiel :'.$case->p());
			} else {
				// e('case['.$i.','.$j.'] : '.$case->valeur);
			}
		}
		// echo '<br/>';
	}

	$val_trouvee = false;
	for($i=0 ; $i<9 ; $i++){
		for($j=0 ;$j<9 ; $j++){
			if(count($tableau[$i][$j]->potentiel) == 1){
				$tableau[$i][$j]->valeur = current(array_filter($tableau[$i][$j]->potentiel));
				$tableau[$i][$j]->potentiel = array();
				e('valeur '.$tableau[$i][$j]->valeur.' trouvee en case['.$i.','.$j.']');
				$val_trouvee = true;
			}
		}
	}
	if(!$val_trouvee){
		$termine = true;
		e( 'aucune val trouvee... Recherche des potentiel 2(ou terminé ?)');
		for($i=0 ; $i<9 ; $i++){
			for($j=0 ;$j<9 ; $j++){
				if(count($tableau[$i][$j]->potentiel) == 2){
					// $tableau[$i][$j]->valeur = current(array_filter($tableau[$i][$j]->potentiel));
					// $tableau[$i][$j]->potentiel = array();
					e('potentiel 2  '.$tableau[$i][$j]->p().' trouve en case['.$i.','.$j.']');
					// $val_trouvee = true;
				}
				if($tableau[$i][$j]->valeur == 0){
					$termine = false;
				}
			}
		}
	}
	printTableau($tableau);
	if(!$val_trouvee && $termine){
		e('CEST TERMINE');
		$y = '';
		for($i=0 ; $i<9 ; $i++){
			for($j=0 ;$j<9 ; $j++){
				$y .= $tableau[$i][$j]->valeur;
			}
			if($i != 8)
				$y .= '-';
		}
		e('url '.$y);
		echo file_get_contents('http://www.newbiecontest.org/epreuves/prog/verifprsudoku.php?solution='.$y, false, $context);
	}
}while($val_trouvee);


exit();
echo file_get_contents('http://www.newbiecontest.org/epreuves/prog/verifprsudoku.php?solution='.$y, false, $context);


function htmlToObject($table){
	$i=0;
	$j=0;
	for($carre_vertical=0 ; $carre_vertical<3 ; $carre_vertical++){
		for($ligne=0 ; $ligne<3 ; $ligne++){
			for($carre_horizontal=0 ; $carre_horizontal<3 ; $carre_horizontal++){
				for($trio=0 ; $trio<3 ; $trio++){
					echo $table[27*$carre_vertical+9*$carre_horizontal+3*$ligne+$trio];
					// echo $table[9*$carre_horizontal+3*$ligne+$trio].'('.(9*$carre_horizontal+3*$ligne+$trio).')';
					$tableau[$i][$j] = new Toto($i, $j, intval($table[27*$carre_vertical+9*$carre_horizontal+3*$ligne+$trio]), $carre_vertical, $carre_horizontal);
					$j++;
				}	
			}
			echo '<br/>';
			$i++;
			$j=0;
		}
	}
	return $tableau;
}

function printTableau($tableau){
	echo '++++++++++++++<br/>';
	for($i=0 ; $i<9 ; $i++){
		for($j=0 ;$j<9 ; $j++){
			if($j%3 == 0){
				echo '|';
			}
			echo $tableau[$i][$j]->valeur.'  ';
		}	
		echo '|<br/>';
		if(($i+1)%3 == 0 && $i !=8){
			echo '-----------------------<br/>';
		}
		
	}
	echo '++++++++++++++<br/>';
}

class Toto {
	var $valeur;
	var $potentiel;
	var $carre_vertical;
	var $carre_horizontal;
	var $i;
	var $j;

	public function Toto($i, $j, $valeur, $carre_vertical, $carre_horizontal){
		$this->i = $i;
		$this->j = $j;
		$this->carre_vertical = $carre_vertical;
		$this->carre_horizontal = $carre_horizontal;
		$this->potentiel = array();
		if($valeur == 0){
			for($i=0 ; $i<9 ; $i++){
				array_push($this->potentiel, $i+1);
			}
		}
		$this->valeur = $valeur;
	}

	public function p(){
		$r = '{';
		for($k=0;$k<9;$k++){
			if(isset($this->potentiel[$k]))
				$r .= $this->potentiel[$k].',';
		}
		$r .= '}';
		return $r;
	}
}
