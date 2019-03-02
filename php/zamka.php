<?php
$values = array();
for ($i=1; $i<=3; $i++) {
	fscanf(STDIN, '%d', $val);
	$values[$i] = $val;
}
$l = $values[1];
$d = $values[2];
$x = $values[3];

$min = $d;
$max = $l;

//print_r("$l $d $x");

for ($i=$l; $i<=$d; $i++) {
	$sum = 0;
	for($j=0; $j<strlen($i); $j++) {
		$digit = substr($i, $j, 1);
		$sum += $digit;
	}
	if ($sum == $x) {
		if ($i < $min) $min = $i;
		if ($i > $max) $max = $i;
		//echo "digit sum for $i: $sum\n";
	}
}

echo "$min\n$max";
