<?php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function searchInsert($nums, $target) {
        $r = array_search($target, $nums);
		if ($r) return $r;
		for($i=0; $i<count($nums); $i++) {
			if ($nums[$i]>=$target) {
				return $i;
			}
		}
		return $i;
    }
}

echo Solution::searchInsert([1,3,5,6], 5); //2
//echo Solution::searchInsert([1,3,5,6], 2); //1
//echo Solution::searchInsert([1,3,5,6], 7); //4
//echo Solution::searchInsert([1], 1); //0