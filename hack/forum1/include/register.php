<?php
if (isset($_GET['go']) && !empty($_POST['mail']) && !empty($_POST['pseudo']) && !empty($_POST['passwd']) && !empty($_POST['langue']))
{
$login = secu($_POST['pseudo']);
$pass = secu($_POST['passwd']);
$mail = $_POST['mail'];
$langue = secu($_POST['langue']);
	if (verif_mail($mail))
	{
		$v = mysql_query("SELECT id FROM membres_hack WHERE login='$login' OR mail='$mail'", $db) or die(mysql_error());
		if (!mysql_num_rows($v))
		{
			mysql_query("INSERT INTO membres_hack (login, pass, mail, langue) VALUES('$login','$pass','$mail','$langue')", $db) or die(mysql_error());
			$_SESSION['user_hack'] = stripslashes($login);
			echo ins_success;
			echo "<script>self.location.href=\"?\";</script>";
		} else erreur(ins_err1);
	} else erreur(ins_err2);
}
else
{
?>
<form method="post" action="?p=register&go">
Login :&nbsp;<input type="text" name="pseudo" value="" /><br />
Pass :&nbsp;<input type="text" name="passwd" value="" /><br />
Mail :&nbsp;<input type="text" name="mail" value="" /><br />
<select name="langue">
<option value="FR">Français
<option value="EN">English
</select><br /><br />
<input type="submit" value="<? echo register; ?>" />
</form>
<?
}
?>