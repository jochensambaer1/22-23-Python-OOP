$(document).ready(function() {
    $('#bikesTable').DataTable({
        "ajax": "static/bikes.geojson",
        "columns": [
            {"data": "id"},
            {"data": "latitude"},
            {"data": "longitude"},
            {"data": "state"},
            {"data": "borrow_time"}
        ]
    });
});
