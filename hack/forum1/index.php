<?php
session_start();
if (file_exists("include/config.php")) include("include/config.php");
else die("Il manque le fichier de configuration");
?><html>
<head>
<link rel="stylesheet" href="style.css" />
</head>
<body>
<center><h2>Fuckin' Forum</h2>
<br />
<table width="60%" bgcolor="#CCCCFF" height="90%">
<tr valign="top"><td>
<?php appel("include/menu.php"); ?>
</td></tr>
<tr><td valign="top" align="center"><br />
<?php
if (isset($_SESSION['user_hack'])) {
	if (in_array($_GET['p'], $allowed_pages_log)) appel("include/" . $_GET['p'] . ".php");
	else appel("include/main.php");
}
else
{
	if (in_array($_GET['p'], $allowed_pages_nolog)) appel("include/" . $_GET['p'] . ".php");
	else appel("include/main.php");
}
?></td>
</tr>
</table></center>
</body>
</html>
<?php
mysql_close($db);
?>