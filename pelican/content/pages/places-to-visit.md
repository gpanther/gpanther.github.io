Title: Places to visit

<link rel="stylesheet" href="/extra/leaflet/leaflet.css" />
<script src="/extra/leaflet/leaflet.js"></script>
<div id="map" style="height: 600px"></div>

<script>
(function () {
	var map = new L.Map('map');                       
                
	L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
		maxZoom: 18
	}).addTo(map);

	var center = new L.LatLng(46.7712101, 23.6236353); 
	map.setView(center, 1);

	var markers = [
		[ 48.1853715, 16.3189717, "Vienna Zoo" ],
		[ 37.4143233, -122.0773213, "Computer History Museum" ],
		[ 47.406968, 19.015177, "Csodák Palotája - csopa.hu" ],
		[ 47.7131424, 24.4375912, "Vişeu de Sus - cffviseu.ro" ],
		[ 33.1262476, -117.3115765, "Legoland California" ],
		[ 48.427275, 10.296693, "Legoland Deutschland" ],
		[ 51.462824, -0.647795, "Legoland England" ],
		[ 48.184865, 16.31224, "Schönbrunn" ],
		[ 48.190384, 16.31926, "Vienna Technical Museum" ],
		[ 44.805516, 20.469905, "Tesla Museum" ],
		[ 4.1754959, 73.5093474, "Maldives" ],
		[ 45.2025, 29.3132, "Pădurea Letea" ],
		[ 47.477824, 19.069902, "Pilots Repülőgépszimulátor-központ" ],
		[ 45.5889681, 25.4701133, "Dino Parc Râșnov" ],
		[ 45.8600472, 25.7923821, "Muzeu al radiocomunicaţiilor" ],
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

[Geocoder](http://www.gpsvisualizer.com/geocode) and [alternative geocoder](http://www.findlatitudeandlongitude.com/batch-geocode/)

