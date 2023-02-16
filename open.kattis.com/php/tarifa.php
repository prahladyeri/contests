<?php
$x = $n = 0;
$i = 1; //line number
$values = array();
while(fscanf(STDIN, '%d', $val) === 1)
{
	if ($i == 1) {
		$x = $val;
	}
	else if ($i == 2) {
		$n = $val;
	}
	else {
		$values[($i - 2 - 1)] = $val;
	}
	if ($i - 2 == $n) break;
	$i++;
}

$bal = 0;
for($i=0;$i<count($values);$i++) {
	$bal += $x;
	$spent = $values[$i];
	$bal -= $spent;
}


echo ($bal + $x);
