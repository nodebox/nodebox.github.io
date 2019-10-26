function pop(url, name, params) {
	newWindow = window.open('', name, params);
	newWindow.focus();
	if (newWindow.opener == null) newWindow.opener = self;
	newWindow.location.href=url;
}