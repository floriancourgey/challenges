<?php
$a = "H";
$b = "F";
$c = "";
$nbEnleves = 2;
while($nbEnleves < 1000000000){
	$c = $a.$b;
	$a = $b;
	$b = $c;
	$nbEnleves += strlen($c);
	// echo $c."<br/>";
}
echo $c."<br/>";
exit();

$retour = get("epreuves/prog/frok-fichus_nb/prog_2.php");
echo $retour;
preg_match('@enlever ([0-9]*) habitants@', $retour, $m);
$nbHabitantsAEnlever = 5;//$m[1];
$a = 1;
$b = 2;
$c = 0;
$nbAnneesPourEnleverLesHabitants=1;
while($c <= $nbHabitantsAEnlever){
	$c = $a+$b;
	$a = $b;
	$b = $c;
	$nbAnneesPourEnleverLesHabitants++;
}
echo $nbAnneesPourEnleverLesHabitants." années pour enlever ".$nbHabitantsAEnlever." habitants<br/>";
preg_match("@la ([0-9]*)ème année@", $retour, $m);
$anneeCaptivite = $m[1];
$c=0;
$cMoinsUn=0;
for ($i=0; $i < $anneeCaptivite; $i++) {
	$cMoinsUn = $c;
	$c = bcadd($a, $b);
	$a = $b;
	$b = $c;
	$nbAnneesPourEnleverLesHabitants++;
}
echo $cMoinsUn." captifs la ".$anneeCaptivite."ème année<br/>";