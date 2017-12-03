GENERATE HOROSCOPES:

EITHER RUN THE MASTER SCRIPT run_all.sh:

  $ bash run_all.sh

OR ALTERNATIVELY RUN THE SCRIPTS INDIVIDUALLY IN THE FOLLOWING ORDER:

first run download.sh this will collect all external data sets we need:

  $ bash download.sh

then run genAnim.py:

  $ python genAnim.py

This will:

 * select an animal
 * download images of that animal from flickr (downloads folder)

then run editImage.sh:

  $ bash editImage.sh

This will:

 * generate an image outline based on a random image downloaded from flickr

then run getStars.sh:

  $ bash getStars.sh

This will:

 * download images tagged with 'galaxy' from flickr

then run genText.py: 
NOTE: DO THIS STEP LAST AS IT PRINTS TO TERMINAL
	
  $ python genText.py

This will:
 
 * generate details about a fictional horoscope
 * generate 12 monthly horoscope passages based on this new horoscope