//import "/styles.css";
import L from 'leaflet';
var map = L.map('map').setView([51.505, -0.09], 13);
L.geoJSON('route.geojson').addTo(map);