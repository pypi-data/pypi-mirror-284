#!/bin/bash
set +ex

VERSION="1.9.4"
URL="https://leafletjs-cdn.s3.amazonaws.com/content/leaflet/v$VERSION/leaflet.zip"
OUTPUT_ZIP="dist.zip"
curl -L -o $OUTPUT_ZIP $URL
rm -drv js_lib_leaflet/static/js_lib_leaflet/*
unzip $OUTPUT_ZIP -d js_lib_leaflet/static/js_lib_leaflet/
rm $OUTPUT_ZIP

