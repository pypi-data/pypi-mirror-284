# Leaflet JS Repackaged for Django

[Leaflet JS](https://leafletjs.com/) packaged in a Django reusable app.


## Installation

    pip install django-js-lib-leaflet

## Usage

1. Add `"js_lib_leaflet"` to your `INSTALLED_APPS` setting like this::

       INSTALLED_APPS = [
           ...
           "js_lib_leaflet",
           ...
       ]

2. In your template use:
   
       {% load static %}
   
   ...
   
       <link rel="stylesheet" href="{%static "js_lib_leaflet/leaflet.css" %}">

   ...
   
       <script src="{%static "js_lib_leaflet/leaflet.js" %}"></script>
