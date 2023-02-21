<?php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        for($i=0; $i<count($nums); $i++) {
			for($j=0; $j<count($nums); $j++) {
				if ($i==$j) continue;
				if (($nums[$i]+$nums[$j]) == $target) {
					return array($i, $j);
				}
			}
		}
    }
}

//print_r( Solution::twoSum([2,7,11,15], 9) );
//print_r( Solution::twoSum([3,2,4], 6) );
print_r( Solution::twoSum([3,3], 6) );