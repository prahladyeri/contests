stdin = process.openStdin();
stdin.addListener("data", function(d) {
    // note:  d is an object, and when converted to a string it will
    // end with a linefeed.  so we (rather crudely) account for that  
    // with toString() and then trim()
	var s = d.toString().trim();
	var nums = s.split(" ");
	var a = parseInt(nums[0]);
	var b = parseInt(nums[1]);
    console.log("you entered: ",a,b);
  });