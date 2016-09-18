<?php
	$s=0;
	$nb=1000;
	for($i=1;$i<=$nb;$i++) {
		$a=(string)($i);
		for($j=0;$j<strlen($a);$j++) {
			if ($a[$j]=="0") {
				$s++;
			}
		}
	}
	var_dump($s);