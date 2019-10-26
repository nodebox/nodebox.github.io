function confirm_delete() {
	var b = confirm("This page will be moved to the Trash folder.");
	if (b) {
		return true ;
	} else {
		return false ;
	}
}