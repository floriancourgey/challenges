<script type="text/javascript">
	function Check() {
		var tab="azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789_$&#@";
		checksum=3696619;
		var login=document.forms["flog"].elements["login"].value;
		var password="souris";
		var tailleLogin=login.length;
		var taillePass=password.length;
		var sum=1;
		var n=Math.max(tailleLogin,taillePass);
		sum2tot = 0;
		for (var i=0;i<n;i++) {
			var index1=tab.indexOf(login.substring(i,i+1))+10;
			console.log("index1("+index1);
			var index2=tab.indexOf(password.substring(i,i+1))+10;
			console.log("index2("+index1);
			sum1 = (index1*n*(i+1));
			sum2 = (index2*(i+1)*(i+1));
			sum2tot += sum2;
			console.log("sum1("+sum1);
			console.log("sum2("+sum2);
			sum=sum+sum1*sum2;
			console.log("\n");
		}
		console.log("sum2tot("+sum2tot);
        if (sum==checksum) {
			window.location="/epreuves/javascript/"+login+".php";
		} else {
			alert("Mauvais login ou mot de passe sum("+sum);
		}
	}
	function Verifie() {
		Check(3696619)
	}
	
</script>

<form onsubmit="Verifie();return false;" action="#" method="get" name="flog">
	<table border="0">
	  <tbody><tr>
		<td>Login : </td>
		<td><input name="login" size="8" type="text"></td>
	  </tr>
	  <tr>
		<td colspan="2" align="center"><input name="bouton" value="Tester" type="submit"></td>
	  </tr>
	</tbody></table>
	</form>