<?php
fscanf(STDIN, '%d', $n);
$ss = "";
for($i=0; $i<$n; $i++) {
	$ss .= "%d ";
}
$ss = trim($ss);

$temp = fscanf(STDIN, $ss);
$cnt = 0;
foreach($temp as $val) {
	if ($val != abs($val)) $cnt++;
}
echo $cnt;
