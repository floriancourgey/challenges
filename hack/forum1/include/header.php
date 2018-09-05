<?php

if (isset($_SESSION['user_hack']) && !empty($_SESSION['user_hack']))
{
	$login = secu($_SESSION['user_hack']);
	$req = mysql_query("SELECT * FROM membres_hack WHERE login='$login'", $db) or die(mysql_error());
		if (mysql_num_rows($req) == 1)
		{
			$data = mysql_fetch_array($req);
			define("LANGUAGE", stripslashes($data['langue']));
		} else die("Roh le vilain hacker ;)");
}
else define("LANGUAGE", "FR");
?>