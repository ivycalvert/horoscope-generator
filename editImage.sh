#!/bin/bash

# show commands and stop if there is an error
set -ex

# this command converts the flickr scraped image
# and converts it in a black and white outlined image
# please note, due to the edge detection method used
# and the real photos srapced from flickr,
# the resulted image suffers in quality and there is 
# too much detail in real images for this method to 
# function properly
cd downloads
convert *.jpg \
  -colorspace Gray \
  -canny 0x1+22%+32% \
  -negate \
  editedAnim.jpg