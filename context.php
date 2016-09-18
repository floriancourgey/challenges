
<!DOCTYPE html>
<html>
<head>
	<title><?= $titre ?></title>
	<meta charset="UTF-8">
</head>
<body>

</body>
</html>
<?php
require_once "config.php";
function get($relativeUrl){
	$c = curl_init("http://www.newbiecontest.org/".$relativeUrl);
	curl_setopt($c, CURLOPT_COOKIE, getCookies()) ;
	curl_setopt($c, CURLOPT_RETURNTRANSFER, true);
	$retour = curl_exec ($c);
	curl_close($c);
	return $retour;
}
function post($relativeUrl, $array){
	// conversion de l'array en données post html
	$fields_string = '';
	foreach($array as $key=>$value){
		$fields_string .= 'rep'.($key+1).'='.$value.'&';
	}
	rtrim($fields_string, '&');

	$c = curl_init("http://www.newbiecontest.org/".$relativeUrl);
	curl_setopt($c, CURLOPT_POST, count($array));
	curl_setopt($c, CURLOPT_POSTFIELDS, $fields_string);
	curl_setopt($c, CURLOPT_COOKIE, getCookies()) ;
	curl_setopt($c, CURLOPT_RETURNTRANSFER, 1);
	$retour = curl_exec ($c);
	curl_close($c);
	return $retour;
}

function getCookies(){
	$cookies = "SMFCookie89=".SMFCookie89.";";
	if(defined(PHPSESSID)){
		$cookies .= "PHPSESSID=".PHPSESSID;
	}
	return $cookies;
}
?>
