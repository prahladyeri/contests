<?php
class Solution {

    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
		return (strrev($x) == $x);
	}
}

echo Solution::isPalindrome(121);