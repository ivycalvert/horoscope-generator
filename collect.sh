#!/bin/bash

# show commands and stop if there is an error
set -ex

# make the directory if it is not there
mkdir -p downloads

# clean the directory if there are old results
rm -f downloads/*

URL=$1

echo "about to fetch URL: " $URL
sleep 1

# fetch the images
wget --adjust-extension \
     --random-wait \
     --limit-rate=100k \
     --span-hosts \
     --convert-links \
     --backup-converted \
     --no-directories \
     --timestamping \
     --page-requisites \
     --directory-prefix=downloads \
     --execute robots=off \
     --accept=.jpg \
     $URL
