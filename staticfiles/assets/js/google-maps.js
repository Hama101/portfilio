function initMap() {
    // Latitude and Longitude
    var myLatLng = {lat: 35.038849 , lng: 9.490260};

    var map = new google.maps.Map(document.getElementById('google-maps'), {
        zoom: 10,
        center: myLatLng
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'Sidi Bouzid' // Title Location
    });
}