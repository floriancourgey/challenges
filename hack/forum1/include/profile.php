<?php
if (isset($_GET['go']) && !empty($_POST['newpass1']) && ($_POST['newpass1']==$_POST['newpass2']) && !empty($_POST['oldpass']) && !empty($_POST['mail']))
{
$login=secu($_SESSION['user_hack']);
$newpass=secu($_POST['newpass1']);
$oldpass=secu($_POST['oldpass']);
$mail=$_POST['mail'];
	if (verif_mail($mail))
	{
		$verif = mysql_query("SELECT id FROM membres_hack WHERE login='$login' AND pass='$oldpass'", $db) or die(mysql_error());
		if (mysql_num_rows($verif)==1)
		{
			mysql_query("UPDATE membres_hack SET pass='$newpass', mail='$mail' WHERE login='$login'");
			echo profile_ok;
		} else erreur(pass_invalide);
	}else erreur(ins_err2);
}
else
{
echo '<form method="post" action="?p=profile&go">
' . change_pass . ' :&nbsp;<input type="password" name="newpass1" value="" /><br />
' . change_pass2 . ' :&nbsp;<input type="password" name="newpass2" value="" /><br /><br />
' . change_email . ' :&nbsp;<input type="text" name="mail" value="' . $_SESSION['mail_hack'] . '" /><br /><br />
' . text_confirm . '<br />
Pass : &nbsp;<input type="password" value="" name="oldpass" /><br /><br />
<input type="submit" value="' . send . '" />
</form>';
}
?>