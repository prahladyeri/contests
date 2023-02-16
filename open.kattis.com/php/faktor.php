<?php
fscanf(STDIN, '%d %d', $n, $ifact);
$ifact = ($ifact - 1) + 0.01; //rounding allowed, so make target easy to achieve
echo ceil($n*$ifact);
