<?php
require_once 'db_params.php';
$allowed_pages_log=array("memberlist","logout","profile");
$allowed_pages_nolog=array("register","login");
if (file_exists("include/fonctions.php")) include("include/fonctions.php");
else die("Il manque un fichier");
$db = @mysql_connect(HOST, USER, PASS) or die(mysql_error());
mysql_select_db(DB, $db) or die(mysql_error());
appel("include/header.php");
appel("langue/" . LANGUAGE . ".php");
?>
