<?php
?>
<script>
testor();
function testor(){
	var code = new Array("a", "b", "c", "d", "e", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z");
	// Meca = window.prompt("Password : ","");
	Meca = Math.round((code.length*54)/48-7+(45*3));
	alert(Meca);
	if(Meca != Math.round((code.length*54)/48-7+(45*3))) {
		alert("Erreur !!");
	} else {
		window.location.href="/epreuves/javascript/"+Meca+".php";
	}
	}
</script>