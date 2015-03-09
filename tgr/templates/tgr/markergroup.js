var markergroup = [
      {% for community in markergroup %}
      { lat: "{{ community.point.y }}", lng: "{{ community.point.x }}", title: "{{ community.name }}", icon: { url: "{{ community.marker.url }}", scaledSize: new google.maps.Size (24, 24) }, click: function(e) { $('#community-modal{{ community.publish|yesno:"-with-media," }}').foundation('reveal', 'open', '{% url 'community_modal' region=region.slug slug=community.slug %}'); }, opacity: 0.8 },
      {% endfor %}
];
