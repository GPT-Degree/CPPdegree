// Initialize and add the map
let map;

async function initMap() {
  // The location of Uluru
  const position = { lat: 34.0556, lng: -117.8193 };
  const position2 = { lat: 33.8823, lng: -117.8851 };
  const position3 = { lat: 34.0664, lng: -118.1685 };
  const center = { lat: 33.9931, lng: -117.9687 };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("map"), {
    zoom: 10,
    center: center,
    mapId: "DEMO_MAP_ID",
  });

  // The marker, positioned at Uluru
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "CPP",
  });
  const marker2 = new AdvancedMarkerElement({
    map: map,
    position: position2,
    title: "CSUF",
  });
  const marker3 = new AdvancedMarkerElement({
    map: map,
    position: position3,
    title: "CSULA",
  });
}

initMap();
