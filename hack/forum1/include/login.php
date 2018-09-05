<?php
if (isset($_GET['go']) && !empty($_POST['pseudo']) && !empty($_POST['passwd']))
{
	$login = secu($_POST['pseudo']);
	$pass = secu($_POST['passwd']);
	$req = mysql_query("SELECT id, mail, admin FROM membres_hack WHERE login='$login' AND pass='$pass'", $db) or die(mysql_error());
		if (mysql_num_rows($req) == 1)
		{
			$a = mysql_fetch_array($req);
			$_SESSION['user_hack'] = stripslashes($login);
			$_SESSION['mail_hack'] = $a['mail'];
			($a['admin']==1)?($_SESSION['admin_hack'] = 1):"";
			echo login_success;
			echo "<script>self.location.href=\"?\";</script>";
		} else erreur(login_err1);
}
else erreur(login_err1);
?>