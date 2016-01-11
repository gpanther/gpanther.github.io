Title: Places to visit

<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
<script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
<link rel="stylesheet" href="/extra/leaflet-control-geocoder/Control.Geocoder.css" />
<script src="/extra/leaflet-control-geocoder/Control.Geocoder.js"></script>
<div id="map" style="height: 600px"></div>

<script>
(function () {
	var map = new L.Map('map');                       
                
	L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
		maxZoom: 18
	}).addTo(map);

	var center = new L.LatLng(46.7712101, 23.6236353); 
	map.setView(center, 1);

	var markers = [
		[ 48.1853715, 16.3189717, "Vienna Zoo" ],
		[ 37.4143233, -122.0773213, "Computer History Museum" ],
	];
         
	for (var i=0; i<markers.length; i++) {
		var lat = markers[i][0];
		var lon = markers[i][1];
		var popupText = markers[i][2];

		var markerLocation = new L.LatLng(lat, lon);
		var marker = new L.Marker(markerLocation);
		map.addLayer(marker);
         
		marker.bindPopup(popupText);
	}
})();
</script>

[Geocoder](http://www.gpsvisualizer.com/geocode)
