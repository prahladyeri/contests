<?php
$x = $y = 0;
$i = 1; //line number
//$values = array();
while(fscanf(STDIN, '%d', $val) === 1)
{
	if ($i == 1) {
		$x = $val;
	}
	else if ($i == 2) {
		$y = $val;
	}
	if ($i  == 2) break;
	$i++;
}

$xpos = (abs($x) == $x);
$ypos = (abs($y) == $y);

if ($xpos && $ypos) {
	$quad = 1;
}
else if (!$xpos && $ypos) {
	$quad = 2;
}
else if (!$xpos && !$ypos) {
	$quad = 3;
}
else if ($xpos && !$ypos) {
	$quad = 4;
}

echo $quad;
//echo $x . "::" . $n . "\n";
//echo $x, " ", $y;
//~ print_r($values);

//~ $bal = 0;
//~ for($i=0;$i<count($values);$i++) {
	//~ $bal += $x;
	//~ $spent = $values[$i];
	//~ $bal -= $spent;
//~ }


//~ echo ($bal + $x);
