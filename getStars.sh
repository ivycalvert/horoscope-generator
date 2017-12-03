#!/bin/bash

# show commands and stop if there is an error
set -ex

mkdir -p stars

SEARCH_STRING="galaxy"

PAGE="1"


    # build the url
    URL='https://www.flickr.com/photos/tags/'$SEARCH_STRING'/page'$PAGE''
    
    # fetch the images
    wget \
      --adjust-extension \
      --no-directories \
      --convert-links \
      --backup-converted \
      --random-wait \
      --limit-rate=100k \
      --span-hosts \
      --directory-prefix=stars \
      --page-requisites \
      --timestamping \
      --execute robots=off \
      --accept=*.jpg \
      $URL

