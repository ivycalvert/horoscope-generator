#!/bin/bash

# show commands and stop if there is an error
set -ex

bash download.sh
python genAnim.py
bash editImage.sh
bash getStars.sh
python genText.py
