//round 2 of api_key boogaloo, CORS stops me from doing this nicely and i dont care enough to do it better :3
const key = "64a7b3d673c540e790020329c9420dc4";

'use strict';

var map
const tvform = document.querySelector('#source')
tvform.addEventListener('submit', async function (evt) {
    document.getElementById("status").textContent = "Loading...";
    evt.preventDefault();
    if (map) {
        map.remove();
    }
    document.getElementById("map").innerHTML = '';
    const startAddress = document.forms["f"]["q"].value;    
    const endAddress = "Karaportti 2";
    //console.log(key);
    const sresult = await fetch(`https://api.digitransit.fi/geocoding/v1/search?text=${startAddress}&digitransit-subscription-key=${key}`);
    const sjson = await sresult.json();
    const sLon = sjson.features[0].geometry.coordinates[0];
    const sLat = sjson.features[0].geometry.coordinates[1];
    const eresult = await fetch(`https://api.digitransit.fi/geocoding/v1/search?text=${endAddress}&digitransit-subscription-key=${key}`);
    const ejson = await eresult.json();
    const eLon = ejson.features[0].geometry.coordinates[0];
    const eLat = ejson.features[0].geometry.coordinates[1];
    //console.log(ejson);//LAT, LON
    //console.log(eLat);

    const graphql = `query {
  planConnection(
    origin: {location: {coordinate: {latitude: ${sLat}, longitude: ${sLon}}}, label: "${startAddress}"}
    destination: {location: {coordinate: {latitude: ${eLat}, longitude: ${eLon}}}, label: "${endAddress}"}
    first: 2
  ) {
    pageInfo {
      endCursor
    }
    edges {
      node {
        start
        end
        legs {
          from {
            name
          }
          to {
            name
          }
          start {
            scheduledTime
          }
          end {
            scheduledTime
          }
          mode
          duration
          realtimeState
          legGeometry {
          points
          }
        }
        emissionsPerPerson {
          co2
        }
      }
    }
  }
}`;//LAT, LON
    console.log(graphql);
    const Gquery = `https://api.digitransit.fi/routing/v2/finland/gtfs/v1`;
    //console.log(query);
    const result = await fetch(Gquery, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'digitransit-subscription-key': key,
        },
        body: JSON.stringify({ query: graphql })
    });
    const json = await result.json();
    console.log(json);

    if (json.data.planConnection.edges[0] != undefined) {
        const googleEncodedRoute = json.data.planConnection.edges[0].node.legs;
        console.log(googleEncodedRoute);


        map = L.map('map').setView([(sLat + eLat) / 2, (sLon + eLon) / 2], 13 - ((Math.abs(sLat - eLat) + Math.abs(sLon - eLon)) * 4));//LAT, LON

        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);


        for (let i = 0; i < googleEncodedRoute.length; i++) {
            const route = (googleEncodedRoute[i].legGeometry.points);
            const pointObjects = L.Polyline.fromEncoded(route).getLatLngs();
            L.polyline(pointObjects).setStyle({
                "color": "#ff7800",
                "weight": 5,
                "opacity": 0.9
            }).addTo(map);
        }


        var geojsonFeature = {
            "type": "Feature",
            "properties": {
                "name": "Route between " + startAddress + " and Karaportti 2",
                "amenity": "Route",
                "popupContent": "It insists upon itself."
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [[0, 51.505], [1, 51.505]] //LAT, LON
            }
        };
        var myStyle = {
            "color": "#ff7800",
            "weight": 5,
            "opacity": 0.9
        };
        L.geoJSON(geojsonFeature, { style: myStyle }).addTo(map);
        document.getElementById("status").textContent = "Route found";
    }
    else { document.getElementById("status").textContent = "Place not found :("; }
});

//Author's note: fun challenge, i would rather do a few of these instead of dozens of menial assignments. :3