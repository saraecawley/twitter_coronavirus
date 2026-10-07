#!/bin/sh

for file in /data/Twitter\ dataset/geoTwitter20-*; do
    nohup python3 map.py --input_path="$file" &
done
