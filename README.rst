========
Hue Ctrl
========

HueCtrl is a program that creates ambient lighting using screen-capture monitoring. This is a refactoring of an old project I created in python 2.7.x. The main goals here are to increase screen capturing speed and create a more fluid up-to-date code that is easier to use.

.. code:: bash

	pipenv install
	pipenv run python src\main.py

Screen Grabbing
---------------

To grab the data from the screen we have a python file called screenGrab. What this does is pretty simple. We use mss and numpy to capture pixel data from the monitor and return it. Its just that simple. Using mss over say the Pillow library has two big advantages: 

	1) its way faster than PILs ImageGrab
	2) it can be used cross-platform, unlike PIL's ImageGrab

Originally I had debated on making this a c++ function as it can be done MUCH quicker (with mss we can get 20-30 fps, where as c++ can do 60+ easy) HOWEVER it actually doesn't matter how fast we screencapture over 10 fps because we are limited by how often we can update our bulb without bottlenecking the Phillips Bridge.

TODOS: I want to make this a threaded process that way it can be constantly getting new screen information while we are running our mainloop in our application. This way we can limit the frames without having to account for how long our screengrabs are taking. More on this later.

Phillips Bridge Connection
--------------------------

Originally when I wrote this program in python 2.7.x I used <https://pypi.python.org/pypi/pyhue/0.7.6> and although this library has been updated for python 3.x.x I had problems with it immediately (unexplained recursion errors) so I've rewritten pyhue for my own needs. I will be expanding on it as I need to but for now it is a bridge class which houses our connection along with some nice wrapper functions that make the API calls easier for me.
