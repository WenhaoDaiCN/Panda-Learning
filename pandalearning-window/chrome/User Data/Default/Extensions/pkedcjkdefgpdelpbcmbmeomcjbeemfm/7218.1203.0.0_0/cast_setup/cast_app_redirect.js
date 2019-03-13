// Get "devices" from cast_app/devices.html.
var hash = location.pathname.split('/')[2].split('.')[0];
history.replaceState({},'', 'index.html#' + hash);

// history.replaceState dosen't load the new page, so load it here.
location.reload();
