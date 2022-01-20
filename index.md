<!DOCTYPE html>
<html>
<body>

<h2>My First JavaScript</h2>

<button type="button"
onclick="document.getElementById('demo').innerHTML = Date()">
Click me to display Date and Time.</button>

<div>
<head>    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_f81be1f6d3f64b86a2af11ace2b1d3e2 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
            </style>
        
    <script src="https://cdn.jsdelivr.net/gh/marslan390/BeautifyMarker/leaflet-beautify-marker-icon.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/marslan390/BeautifyMarker/leaflet-beautify-marker-icon.min.css"/>
</head>
<body>    
    
            <div class="folium-map" id="map_f81be1f6d3f64b86a2af11ace2b1d3e2" ></div>
        
</body>
<script>    
    
            var map_f81be1f6d3f64b86a2af11ace2b1d3e2 = L.map(
                "map_f81be1f6d3f64b86a2af11ace2b1d3e2",
                {
                    center: [49.225, -123.275],
                    crs: L.CRS.EPSG3857,
                    zoom: 9,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_fdf3082667d94b84b06747306a880108 = L.tileLayer(
                "https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png",
                {"attribution": "\u0026copy; \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors \u0026copy; \u003ca href=\"http://cartodb.com/attributions\"\u003eCartoDB\u003c/a\u003e, CartoDB \u003ca href =\"http://cartodb.com/attributions\"\u003eattributions\u003c/a\u003e", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
        
    
            var feature_group_20508be17e294f409fe58ef01f7f2234 = L.featureGroup(
                {}
            ).addTo(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
        
    
            var marker_699da318624b49978a036fcc7835793c = L.marker(
                [49.279367161347785, -123.2415175867091],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_813f79a56477404aba91a66e132e3f95 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_699da318624b49978a036fcc7835793c.setIcon(beautify_icon_813f79a56477404aba91a66e132e3f95);
        
    
            marker_699da318624b49978a036fcc7835793c.bindTooltip(
                `<div>
                     AcadiaBeach
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ef828547eb55437bb9fe7e7c73f18cfd = L.marker(
                [49.277086773057036, -123.22542452176616],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_30b58293a6fc4045932ae4c2eb243eba = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ef828547eb55437bb9fe7e7c73f18cfd.setIcon(beautify_icon_30b58293a6fc4045932ae4c2eb243eba);
        
    
            marker_ef828547eb55437bb9fe7e7c73f18cfd.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_3d7ed44926c34087921fe0156d62ca37 = L.marker(
                [49.277411549383096, -123.2281130458741],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_32deb3826cb742029800ffaf48bb9e40 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_3d7ed44926c34087921fe0156d62ca37.setIcon(beautify_icon_32deb3826cb742029800ffaf48bb9e40);
        
    
            marker_3d7ed44926c34087921fe0156d62ca37.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4615967633224d438e142a06ee04c0fc = L.marker(
                [49.277415748889865, -123.23157294794753],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_546fd512eb13440e839f1dd1dbb19fca = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_4615967633224d438e142a06ee04c0fc.setIcon(beautify_icon_546fd512eb13440e839f1dd1dbb19fca);
        
    
            marker_4615967633224d438e142a06ee04c0fc.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1ebd77f3eed84fc58a9e73d6ed2c0e09 = L.marker(
                [49.277465445144415, -123.23061039535486],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_06b2217dbfe14429be71d83428cc58a4 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_1ebd77f3eed84fc58a9e73d6ed2c0e09.setIcon(beautify_icon_06b2217dbfe14429be71d83428cc58a4);
        
    
            marker_1ebd77f3eed84fc58a9e73d6ed2c0e09.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_74c6603ce9ee44c1b97e3e32929e80c3 = L.marker(
                [49.278014899173215, -123.23105476271542],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_6286167efe96484eb4212b3b9fce0de5 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_74c6603ce9ee44c1b97e3e32929e80c3.setIcon(beautify_icon_6286167efe96484eb4212b3b9fce0de5);
        
    
            marker_74c6603ce9ee44c1b97e3e32929e80c3.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_eab420d688544625bd060d76a05b8ae5 = L.marker(
                [49.278299072800586, -123.23659531243227],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_ee9b901d8fc547ccb38b1e53f2c0ebb4 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_eab420d688544625bd060d76a05b8ae5.setIcon(beautify_icon_ee9b901d8fc547ccb38b1e53f2c0ebb4);
        
    
            marker_eab420d688544625bd060d76a05b8ae5.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_98bdddf7539e4fcf998c4812f7b684d4 = L.marker(
                [49.27887581508334, -123.24255526064007],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_1b86840bb8214443916f25dc274c5efd = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_98bdddf7539e4fcf998c4812f7b684d4.setIcon(beautify_icon_1b86840bb8214443916f25dc274c5efd);
        
    
            marker_98bdddf7539e4fcf998c4812f7b684d4.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_601ec5b3ca9940f8a18fed4448cc9cdd = L.marker(
                [49.27912008855083, -123.24128794767657],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_56604d9ae323430a8732cc75418e2758 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_601ec5b3ca9940f8a18fed4448cc9cdd.setIcon(beautify_icon_56604d9ae323430a8732cc75418e2758);
        
    
            marker_601ec5b3ca9940f8a18fed4448cc9cdd.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_65565d9ceb7e49709f9e8c6de69a6e92 = L.marker(
                [49.25079661267171, -123.22859905597366],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_d69453c4ec5b4ac3ba0cd739323bcd3a = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_65565d9ceb7e49709f9e8c6de69a6e92.setIcon(beautify_icon_d69453c4ec5b4ac3ba0cd739323bcd3a);
        
    
            marker_65565d9ceb7e49709f9e8c6de69a6e92.bindTooltip(
                `<div>
                     Aims
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_284bf9e02fd34186968942c9071d1027 = L.marker(
                [49.25036241002851, -123.1991790738853],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_6d18cb43162e46e6b407aeaefc60fbaf = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_284bf9e02fd34186968942c9071d1027.setIcon(beautify_icon_6d18cb43162e46e6b407aeaefc60fbaf);
        
    
            marker_284bf9e02fd34186968942c9071d1027.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a65c44057c714fc99e723928c4dbd33a = L.marker(
                [49.25146191592837, -123.19949840154771],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_8c44d67a57154229963af50b27adfde0 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_a65c44057c714fc99e723928c4dbd33a.setIcon(beautify_icon_8c44d67a57154229963af50b27adfde0);
        
    
            marker_a65c44057c714fc99e723928c4dbd33a.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_9439b231000143cf9c460c50a19d2e05 = L.marker(
                [49.251515840200796, -123.20023789104643],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_53c9526108704345900305a33be96607 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_9439b231000143cf9c460c50a19d2e05.setIcon(beautify_icon_53c9526108704345900305a33be96607);
        
    
            marker_9439b231000143cf9c460c50a19d2e05.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6dfed8d356fa4bce996de0fd0baa0a80 = L.marker(
                [49.2521125038212, -123.20027236031547],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_40474cfbd7c34c02ad4d01fab99f43e3 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6dfed8d356fa4bce996de0fd0baa0a80.setIcon(beautify_icon_40474cfbd7c34c02ad4d01fab99f43e3);
        
    
            marker_6dfed8d356fa4bce996de0fd0baa0a80.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_fd532d1c897d4c7d9e446832294fd7b8 = L.marker(
                [49.25213736475354, -123.19979137418355],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_f86e72ba6f5546778357da5d98589485 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_fd532d1c897d4c7d9e446832294fd7b8.setIcon(beautify_icon_f86e72ba6f5546778357da5d98589485);
        
    
            marker_fd532d1c897d4c7d9e446832294fd7b8.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4ed05631a474407e828c12dd96c24a95 = L.marker(
                [49.252193039182075, -123.19439576029895],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_b7b04d8f32914b57ad2366b224aab9bf = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_4ed05631a474407e828c12dd96c24a95.setIcon(beautify_icon_b7b04d8f32914b57ad2366b224aab9bf);
        
    
            marker_4ed05631a474407e828c12dd96c24a95.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c4ade575443b4b80ba6b1ea5b4b750f4 = L.marker(
                [49.25223645767689, -123.2001693855924],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_20688903575841d594b3364b9b0c278c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_c4ade575443b4b80ba6b1ea5b4b750f4.setIcon(beautify_icon_20688903575841d594b3364b9b0c278c);
        
    
            marker_c4ade575443b4b80ba6b1ea5b4b750f4.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_425a9d1c1c7041068c41d08094b073bc = L.marker(
                [49.25230228636072, -123.20074496538511],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_2c5004b5ff1e4ac9aa157504aff9d8d4 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_425a9d1c1c7041068c41d08094b073bc.setIcon(beautify_icon_2c5004b5ff1e4ac9aa157504aff9d8d4);
        
    
            marker_425a9d1c1c7041068c41d08094b073bc.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_29c116a862be40c2807fa7a4b2e567cb = L.marker(
                [49.25231454165429, -123.2005357974469],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_3c9fda6e1d9043a2ba1ef5dcfab0b0cf = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_29c116a862be40c2807fa7a4b2e567cb.setIcon(beautify_icon_3c9fda6e1d9043a2ba1ef5dcfab0b0cf);
        
    
            marker_29c116a862be40c2807fa7a4b2e567cb.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_18e1b1bf338e40b391177fb17fea950e = L.marker(
                [49.25241993699468, -123.20091128639652],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_778c75071faf4ceea3b9d4826db8e70c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_18e1b1bf338e40b391177fb17fea950e.setIcon(beautify_icon_778c75071faf4ceea3b9d4826db8e70c);
        
    
            marker_18e1b1bf338e40b391177fb17fea950e.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_bd44acd0fc4647a1b6b7b5591b28227d = L.marker(
                [49.2525852078819, -123.19963866360983],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_d46f2e40216043ce8795ab655a2fb869 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_bd44acd0fc4647a1b6b7b5591b28227d.setIcon(beautify_icon_d46f2e40216043ce8795ab655a2fb869);
        
    
            marker_bd44acd0fc4647a1b6b7b5591b28227d.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a3fd2af1839e4e359c0878c85e1f701f = L.marker(
                [49.25268885176815, -123.19904144965912],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_afa1d000c150427698ef005fec858df8 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_a3fd2af1839e4e359c0878c85e1f701f.setIcon(beautify_icon_afa1d000c150427698ef005fec858df8);
        
    
            marker_a3fd2af1839e4e359c0878c85e1f701f.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_0f71c6309bdf4ec3add0e745d08bd8a7 = L.marker(
                [49.25325188785817, -123.19591356867114],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_551b4fc2da914b7aacb2a264043fa771 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_0f71c6309bdf4ec3add0e745d08bd8a7.setIcon(beautify_icon_551b4fc2da914b7aacb2a264043fa771);
        
    
            marker_0f71c6309bdf4ec3add0e745d08bd8a7.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1b19efaf70c643c8857f789632a2dfdc = L.marker(
                [49.25330580996164, -123.19463067191795],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_89bdfec0580344fdad3b848830afec48 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_1b19efaf70c643c8857f789632a2dfdc.setIcon(beautify_icon_89bdfec0580344fdad3b848830afec48);
        
    
            marker_1b19efaf70c643c8857f789632a2dfdc.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6fb886841f464cb99b980b90695aeae2 = L.marker(
                [49.25335553050497, -123.20017713709967],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_12d99cdd7536491a8ff5f07a2111cf3c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6fb886841f464cb99b980b90695aeae2.setIcon(beautify_icon_12d99cdd7536491a8ff5f07a2111cf3c);
        
    
            marker_6fb886841f464cb99b980b90695aeae2.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_b0d4684cb1de40f9addd152b653ee6dc = L.marker(
                [49.25351169426171, -123.19909478573177],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_7e13832a63f64591895614351b909e19 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_b0d4684cb1de40f9addd152b653ee6dc.setIcon(beautify_icon_7e13832a63f64591895614351b909e19);
        
    
            marker_b0d4684cb1de40f9addd152b653ee6dc.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ffebd58da3074786a5b035d3331f3c65 = L.marker(
                [49.25380231193569, -123.19621549164158],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_19eb3a8062764ac78cef06dd429548f5 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ffebd58da3074786a5b035d3331f3c65.setIcon(beautify_icon_19eb3a8062764ac78cef06dd429548f5);
        
    
            marker_ffebd58da3074786a5b035d3331f3c65.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_9eb55553b0da4b7aa632917f158d99e2 = L.marker(
                [49.25409012688605, -123.196567880115],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_d32c204349694bc2b54968eb9e205447 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_9eb55553b0da4b7aa632917f158d99e2.setIcon(beautify_icon_d32c204349694bc2b54968eb9e205447);
        
    
            marker_9eb55553b0da4b7aa632917f158d99e2.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_caa76d4d80d94673a226e05705580ae6 = L.marker(
                [49.25413564504425, -123.19790011911398],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_43a9f47545394d789c8faad69f7697dc = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_caa76d4d80d94673a226e05705580ae6.setIcon(beautify_icon_43a9f47545394d789c8faad69f7697dc);
        
    
            marker_caa76d4d80d94673a226e05705580ae6.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_be3e77de5f00436e83a07efd45e252a0 = L.marker(
                [49.25434922861495, -123.20065255471519],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_af9c961f4a184d8d95d656de8c29b399 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_be3e77de5f00436e83a07efd45e252a0.setIcon(beautify_icon_af9c961f4a184d8d95d656de8c29b399);
        
    
            marker_be3e77de5f00436e83a07efd45e252a0.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_5b0096e1bafa492fa95e243c65d4eccc = L.marker(
                [49.2543597327169, -123.1993278244398],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_f8fde8e8007a40619b1c5e76f770f51a = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_5b0096e1bafa492fa95e243c65d4eccc.setIcon(beautify_icon_f8fde8e8007a40619b1c5e76f770f51a);
        
    
            marker_5b0096e1bafa492fa95e243c65d4eccc.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_8c2064e3cf7d4b3b9f6a064e6b833bd5 = L.marker(
                [49.25437583867633, -123.19693670213738],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_f3ba7b32c07a41e2a9d6560dab1a4ae6 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_8c2064e3cf7d4b3b9f6a064e6b833bd5.setIcon(beautify_icon_f3ba7b32c07a41e2a9d6560dab1a4ae6);
        
    
            marker_8c2064e3cf7d4b3b9f6a064e6b833bd5.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_8045483ae3394cc595f9f8139a0274b4 = L.marker(
                [49.25440174910239, -123.19976225015763],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_1ced6bf2b6384178a6046b0e5d776d0d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_8045483ae3394cc595f9f8139a0274b4.setIcon(beautify_icon_1ced6bf2b6384178a6046b0e5d776d0d);
        
    
            marker_8045483ae3394cc595f9f8139a0274b4.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_466859f689354a83b2854e472763a97e = L.marker(
                [49.25443256083923, -123.19702720576947],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_66f88c470e784ee38caa2c446d4603d6 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_466859f689354a83b2854e472763a97e.setIcon(beautify_icon_66f88c470e784ee38caa2c446d4603d6);
        
    
            marker_466859f689354a83b2854e472763a97e.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_33d1bba14eca4aadbfcb224b57bf6d59 = L.marker(
                [49.254461272574474, -123.19731552154306],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_bd586e4017db4bb9b0f7da640bb38cc9 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_33d1bba14eca4aadbfcb224b57bf6d59.setIcon(beautify_icon_bd586e4017db4bb9b0f7da640bb38cc9);
        
    
            marker_33d1bba14eca4aadbfcb224b57bf6d59.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_909013b720134f8e937a5ab81ea53369 = L.marker(
                [49.25454180346234, -123.19955844549989],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_3ea6167146af4cc78503a92cd5523b1d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_909013b720134f8e937a5ab81ea53369.setIcon(beautify_icon_3ea6167146af4cc78503a92cd5523b1d);
        
    
            marker_909013b720134f8e937a5ab81ea53369.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_dcc74c3c56984d11be4367b7159659ab = L.marker(
                [49.254572615646026, -123.1986059266925],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_cb46816df9cf4537af97cdd668e4a5b3 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_dcc74c3c56984d11be4367b7159659ab.setIcon(beautify_icon_cb46816df9cf4537af97cdd668e4a5b3);
        
    
            marker_dcc74c3c56984d11be4367b7159659ab.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7c7c4185c2284ac08c05d3a5180044ba = L.marker(
                [49.25474138055923, -123.19762659181015],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_910b8de209284f33b4bf85c8cc18eca7 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7c7c4185c2284ac08c05d3a5180044ba.setIcon(beautify_icon_910b8de209284f33b4bf85c8cc18eca7);
        
    
            marker_7c7c4185c2284ac08c05d3a5180044ba.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4e88490144734451be2032aa873cc228 = L.marker(
                [49.25481070699733, -123.19666120132608],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_37bbdbde17b6403897ceba5d6d719674 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_4e88490144734451be2032aa873cc228.setIcon(beautify_icon_37bbdbde17b6403897ceba5d6d719674);
        
    
            marker_4e88490144734451be2032aa873cc228.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7981a80a3f104cc5b7302779bfba06b5 = L.marker(
                [49.255118123847666, -123.20018701007947],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_5c2aebbef4154cd086def43880fcae25 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7981a80a3f104cc5b7302779bfba06b5.setIcon(beautify_icon_5c2aebbef4154cd086def43880fcae25);
        
    
            marker_7981a80a3f104cc5b7302779bfba06b5.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c98ba9c6782446f1a98112ea2c24a9eb = L.marker(
                [49.25567132785152, -123.20032106743712],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_528abf4a54324264b136106d1549784d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_c98ba9c6782446f1a98112ea2c24a9eb.setIcon(beautify_icon_528abf4a54324264b136106d1549784d);
        
    
            marker_c98ba9c6782446f1a98112ea2c24a9eb.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ca0df424a94845329accf5ced16b53fe = L.marker(
                [49.255701088670776, -123.20019771198635],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_5a2cb3705f3d41acbcd1a67c7e97c1d2 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ca0df424a94845329accf5ced16b53fe.setIcon(beautify_icon_5a2cb3705f3d41acbcd1a67c7e97c1d2);
        
    
            marker_ca0df424a94845329accf5ced16b53fe.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1c8d8082d96940e19f5d4ee7678b78b7 = L.marker(
                [49.255739602645555, -123.20028352447383],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_313932dfccef416fb0184e6400cd5450 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_1c8d8082d96940e19f5d4ee7678b78b7.setIcon(beautify_icon_313932dfccef416fb0184e6400cd5450);
        
    
            marker_1c8d8082d96940e19f5d4ee7678b78b7.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e630dd2422d8445093bc87798c00ed51 = L.marker(
                [49.25612159183446, -123.20159361174434],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_a9289ef9a032454ca666342bc816fdf4 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e630dd2422d8445093bc87798c00ed51.setIcon(beautify_icon_a9289ef9a032454ca666342bc816fdf4);
        
    
            marker_e630dd2422d8445093bc87798c00ed51.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a0a30b71c75c4487a90d53785452ca4a = L.marker(
                [49.25618321207332, -123.19954985242543],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_09bf18feb62a41cf9d22f47532d1c8db = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_a0a30b71c75c4487a90d53785452ca4a.setIcon(beautify_icon_09bf18feb62a41cf9d22f47532d1c8db);
        
    
            marker_a0a30b71c75c4487a90d53785452ca4a.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_36205fe49fbd4a74ab4a4c8a011b0924 = L.marker(
                [49.26902057980597, -123.2236407793207],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_be83c43173b9415cb0f6588ce1b3825c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_36205fe49fbd4a74ab4a4c8a011b0924.setIcon(beautify_icon_be83c43173b9415cb0f6588ce1b3825c);
        
    
            marker_36205fe49fbd4a74ab4a4c8a011b0924.bindTooltip(
                `<div>
                     Chancellor
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_eadbc31927874817a549a6ab012997f9 = L.marker(
                [49.270760211921264, -123.22665678758698],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_7514318bbe45495092691bc296cecaa2 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_eadbc31927874817a549a6ab012997f9.setIcon(beautify_icon_7514318bbe45495092691bc296cecaa2);
        
    
            marker_eadbc31927874817a549a6ab012997f9.bindTooltip(
                `<div>
                     Chancellor
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c2f1dea5cf8e4954b570344c34188a97 = L.marker(
                [49.27099752451536, -123.22886167332753],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_d28d393d1fa54dfab4917557ce89d78e = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_c2f1dea5cf8e4954b570344c34188a97.setIcon(beautify_icon_d28d393d1fa54dfab4917557ce89d78e);
        
    
            marker_c2f1dea5cf8e4954b570344c34188a97.bindTooltip(
                `<div>
                     Chancellor
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_b531c60365c64ef980ccd86aa0383805 = L.marker(
                [49.256059967672115, -123.21889919428973],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_7a84e0cf195a4b71bc45fc09ae8e88e2 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_b531c60365c64ef980ccd86aa0383805.setIcon(beautify_icon_7a84e0cf195a4b71bc45fc09ae8e88e2);
        
    
            marker_b531c60365c64ef980ccd86aa0383805.bindTooltip(
                `<div>
                     Cleveland
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e38b034c759648319950319567379f9f = L.marker(
                [49.25756688117963, -123.22096083715711],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_a9a3816dfcf548b7baf22b40d43a2bb9 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e38b034c759648319950319567379f9f.setIcon(beautify_icon_a9a3816dfcf548b7baf22b40d43a2bb9);
        
    
            marker_e38b034c759648319950319567379f9f.bindTooltip(
                `<div>
                     Cleveland
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_231113168249499c8c616f7518126103 = L.marker(
                [49.259608703512654, -123.22335500503388],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_1bcb2a455c27413e9a2cf03dab771560 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_231113168249499c8c616f7518126103.setIcon(beautify_icon_1bcb2a455c27413e9a2cf03dab771560);
        
    
            marker_231113168249499c8c616f7518126103.bindTooltip(
                `<div>
                     Cleveland
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6ca4d5d97a7b4c84988b1b5faf74a091 = L.marker(
                [49.26060857735795, -123.22510343446619],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_b775143f042143fe8813c20cc23c9861 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6ca4d5d97a7b4c84988b1b5faf74a091.setIcon(beautify_icon_b775143f042143fe8813c20cc23c9861);
        
    
            marker_6ca4d5d97a7b4c84988b1b5faf74a091.bindTooltip(
                `<div>
                     Cleveland
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ef8cf2082f0e4a49a3d7e98064461ba3 = L.marker(
                [49.26224978304391, -123.22780223759005],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_1583c9a22bd64e5aaf15b54cf8ed882b = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ef8cf2082f0e4a49a3d7e98064461ba3.setIcon(beautify_icon_1583c9a22bd64e5aaf15b54cf8ed882b);
        
    
            marker_ef8cf2082f0e4a49a3d7e98064461ba3.bindTooltip(
                `<div>
                     Cleveland
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d8f8d1b8b47a49079fb421da4e0b9523 = L.marker(
                [49.23742772011205, -123.20365106889676],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_c7be4bb91c3d4ed1984d563c06560ef2 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d8f8d1b8b47a49079fb421da4e0b9523.setIcon(beautify_icon_c7be4bb91c3d4ed1984d563c06560ef2);
        
    
            marker_d8f8d1b8b47a49079fb421da4e0b9523.bindTooltip(
                `<div>
                     Clinton
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4ec1e219ad68407f9fbe0829c18cf5f7 = L.marker(
                [49.24104853993467, -123.2032413388453],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_f9d745122a8c4b4980aa24ab9bdd1d68 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_4ec1e219ad68407f9fbe0829c18cf5f7.setIcon(beautify_icon_f9d745122a8c4b4980aa24ab9bdd1d68);
        
    
            marker_4ec1e219ad68407f9fbe0829c18cf5f7.bindTooltip(
                `<div>
                     Clinton
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d1e8476ed4314fd8b02e94ff64a30d6e = L.marker(
                [49.257129936924855, -123.20959368261413],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_1bef3b253ea641638ed069cf0e489fc0 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d1e8476ed4314fd8b02e94ff64a30d6e.setIcon(beautify_icon_1bef3b253ea641638ed069cf0e489fc0);
        
    
            marker_d1e8476ed4314fd8b02e94ff64a30d6e.bindTooltip(
                `<div>
                     ConcreteMystery
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_b7a5f416322e4468a1cf52489ae86bdc = L.marker(
                [49.25659145332148, -123.21012321536087],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_fd869da234c542ea87aee47e26cec27c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_b7a5f416322e4468a1cf52489ae86bdc.setIcon(beautify_icon_fd869da234c542ea87aee47e26cec27c);
        
    
            marker_b7a5f416322e4468a1cf52489ae86bdc.bindTooltip(
                `<div>
                     ConcreteMystery
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e4be0f03f159449280d3ad575cf4e091 = L.marker(
                [49.256258837379846, -123.2096566099602],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_eb9d10fecc17487cb9855d0dc550fafe = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e4be0f03f159449280d3ad575cf4e091.setIcon(beautify_icon_eb9d10fecc17487cb9855d0dc550fafe);
        
    
            marker_e4be0f03f159449280d3ad575cf4e091.bindTooltip(
                `<div>
                     ConcreteMystery
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c20600ca10b647c3a8e311f57d0ade51 = L.marker(
                [49.25094928243402, -123.20959224978441],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_0fbb4e09dcb047948cf9394b4262fd2e = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_c20600ca10b647c3a8e311f57d0ade51.setIcon(beautify_icon_0fbb4e09dcb047948cf9394b4262fd2e);
        
    
            marker_c20600ca10b647c3a8e311f57d0ade51.bindTooltip(
                `<div>
                     Council
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ed09a4003fed47598d4c6e715708b348 = L.marker(
                [49.25155015498478, -123.2159295028355],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_8e691c49ad6649c9b331cb7bdee3f691 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ed09a4003fed47598d4c6e715708b348.setIcon(beautify_icon_8e691c49ad6649c9b331cb7bdee3f691);
        
    
            marker_ed09a4003fed47598d4c6e715708b348.bindTooltip(
                `<div>
                     Council
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_325ba17d5709452f933a515910a825f6 = L.marker(
                [49.251701423044786, -123.22921852583814],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_4a36dcdd78064eac863f3cae66622de6 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_325ba17d5709452f933a515910a825f6.setIcon(beautify_icon_4a36dcdd78064eac863f3cae66622de6);
        
    
            marker_325ba17d5709452f933a515910a825f6.bindTooltip(
                `<div>
                     Council
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_38464421749e4a3f96c7abfd6bdac552 = L.marker(
                [49.251724533220234, -123.22838185408527],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_56721adcb00c42f8b884a3d0532cd19d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_38464421749e4a3f96c7abfd6bdac552.setIcon(beautify_icon_56721adcb00c42f8b884a3d0532cd19d);
        
    
            marker_38464421749e4a3f96c7abfd6bdac552.bindTooltip(
                `<div>
                     Council
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7fd015eb7334459aad8ccd031c7a4074 = L.marker(
                [49.251948632158964, -123.22784767148168],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_c572852fe2424f099192829215fa7830 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7fd015eb7334459aad8ccd031c7a4074.setIcon(beautify_icon_c572852fe2424f099192829215fa7830);
        
    
            marker_7fd015eb7334459aad8ccd031c7a4074.bindTooltip(
                `<div>
                     Council
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c563ddefbc1248149feee77c758f33a6 = L.marker(
                [49.25202286464399, -123.22546087175357],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_b181f246fc5e4b1c8b78d2259e390759 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_c563ddefbc1248149feee77c758f33a6.setIcon(beautify_icon_b181f246fc5e4b1c8b78d2259e390759);
        
    
            marker_c563ddefbc1248149feee77c758f33a6.bindTooltip(
                `<div>
                     Council
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1d2891f993c4467b89616568f5978c50 = L.marker(
                [49.25228127634392, -123.2213657241134],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_f145330f2b5843028eb0dd90cad1f0cf = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_1d2891f993c4467b89616568f5978c50.setIcon(beautify_icon_f145330f2b5843028eb0dd90cad1f0cf);
        
    
            marker_1d2891f993c4467b89616568f5978c50.bindTooltip(
                `<div>
                     Council
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d4c97839d53f406daa92e03b2f3d789f = L.marker(
                [49.254414353498156, -123.21482410380209],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_2e0613a49a3d4e6bae31cacd4fba9d26 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d4c97839d53f406daa92e03b2f3d789f.setIcon(beautify_icon_2e0613a49a3d4e6bae31cacd4fba9d26);
        
    
            marker_d4c97839d53f406daa92e03b2f3d789f.bindTooltip(
                `<div>
                     DeerFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_50c1b8e86a1043198d6d874d0376c8aa = L.marker(
                [49.25480650834432, -123.22927171538599],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_36436aa56157486aa4bbf645dc5163e9 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_50c1b8e86a1043198d6d874d0376c8aa.setIcon(beautify_icon_36436aa56157486aa4bbf645dc5163e9);
        
    
            marker_50c1b8e86a1043198d6d874d0376c8aa.bindTooltip(
                `<div>
                     DouglasFir
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6786f8ac68cf49419ef9ed46fb6a39b2 = L.marker(
                [49.270955172164186, -123.2293803226852],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_2058f4bfcee34f12878936fc1802ee53 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6786f8ac68cf49419ef9ed46fb6a39b2.setIcon(beautify_icon_2058f4bfcee34f12878936fc1802ee53);
        
    
            marker_6786f8ac68cf49419ef9ed46fb6a39b2.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_955d7b22f475420ba4dfd25de82f9fb4 = L.marker(
                [49.271323741033676, -123.2294267721951],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_d8fe193c31484d529328d12e53980760 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_955d7b22f475420ba4dfd25de82f9fb4.setIcon(beautify_icon_d8fe193c31484d529328d12e53980760);
        
    
            marker_955d7b22f475420ba4dfd25de82f9fb4.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_53b5df104ebc4f44ab6abbe107f6594e = L.marker(
                [49.27245567977517, -123.22986593146656],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_873d1d618965400397b3ea3ea3dd5606 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_53b5df104ebc4f44ab6abbe107f6594e.setIcon(beautify_icon_873d1d618965400397b3ea3ea3dd5606);
        
    
            marker_53b5df104ebc4f44ab6abbe107f6594e.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_cdb4adf8e97f46e3859fe5b382f65a3f = L.marker(
                [49.27302164060763, -123.22965976506511],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_303e5afba87b4be4a5c95d47813021aa = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_cdb4adf8e97f46e3859fe5b382f65a3f.setIcon(beautify_icon_303e5afba87b4be4a5c95d47813021aa);
        
    
            marker_cdb4adf8e97f46e3859fe5b382f65a3f.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7b81cb68814d46bc946a112077c894ac = L.marker(
                [49.27425889093808, -123.23057514864767],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_d59f066cfa7444109fdb15fc91df4fcc = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7b81cb68814d46bc946a112077c894ac.setIcon(beautify_icon_d59f066cfa7444109fdb15fc91df4fcc);
        
    
            marker_7b81cb68814d46bc946a112077c894ac.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7c16bd6335b54c9eaacf3efbfc0005a3 = L.marker(
                [49.27629022342389, -123.23071030370826],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_beca770f9a9c46329ad4d0417d233744 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7c16bd6335b54c9eaacf3efbfc0005a3.setIcon(beautify_icon_beca770f9a9c46329ad4d0417d233744);
        
    
            marker_7c16bd6335b54c9eaacf3efbfc0005a3.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_25381845098e4bb6bf2a687f643855d0 = L.marker(
                [49.2772533616488, -123.23020452602734],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_365567cc80e844d9a1f99a65e5c68acf = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_25381845098e4bb6bf2a687f643855d0.setIcon(beautify_icon_365567cc80e844d9a1f99a65e5c68acf);
        
    
            marker_25381845098e4bb6bf2a687f643855d0.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6bfd5ea5280143218423c79bddfdf4db = L.marker(
                [49.24805827227578, -123.24406965669253],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_5253cb8c7c46411d84ecbf78e7d63268 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6bfd5ea5280143218423c79bddfdf4db.setIcon(beautify_icon_5253cb8c7c46411d84ecbf78e7d63268);
        
    
            marker_6bfd5ea5280143218423c79bddfdf4db.bindTooltip(
                `<div>
                     Foreshore
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_28fc63af29c048a1a10eca97f87abeb2 = L.marker(
                [49.255489960771136, -123.25460554754565],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_47ea38e669b7494a9e826c662dbd04e1 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_28fc63af29c048a1a10eca97f87abeb2.setIcon(beautify_icon_47ea38e669b7494a9e826c662dbd04e1);
        
    
            marker_28fc63af29c048a1a10eca97f87abeb2.bindTooltip(
                `<div>
                     Foreshore
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f873588c91cb4aea9ca1ef0347ac581a = L.marker(
                [49.25761729668581, -123.25633895953075],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_649d45ab66444254a92e06626d39632f = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_f873588c91cb4aea9ca1ef0347ac581a.setIcon(beautify_icon_649d45ab66444254a92e06626d39632f);
        
    
            marker_f873588c91cb4aea9ca1ef0347ac581a.bindTooltip(
                `<div>
                     Foreshore
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_498b6fae364d4b0389cc9a2b0fedba1e = L.marker(
                [49.24690825926302, -123.20649395986956],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_662aa53475a1403fa3597169403c2ead = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_498b6fae364d4b0389cc9a2b0fedba1e.setIcon(beautify_icon_662aa53475a1403fa3597169403c2ead);
        
    
            marker_498b6fae364d4b0389cc9a2b0fedba1e.bindTooltip(
                `<div>
                     Hemlock
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_5d563f62721d4a95b7e976f8902c400f = L.marker(
                [49.250795211724615, -123.21183964193173],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_be20991937b04a9b9c0bf0ba2aef288c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_5d563f62721d4a95b7e976f8902c400f.setIcon(beautify_icon_be20991937b04a9b9c0bf0ba2aef288c);
        
    
            marker_5d563f62721d4a95b7e976f8902c400f.bindTooltip(
                `<div>
                     Hemlock
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d5bf883486c8480e8fa876a1df34fb9e = L.marker(
                [49.25225816728398, -123.21371159239975],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_59040d86ba87402bb261a3adb9122015 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d5bf883486c8480e8fa876a1df34fb9e.setIcon(beautify_icon_59040d86ba87402bb261a3adb9122015);
        
    
            marker_d5bf883486c8480e8fa876a1df34fb9e.bindTooltip(
                `<div>
                     Hemlock
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c1c1118c62444d049e8760ee5f7d1a75 = L.marker(
                [49.25310342577818, -123.21682304034601],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_0dc1d004dc2e4e6abad7b869b906a1be = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_c1c1118c62444d049e8760ee5f7d1a75.setIcon(beautify_icon_0dc1d004dc2e4e6abad7b869b906a1be);
        
    
            marker_c1c1118c62444d049e8760ee5f7d1a75.bindTooltip(
                `<div>
                     Hemlock
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_706f35fbf0e34b54a5b7a6b9a1fb298d = L.marker(
                [49.25364754913639, -123.22066801678287],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_871b25a02d9244bebeb4d0c490f1163d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_706f35fbf0e34b54a5b7a6b9a1fb298d.setIcon(beautify_icon_871b25a02d9244bebeb4d0c490f1163d);
        
    
            marker_706f35fbf0e34b54a5b7a6b9a1fb298d.bindTooltip(
                `<div>
                     Hemlock
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_3c4d7935e17c463d95a69c10dbc736a3 = L.marker(
                [49.25874464956123, -123.21896105165592],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_19d906a393994a3ab5c773e8f62feb00 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_3c4d7935e17c463d95a69c10dbc736a3.setIcon(beautify_icon_19d906a393994a3ab5c773e8f62feb00);
        
    
            marker_3c4d7935e17c463d95a69c10dbc736a3.bindTooltip(
                `<div>
                     Heron
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_9edc018376334a6e895bef66b9331106 = L.marker(
                [49.25949527021685, -123.22151906618171],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_58a9117477e24dcfb25789e4150808ff = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_9edc018376334a6e895bef66b9331106.setIcon(beautify_icon_58a9117477e24dcfb25789e4150808ff);
        
    
            marker_9edc018376334a6e895bef66b9331106.bindTooltip(
                `<div>
                     Heron
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1b6dbeb97022412799cb58c5eee8e6a1 = L.marker(
                [49.25967172094799, -123.23033273075205],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_7ce93370dd574f4ab25323a2ebd63ea2 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_1b6dbeb97022412799cb58c5eee8e6a1.setIcon(beautify_icon_7ce93370dd574f4ab25323a2ebd63ea2);
        
    
            marker_1b6dbeb97022412799cb58c5eee8e6a1.bindTooltip(
                `<div>
                     Heron
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_be3b41af35034fe889d78be01915aee5 = L.marker(
                [49.26018723857225, -123.23321028062318],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_4e1ff2d130264246b9bdd0b71fdc7629 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_be3b41af35034fe889d78be01915aee5.setIcon(beautify_icon_4e1ff2d130264246b9bdd0b71fdc7629);
        
    
            marker_be3b41af35034fe889d78be01915aee5.bindTooltip(
                `<div>
                     Heron
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_2349b4f9629c4b75b932b49176cfb73c = L.marker(
                [49.26035143299998, -123.23285362247212],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_42523f0a58d24dae846561039d3f4d0c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_2349b4f9629c4b75b932b49176cfb73c.setIcon(beautify_icon_42523f0a58d24dae846561039d3f4d0c);
        
    
            marker_2349b4f9629c4b75b932b49176cfb73c.bindTooltip(
                `<div>
                     Heron
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f872eae88aed46f1b83c943046557b6a = L.marker(
                [49.260391518864836, -123.23184201170109],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_641e10c014b24161ba33b2808496ab19 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_f872eae88aed46f1b83c943046557b6a.setIcon(beautify_icon_641e10c014b24161ba33b2808496ab19);
        
    
            marker_f872eae88aed46f1b83c943046557b6a.bindTooltip(
                `<div>
                     Heron
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f0e702c84eea41a1a135ac4dacf7c771 = L.marker(
                [49.2604027218579, -123.23294337190019],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_c24b66e178fc4c91a25ca8dcdb58d927 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_f0e702c84eea41a1a135ac4dacf7c771.setIcon(beautify_icon_c24b66e178fc4c91a25ca8dcdb58d927);
        
    
            marker_f0e702c84eea41a1a135ac4dacf7c771.bindTooltip(
                `<div>
                     Heron
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_0a7e21adba1543ed93e052418a9262bf = L.marker(
                [49.26041112414111, -123.22677722648264],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_9040be209af04ab4a942d0eceec7baaa = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_0a7e21adba1543ed93e052418a9262bf.setIcon(beautify_icon_9040be209af04ab4a942d0eceec7baaa);
        
    
            marker_0a7e21adba1543ed93e052418a9262bf.bindTooltip(
                `<div>
                     Heron
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_916a54d364de4a7186bd0685e6b3e7c5 = L.marker(
                [49.26043563069881, -123.23010579798104],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_2e7d264d685549e8aec97282c713b256 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_916a54d364de4a7186bd0685e6b3e7c5.setIcon(beautify_icon_2e7d264d685549e8aec97282c713b256);
        
    
            marker_916a54d364de4a7186bd0685e6b3e7c5.bindTooltip(
                `<div>
                     Heron
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_bab129f264cf412e93e296252eb493e1 = L.marker(
                [49.26046398823978, -123.23325712380753],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_002d4f904fae43879b6e676f9826469c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_bab129f264cf412e93e296252eb493e1.setIcon(beautify_icon_002d4f904fae43879b6e676f9826469c);
        
    
            marker_bab129f264cf412e93e296252eb493e1.bindTooltip(
                `<div>
                     Heron
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c93384fe2c124301a438c3b7f272df6a = L.marker(
                [49.25272946911107, -123.21410109952554],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_6f2bf627563c419b85d538fd87e69975 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_c93384fe2c124301a438c3b7f272df6a.setIcon(beautify_icon_6f2bf627563c419b85d538fd87e69975);
        
    
            marker_c93384fe2c124301a438c3b7f272df6a.bindTooltip(
                `<div>
                     Huckleberry
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_571e802cc666406b805c2c13a64f0cc8 = L.marker(
                [49.253975980905665, -123.21228727214111],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_e958b9eee522433aa5a57811696379c8 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_571e802cc666406b805c2c13a64f0cc8.setIcon(beautify_icon_e958b9eee522433aa5a57811696379c8);
        
    
            marker_571e802cc666406b805c2c13a64f0cc8.bindTooltip(
                `<div>
                     Huckleberry
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a1c0fe5d4b5a4c089516f27d0d1cf271 = L.marker(
                [49.25513562939522, -123.20912126298352],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_ad6ca89320684866a9484c38dd841e80 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_a1c0fe5d4b5a4c089516f27d0d1cf271.setIcon(beautify_icon_ad6ca89320684866a9484c38dd841e80);
        
    
            marker_a1c0fe5d4b5a4c089516f27d0d1cf271.bindTooltip(
                `<div>
                     Huckleberry
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d0c0ae9494334478b01cc7a76ec89e79 = L.marker(
                [49.25698498784965, -123.20568661836877],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_14a7ba3bf1d14c5e8324c8270e1b195b = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d0c0ae9494334478b01cc7a76ec89e79.setIcon(beautify_icon_14a7ba3bf1d14c5e8324c8270e1b195b);
        
    
            marker_d0c0ae9494334478b01cc7a76ec89e79.bindTooltip(
                `<div>
                     Huckleberry
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_12e2ff289b9648bea6af9259f841beba = L.marker(
                [49.2457666302785, -123.22703894280102],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_6831452ed92a48cc9f3161cbd798ceef = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_12e2ff289b9648bea6af9259f841beba.setIcon(beautify_icon_6831452ed92a48cc9f3161cbd798ceef);
        
    
            marker_12e2ff289b9648bea6af9259f841beba.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1ea54bc6918740928129d570d5833238 = L.marker(
                [49.24649083365288, -123.22431010543744],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_d82cb19ea88d44da95297df8bcc35e86 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_1ea54bc6918740928129d570d5833238.setIcon(beautify_icon_d82cb19ea88d44da95297df8bcc35e86);
        
    
            marker_1ea54bc6918740928129d570d5833238.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_8342c5e946bc44afa2de4f2d27587f65 = L.marker(
                [49.24814091364694, -123.21965002753038],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_c01e68e3f7e043e99c0bd448089afdf2 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_8342c5e946bc44afa2de4f2d27587f65.setIcon(beautify_icon_c01e68e3f7e043e99c0bd448089afdf2);
        
    
            marker_8342c5e946bc44afa2de4f2d27587f65.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6af53b7c404d4e49932389d233c95f1a = L.marker(
                [49.2492369671851, -123.21722878274943],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_5b51ec4deb6a4ed6b1a3e487b8092107 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6af53b7c404d4e49932389d233c95f1a.setIcon(beautify_icon_5b51ec4deb6a4ed6b1a3e487b8092107);
        
    
            marker_6af53b7c404d4e49932389d233c95f1a.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_fdebd69496f24c14a101531c83834066 = L.marker(
                [49.24919844813672, -123.21555007596322],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_79ce4c1496b6413382f3f4aff3a38b5c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_fdebd69496f24c14a101531c83834066.setIcon(beautify_icon_79ce4c1496b6413382f3f4aff3a38b5c);
        
    
            marker_fdebd69496f24c14a101531c83834066.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_def065fdce4e422e913ff6a4de57d223 = L.marker(
                [49.24907308587069, -123.21297248317428],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_5bd7cff20c9d4b089d932153aed4492a = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_def065fdce4e422e913ff6a4de57d223.setIcon(beautify_icon_5bd7cff20c9d4b089d932153aed4492a);
        
    
            marker_def065fdce4e422e913ff6a4de57d223.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_26239e37814e4c40a85f37776b7cc8ef = L.marker(
                [49.248941420177204, -123.21058796880955],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_a84b9ab492654e5096f0c77b374a44b6 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_26239e37814e4c40a85f37776b7cc8ef.setIcon(beautify_icon_a84b9ab492654e5096f0c77b374a44b6);
        
    
            marker_26239e37814e4c40a85f37776b7cc8ef.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4486f0d0af454291aaf3775fb74b1acf = L.marker(
                [49.24898694292271, -123.20761242070814],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_25de452dda9d4aa3a8c038c191bdc139 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_4486f0d0af454291aaf3775fb74b1acf.setIcon(beautify_icon_25de452dda9d4aa3a8c038c191bdc139);
        
    
            marker_4486f0d0af454291aaf3775fb74b1acf.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_eac6ced6155b422fa5648a5db9706ebb = L.marker(
                [49.249312254168984, -123.20513537354506],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_c0b3e344a76d4331ad5ede1e6fb4db22 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_eac6ced6155b422fa5648a5db9706ebb.setIcon(beautify_icon_c0b3e344a76d4331ad5ede1e6fb4db22);
        
    
            marker_eac6ced6155b422fa5648a5db9706ebb.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_39bec518d49f45a795a779fa203a5fff = L.marker(
                [49.24924046875497, -123.20546523861384],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_0f34e88954254ddb9153b5d5b8f27a2d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_39bec518d49f45a795a779fa203a5fff.setIcon(beautify_icon_0f34e88954254ddb9153b5d5b8f27a2d);
        
    
            marker_39bec518d49f45a795a779fa203a5fff.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_38253bdce6dd439abc0217f1761aa137 = L.marker(
                [49.24918619190925, -123.20489458560488],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_9a0f65f3f0c7477b97ad8af8289b561d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_38253bdce6dd439abc0217f1761aa137.setIcon(beautify_icon_9a0f65f3f0c7477b97ad8af8289b561d);
        
    
            marker_38253bdce6dd439abc0217f1761aa137.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e0864debc7b74330881f6fade3b011a5 = L.marker(
                [49.2524157349326, -123.22336033758386],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_0919a5886a0c47d4b7a919572b16366e = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e0864debc7b74330881f6fade3b011a5.setIcon(beautify_icon_0919a5886a0c47d4b7a919572b16366e);
        
    
            marker_e0864debc7b74330881f6fade3b011a5.bindTooltip(
                `<div>
                     IronKnee
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_262cb67801974633848dabe26c794300 = L.marker(
                [49.25073918577631, -123.22405970948772],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_a0f716a4a2a441b28c35bd499aabb0d8 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_262cb67801974633848dabe26c794300.setIcon(beautify_icon_a0f716a4a2a441b28c35bd499aabb0d8);
        
    
            marker_262cb67801974633848dabe26c794300.bindTooltip(
                `<div>
                     IronKnee
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_79fb4ef09100467aa3647dc52ebe3c2a = L.marker(
                [49.24944987135155, -123.22369719053619],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_cce0eb3e63e54065bd810baed1c4dca4 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_79fb4ef09100467aa3647dc52ebe3c2a.setIcon(beautify_icon_cce0eb3e63e54065bd810baed1c4dca4);
        
    
            marker_79fb4ef09100467aa3647dc52ebe3c2a.bindTooltip(
                `<div>
                     IronKnee
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f24a3319ce1d413e8db94e8530fbbf8f = L.marker(
                [49.24812970674851, -123.22318055238928],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_f3cf59c39c5e4cfcb2fc097979ae1d0c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_f24a3319ce1d413e8db94e8530fbbf8f.setIcon(beautify_icon_f3cf59c39c5e4cfcb2fc097979ae1d0c);
        
    
            marker_f24a3319ce1d413e8db94e8530fbbf8f.bindTooltip(
                `<div>
                     IronKnee
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_9620d471bd604945950726a476e100d9 = L.marker(
                [49.261220534552244, -123.22180519817867],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_6ab6776381dd4c16bbfa9136b0f4f244 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_9620d471bd604945950726a476e100d9.setIcon(beautify_icon_6ab6776381dd4c16bbfa9136b0f4f244);
        
    
            marker_9620d471bd604945950726a476e100d9.bindTooltip(
                `<div>
                     LilyOfTheValley
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_416efc73d9454f0e959bc84dfe310251 = L.marker(
                [49.261363370217595, -123.22737657484453],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_7bffece5492d411dbef67a1407c55ee5 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_416efc73d9454f0e959bc84dfe310251.setIcon(beautify_icon_7bffece5492d411dbef67a1407c55ee5);
        
    
            marker_416efc73d9454f0e959bc84dfe310251.bindTooltip(
                `<div>
                     LilyOfTheValley
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_062e278c9cf142189d5d8c9a560a5355 = L.marker(
                [49.261592326571694, -123.21780764100585],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_25c70a91106a4b4fbafc93a6454bc15d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_062e278c9cf142189d5d8c9a560a5355.setIcon(beautify_icon_25c70a91106a4b4fbafc93a6454bc15d);
        
    
            marker_062e278c9cf142189d5d8c9a560a5355.bindTooltip(
                `<div>
                     LilyOfTheValley
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_fd9705a84523496991225c941979c4f1 = L.marker(
                [49.261896899492776, -123.21588849533929],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_c6b0192cf4d343d4a6984ac5dd905d0f = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_fd9705a84523496991225c941979c4f1.setIcon(beautify_icon_c6b0192cf4d343d4a6984ac5dd905d0f);
        
    
            marker_fd9705a84523496991225c941979c4f1.bindTooltip(
                `<div>
                     LilyOfTheValley
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_595d25e096074d2089baf5fc01778dc6 = L.marker(
                [49.2486395680387, -123.22681640867367],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_ca226d9a2ee348ecb41bd0a156f72a00 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_595d25e096074d2089baf5fc01778dc6.setIcon(beautify_icon_ca226d9a2ee348ecb41bd0a156f72a00);
        
    
            marker_595d25e096074d2089baf5fc01778dc6.bindTooltip(
                `<div>
                     Long
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_5f6d5dd1514c40a9a79e274a7208e6f4 = L.marker(
                [49.24901005415512, -123.22440614997345],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_7ea4d59cdda946a8806f2deb499d5796 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_5f6d5dd1514c40a9a79e274a7208e6f4.setIcon(beautify_icon_7ea4d59cdda946a8806f2deb499d5796);
        
    
            marker_5f6d5dd1514c40a9a79e274a7208e6f4.bindTooltip(
                `<div>
                     Long
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_2953db39d25a4287b673824a54c468ab = L.marker(
                [49.24931050303928, -123.2220473789621],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_3b679ed0bc3c41da9360f67670289dfb = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_2953db39d25a4287b673824a54c468ab.setIcon(beautify_icon_3b679ed0bc3c41da9360f67670289dfb);
        
    
            marker_2953db39d25a4287b673824a54c468ab.bindTooltip(
                `<div>
                     Long
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ca53cfd659974597b2a7c09d92369551 = L.marker(
                [49.24934622066505, -123.21909757454151],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_30c92ed390da457abe4d0c94b75305dd = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ca53cfd659974597b2a7c09d92369551.setIcon(beautify_icon_30c92ed390da457abe4d0c94b75305dd);
        
    
            marker_ca53cfd659974597b2a7c09d92369551.bindTooltip(
                `<div>
                     Long
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_40ca93be75b2419fac8ecf03e7a2fdd0 = L.marker(
                [49.25455510856313, -123.21876597583544],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_19f56932ad164344a117e3d07b41e8cf = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_40ca93be75b2419fac8ecf03e7a2fdd0.setIcon(beautify_icon_19f56932ad164344a117e3d07b41e8cf);
        
    
            marker_40ca93be75b2419fac8ecf03e7a2fdd0.bindTooltip(
                `<div>
                     Nature
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_79aa89e4c1de4aadafc30746fe8964eb = L.marker(
                [49.25518534809546, -123.2170722519294],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_d57899b02e404e2baa42443d5a5cfd23 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_79aa89e4c1de4aadafc30746fe8964eb.setIcon(beautify_icon_d57899b02e404e2baa42443d5a5cfd23);
        
    
            marker_79aa89e4c1de4aadafc30746fe8964eb.bindTooltip(
                `<div>
                     Nature
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_858ef9fb245049e784560871f0a34ac5 = L.marker(
                [49.25692266688955, -123.21489190607875],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_b903358c817c4b838d9f27da2bb8f3c7 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_858ef9fb245049e784560871f0a34ac5.setIcon(beautify_icon_b903358c817c4b838d9f27da2bb8f3c7);
        
    
            marker_858ef9fb245049e784560871f0a34ac5.bindTooltip(
                `<div>
                     Nature
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d2c1a7fb8c994815b98eca8dd2eb7741 = L.marker(
                [49.26074196164327, -123.2161798281786],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_8fd6b57126bf4659ae73977c757ca954 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d2c1a7fb8c994815b98eca8dd2eb7741.setIcon(beautify_icon_8fd6b57126bf4659ae73977c757ca954);
        
    
            marker_d2c1a7fb8c994815b98eca8dd2eb7741.bindTooltip(
                `<div>
                     NewtLoop
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_2af7cc0df855455d987afe2387647757 = L.marker(
                [49.26116767099691, -123.21572341297808],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_e98b94cc102846589eeaec3b9bf8ab19 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_2af7cc0df855455d987afe2387647757.setIcon(beautify_icon_e98b94cc102846589eeaec3b9bf8ab19);
        
    
            marker_2af7cc0df855455d987afe2387647757.bindTooltip(
                `<div>
                     NewtLoop
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_dc1b5e4b3e2b4ddd9ce5445e440f533c = L.marker(
                [49.26145649318973, -123.2161193466862],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_adf30b2281ed408b864c262cef8eec6b = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_dc1b5e4b3e2b4ddd9ce5445e440f533c.setIcon(beautify_icon_adf30b2281ed408b864c262cef8eec6b);
        
    
            marker_dc1b5e4b3e2b4ddd9ce5445e440f533c.bindTooltip(
                `<div>
                     NewtLoop
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_50af7f5b1f654451960746e44ecfc0d1 = L.marker(
                [49.26901567872852, -123.22868189178706],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_39c51ef21fb94249ac28c848ef803801 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_50af7f5b1f654451960746e44ecfc0d1.setIcon(beautify_icon_39c51ef21fb94249ac28c848ef803801);
        
    
            marker_50af7f5b1f654451960746e44ecfc0d1.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_44b728f6a27a47499a88cef59d1ce110 = L.marker(
                [49.27066990652504, -123.22859816753724],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_53b00e7c8eb94559a171d0479f95a309 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_44b728f6a27a47499a88cef59d1ce110.setIcon(beautify_icon_53b00e7c8eb94559a171d0479f95a309);
        
    
            marker_44b728f6a27a47499a88cef59d1ce110.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_0eb0b6c5c1474179aa4524b7cbb2dcc6 = L.marker(
                [49.271967066203835, -123.22860348645277],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_bd3b93d82b60467bb3d115b90c421bd1 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_0eb0b6c5c1474179aa4524b7cbb2dcc6.setIcon(beautify_icon_bd3b93d82b60467bb3d115b90c421bd1);
        
    
            marker_0eb0b6c5c1474179aa4524b7cbb2dcc6.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e1b78df5f580480d97505eaeecf6e12c = L.marker(
                [49.272849087800644, -123.22902933072545],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_9405d361c612433899f6fab27c51c01a = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e1b78df5f580480d97505eaeecf6e12c.setIcon(beautify_icon_9405d361c612433899f6fab27c51c01a);
        
    
            marker_e1b78df5f580480d97505eaeecf6e12c.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_eac67082ddc44a2ca823914278c056b6 = L.marker(
                [49.27408949187421, -123.22922903300501],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_8bdb6e916ed04fe38c9cfba2c64e34c5 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_eac67082ddc44a2ca823914278c056b6.setIcon(beautify_icon_8bdb6e916ed04fe38c9cfba2c64e34c5);
        
    
            marker_eac67082ddc44a2ca823914278c056b6.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a46aca8746644d9597feac0a6135d3b9 = L.marker(
                [49.275247967589465, -123.23016049789722],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_63f150a2ed43400a908ff77ea09de74e = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_a46aca8746644d9597feac0a6135d3b9.setIcon(beautify_icon_63f150a2ed43400a908ff77ea09de74e);
        
    
            marker_a46aca8746644d9597feac0a6135d3b9.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_19961a5926674c07b503e35aecfa4cb5 = L.marker(
                [49.27582754500957, -123.22985422935977],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_617d5f894d964cb6a898c6e40965b1e1 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_19961a5926674c07b503e35aecfa4cb5.setIcon(beautify_icon_617d5f894d964cb6a898c6e40965b1e1);
        
    
            marker_19961a5926674c07b503e35aecfa4cb5.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4ca7faeb1b4b43948dbc9a37e2127451 = L.marker(
                [49.27586114373477, -123.22675939096546],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_69b00908249a478596e235ef84f5bef8 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_4ca7faeb1b4b43948dbc9a37e2127451.setIcon(beautify_icon_69b00908249a478596e235ef84f5bef8);
        
    
            marker_4ca7faeb1b4b43948dbc9a37e2127451.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_b488d852d3e149c5a98edf7fa5a25525 = L.marker(
                [49.27602213618289, -123.22633569180857],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_242f866f0be34db08d5308a8d144acf1 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_b488d852d3e149c5a98edf7fa5a25525.setIcon(beautify_icon_242f866f0be34db08d5308a8d144acf1);
        
    
            marker_b488d852d3e149c5a98edf7fa5a25525.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_41a537eddce84ee09a24d42442be84ab = L.marker(
                [49.276249624615865, -123.2267218480022],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_1e3144d8995f4eef902be7791862a5d9 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_41a537eddce84ee09a24d42442be84ab.setIcon(beautify_icon_1e3144d8995f4eef902be7791862a5d9);
        
    
            marker_41a537eddce84ee09a24d42442be84ab.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_69415858d71648398fcc24a26b714d5e = L.marker(
                [49.27625067457073, -123.22851208642129],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_6f7de24111f44bff9f67d8483cdef437 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_69415858d71648398fcc24a26b714d5e.setIcon(beautify_icon_6f7de24111f44bff9f67d8483cdef437);
        
    
            marker_69415858d71648398fcc24a26b714d5e.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_5d1ae974cb5445e2b453b0a98c50df55 = L.marker(
                [49.27664860184877, -123.22994378881488],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_f5ff1cfada8c41f7a94b19b95b8da384 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_5d1ae974cb5445e2b453b0a98c50df55.setIcon(beautify_icon_f5ff1cfada8c41f7a94b19b95b8da384);
        
    
            marker_5d1ae974cb5445e2b453b0a98c50df55.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_22539927cde746da94e696255ad886df = L.marker(
                [49.276809416700544, -123.22603622821373],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_ac36d653a389493d96186b2e20d495ad = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_22539927cde746da94e696255ad886df.setIcon(beautify_icon_ac36d653a389493d96186b2e20d495ad);
        
    
            marker_22539927cde746da94e696255ad886df.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_81d0029c9b1047e0ac2faa9798a7b502 = L.marker(
                [49.24971460054638, -123.2287023290655],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_236a8882adfa4656800366b59c2bf14b = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_81d0029c9b1047e0ac2faa9798a7b502.setIcon(beautify_icon_236a8882adfa4656800366b59c2bf14b);
        
    
            marker_81d0029c9b1047e0ac2faa9798a7b502.bindTooltip(
                `<div>
                     Powerline
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_fb73271c76c04ef691a9d8227e927f99 = L.marker(
                [49.24973000809374, -123.22688846754605],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_da95ced700b742adab1d0113216891ff = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_fb73271c76c04ef691a9d8227e927f99.setIcon(beautify_icon_da95ced700b742adab1d0113216891ff);
        
    
            marker_fb73271c76c04ef691a9d8227e927f99.bindTooltip(
                `<div>
                     Powerline
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_9ad53fd95564445c85c197554f37d75c = L.marker(
                [49.24973701148393, -123.22462838118993],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_c647653cbf6d444a843971d0c63b0b57 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_9ad53fd95564445c85c197554f37d75c.setIcon(beautify_icon_c647653cbf6d444a843971d0c63b0b57);
        
    
            marker_9ad53fd95564445c85c197554f37d75c.bindTooltip(
                `<div>
                     Powerline
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_53bff08a6af34e73be18ed60dc835ff5 = L.marker(
                [49.24960674811446, -123.2222374309868],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_93e9b38a94b24a778a4be565568ae1c5 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_53bff08a6af34e73be18ed60dc835ff5.setIcon(beautify_icon_93e9b38a94b24a778a4be565568ae1c5);
        
    
            marker_53bff08a6af34e73be18ed60dc835ff5.bindTooltip(
                `<div>
                     Powerline
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_233d8cc91127476b8f023b2977a6df9a = L.marker(
                [49.25766561229445, -123.21883223688657],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_b378e0dbc8744b12b988985a86b09f35 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_233d8cc91127476b8f023b2977a6df9a.setIcon(beautify_icon_b378e0dbc8744b12b988985a86b09f35);
        
    
            marker_233d8cc91127476b8f023b2977a6df9a.bindTooltip(
                `<div>
                     Salal
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_847e965bfa0e4536bc9507564e9ace5e = L.marker(
                [49.25968432410487, -123.21862289669356],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_b96b4b8abe4f43fe9b63b9e78f690ae0 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_847e965bfa0e4536bc9507564e9ace5e.setIcon(beautify_icon_b96b4b8abe4f43fe9b63b9e78f690ae0);
        
    
            marker_847e965bfa0e4536bc9507564e9ace5e.bindTooltip(
                `<div>
                     Salal
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ff32590dd2024a2aa031fc101cd4765e = L.marker(
                [49.23717062906145, -123.2023274682292],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_4fb626ae222f46aaae03c4dc512fa5e2 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ff32590dd2024a2aa031fc101cd4765e.setIcon(beautify_icon_4fb626ae222f46aaae03c4dc512fa5e2);
        
    
            marker_ff32590dd2024a2aa031fc101cd4765e.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_74e3e856615d4e169afdbc6ea4dce074 = L.marker(
                [49.24460676084016, -123.2127021974411],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_8a2708d0561146a3b137b63714427f42 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_74e3e856615d4e169afdbc6ea4dce074.setIcon(beautify_icon_8a2708d0561146a3b137b63714427f42);
        
    
            marker_74e3e856615d4e169afdbc6ea4dce074.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_07a048cd9be146a587097e0e39c3dd57 = L.marker(
                [49.250994103926, -123.2179313486018],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_aaab6ac3883d4a75a95b8036697f7474 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_07a048cd9be146a587097e0e39c3dd57.setIcon(beautify_icon_aaab6ac3883d4a75a95b8036697f7474);
        
    
            marker_07a048cd9be146a587097e0e39c3dd57.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_35235257e7ee4ba5bddb485e91aa0b17 = L.marker(
                [49.25277568806114, -123.22042031733946],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_f56a345a981e451bb26186776607763d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_35235257e7ee4ba5bddb485e91aa0b17.setIcon(beautify_icon_f56a345a981e451bb26186776607763d);
        
    
            marker_35235257e7ee4ba5bddb485e91aa0b17.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_72097689602f4255ae8492203cfa39da = L.marker(
                [49.25320531806571, -123.22263174057468],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_adad63647fbd46b59f892ac244a4f776 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_72097689602f4255ae8492203cfa39da.setIcon(beautify_icon_adad63647fbd46b59f892ac244a4f776);
        
    
            marker_72097689602f4255ae8492203cfa39da.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7abcf9693dc74a37a94a14adbac833c6 = L.marker(
                [49.2550445951482, -123.22485140301244],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_543fb60b9fa04a53ba26a45a6c9c13be = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7abcf9693dc74a37a94a14adbac833c6.setIcon(beautify_icon_543fb60b9fa04a53ba26a45a6c9c13be);
        
    
            marker_7abcf9693dc74a37a94a14adbac833c6.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_3a14397e685349ec89253f5126c35bbd = L.marker(
                [49.25831261739348, -123.22858243066761],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_ca8358ae5e61456e8e7df97b6d15c9ac = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_3a14397e685349ec89253f5126c35bbd.setIcon(beautify_icon_ca8358ae5e61456e8e7df97b6d15c9ac);
        
    
            marker_3a14397e685349ec89253f5126c35bbd.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4891b450acca441785e55d5b0d985f2b = L.marker(
                [49.25868583182979, -123.22907799758634],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_f2ab164466014d5ca1c1ef05816c3130 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_4891b450acca441785e55d5b0d985f2b.setIcon(beautify_icon_f2ab164466014d5ca1c1ef05816c3130);
        
    
            marker_4891b450acca441785e55d5b0d985f2b.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ed71e26e241c419b95923532fb098c52 = L.marker(
                [49.25978935367037, -123.229477642343],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_050e940849094a2a91f6549eb94995a6 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ed71e26e241c419b95923532fb098c52.setIcon(beautify_icon_050e940849094a2a91f6549eb94995a6);
        
    
            marker_ed71e26e241c419b95923532fb098c52.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d44c061a04d64425b5bb9ec5e7611f10 = L.marker(
                [49.260932060876236, -123.2293391480532],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_0cf0239f78864b538d9ea5e7c3979e24 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d44c061a04d64425b5bb9ec5e7611f10.setIcon(beautify_icon_0cf0239f78864b538d9ea5e7c3979e24);
        
    
            marker_d44c061a04d64425b5bb9ec5e7611f10.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_13fef6a39bb849c9ab49052bffe00eac = L.marker(
                [49.26253544725521, -123.22915786891156],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_4653e633d90d421d9bfbb4c79fd3ef39 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_13fef6a39bb849c9ab49052bffe00eac.setIcon(beautify_icon_4653e633d90d421d9bfbb4c79fd3ef39);
        
    
            marker_13fef6a39bb849c9ab49052bffe00eac.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e56552456fbb4af79dbfd93fb5ceb54f = L.marker(
                [49.265369603240536, -123.23298825563292],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_a879d4df56654f089bbc609f9fd7d6a5 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e56552456fbb4af79dbfd93fb5ceb54f.setIcon(beautify_icon_a879d4df56654f089bbc609f9fd7d6a5);
        
    
            marker_e56552456fbb4af79dbfd93fb5ceb54f.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_8ce4629dd5c947d7a34e8f64ac83e7b7 = L.marker(
                [49.26730608898525, -123.23539445795662],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_a3b96e4b1c8242668a29acd897f8ab16 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_8ce4629dd5c947d7a34e8f64ac83e7b7.setIcon(beautify_icon_a3b96e4b1c8242668a29acd897f8ab16);
        
    
            marker_8ce4629dd5c947d7a34e8f64ac83e7b7.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_dd48754b645f41ed8bd1c1907f5e5f1b = L.marker(
                [49.26916969288675, -123.23711985141821],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_3e44c84b4f81469896be508f09bcc904 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_dd48754b645f41ed8bd1c1907f5e5f1b.setIcon(beautify_icon_3e44c84b4f81469896be508f09bcc904);
        
    
            marker_dd48754b645f41ed8bd1c1907f5e5f1b.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_2ef0e742fd0e4d74a91f17be360206a5 = L.marker(
                [49.271010824913, -123.23824740495861],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_cf38808031b24eb5becd25b94fcdf5c6 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_2ef0e742fd0e4d74a91f17be360206a5.setIcon(beautify_icon_cf38808031b24eb5becd25b94fcdf5c6);
        
    
            marker_2ef0e742fd0e4d74a91f17be360206a5.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_03d79706079c45c084dfbe22459540ca = L.marker(
                [49.27269788556626, -123.23863230593781],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_67a4da8865d3454ebcb6b475d4c0db43 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_03d79706079c45c084dfbe22459540ca.setIcon(beautify_icon_67a4da8865d3454ebcb6b475d4c0db43);
        
    
            marker_03d79706079c45c084dfbe22459540ca.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_5267f7b98ac6459098e53bbbd3c6e202 = L.marker(
                [49.275888442768924, -123.24069904963605],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_d8cb1e5d7abd47fb996253143bff4dff = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_5267f7b98ac6459098e53bbbd3c6e202.setIcon(beautify_icon_d8cb1e5d7abd47fb996253143bff4dff);
        
    
            marker_5267f7b98ac6459098e53bbbd3c6e202.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_b2efcf7949804134b7152f49d8dd2823 = L.marker(
                [49.279092091660544, -123.24361397558427],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_2e2e5ebb6a7b4ff3a266e1cf095ed1ff = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_b2efcf7949804134b7152f49d8dd2823.setIcon(beautify_icon_2e2e5ebb6a7b4ff3a266e1cf095ed1ff);
        
    
            marker_b2efcf7949804134b7152f49d8dd2823.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7d26e9d645614025b90ce1b85c08c8b3 = L.marker(
                [49.24258112866778, -123.19765475330254],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_dc0cb70ee4c54da4b16a85ddb37683cd = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7d26e9d645614025b90ce1b85c08c8b3.setIcon(beautify_icon_dc0cb70ee4c54da4b16a85ddb37683cd);
        
    
            marker_7d26e9d645614025b90ce1b85c08c8b3.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c279fef3464442debf543b954b62ffa2 = L.marker(
                [49.24259513747525, -123.19895266717558],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_eff70105346f487799b489deff7bf314 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_c279fef3464442debf543b954b62ffa2.setIcon(beautify_icon_eff70105346f487799b489deff7bf314);
        
    
            marker_c279fef3464442debf543b954b62ffa2.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_034dbee1c992441ab6ba715a54e227fc = L.marker(
                [49.24380548238857, -123.20151080261854],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_9f6c9999256f4ec2a5e24ff445f7d0ed = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_034dbee1c992441ab6ba715a54e227fc.setIcon(beautify_icon_9f6c9999256f4ec2a5e24ff445f7d0ed);
        
    
            marker_034dbee1c992441ab6ba715a54e227fc.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e00090bc113e409eb9fdbf422d331f9e = L.marker(
                [49.246032779557034, -123.20186391132458],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_d022ed7d0ce74bd09dce57671af592fe = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e00090bc113e409eb9fdbf422d331f9e.setIcon(beautify_icon_d022ed7d0ce74bd09dce57671af592fe);
        
    
            marker_e00090bc113e409eb9fdbf422d331f9e.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_767224c86ac74ba09672550c63805c37 = L.marker(
                [49.2481605224002, -123.20376687630021],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_94cd7c8e82274ba1b964b90392849098 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_767224c86ac74ba09672550c63805c37.setIcon(beautify_icon_94cd7c8e82274ba1b964b90392849098);
        
    
            marker_767224c86ac74ba09672550c63805c37.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_9fd67c1cb84d4b169a1ffbac1a741314 = L.marker(
                [49.248272580085974, -123.2032627279363],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_a12d4e93510340289ca9e5fc9aa623d7 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_9fd67c1cb84d4b169a1ffbac1a741314.setIcon(beautify_icon_a12d4e93510340289ca9e5fc9aa623d7);
        
    
            marker_9fd67c1cb84d4b169a1ffbac1a741314.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_01148ac661764b4498962ed30e08d9f7 = L.marker(
                [49.24854571962957, -123.20408330984777],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_1d8b86123b744902b978e5d019ce1053 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_01148ac661764b4498962ed30e08d9f7.setIcon(beautify_icon_1d8b86123b744902b978e5d019ce1053);
        
    
            marker_01148ac661764b4498962ed30e08d9f7.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_2abc3fc8585d437d921f37b1afe4d803 = L.marker(
                [49.248697697024824, -123.2052539552183],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_cd0e78574a9747f0a0b49541f7119f86 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_2abc3fc8585d437d921f37b1afe4d803.setIcon(beautify_icon_cd0e78574a9747f0a0b49541f7119f86);
        
    
            marker_2abc3fc8585d437d921f37b1afe4d803.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ccb214d449614c368345e1d8c70b8a08 = L.marker(
                [49.24934972153255, -123.20598115270622],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_c19a7a5ed77a479d9bc91b49438c59cc = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ccb214d449614c368345e1d8c70b8a08.setIcon(beautify_icon_c19a7a5ed77a479d9bc91b49438c59cc);
        
    
            marker_ccb214d449614c368345e1d8c70b8a08.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e7a71c1c4d03426cb85b3a4c791a1e39 = L.marker(
                [49.252454950959084, -123.20919683676077],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_0238df8e9856498fa0acfa64e913c348 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e7a71c1c4d03426cb85b3a4c791a1e39.setIcon(beautify_icon_0238df8e9856498fa0acfa64e913c348);
        
    
            marker_e7a71c1c4d03426cb85b3a4c791a1e39.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_095302ae8b4d42abb58c4c38f8327415 = L.marker(
                [49.255899609410235, -123.21139981294691],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_49ab372bf6f84b1faa2216fe6e6c9427 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_095302ae8b4d42abb58c4c38f8327415.setIcon(beautify_icon_49ab372bf6f84b1faa2216fe6e6c9427);
        
    
            marker_095302ae8b4d42abb58c4c38f8327415.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_74230009e2544cdc9c96552dbd65ecae = L.marker(
                [49.25695277655975, -123.21046014225477],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_40e13449431745d59bc10164875dfb1b = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_74230009e2544cdc9c96552dbd65ecae.setIcon(beautify_icon_40e13449431745d59bc10164875dfb1b);
        
    
            marker_74230009e2544cdc9c96552dbd65ecae.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_cc6142dffec14e4b9ee7ce29ccf76b18 = L.marker(
                [49.25749685727255, -123.2098656119698],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_366d20b580e24923b0b68462a71b44f2 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_cc6142dffec14e4b9ee7ce29ccf76b18.setIcon(beautify_icon_366d20b580e24923b0b68462a71b44f2);
        
    
            marker_cc6142dffec14e4b9ee7ce29ccf76b18.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1528b5d3ae1d49128470269375eb647f = L.marker(
                [49.25798001283702, -123.20948481905664],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_22588ca3863440c7a52d432e91f69982 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_1528b5d3ae1d49128470269375eb647f.setIcon(beautify_icon_22588ca3863440c7a52d432e91f69982);
        
    
            marker_1528b5d3ae1d49128470269375eb647f.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_0dfea24a052f4b78b90524b1ea420be1 = L.marker(
                [49.257719528935354, -123.22974591719282],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_174ac1daf2a24a198c2e78aae28fdc7b = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_0dfea24a052f4b78b90524b1ea420be1.setIcon(beautify_icon_174ac1daf2a24a198c2e78aae28fdc7b);
        
    
            marker_0dfea24a052f4b78b90524b1ea420be1.bindTooltip(
                `<div>
                     SherrySakamoto
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e1f95e8afacd409e81d4b8a3becf74cd = L.marker(
                [49.25812425862052, -123.20653955432931],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_4f22602bc423443e931382223dc2589c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e1f95e8afacd409e81d4b8a3becf74cd.setIcon(beautify_icon_4f22602bc423443e931382223dc2589c);
        
    
            marker_e1f95e8afacd409e81d4b8a3becf74cd.bindTooltip(
                `<div>
                     SherrySakamoto
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ccb8cc59616c4d25a0d43d3739f09c28 = L.marker(
                [49.258187278912885, -123.21084067596733],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_964da4f30ff141708e0436ef130180f5 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ccb8cc59616c4d25a0d43d3739f09c28.setIcon(beautify_icon_964da4f30ff141708e0436ef130180f5);
        
    
            marker_ccb8cc59616c4d25a0d43d3739f09c28.bindTooltip(
                `<div>
                     SherrySakamoto
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e4f00817731b419db2095740fc7635fd = L.marker(
                [49.25822228985484, -123.21319408337084],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_797f1192e2cd4642bd07573fd86145de = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e4f00817731b419db2095740fc7635fd.setIcon(beautify_icon_797f1192e2cd4642bd07573fd86145de);
        
    
            marker_e4f00817731b419db2095740fc7635fd.bindTooltip(
                `<div>
                     SherrySakamoto
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e516e5724d4b4ba8af2a0ec4088cfe4f = L.marker(
                [49.258239445079134, -123.21475192791627],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_e7b8e439dfab4679ab49f99f592cfe29 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e516e5724d4b4ba8af2a0ec4088cfe4f.setIcon(beautify_icon_e7b8e439dfab4679ab49f99f592cfe29);
        
    
            marker_e516e5724d4b4ba8af2a0ec4088cfe4f.bindTooltip(
                `<div>
                     SherrySakamoto
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a72e5b2e3d544d1b8d7567416897f583 = L.marker(
                [49.25825239873222, -123.21734547615053],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_eb21ac72abd1448cb96983f40110708e = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_a72e5b2e3d544d1b8d7567416897f583.setIcon(beautify_icon_eb21ac72abd1448cb96983f40110708e);
        
    
            marker_a72e5b2e3d544d1b8d7567416897f583.bindTooltip(
                `<div>
                     SherrySakamoto
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_41b7d8df186f4a46931a91fd69e28fb1 = L.marker(
                [49.258281107711326, -123.22467649031778],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_a870272fb6e44138af20f95e6726ea43 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_41b7d8df186f4a46931a91fd69e28fb1.setIcon(beautify_icon_a870272fb6e44138af20f95e6726ea43);
        
    
            marker_41b7d8df186f4a46931a91fd69e28fb1.bindTooltip(
                `<div>
                     SherrySakamoto
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d1e45684e78b4e1eacbc39167b57e9a9 = L.marker(
                [49.258281107711326, -123.22028195922982],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_6c1bf9e9d6ab4ce3af83aff0b9d1e03f = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d1e45684e78b4e1eacbc39167b57e9a9.setIcon(beautify_icon_6c1bf9e9d6ab4ce3af83aff0b9d1e03f);
        
    
            marker_d1e45684e78b4e1eacbc39167b57e9a9.bindTooltip(
                `<div>
                     SherrySakamoto
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e565fe735ab1497b81ee35e4ab2071d2 = L.marker(
                [49.26699174812226, -123.2275451457667],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_5a21e94534814c96870fad1c3c199ab9 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e565fe735ab1497b81ee35e4ab2071d2.setIcon(beautify_icon_5a21e94534814c96870fad1c3c199ab9);
        
    
            marker_e565fe735ab1497b81ee35e4ab2071d2.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_73129dad0dad4fa6b21b4793c2270470 = L.marker(
                [49.267807351138906, -123.22588786772252],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_8f1d389d9ba94c6094d65395dbb9cbf5 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_73129dad0dad4fa6b21b4793c2270470.setIcon(beautify_icon_8f1d389d9ba94c6094d65395dbb9cbf5);
        
    
            marker_73129dad0dad4fa6b21b4793c2270470.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_5e37002211a74679b62c1dc83bbef357 = L.marker(
                [49.26836671373096, -123.23667965143653],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_b3b0fc1331a148ceba3594450b8b4212 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_5e37002211a74679b62c1dc83bbef357.setIcon(beautify_icon_b3b0fc1331a148ceba3594450b8b4212);
        
    
            marker_5e37002211a74679b62c1dc83bbef357.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ddad2ccef7d042c4835f0a374df0569c = L.marker(
                [49.26861243941978, -123.23609851940927],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_3f34428a8d0d433f94a546c6ec74eb9a = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ddad2ccef7d042c4835f0a374df0569c.setIcon(beautify_icon_3f34428a8d0d433f94a546c6ec74eb9a);
        
    
            marker_ddad2ccef7d042c4835f0a374df0569c.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_24a3ed4e3b194afeaacb8b6aa6202052 = L.marker(
                [49.26914134034848, -123.23218396320507],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_8b1978126c8e4cf9a2a0a2d021cb6cc7 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_24a3ed4e3b194afeaacb8b6aa6202052.setIcon(beautify_icon_8b1978126c8e4cf9a2a0a2d021cb6cc7);
        
    
            marker_24a3ed4e3b194afeaacb8b6aa6202052.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6c9759045e16405f91fc9893fb2e0286 = L.marker(
                [49.26925300030199, -123.22508963029917],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_3b360f82dad74eca8ca0e6804673e87a = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6c9759045e16405f91fc9893fb2e0286.setIcon(beautify_icon_3b360f82dad74eca8ca0e6804673e87a);
        
    
            marker_6c9759045e16405f91fc9893fb2e0286.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_eee379673fa14a17bb4aec8d08d38acd = L.marker(
                [49.269410514232334, -123.236824664439],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_e73befce5288446f9213365501a2819c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_eee379673fa14a17bb4aec8d08d38acd.setIcon(beautify_icon_e73befce5288446f9213365501a2819c);
        
    
            marker_eee379673fa14a17bb4aec8d08d38acd.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7871306b17a040618a0e6364dae1c492 = L.marker(
                [49.269463018586016, -123.23824655926265],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_8a409ef4d4f54d52b76da116c013fa64 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7871306b17a040618a0e6364dae1c492.setIcon(beautify_icon_8a409ef4d4f54d52b76da116c013fa64);
        
    
            marker_7871306b17a040618a0e6364dae1c492.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e3527fc7f53b4c3cb2767ba9bda86241 = L.marker(
                [49.269517973077306, -123.2396608563873],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_ea33374fdbc44fa1affe9f9a4e4fee7e = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e3527fc7f53b4c3cb2767ba9bda86241.setIcon(beautify_icon_ea33374fdbc44fa1affe9f9a4e4fee7e);
        
    
            marker_e3527fc7f53b4c3cb2767ba9bda86241.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_2384e3b8075345ec92353d08870dfae2 = L.marker(
                [49.269935555468216, -123.22464750117899],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_0a3168d09fe74f69875a6b6ddbde08e5 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_2384e3b8075345ec92353d08870dfae2.setIcon(beautify_icon_0a3168d09fe74f69875a6b6ddbde08e5);
        
    
            marker_2384e3b8075345ec92353d08870dfae2.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7700d892ee4243b08f9441c7eb517c8f = L.marker(
                [49.273416093707475, -123.22652292641796],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_7756879ce6a2430fb707d63a9b6b3b58 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7700d892ee4243b08f9441c7eb517c8f.setIcon(beautify_icon_7756879ce6a2430fb707d63a9b6b3b58);
        
    
            marker_7700d892ee4243b08f9441c7eb517c8f.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_984f6f178ca744f1b8562d23879c0790 = L.marker(
                [49.276369318151325, -123.22566353169596],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_54a0089f82ff410d9f522ac6ac9e0eee = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_984f6f178ca744f1b8562d23879c0790.setIcon(beautify_icon_54a0089f82ff410d9f522ac6ac9e0eee);
        
    
            marker_984f6f178ca744f1b8562d23879c0790.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_cf3c673c18204c7784fd4dee346f1cac = L.marker(
                [49.277224663173136, -123.22475370104767],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_2488c08627f34ea591244b21fd59086a = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_cf3c673c18204c7784fd4dee346f1cac.setIcon(beautify_icon_2488c08627f34ea591244b21fd59086a);
        
    
            marker_cf3c673c18204c7784fd4dee346f1cac.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_3c4a1f93691a4c9f9d7f51aeabf58746 = L.marker(
                [49.235906879671695, -123.19732040461656],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_be303161d5d04f36b901923fee56eee2 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_3c4a1f93691a4c9f9d7f51aeabf58746.setIcon(beautify_icon_be303161d5d04f36b901923fee56eee2);
        
    
            marker_3c4a1f93691a4c9f9d7f51aeabf58746.bindTooltip(
                `<div>
                     StGeorges
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_39138fe142544e8a95483f2fb52f0cf0 = L.marker(
                [49.24460115666956, -123.19866919610129],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_7cce04b488dc464bbeefda160b128d5d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_39138fe142544e8a95483f2fb52f0cf0.setIcon(beautify_icon_7cce04b488dc464bbeefda160b128d5d);
        
    
            marker_39138fe142544e8a95483f2fb52f0cf0.bindTooltip(
                `<div>
                     StGeorges
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6f2a9936144d448c97b430cef37c8fe4 = L.marker(
                [49.24065628050064, -123.19805555088485],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_1f65627861c34e08b811c521cc5b0f1d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6f2a9936144d448c97b430cef37c8fe4.setIcon(beautify_icon_1f65627861c34e08b811c521cc5b0f1d);
        
    
            marker_6f2a9936144d448c97b430cef37c8fe4.bindTooltip(
                `<div>
                     StGeorges
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1818d19edabd45ff9a7bd5e3f3332a5b = L.marker(
                [49.235261334425765, -123.19719307452199],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_024842abdffe4a1e903a69d31984968e = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_1818d19edabd45ff9a7bd5e3f3332a5b.setIcon(beautify_icon_024842abdffe4a1e903a69d31984968e);
        
    
            marker_1818d19edabd45ff9a7bd5e3f3332a5b.bindTooltip(
                `<div>
                     SWMarine
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_b3e60152acb5483eb1c7d0e9ca019681 = L.marker(
                [49.235976935113186, -123.19963935867693],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_850fa466cf4745d68b89fcc4c1bbe3d4 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_b3e60152acb5483eb1c7d0e9ca019681.setIcon(beautify_icon_850fa466cf4745d68b89fcc4c1bbe3d4);
        
    
            marker_b3e60152acb5483eb1c7d0e9ca019681.bindTooltip(
                `<div>
                     SWMarine
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d37f43a462bf4883b34ff00f9d8d113c = L.marker(
                [49.236817568930825, -123.20255493499178],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_3832abc741f348c2a0d5149c2acbe9d6 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d37f43a462bf4883b34ff00f9d8d113c.setIcon(beautify_icon_3832abc741f348c2a0d5149c2acbe9d6);
        
    
            marker_d37f43a462bf4883b34ff00f9d8d113c.bindTooltip(
                `<div>
                     SWMarine
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_554af175d267449486bcfe38bd8954db = L.marker(
                [49.23913203905868, -123.21319816578028],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_a158989bb26c4194848c757dfbdf8fc4 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_554af175d267449486bcfe38bd8954db.setIcon(beautify_icon_a158989bb26c4194848c757dfbdf8fc4);
        
    
            marker_554af175d267449486bcfe38bd8954db.bindTooltip(
                `<div>
                     SWMarine
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_52b53e863a7140b1989f98e0c4bcf68b = L.marker(
                [49.24169856669397, -123.22657827077154],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_4e8f534492df44149c9fb1160b519d1d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_52b53e863a7140b1989f98e0c4bcf68b.setIcon(beautify_icon_4e8f534492df44149c9fb1160b519d1d);
        
    
            marker_52b53e863a7140b1989f98e0c4bcf68b.bindTooltip(
                `<div>
                     SWMarine
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_01221dd0bf5149faa72884ab2b9cede3 = L.marker(
                [49.24280877231211, -123.22917528727058],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_29648946684a4b04a217b128d528c0b8 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_01221dd0bf5149faa72884ab2b9cede3.setIcon(beautify_icon_29648946684a4b04a217b128d528c0b8);
        
    
            marker_01221dd0bf5149faa72884ab2b9cede3.bindTooltip(
                `<div>
                     SWMarine
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_36cfed0c1daf4fceb7085e5cbc281e9f = L.marker(
                [49.244152892993725, -123.22571937721548],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_c2a824ddc5c44d2fafbd615aba1be8e8 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_36cfed0c1daf4fceb7085e5cbc281e9f.setIcon(beautify_icon_c2a824ddc5c44d2fafbd615aba1be8e8);
        
    
            marker_36cfed0c1daf4fceb7085e5cbc281e9f.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_5aa3505cf3e6483bad27feb8f2c5801b = L.marker(
                [49.24761844043816, -123.22539114536748],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_55457b3f167b40d3b94d840092a4f2fd = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_5aa3505cf3e6483bad27feb8f2c5801b.setIcon(beautify_icon_55457b3f167b40d3b94d840092a4f2fd);
        
    
            marker_5aa3505cf3e6483bad27feb8f2c5801b.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_73431c21c9f340c8827a19d85ec79a5e = L.marker(
                [49.249332213665966, -123.22563092656476],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_9639010748134b12b2245f2e97dc5add = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_73431c21c9f340c8827a19d85ec79a5e.setIcon(beautify_icon_9639010748134b12b2245f2e97dc5add);
        
    
            marker_73431c21c9f340c8827a19d85ec79a5e.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f8d1c11904404a19a31acaa6264462ef = L.marker(
                [49.25074759018555, -123.22706200443643],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_96d0980e3bc44573b72bb0a5ec5fbf6c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_f8d1c11904404a19a31acaa6264462ef.setIcon(beautify_icon_96d0980e3bc44573b72bb0a5ec5fbf6c);
        
    
            marker_f8d1c11904404a19a31acaa6264462ef.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_0eb1ee7d8d3b40d4baa700ca163872bc = L.marker(
                [49.25509501355131, -123.22802586958822],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_a5b2d4fa6d864ab6b6e66382320ed150 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_0eb1ee7d8d3b40d4baa700ca163872bc.setIcon(beautify_icon_a5b2d4fa6d864ab6b6e66382320ed150);
        
    
            marker_0eb1ee7d8d3b40d4baa700ca163872bc.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d192eda934664903a4c8c1d419e4f832 = L.marker(
                [49.25745414324946, -123.22724728795409],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_a0da33e1b1f34290991a07070ec05909 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d192eda934664903a4c8c1d419e4f832.setIcon(beautify_icon_a0da33e1b1f34290991a07070ec05909);
        
    
            marker_d192eda934664903a4c8c1d419e4f832.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6b562e6eeff345129f2d790a1b5fdd8d = L.marker(
                [49.25919138261423, -123.23231456337898],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_8b8cc8beb4b5446799d6226ede0eba01 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6b562e6eeff345129f2d790a1b5fdd8d.setIcon(beautify_icon_8b8cc8beb4b5446799d6226ede0eba01);
        
    
            marker_6b562e6eeff345129f2d790a1b5fdd8d.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_3101c444be494becb898169d5aa0226e = L.marker(
                [49.260384866994656, -123.23315819132735],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_8303aded4fe34a8a9d01a06d04cfd50f = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_3101c444be494becb898169d5aa0226e.setIcon(beautify_icon_8303aded4fe34a8a9d01a06d04cfd50f);
        
    
            marker_3101c444be494becb898169d5aa0226e.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d745033d01024c65b013caf096504da3 = L.marker(
                [49.26061400305219, -123.23368234579458],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_f0d9b985c59b48b7afd7231854dc5581 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d745033d01024c65b013caf096504da3.setIcon(beautify_icon_f0d9b985c59b48b7afd7231854dc5581);
        
    
            marker_d745033d01024c65b013caf096504da3.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_401f2435824a48ea9ff3942b8d6da2b0 = L.marker(
                [49.26742790482839, -123.23652978623842],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_d69d62af3f3c40a589345c58aea74de1 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_401f2435824a48ea9ff3942b8d6da2b0.setIcon(beautify_icon_d69d62af3f3c40a589345c58aea74de1);
        
    
            marker_401f2435824a48ea9ff3942b8d6da2b0.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7e19aae1724a4488bb91a0e66130a170 = L.marker(
                [49.26895967378132, -123.23792415270513],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_79fda1b1028743839a60ca5a24fc7c6b = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7e19aae1724a4488bb91a0e66130a170.setIcon(beautify_icon_79fda1b1028743839a60ca5a24fc7c6b);
        
    
            marker_7e19aae1724a4488bb91a0e66130a170.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7594dc1ac33f46de9a017e096048b412 = L.marker(
                [49.271038826924624, -123.23952455572746],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_da621d98fa6143429287b026d492822d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7594dc1ac33f46de9a017e096048b412.setIcon(beautify_icon_da621d98fa6143429287b026d492822d);
        
    
            marker_7594dc1ac33f46de9a017e096048b412.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_fd0f6d57e5ac443687942525b4b1e850 = L.marker(
                [49.27226457601742, -123.23931623186071],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_5fa7a59867234f02abb3fce782a20ba4 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_fd0f6d57e5ac443687942525b4b1e850.setIcon(beautify_icon_5fa7a59867234f02abb3fce782a20ba4);
        
    
            marker_fd0f6d57e5ac443687942525b4b1e850.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_12e80c2340434cadbc009429f2d46c7f = L.marker(
                [49.27231707744041, -123.24068386837985],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_02d8d555ad7c4548add8d807e78cf1ae = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_12e80c2340434cadbc009429f2d46c7f.setIcon(beautify_icon_02d8d555ad7c4548add8d807e78cf1ae);
        
    
            marker_12e80c2340434cadbc009429f2d46c7f.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ba1f86f7f9a14c99a62fa82cbf54ea5b = L.marker(
                [49.24961655396423, -123.19659844469622],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_1bcfa76acdc34534a0877dfa49944a79 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ba1f86f7f9a14c99a62fa82cbf54ea5b.setIcon(beautify_icon_1bcfa76acdc34534a0877dfa49944a79);
        
    
            marker_ba1f86f7f9a14c99a62fa82cbf54ea5b.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_40cbac5ce0a64427b01dade3626dfbeb = L.marker(
                [49.24969149001777, -123.20346136911543],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_befa96c90d674af795c8d921c1d8e955 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_40cbac5ce0a64427b01dade3626dfbeb.setIcon(beautify_icon_befa96c90d674af795c8d921c1d8e955);
        
    
            marker_40cbac5ce0a64427b01dade3626dfbeb.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f5f42773324046da98f30750f61dc6d6 = L.marker(
                [49.2499964868117, -123.19769718017821],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_47ecdefcac634c3fa9d841c375ebcb7a = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_f5f42773324046da98f30750f61dc6d6.setIcon(beautify_icon_47ecdefcac634c3fa9d841c375ebcb7a);
        
    
            marker_f5f42773324046da98f30750f61dc6d6.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_b50a4a8de62d4ea79b7f1c36ea79300c = L.marker(
                [49.250014695194515, -123.2013588349101],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_f281ca580c9e433aaeaaf19ddb4e501b = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_b50a4a8de62d4ea79b7f1c36ea79300c.setIcon(beautify_icon_f281ca580c9e433aaeaaf19ddb4e501b);
        
    
            marker_b50a4a8de62d4ea79b7f1c36ea79300c.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_161331a1b42f4f76ad7c307fa7985c9a = L.marker(
                [49.250025900596434, -123.2017251470642],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_6a78500b7e5a45cead47593809e2b1bf = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_161331a1b42f4f76ad7c307fa7985c9a.setIcon(beautify_icon_6a78500b7e5a45cead47593809e2b1bf);
        
    
            marker_161331a1b42f4f76ad7c307fa7985c9a.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6e57a6d65a7548c2910cc8e4038082a6 = L.marker(
                [49.25009628601198, -123.19516363894176],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_68e457e7cbc4468593658a16d8158f07 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6e57a6d65a7548c2910cc8e4038082a6.setIcon(beautify_icon_68e457e7cbc4468593658a16d8158f07);
        
    
            marker_6e57a6d65a7548c2910cc8e4038082a6.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_bf918c05786b4c9baca1e011da94bc6b = L.marker(
                [49.25014968458406, -123.20250884257015],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_d5f201313b74414f8181e40bc66f0876 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_bf918c05786b4c9baca1e011da94bc6b.setIcon(beautify_icon_d5f201313b74414f8181e40bc66f0876);
        
    
            marker_bf918c05786b4c9baca1e011da94bc6b.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e6deb0a9098c44dd9af36138f772c9e7 = L.marker(
                [49.2501561627531, -123.19898916914221],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_7afc6a773cee4f1aa6c06534fc5ed30a = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e6deb0a9098c44dd9af36138f772c9e7.setIcon(beautify_icon_7afc6a773cee4f1aa6c06534fc5ed30a);
        
    
            marker_e6deb0a9098c44dd9af36138f772c9e7.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_eb27dac866f34fafa58d9f5d06c4f830 = L.marker(
                [49.25017752316746, -123.20017965282354],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_fff8bbaef2f1483499608f65f252b1b0 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_eb27dac866f34fafa58d9f5d06c4f830.setIcon(beautify_icon_fff8bbaef2f1483499608f65f252b1b0);
        
    
            marker_eb27dac866f34fafa58d9f5d06c4f830.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d2dcea178192473e83d3d2029b4a1ed8 = L.marker(
                [49.253707074372755, -123.20591064578846],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_6011762063294bd4afea6e2217e1f653 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d2dcea178192473e83d3d2029b4a1ed8.setIcon(beautify_icon_6011762063294bd4afea6e2217e1f653);
        
    
            marker_d2dcea178192473e83d3d2029b4a1ed8.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_47e277fa076e40a9a5ffe8e0281051ba = L.marker(
                [49.2565753478446, -123.20868433795873],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_907902570c8442a88d0c1bd26456d675 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_47e277fa076e40a9a5ffe8e0281051ba.setIcon(beautify_icon_907902570c8442a88d0c1bd26456d675);
        
    
            marker_47e277fa076e40a9a5ffe8e0281051ba.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6d0bb85cc63f4a6ea4d17579eb38029c = L.marker(
                [49.256987088339024, -123.2099409545067],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_ef018e36b6514a2c8747420b13adcae9 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6d0bb85cc63f4a6ea4d17579eb38029c.setIcon(beautify_icon_ef018e36b6514a2c8747420b13adcae9);
        
    
            marker_6d0bb85cc63f4a6ea4d17579eb38029c.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ee299f933b0a48ecb1ffd2cc843f84d4 = L.marker(
                [49.25770622570259, -123.21143460691229],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_1a85296300a34ef998ede7dd6d72e9c1 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ee299f933b0a48ecb1ffd2cc843f84d4.setIcon(beautify_icon_1a85296300a34ef998ede7dd6d72e9c1);
        
    
            marker_ee299f933b0a48ecb1ffd2cc843f84d4.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a969389da5da4b40911fe55a4d41b5a7 = L.marker(
                [49.272353478212686, -123.25557951783816],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_6d57b55bddda48a5bf47688983aab6f5 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_a969389da5da4b40911fe55a4d41b5a7.setIcon(beautify_icon_6d57b55bddda48a5bf47688983aab6f5);
        
    
            marker_a969389da5da4b40911fe55a4d41b5a7.bindTooltip(
                `<div>
                     Trail3
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c41c9ae5b7a44eeea44b284a76f8f249 = L.marker(
                [49.26270768550325, -123.26013187186993],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_af9c6522df2143b2a5d92b0572bbbf1b = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_c41c9ae5b7a44eeea44b284a76f8f249.setIcon(beautify_icon_af9c6522df2143b2a5d92b0572bbbf1b);
        
    
            marker_c41c9ae5b7a44eeea44b284a76f8f249.bindTooltip(
                `<div>
                     Trail6
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_be12cbf3775349d781faa3e9059893d0 = L.marker(
                [49.251882104228436, -123.25109696206337],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_2dfb4bb8aa9a4d1a88a6c0f92779f78a = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_be12cbf3775349d781faa3e9059893d0.setIcon(beautify_icon_2dfb4bb8aa9a4d1a88a6c0f92779f78a);
        
    
            marker_be12cbf3775349d781faa3e9059893d0.bindTooltip(
                `<div>
                     Trail7
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ab612061eede48c5807abcadeca2733c = L.marker(
                [49.259746641524444, -123.21631657719769],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_9d7da65d2d06483ea27b54826511f66a = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ab612061eede48c5807abcadeca2733c.setIcon(beautify_icon_9d7da65d2d06483ea27b54826511f66a);
        
    
            marker_ab612061eede48c5807abcadeca2733c.bindTooltip(
                `<div>
                     VineMaple
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6c06807f1eb742428534285b477cdd6a = L.marker(
                [49.26043142953275, -123.21779789941863],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_6a13fc513bae4b5e8cc4e5c79e6c3bea = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6c06807f1eb742428534285b477cdd6a.setIcon(beautify_icon_6a13fc513bae4b5e8cc4e5c79e6c3bea);
        
    
            marker_6c06807f1eb742428534285b477cdd6a.bindTooltip(
                `<div>
                     VineMaple
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_306d5e644da2498cbb6241b78b4ce198 = L.marker(
                [49.274789480143426, -123.23226658719038],
                {"riseOnHover": true}
            ).addTo(feature_group_20508be17e294f409fe58ef01f7f2234);
        
    
            var beautify_icon_955147da35994284a645974d06689068 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#cc0000;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_306d5e644da2498cbb6241b78b4ce198.setIcon(beautify_icon_955147da35994284a645974d06689068);
        
    
            marker_306d5e644da2498cbb6241b78b4ce198.bindTooltip(
                `<div>
                     WestCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var feature_group_84e81030d853452fb395d2aa9dc3ec58 = L.featureGroup(
                {}
            ).addTo(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
        
    
            var marker_e089816385d342788c00a64a88aa1d0c = L.marker(
                [49.279367161347785, -123.2415175867091],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_dde073deb35d46aabec967308849cd2b = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e089816385d342788c00a64a88aa1d0c.setIcon(beautify_icon_dde073deb35d46aabec967308849cd2b);
        
    
            marker_e089816385d342788c00a64a88aa1d0c.bindTooltip(
                `<div>
                     AcadiaBeach
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_82e6a2d95c9e4b9b80e8b1d2827aee36 = L.marker(
                [49.277086773057036, -123.22542452176616],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_6d0c3a53ed1c498a9e449488aa75c3ac = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_82e6a2d95c9e4b9b80e8b1d2827aee36.setIcon(beautify_icon_6d0c3a53ed1c498a9e449488aa75c3ac);
        
    
            marker_82e6a2d95c9e4b9b80e8b1d2827aee36.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7f1baba0afb54c09b5546e57c9a3378a = L.marker(
                [49.277411549383096, -123.2281130458741],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_0082b3f3bcd14a6f8cb65d47ecc817a1 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7f1baba0afb54c09b5546e57c9a3378a.setIcon(beautify_icon_0082b3f3bcd14a6f8cb65d47ecc817a1);
        
    
            marker_7f1baba0afb54c09b5546e57c9a3378a.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_744be09380704fdb89b3919dffffd781 = L.marker(
                [49.277415748889865, -123.23157294794753],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_9aadf3cf6a9942298af3f3e2e7e0bf88 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_744be09380704fdb89b3919dffffd781.setIcon(beautify_icon_9aadf3cf6a9942298af3f3e2e7e0bf88);
        
    
            marker_744be09380704fdb89b3919dffffd781.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d275b8a941ba45b3bb852c3a80e3983b = L.marker(
                [49.277465445144415, -123.23061039535486],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_b2524669230a410cb564735d206a780e = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d275b8a941ba45b3bb852c3a80e3983b.setIcon(beautify_icon_b2524669230a410cb564735d206a780e);
        
    
            marker_d275b8a941ba45b3bb852c3a80e3983b.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a1f9269eaf924c6891bc6840b6b49f0b = L.marker(
                [49.278299072800586, -123.23659531243227],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_85c8df434ce0415996d851fae818c18a = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_a1f9269eaf924c6891bc6840b6b49f0b.setIcon(beautify_icon_85c8df434ce0415996d851fae818c18a);
        
    
            marker_a1f9269eaf924c6891bc6840b6b49f0b.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e90df91d355c45dabcf9270bff9153db = L.marker(
                [49.27887581508334, -123.24255526064007],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_eb16818cbfb74fcaa931a24a36483bf9 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e90df91d355c45dabcf9270bff9153db.setIcon(beautify_icon_eb16818cbfb74fcaa931a24a36483bf9);
        
    
            marker_e90df91d355c45dabcf9270bff9153db.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_9305ef51834044e3b941dfee32e7a32e = L.marker(
                [49.27912008855083, -123.24128794767657],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_37e1df57840e4568913b7f14a55dee2b = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_9305ef51834044e3b941dfee32e7a32e.setIcon(beautify_icon_37e1df57840e4568913b7f14a55dee2b);
        
    
            marker_9305ef51834044e3b941dfee32e7a32e.bindTooltip(
                `<div>
                     Admiralty
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_8d6f37de6a23478ab63ca8148fe059bb = L.marker(
                [49.25036241002851, -123.1991790738853],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_10ad7991d2a04971b3c6f22bf9ab1c99 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_8d6f37de6a23478ab63ca8148fe059bb.setIcon(beautify_icon_10ad7991d2a04971b3c6f22bf9ab1c99);
        
    
            marker_8d6f37de6a23478ab63ca8148fe059bb.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_10d105cbd0b84e0c9a36b8a955a624a3 = L.marker(
                [49.25146191592837, -123.19949840154771],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_9c459c1b121a4b35ad94118c08c28283 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_10d105cbd0b84e0c9a36b8a955a624a3.setIcon(beautify_icon_9c459c1b121a4b35ad94118c08c28283);
        
    
            marker_10d105cbd0b84e0c9a36b8a955a624a3.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_3c7742b554754a1aa81c4073281c654d = L.marker(
                [49.25213736475354, -123.19979137418355],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_d8c606eb602c4aa3a7fc2ac5f4de351c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_3c7742b554754a1aa81c4073281c654d.setIcon(beautify_icon_d8c606eb602c4aa3a7fc2ac5f4de351c);
        
    
            marker_3c7742b554754a1aa81c4073281c654d.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_245aad4594b84f0baa62baeb3f75ac35 = L.marker(
                [49.2525852078819, -123.19963866360983],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_acdaa0ac8e174a368ce61b8514b5c5be = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_245aad4594b84f0baa62baeb3f75ac35.setIcon(beautify_icon_acdaa0ac8e174a368ce61b8514b5c5be);
        
    
            marker_245aad4594b84f0baa62baeb3f75ac35.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_0473cc2e69f548e182df5dabe47947e5 = L.marker(
                [49.25351169426171, -123.19909478573177],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_466c7c831fd64e2a97a0035904cdc3f7 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_0473cc2e69f548e182df5dabe47947e5.setIcon(beautify_icon_466c7c831fd64e2a97a0035904cdc3f7);
        
    
            marker_0473cc2e69f548e182df5dabe47947e5.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_0ec6708586074023aefb748b3e6b08a2 = L.marker(
                [49.25413564504425, -123.19790011911398],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_84e61864f14f44dab425cce2555884fd = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_0ec6708586074023aefb748b3e6b08a2.setIcon(beautify_icon_84e61864f14f44dab425cce2555884fd);
        
    
            marker_0ec6708586074023aefb748b3e6b08a2.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a73050dc148c4dfe83a3aca4c971815b = L.marker(
                [49.2543597327169, -123.1993278244398],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_c10be227e3764333b96aac799b7f2968 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_a73050dc148c4dfe83a3aca4c971815b.setIcon(beautify_icon_c10be227e3764333b96aac799b7f2968);
        
    
            marker_a73050dc148c4dfe83a3aca4c971815b.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_b8f9f95f7d5c487aabdf10b09ffdb5ba = L.marker(
                [49.25437583867633, -123.19693670213738],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_0d0179f166a149cc89bf3211dcbe3937 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_b8f9f95f7d5c487aabdf10b09ffdb5ba.setIcon(beautify_icon_0d0179f166a149cc89bf3211dcbe3937);
        
    
            marker_b8f9f95f7d5c487aabdf10b09ffdb5ba.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a1a01fae73d24dd9abad63d4df7fd5aa = L.marker(
                [49.25440174910239, -123.19976225015763],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_f6a105943f2746e2a6857b1ff7bea062 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_a1a01fae73d24dd9abad63d4df7fd5aa.setIcon(beautify_icon_f6a105943f2746e2a6857b1ff7bea062);
        
    
            marker_a1a01fae73d24dd9abad63d4df7fd5aa.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ce473a406fba47cd8a272186d283167d = L.marker(
                [49.25443256083923, -123.19702720576947],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_e6337aa12df34e2faf2bd9847e7bf00d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ce473a406fba47cd8a272186d283167d.setIcon(beautify_icon_e6337aa12df34e2faf2bd9847e7bf00d);
        
    
            marker_ce473a406fba47cd8a272186d283167d.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_84dec8c1c28b47619f9c64b52cb10369 = L.marker(
                [49.254461272574474, -123.19731552154306],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_ced283587fe646678f4f1ff4505aa8d6 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_84dec8c1c28b47619f9c64b52cb10369.setIcon(beautify_icon_ced283587fe646678f4f1ff4505aa8d6);
        
    
            marker_84dec8c1c28b47619f9c64b52cb10369.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_9488b831adee4a76a1e48b3069dd341d = L.marker(
                [49.25454180346234, -123.19955844549989],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_47d657eecc8a49c4b312e048cad81832 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_9488b831adee4a76a1e48b3069dd341d.setIcon(beautify_icon_47d657eecc8a49c4b312e048cad81832);
        
    
            marker_9488b831adee4a76a1e48b3069dd341d.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1dcc1ac93d1148d3907f03054e9e9363 = L.marker(
                [49.254572615646026, -123.1986059266925],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_731ca28b012046e3b9214a064278502c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_1dcc1ac93d1148d3907f03054e9e9363.setIcon(beautify_icon_731ca28b012046e3b9214a064278502c);
        
    
            marker_1dcc1ac93d1148d3907f03054e9e9363.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_42ad608ede6d4aeaab5ead0eabdd6144 = L.marker(
                [49.25474138055923, -123.19762659181015],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_83a3fdf5bff346288e3cbb605794a298 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_42ad608ede6d4aeaab5ead0eabdd6144.setIcon(beautify_icon_83a3fdf5bff346288e3cbb605794a298);
        
    
            marker_42ad608ede6d4aeaab5ead0eabdd6144.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_cf2b5575886847649307a378a50c86cd = L.marker(
                [49.25481070699733, -123.19666120132608],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_36fff7b4a1d64153a326a26b095853ff = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_cf2b5575886847649307a378a50c86cd.setIcon(beautify_icon_36fff7b4a1d64153a326a26b095853ff);
        
    
            marker_cf2b5575886847649307a378a50c86cd.bindTooltip(
                `<div>
                     Camosun
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_5a45221e75474211b84ee3d23ef2b45b = L.marker(
                [49.270760211921264, -123.22665678758698],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_6507c1d037824c48ae1104d548eafcff = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_5a45221e75474211b84ee3d23ef2b45b.setIcon(beautify_icon_6507c1d037824c48ae1104d548eafcff);
        
    
            marker_5a45221e75474211b84ee3d23ef2b45b.bindTooltip(
                `<div>
                     Chancellor
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_b4d2cc5470764b3082775cbef5fb6324 = L.marker(
                [49.27099752451536, -123.22886167332753],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_729cb6a374174814bd6b27d0ac1c8e5d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_b4d2cc5470764b3082775cbef5fb6324.setIcon(beautify_icon_729cb6a374174814bd6b27d0ac1c8e5d);
        
    
            marker_b4d2cc5470764b3082775cbef5fb6324.bindTooltip(
                `<div>
                     Chancellor
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ea693e6545e84cdb9cf7765ea1da51b5 = L.marker(
                [49.26060857735795, -123.22510343446619],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_b1080b0ec9dc42b681e191b4bb65f77d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_ea693e6545e84cdb9cf7765ea1da51b5.setIcon(beautify_icon_b1080b0ec9dc42b681e191b4bb65f77d);
        
    
            marker_ea693e6545e84cdb9cf7765ea1da51b5.bindTooltip(
                `<div>
                     Cleveland
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_3b0feaf5ec944ad5be2bbcabf7704545 = L.marker(
                [49.26224978304391, -123.22780223759005],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_13204ca8bb5647ddaa6e8c5d6ec030c3 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_3b0feaf5ec944ad5be2bbcabf7704545.setIcon(beautify_icon_13204ca8bb5647ddaa6e8c5d6ec030c3);
        
    
            marker_3b0feaf5ec944ad5be2bbcabf7704545.bindTooltip(
                `<div>
                     Cleveland
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c9b34f17685a4c8b8b317e28aaedc803 = L.marker(
                [49.257129936924855, -123.20959368261413],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_c7f7b9cf3c7c4f029ca3c95974b18d85 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_c9b34f17685a4c8b8b317e28aaedc803.setIcon(beautify_icon_c7f7b9cf3c7c4f029ca3c95974b18d85);
        
    
            marker_c9b34f17685a4c8b8b317e28aaedc803.bindTooltip(
                `<div>
                     ConcreteMystery
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_469f12e076eb450d9966701084a547b9 = L.marker(
                [49.25659145332148, -123.21012321536087],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_10d2e590dbdf4ab7aafc773de4e739a5 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_469f12e076eb450d9966701084a547b9.setIcon(beautify_icon_10d2e590dbdf4ab7aafc773de4e739a5);
        
    
            marker_469f12e076eb450d9966701084a547b9.bindTooltip(
                `<div>
                     ConcreteMystery
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7f78726bad284d48ade1d28182c9788f = L.marker(
                [49.256258837379846, -123.2096566099602],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_5596bb4cf1d74425a973acc6be80cb2d = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7f78726bad284d48ade1d28182c9788f.setIcon(beautify_icon_5596bb4cf1d74425a973acc6be80cb2d);
        
    
            marker_7f78726bad284d48ade1d28182c9788f.bindTooltip(
                `<div>
                     ConcreteMystery
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_df4f4147eef84ceba96b26dc3b4a914d = L.marker(
                [49.270955172164186, -123.2293803226852],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_dd39613c98e54f759e898b45719d0bab = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_df4f4147eef84ceba96b26dc3b4a914d.setIcon(beautify_icon_dd39613c98e54f759e898b45719d0bab);
        
    
            marker_df4f4147eef84ceba96b26dc3b4a914d.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_551886aaabd8409cb69b28b59cabe549 = L.marker(
                [49.271323741033676, -123.2294267721951],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_1e53531558be4ead9377c91ebc65abab = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_551886aaabd8409cb69b28b59cabe549.setIcon(beautify_icon_1e53531558be4ead9377c91ebc65abab);
        
    
            marker_551886aaabd8409cb69b28b59cabe549.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_fb9be8d4a0694b059a84115c657c1379 = L.marker(
                [49.27245567977517, -123.22986593146656],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_1020d6aa74c94f58a9fa054d4cccee09 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_fb9be8d4a0694b059a84115c657c1379.setIcon(beautify_icon_1020d6aa74c94f58a9fa054d4cccee09);
        
    
            marker_fb9be8d4a0694b059a84115c657c1379.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7d8e8f7c4b0b41ca93a1e821f8c20151 = L.marker(
                [49.27302164060763, -123.22965976506511],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_e40697ee1ad64a2d9fd9519b16c9becc = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7d8e8f7c4b0b41ca93a1e821f8c20151.setIcon(beautify_icon_e40697ee1ad64a2d9fd9519b16c9becc);
        
    
            marker_7d8e8f7c4b0b41ca93a1e821f8c20151.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_40f927bc5efa44dea2ed257f96c6b36d = L.marker(
                [49.27425889093808, -123.23057514864767],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_8f3a473555c24cea92ba9b0003c0de2e = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_40f927bc5efa44dea2ed257f96c6b36d.setIcon(beautify_icon_8f3a473555c24cea92ba9b0003c0de2e);
        
    
            marker_40f927bc5efa44dea2ed257f96c6b36d.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a36d23f0575a4bfd99dcc0410c41ddea = L.marker(
                [49.27629022342389, -123.23071030370826],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_402f5baba0db42d2ad5631f1f24f8fd4 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_a36d23f0575a4bfd99dcc0410c41ddea.setIcon(beautify_icon_402f5baba0db42d2ad5631f1f24f8fd4);
        
    
            marker_a36d23f0575a4bfd99dcc0410c41ddea.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_18482f0519f94036b8c5b73c8dfd28ac = L.marker(
                [49.2772533616488, -123.23020452602734],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_48b2b772e0aa4ed88303b394f8fc42de = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_18482f0519f94036b8c5b73c8dfd28ac.setIcon(beautify_icon_48b2b772e0aa4ed88303b394f8fc42de);
        
    
            marker_18482f0519f94036b8c5b73c8dfd28ac.bindTooltip(
                `<div>
                     EastCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_11c752bbec194fa4aa7bdda613b54475 = L.marker(
                [49.25874464956123, -123.21896105165592],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_773f15ab54984700a7ad53dc6cfb5c2f = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_11c752bbec194fa4aa7bdda613b54475.setIcon(beautify_icon_773f15ab54984700a7ad53dc6cfb5c2f);
        
    
            marker_11c752bbec194fa4aa7bdda613b54475.bindTooltip(
                `<div>
                     Heron
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_2ae7ead581bf49bdbe5f60a57055816c = L.marker(
                [49.25949527021685, -123.22151906618171],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_ce750f13990a4cc69b3d4f1527291073 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_2ae7ead581bf49bdbe5f60a57055816c.setIcon(beautify_icon_ce750f13990a4cc69b3d4f1527291073);
        
    
            marker_2ae7ead581bf49bdbe5f60a57055816c.bindTooltip(
                `<div>
                     Heron
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_47435c4590b7472ea08568f32256421a = L.marker(
                [49.26046398823978, -123.23325712380753],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_d8709bdc9ba04c79afc6f49101b405dc = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_47435c4590b7472ea08568f32256421a.setIcon(beautify_icon_d8709bdc9ba04c79afc6f49101b405dc);
        
    
            marker_47435c4590b7472ea08568f32256421a.bindTooltip(
                `<div>
                     Heron
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_95acc5be0caf4037b4b8c68af38a3c90 = L.marker(
                [49.249312254168984, -123.20513537354506],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_e0918cab70e14338a13f63597b7b7bf9 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_95acc5be0caf4037b4b8c68af38a3c90.setIcon(beautify_icon_e0918cab70e14338a13f63597b7b7bf9);
        
    
            marker_95acc5be0caf4037b4b8c68af38a3c90.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_07401eb4f7914c8c9a2c3a388f895d8b = L.marker(
                [49.24924046875497, -123.20546523861384],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_f76d0fa1228d43d1961005dbf0089b39 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_07401eb4f7914c8c9a2c3a388f895d8b.setIcon(beautify_icon_f76d0fa1228d43d1961005dbf0089b39);
        
    
            marker_07401eb4f7914c8c9a2c3a388f895d8b.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4fa39d24784a4035be08aa4ef5e2538b = L.marker(
                [49.24918619190925, -123.20489458560488],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_18da34ef6b1a4bd080c10aef4c819108 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_4fa39d24784a4035be08aa4ef5e2538b.setIcon(beautify_icon_18da34ef6b1a4bd080c10aef4c819108);
        
    
            marker_4fa39d24784a4035be08aa4ef5e2538b.bindTooltip(
                `<div>
                     Imperial
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_99f829cb10344527979a7fb618069c7c = L.marker(
                [49.261363370217595, -123.22737657484453],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_53b321f5fd974cecb323f48c8ce1837a = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_99f829cb10344527979a7fb618069c7c.setIcon(beautify_icon_53b321f5fd974cecb323f48c8ce1837a);
        
    
            marker_99f829cb10344527979a7fb618069c7c.bindTooltip(
                `<div>
                     LilyOfTheValley
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d57c4b46b7084c798d4121ea222f6eaf = L.marker(
                [49.26901567872852, -123.22868189178706],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_0246854054234a46afdde5b05a735c3e = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d57c4b46b7084c798d4121ea222f6eaf.setIcon(beautify_icon_0246854054234a46afdde5b05a735c3e);
        
    
            marker_d57c4b46b7084c798d4121ea222f6eaf.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_932e82e834434bcab0c37578c70e4d66 = L.marker(
                [49.27066990652504, -123.22859816753724],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_cd701f3d15044e53985f5265a5828ef3 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_932e82e834434bcab0c37578c70e4d66.setIcon(beautify_icon_cd701f3d15044e53985f5265a5828ef3);
        
    
            marker_932e82e834434bcab0c37578c70e4d66.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_34dbc5160eb8482888aefcbb6e7f1d79 = L.marker(
                [49.271967066203835, -123.22860348645277],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_42e701866afa40deb42a98911e93e2d1 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_34dbc5160eb8482888aefcbb6e7f1d79.setIcon(beautify_icon_42e701866afa40deb42a98911e93e2d1);
        
    
            marker_34dbc5160eb8482888aefcbb6e7f1d79.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f3dbf21415ba46fc91a908314ddc788d = L.marker(
                [49.27408949187421, -123.22922903300501],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_e8f33cb1105c40e6aa666c91ee8098c8 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_f3dbf21415ba46fc91a908314ddc788d.setIcon(beautify_icon_e8f33cb1105c40e6aa666c91ee8098c8);
        
    
            marker_f3dbf21415ba46fc91a908314ddc788d.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4ee92701b657497280baca1ed92685e7 = L.marker(
                [49.275247967589465, -123.23016049789722],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_89fc32acb4ce4a2999a5869a76c92b37 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_4ee92701b657497280baca1ed92685e7.setIcon(beautify_icon_89fc32acb4ce4a2999a5869a76c92b37);
        
    
            marker_4ee92701b657497280baca1ed92685e7.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e76b36e964a242fc8bd7c24372c43d19 = L.marker(
                [49.27582754500957, -123.22985422935977],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_c512bf4a642945f48140d670b81070b6 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e76b36e964a242fc8bd7c24372c43d19.setIcon(beautify_icon_c512bf4a642945f48140d670b81070b6);
        
    
            marker_e76b36e964a242fc8bd7c24372c43d19.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_fcb14193b9b44510a7ce4c59a2da1390 = L.marker(
                [49.276249624615865, -123.2267218480022],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_da6eaaf58fa942f09ff2a32db3c77a99 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_fcb14193b9b44510a7ce4c59a2da1390.setIcon(beautify_icon_da6eaaf58fa942f09ff2a32db3c77a99);
        
    
            marker_fcb14193b9b44510a7ce4c59a2da1390.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_b1e2beed22e54c67898fabe97b607c8d = L.marker(
                [49.27625067457073, -123.22851208642129],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_c116c968a4f343c4a61ca23ad088a359 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_b1e2beed22e54c67898fabe97b607c8d.setIcon(beautify_icon_c116c968a4f343c4a61ca23ad088a359);
        
    
            marker_b1e2beed22e54c67898fabe97b607c8d.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_817baac22a3e4655a5c5be9e7cc63806 = L.marker(
                [49.276809416700544, -123.22603622821373],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_3c9dbd0cfbf645e5865c0bf399bf9730 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_817baac22a3e4655a5c5be9e7cc63806.setIcon(beautify_icon_3c9dbd0cfbf645e5865c0bf399bf9730);
        
    
            marker_817baac22a3e4655a5c5be9e7cc63806.bindTooltip(
                `<div>
                     Pioneer
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_06eed834102c4ecb8627aa0ac7aa86f3 = L.marker(
                [49.25831261739348, -123.22858243066761],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_41f431e8fdd746aa9e1b849fd096c2e0 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_06eed834102c4ecb8627aa0ac7aa86f3.setIcon(beautify_icon_41f431e8fdd746aa9e1b849fd096c2e0);
        
    
            marker_06eed834102c4ecb8627aa0ac7aa86f3.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a6633c470a7148bb94b21435a9e71b0e = L.marker(
                [49.25868583182979, -123.22907799758634],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_e2a4d1f0363a4819841f5f2d44138841 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_a6633c470a7148bb94b21435a9e71b0e.setIcon(beautify_icon_e2a4d1f0363a4819841f5f2d44138841);
        
    
            marker_a6633c470a7148bb94b21435a9e71b0e.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_0299bc0bca8b46f596a4a1d4f0872177 = L.marker(
                [49.25978935367037, -123.229477642343],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_8e3bfe139d9a480ca639dfda0df85d05 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_0299bc0bca8b46f596a4a1d4f0872177.setIcon(beautify_icon_8e3bfe139d9a480ca639dfda0df85d05);
        
    
            marker_0299bc0bca8b46f596a4a1d4f0872177.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c03a154173964d93ae2eb53aec25fd73 = L.marker(
                [49.260932060876236, -123.2293391480532],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_597e2e8fb5074145bb606b01ffcfa2ac = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_c03a154173964d93ae2eb53aec25fd73.setIcon(beautify_icon_597e2e8fb5074145bb606b01ffcfa2ac);
        
    
            marker_c03a154173964d93ae2eb53aec25fd73.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4582047b726c4fd2b4435fb75acf1630 = L.marker(
                [49.26253544725521, -123.22915786891156],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_d024879bc7bd4380808d593d5361e25e = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_4582047b726c4fd2b4435fb75acf1630.setIcon(beautify_icon_d024879bc7bd4380808d593d5361e25e);
        
    
            marker_4582047b726c4fd2b4435fb75acf1630.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c12312912b674819ba065c1daa04edc2 = L.marker(
                [49.265369603240536, -123.23298825563292],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_5a64537bbcf4451780de2fb9bd33d800 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_c12312912b674819ba065c1daa04edc2.setIcon(beautify_icon_5a64537bbcf4451780de2fb9bd33d800);
        
    
            marker_c12312912b674819ba065c1daa04edc2.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a6943822dc8a44e69c6ce72d4f27e841 = L.marker(
                [49.26730608898525, -123.23539445795662],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_982b6179504b4bc4870ea36683cbbd0c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_a6943822dc8a44e69c6ce72d4f27e841.setIcon(beautify_icon_982b6179504b4bc4870ea36683cbbd0c);
        
    
            marker_a6943822dc8a44e69c6ce72d4f27e841.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_eb77a202f93f4cc48f21d7a667cec4cc = L.marker(
                [49.26916969288675, -123.23711985141821],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_1f98c820af784ab9a25521a537dbe969 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_eb77a202f93f4cc48f21d7a667cec4cc.setIcon(beautify_icon_1f98c820af784ab9a25521a537dbe969);
        
    
            marker_eb77a202f93f4cc48f21d7a667cec4cc.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_bb11272cd04a4c7d993c6ee33acbe906 = L.marker(
                [49.271010824913, -123.23824740495861],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_9296bf0c7cd64929a84c7c493e62b4cf = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_bb11272cd04a4c7d993c6ee33acbe906.setIcon(beautify_icon_9296bf0c7cd64929a84c7c493e62b4cf);
        
    
            marker_bb11272cd04a4c7d993c6ee33acbe906.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_04ec4d01e92647898c645d7f16927f80 = L.marker(
                [49.27269788556626, -123.23863230593781],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_b698ccd21b144485b2895e155a7e343c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_04ec4d01e92647898c645d7f16927f80.setIcon(beautify_icon_b698ccd21b144485b2895e155a7e343c);
        
    
            marker_04ec4d01e92647898c645d7f16927f80.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7c2bb0ff04c246bc9ea046f3a9bdbc9e = L.marker(
                [49.275888442768924, -123.24069904963605],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_196f789cc16b4322b5273f063237ca88 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7c2bb0ff04c246bc9ea046f3a9bdbc9e.setIcon(beautify_icon_196f789cc16b4322b5273f063237ca88);
        
    
            marker_7c2bb0ff04c246bc9ea046f3a9bdbc9e.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6a478b2d4acb4588aed4fe0a1582a39b = L.marker(
                [49.279092091660544, -123.24361397558427],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_b49f302529d94931966bec00e1119d9f = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6a478b2d4acb4588aed4fe0a1582a39b.setIcon(beautify_icon_b49f302529d94931966bec00e1119d9f);
        
    
            marker_6a478b2d4acb4588aed4fe0a1582a39b.bindTooltip(
                `<div>
                     Salish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d0d2236ffbaf41d3b704d010bc71b216 = L.marker(
                [49.24934972153255, -123.20598115270622],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_fc3fbf7101e244bea89dd2b20f7dbdb7 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_d0d2236ffbaf41d3b704d010bc71b216.setIcon(beautify_icon_fc3fbf7101e244bea89dd2b20f7dbdb7);
        
    
            marker_d0d2236ffbaf41d3b704d010bc71b216.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e3476cd0be6d40c9b94f1d3ec0916682 = L.marker(
                [49.252454950959084, -123.20919683676077],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_b182fb3058224e649206ce1497120ac8 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e3476cd0be6d40c9b94f1d3ec0916682.setIcon(beautify_icon_b182fb3058224e649206ce1497120ac8);
        
    
            marker_e3476cd0be6d40c9b94f1d3ec0916682.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_b216e69f56094bc3b9148767ff69c249 = L.marker(
                [49.255899609410235, -123.21139981294691],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_9c1e265be3da4d2e922180c2adf19d58 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_b216e69f56094bc3b9148767ff69c249.setIcon(beautify_icon_9c1e265be3da4d2e922180c2adf19d58);
        
    
            marker_b216e69f56094bc3b9148767ff69c249.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_3c6f5789ceaf4ca799693a509816df78 = L.marker(
                [49.25798001283702, -123.20948481905664],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_13f1697a486a471981cf73eb0f3ebac6 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_3c6f5789ceaf4ca799693a509816df78.setIcon(beautify_icon_13f1697a486a471981cf73eb0f3ebac6);
        
    
            marker_3c6f5789ceaf4ca799693a509816df78.bindTooltip(
                `<div>
                     Sasamat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_30b42a98454c46d4aa48159280138181 = L.marker(
                [49.258187278912885, -123.21084067596733],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_32d16aef4d7041fc990d1175c3b89db5 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_30b42a98454c46d4aa48159280138181.setIcon(beautify_icon_32d16aef4d7041fc990d1175c3b89db5);
        
    
            marker_30b42a98454c46d4aa48159280138181.bindTooltip(
                `<div>
                     SherrySakamoto
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e2e42e78f0994e4ea21e2701d73c4a18 = L.marker(
                [49.25822228985484, -123.21319408337084],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_9ae60c25ff1f47468f81311b4d528719 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e2e42e78f0994e4ea21e2701d73c4a18.setIcon(beautify_icon_9ae60c25ff1f47468f81311b4d528719);
        
    
            marker_e2e42e78f0994e4ea21e2701d73c4a18.bindTooltip(
                `<div>
                     SherrySakamoto
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f25f7a72283b424b86b9adc21a72b134 = L.marker(
                [49.258239445079134, -123.21475192791627],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_acf7f61c90064a0886bf29c19e1faa58 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_f25f7a72283b424b86b9adc21a72b134.setIcon(beautify_icon_acf7f61c90064a0886bf29c19e1faa58);
        
    
            marker_f25f7a72283b424b86b9adc21a72b134.bindTooltip(
                `<div>
                     SherrySakamoto
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_80d507c5b0c649baa7b0363b0ecf1638 = L.marker(
                [49.267807351138906, -123.22588786772252],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_1e854f6d69024840adfaa8eaddfcdae3 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_80d507c5b0c649baa7b0363b0ecf1638.setIcon(beautify_icon_1e854f6d69024840adfaa8eaddfcdae3);
        
    
            marker_80d507c5b0c649baa7b0363b0ecf1638.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_9ce4d5b669954d378d8706a11585190b = L.marker(
                [49.26836671373096, -123.23667965143653],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_5fdab215b239491d9785f5e97d1857b6 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_9ce4d5b669954d378d8706a11585190b.setIcon(beautify_icon_5fdab215b239491d9785f5e97d1857b6);
        
    
            marker_9ce4d5b669954d378d8706a11585190b.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_035de88bf435409ea0a14543f2f845ee = L.marker(
                [49.26861243941978, -123.23609851940927],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_ccf39666b5c941f99f33e7fd97be3c6c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_035de88bf435409ea0a14543f2f845ee.setIcon(beautify_icon_ccf39666b5c941f99f33e7fd97be3c6c);
        
    
            marker_035de88bf435409ea0a14543f2f845ee.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_3873c5f4b7a74ed687ec222c3dfe25a1 = L.marker(
                [49.26914134034848, -123.23218396320507],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_383f640ba5084648bcb4d8d9664f4c6e = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_3873c5f4b7a74ed687ec222c3dfe25a1.setIcon(beautify_icon_383f640ba5084648bcb4d8d9664f4c6e);
        
    
            marker_3873c5f4b7a74ed687ec222c3dfe25a1.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f3d8019dd6d44c6bb91f39588312e126 = L.marker(
                [49.26925300030199, -123.22508963029917],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_0ce4ea604f334df88096799a64773287 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_f3d8019dd6d44c6bb91f39588312e126.setIcon(beautify_icon_0ce4ea604f334df88096799a64773287);
        
    
            marker_f3d8019dd6d44c6bb91f39588312e126.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_65ff4a2ddd154ca2bcbeb86b7052e942 = L.marker(
                [49.269410514232334, -123.236824664439],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_06e9ff7a9e3c4e3f94688b51352a8edb = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_65ff4a2ddd154ca2bcbeb86b7052e942.setIcon(beautify_icon_06e9ff7a9e3c4e3f94688b51352a8edb);
        
    
            marker_65ff4a2ddd154ca2bcbeb86b7052e942.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6b5565faf8b4419e987f1a8f6aacb043 = L.marker(
                [49.269935555468216, -123.22464750117899],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_35c94b3902274e58a56ae4c7de27f40f = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_6b5565faf8b4419e987f1a8f6aacb043.setIcon(beautify_icon_35c94b3902274e58a56ae4c7de27f40f);
        
    
            marker_6b5565faf8b4419e987f1a8f6aacb043.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_389a9c176a4545d5881995b6625af5f5 = L.marker(
                [49.273416093707475, -123.22652292641796],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_8920a8a3184a4eda9b597131db26e0fe = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_389a9c176a4545d5881995b6625af5f5.setIcon(beautify_icon_8920a8a3184a4eda9b597131db26e0fe);
        
    
            marker_389a9c176a4545d5881995b6625af5f5.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_37890ce134b74d519ae35012bea48355 = L.marker(
                [49.276369318151325, -123.22566353169596],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_c868a3c1b41f494c8dd5964b086d3b6c = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_37890ce134b74d519ae35012bea48355.setIcon(beautify_icon_c868a3c1b41f494c8dd5964b086d3b6c);
        
    
            marker_37890ce134b74d519ae35012bea48355.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_fddebf29ad504a3bae7f4c68c38a6be6 = L.marker(
                [49.277224663173136, -123.22475370104767],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_b4f71e341033483ea9e70ecefb06c28e = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_fddebf29ad504a3bae7f4c68c38a6be6.setIcon(beautify_icon_b4f71e341033483ea9e70ecefb06c28e);
        
    
            marker_fddebf29ad504a3bae7f4c68c38a6be6.bindTooltip(
                `<div>
                     Spanish
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7e9d754a384c4bbe9c9d46443e1e9522 = L.marker(
                [49.235261334425765, -123.19719307452199],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_7dadcb5b960c469294897bbdbd0c11fe = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_7e9d754a384c4bbe9c9d46443e1e9522.setIcon(beautify_icon_7dadcb5b960c469294897bbdbd0c11fe);
        
    
            marker_7e9d754a384c4bbe9c9d46443e1e9522.bindTooltip(
                `<div>
                     SWMarine
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_92843ccdd9e74d5d892b84a441d55e92 = L.marker(
                [49.235976935113186, -123.19963935867693],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_8efe369d41b04288935f44d77d8f35bb = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_92843ccdd9e74d5d892b84a441d55e92.setIcon(beautify_icon_8efe369d41b04288935f44d77d8f35bb);
        
    
            marker_92843ccdd9e74d5d892b84a441d55e92.bindTooltip(
                `<div>
                     SWMarine
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4fa9aa590160452ab042cb6c96726918 = L.marker(
                [49.236817568930825, -123.20255493499178],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_28c06b6c7a94416a8fc9caef8465d22f = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_4fa9aa590160452ab042cb6c96726918.setIcon(beautify_icon_28c06b6c7a94416a8fc9caef8465d22f);
        
    
            marker_4fa9aa590160452ab042cb6c96726918.bindTooltip(
                `<div>
                     SWMarine
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_2ae9eca9bfa343df92aa7a8c0f462df9 = L.marker(
                [49.260384866994656, -123.23315819132735],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_6a215d28d2184c228c270fb1f888fee7 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_2ae9eca9bfa343df92aa7a8c0f462df9.setIcon(beautify_icon_6a215d28d2184c228c270fb1f888fee7);
        
    
            marker_2ae9eca9bfa343df92aa7a8c0f462df9.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_cd43081a19b74b038297d684e8ce1676 = L.marker(
                [49.26895967378132, -123.23792415270513],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_b54626ba26e04bef95622fc4ad3b875f = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_cd43081a19b74b038297d684e8ce1676.setIcon(beautify_icon_b54626ba26e04bef95622fc4ad3b875f);
        
    
            marker_cd43081a19b74b038297d684e8ce1676.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_5befec0f2f694a4fab91cb1fdd3c4674 = L.marker(
                [49.271038826924624, -123.23952455572746],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_fd91bc2f8c2c4bccbf5e17b2de248079 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_5befec0f2f694a4fab91cb1fdd3c4674.setIcon(beautify_icon_fd91bc2f8c2c4bccbf5e17b2de248079);
        
    
            marker_5befec0f2f694a4fab91cb1fdd3c4674.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e8776165327047b596e96202e0db3ec5 = L.marker(
                [49.27226457601742, -123.23931623186071],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_9cc54177aa0e4643b8dac62683e33dc1 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e8776165327047b596e96202e0db3ec5.setIcon(beautify_icon_9cc54177aa0e4643b8dac62683e33dc1);
        
    
            marker_e8776165327047b596e96202e0db3ec5.bindTooltip(
                `<div>
                     SwordFern
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_0c4cf189b02b44b9b6f0746c466494d0 = L.marker(
                [49.24969149001777, -123.20346136911543],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_2be3597a867643648bdba7229500d04b = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_0c4cf189b02b44b9b6f0746c466494d0.setIcon(beautify_icon_2be3597a867643648bdba7229500d04b);
        
    
            marker_0c4cf189b02b44b9b6f0746c466494d0.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e8e05ee4ac5f4583b4255541281d5707 = L.marker(
                [49.250014695194515, -123.2013588349101],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_c551af322c114d85b49e700db8b71dc7 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_e8e05ee4ac5f4583b4255541281d5707.setIcon(beautify_icon_c551af322c114d85b49e700db8b71dc7);
        
    
            marker_e8e05ee4ac5f4583b4255541281d5707.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_0021a6cbe9604015b989d3467a8835f6 = L.marker(
                [49.250025900596434, -123.2017251470642],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_0f65357bc62e4b5ea73425976c976e96 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_0021a6cbe9604015b989d3467a8835f6.setIcon(beautify_icon_0f65357bc62e4b5ea73425976c976e96);
        
    
            marker_0021a6cbe9604015b989d3467a8835f6.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_cfe5f97c986b4833ac85a4460e20ded5 = L.marker(
                [49.25017752316746, -123.20017965282354],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_40eadb060ff14d7e9f01ca14b2bc1282 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_cfe5f97c986b4833ac85a4460e20ded5.setIcon(beautify_icon_40eadb060ff14d7e9f01ca14b2bc1282);
        
    
            marker_cfe5f97c986b4833ac85a4460e20ded5.bindTooltip(
                `<div>
                     Top
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_36f5d3f9797849acaed8a758d5fbc26b = L.marker(
                [49.274789480143426, -123.23226658719038],
                {"riseOnHover": true}
            ).addTo(feature_group_84e81030d853452fb395d2aa9dc3ec58);
        
    
            var beautify_icon_17aafdcae1744285a77624a5813fe2b8 = new L.BeautifyIcon.icon(
                {"backgroundColor": "transparent", "borderColor": "transparent", "borderWidth": 3, "icon": "star", "innerIconStyle": "color:#dfb10d;font-size:15px;", "isAlphaNumericIcon": false, "spin": false, "textColor": "#000"}
            )
            marker_36f5d3f9797849acaed8a758d5fbc26b.setIcon(beautify_icon_17aafdcae1744285a77624a5813fe2b8);
        
    
            marker_36f5d3f9797849acaed8a758d5fbc26b.bindTooltip(
                `<div>
                     WestCanyon
                 </div>`,
                {"sticky": true}
            );
        
    
                var lat_lng_popup_4bfa6bcf173f49f5a907066b15b0d1f3 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_4bfa6bcf173f49f5a907066b15b0d1f3
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_e64e998cab65479198b8e3b622d8e051 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_e64e998cab65479198b8e3b622d8e051
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_8a83119833544faa898271450293c27e = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_8a83119833544faa898271450293c27e
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_7cdda0da2feb4a23ae3b5c1f418bce4c = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_7cdda0da2feb4a23ae3b5c1f418bce4c
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_e601dadb0294409aa0f08d43564842ec = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_e601dadb0294409aa0f08d43564842ec
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_d58c0aa5766d4d9cb49ead059d69d6c4 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_d58c0aa5766d4d9cb49ead059d69d6c4
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_c2019e63de80403690f83d944103b22e = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_c2019e63de80403690f83d944103b22e
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_2b979177b6c44896b1d1045c1475b26b = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_2b979177b6c44896b1d1045c1475b26b
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_db79e8b23ac143feb37dc0bdd4307d49 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_db79e8b23ac143feb37dc0bdd4307d49
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_31caedf59f834d168b26b3ae61c72e62 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_31caedf59f834d168b26b3ae61c72e62
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_1505840886d5488a93aa216b4b6b4dda = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_1505840886d5488a93aa216b4b6b4dda
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_5da9e4ebd0fb4896bda493f1a65c8592 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_5da9e4ebd0fb4896bda493f1a65c8592
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_94f70e4f3e6448df9623534877c261f0 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_94f70e4f3e6448df9623534877c261f0
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_f39fede87d5a4d9fb24497b3ed36397d = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_f39fede87d5a4d9fb24497b3ed36397d
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_39aba0b5563f400383cfe5cf0f8e8cff = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_39aba0b5563f400383cfe5cf0f8e8cff
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_5914cb64dae141bf8b394a13d5d5eb58 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_5914cb64dae141bf8b394a13d5d5eb58
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_3b94c1c5a0cc4fc9bcced3bd09a09a63 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_3b94c1c5a0cc4fc9bcced3bd09a09a63
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_c1f79acfbecd4b948d0aa05687ec569e = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_c1f79acfbecd4b948d0aa05687ec569e
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_32abbb10f17b4fb0bee635b8b9790438 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_32abbb10f17b4fb0bee635b8b9790438
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_9ddbd4cd97ed4e52b16de16e114a1cec = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_9ddbd4cd97ed4e52b16de16e114a1cec
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_2c6d6de861404286967b5e94c2beed66 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_2c6d6de861404286967b5e94c2beed66
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_cc67e247ef3949adade3027f77d09128 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_cc67e247ef3949adade3027f77d09128
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_fc9e48d458c04a14bf8cd04c28fab3a4 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_fc9e48d458c04a14bf8cd04c28fab3a4
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_b49e86e2e526480185621d407d7a9191 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_b49e86e2e526480185621d407d7a9191
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_55f14a51cd534a47abf9da920c0e13fb = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_55f14a51cd534a47abf9da920c0e13fb
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_af6e961bee4948d4894c0a740f805eea = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_af6e961bee4948d4894c0a740f805eea
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_135ec668c024430fa5b91836704fe8a6 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_135ec668c024430fa5b91836704fe8a6
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_b891c0be8e3149e6800e5dc5d6099552 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_b891c0be8e3149e6800e5dc5d6099552
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_15d13451f6e14b9a90e8b057d7fdb8be = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_15d13451f6e14b9a90e8b057d7fdb8be
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_53e22039b63f4a2d8e3ca74015f3c8e6 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_53e22039b63f4a2d8e3ca74015f3c8e6
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_a00eb9b094f74ec69cdb93d4c62d5530 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_a00eb9b094f74ec69cdb93d4c62d5530
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_7a5bc4e05841430eb6b85c48fcfd9e2a = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_7a5bc4e05841430eb6b85c48fcfd9e2a
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_1c1a711f7d6d49ffb0ed1aeb94de8519 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_1c1a711f7d6d49ffb0ed1aeb94de8519
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_1e1905b220504171a8d67447e3ed51b3 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_1e1905b220504171a8d67447e3ed51b3
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_e856f90b38234b14898943ea91bcbb4c = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_e856f90b38234b14898943ea91bcbb4c
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_6e75beb126d545508c5fe95359b41b01 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_6e75beb126d545508c5fe95359b41b01
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_cabab45bf9e345b8b9bd3f2a3694cfae = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_cabab45bf9e345b8b9bd3f2a3694cfae
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
                var lat_lng_popup_ff26e6ee4bb145919f5aa15d529921c7 = L.popup();
                function latLngPop(e) {
                    lat_lng_popup_ff26e6ee4bb145919f5aa15d529921c7
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(4))
                        .openOn(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
                    }
                map_f81be1f6d3f64b86a2af11ace2b1d3e2.on('click', latLngPop);
            
    
            var tile_layer_03c88847f34c4b5a86ce10bc3e6fb19f = L.tileLayer(
                "https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg",
                {"attribution": "Map tiles by \u003ca href=\"http://stamen.com\"\u003eStamen Design\u003c/a\u003e, under \u003ca href=\"http://creativecommons.org/licenses/by/3.0\"\u003eCC BY 3.0\u003c/a\u003e. Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://creativecommons.org/licenses/by-sa/3.0\"\u003eCC BY SA\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
        
    
            var tile_layer_03db8ac218654c0686da1cd91f96e516 = L.tileLayer(
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
        
    
            var layer_control_c7539ceb0bd649b5bd490f9564199da2 = {
                base_layers : {
                    "cartodbpositron" : tile_layer_fdf3082667d94b84b06747306a880108,
                    "stamenterrain" : tile_layer_03c88847f34c4b5a86ce10bc3e6fb19f,
                    "openstreetmap" : tile_layer_03db8ac218654c0686da1cd91f96e516,
                },
                overlays :  {
                    "All Stars" : feature_group_20508be17e294f409fe58ef01f7f2234,
                    "Progress" : feature_group_84e81030d853452fb395d2aa9dc3ec58,
                },
            };
            L.control.layers(
                layer_control_c7539ceb0bd649b5bd490f9564199da2.base_layers,
                layer_control_c7539ceb0bd649b5bd490f9564199da2.overlays,
                {"autoZIndex": true, "collapsed": true, "position": "topright"}
            ).addTo(map_f81be1f6d3f64b86a2af11ace2b1d3e2);
            tile_layer_03c88847f34c4b5a86ce10bc3e6fb19f.remove();
            tile_layer_03db8ac218654c0686da1cd91f96e516.remove();
        
    
            map_f81be1f6d3f64b86a2af11ace2b1d3e2.fitBounds(
                [[49.225, -123.275], [49.285, -123.19]],
                {}
            );
        
</script>
</div>
<p id="demo"></p>

</body>
</html> 
