<?php
fscanf(STDIN, '%d %d %d', $n, $w, $h);
$mx = sqrt(pow($w,2) + pow($h,2));
ob_start();
for($i=0;$i<$n;$i++) {
	fscanf(STDIN, '%d', $slen);
	echo ($slen<=$mx ? "DA" : "NE") . ($i==($n-1) ? "" : "\n");
}
ob_flush();
