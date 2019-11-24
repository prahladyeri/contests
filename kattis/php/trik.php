<?php
fscanf(STDIN, '%s', $ss);
$current = 1;
for($i=0; $i<strlen($ss); $i++) {
	$oper = substr($ss, $i, 1);
	switch($oper) {
		case "A":
			if ($current != 1 && $current != 2) break; //no impact
			$current = ($current==1 ? 2 : 1);
			break;
		case "B":
			if ($current != 2 && $current != 3) break; //no impact
			$current = ($current==2 ? 3 : 2);
			break;
		case "C":
			if ($current != 1 && $current != 3) break; //no impact
			$current = ($current==3 ? 1 : 3);
			break;
	}
	//echo "oper: $oper, current: $current\n";
}

echo $current;
