<?php
fscanf(STDIN, '%d %d %d %d %d %d', $a, $b, $c, $d, $e, $f);

//create array (k, q, r, b, k, p)
$items = array($a, $b, $c, $d, $e, $f);

//reference array
$ref = array(1, 1, 2, 2, 2, 8);

//get missing
for($i=0; $i<count($ref); $i++) {
	echo ($ref[$i] - $items[$i]) . ($i==count($ref)-1 ? "" : " ");
}
