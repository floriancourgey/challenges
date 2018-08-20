<?php

$context = stream_context_create(array("http" => array ("header" => "Cookie: Cookie=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2255733%22%3Bi%3A1%3Bs%3A40%3A%229d7f3bfccaa88609c97b73c31412f1e409c9d541%22%3Bi%3A2%3Bi%3A1612301728%3Bi%3A3%3Bi%3A0%3B%7D\r\n"))) ;
$retour = file_get_contents(URL, false, $context) ;
$k = preg_split("/ /", $retour);
// var_dump($keywords[stri]);
echo file_get_contents(URL.$k[9], false, $context);
