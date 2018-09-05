<?php
echo '<h2>' . memberlist . '</h2><br /><br />';
$champ=empty($_GET['type'])? "id" : secu($_GET['type']);
$ord=empty($_GET['ord'])? "DESC" : "";
$req=mysql_query("SELECT login, admin FROM membres_hack ORDER BY $champ $ord", $db) or die(mysql_error());
if (mysql_num_rows($req))
{ 
	$next_login=!empty($ord)?(($champ=="login")?"&ord=1":""):"";
	$next_admin=!empty($ord)?(($champ=="admin")?"&ord=1":""):"";

	echo '<table width="80%" border="1"><tr>
	      <td id="pp"><a href="?p=memberlist&type=login' . $next_login . '">' . user . '<a/></td>
		  <td id="pp"><a href="?p=memberlist&type=admin' . $next_admin . '">' . admin . '</a></td></tr>';

	while($data = mysql_fetch_array($req))
		echo '<tr><td align="center">' . htmlentities(stripslashes($data['login'])) . '</td>
				  <td align="center">' . $data['admin'] . '</td></tr>';
		
	echo '</table>';
}
else echo ml_error;
?>