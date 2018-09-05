<?php
if (!isset($_SESSION['user_hack'])) {
?>
<form method="post" action="?p=login&go">
Login :&nbsp;<input type="text" name="pseudo" value="" />&nbsp;&nbsp;&nbsp;&nbsp;
Pass :&nbsp;<input type="password" name="passwd" value="" />&nbsp;&nbsp;&nbsp;
<input type="submit" value="Log-in" />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="?p=register"><?php echo register; ?></a>
</form>
<?
} else {
echo '<a href="?">' . home . '</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <a href="?p=memberlist">' . memberlist . '</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
	  <a href="?p=profile">' . profile . '</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
	  ' . (($_SESSION['admin_hack']==1)?'<a href="admin/">Administration</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;':"") . '
	  <a href="?p=logout">' . logout . '</a>';


}
?>