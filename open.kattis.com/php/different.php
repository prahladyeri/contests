<?php
$a=0;
$b=0;
while(fscanf(STDIN, '%d %d', $a, $b) === 2) {
	echo abs($a - $b) . "\n";
}