<?php
function appel($var)
{
	if (file_exists($var)) include($var);
	else die("Il manque un fichier ");
}

function secu($var)
{
	return ((get_magic_quotes_gpc()) ? $var : addslashes($var) );
}

function verif_mail($mail)
{
	if (preg_match("/[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}/", $mail)) return 1;
	else return 0;
}

function erreur($var)
{
	echo "<script>alert('" . (addslashes($var)) . "'); history.go(-1);</script>";
}
?>