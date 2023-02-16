<?php
// 1 1 2 
$lst = [];

function fibonacci($n,$k) {
	global $lst;
	if ($n<=$k) {
		array_push($lst, 1);
		return 1;
	}
	else {
		$sm = array_sum(array_slice($lst, $n-$k-1));
		array_push($lst, $sm);
		return $sm;
	}
}


$temp = fopen("php://stdin","r");
$line = fgets($temp);

$t = explode(" ",$line);
$n = $t[0];
$k = $t[1];

//echo $n," ", $k;
for ($i=1;$i<$n+1;$i++) {
	$res = fibonacci($i, $k);
	//echo $i," ",$res, "\n";
}
//echo sprintf("And the result is %d.\n", $res);
//echo sprintf("And the result is %d.\n", $res%(1000000007));
echo $res%(1000000007)."\n";
