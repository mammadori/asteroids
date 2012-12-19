===================
RiceRocks Asteroids
===================

This game is the python3.3 + pyglet version of the final miniproject of the 
coursera's "An Introduction to Interactive Programming in Python" [0] RiceRocks.

Install
=======

It requires pyglet 1.2beta, available at the moment only from the pyglet repository

It should be easy to port to python 2.7 and pyglet 1.1.4 paying attention to
'super()' class methods invocation and integer/float divisions.

If you have troubles installing python3 + pyglet have a look at my blog post [1]
about some issues you could find in doing it.

The Code
========

If you have troubles understanding the code I strongly suggest to have a look 
at the gorgeous asteroid pyglet tutorial from Steve Johnson [2], it provides 
a walkthrough in approaching pyglet and the asteroid game. When you finish his
tutorial you can come back and have another look at this version which is more
advanced since it uses the Object Oriented paradigm a bit more.


The gameplay is exactly the same as described in coursera miniproject assignement
but shares virtually no verbatim code with the version I made from the course
(it is a rewrite from scratch), so it should not help you a lot in future runs of
the same course.


This code is meant as a demo of various concepts you can find in a game and is
meant to help people from the course go on in writing python games out of Codeskulptor[3]
in-browser python interpreter towards real python.


Feel free to fork and improve the code, if you manage do play with it, be sure
to tell me about your version, I'm interestend in suggestions/improvements.


The license for my code is BSD, if you need another licensing, just ask, there
should be no problems.

Game art is created by Kim Lathrop, may be freely re-used in non-commercial
projects, please credit Kim. (Sort of CC-BY-NC IMHO, but IANAL!)

If you need an art repository you could look at Open Game Art project [4]

Future
======

I will probably fork this code and add interesting libraries for games like
pymunk and lepton in order to have a more complete introduction to python games
development.

Thanks.


Links
=====

* [0] https://class.coursera.org/interactivepython-2012-001
* [1] http://ipoveraviancarriers.blogspot.it/2012/11/python-33-and-pyvenv-hackish-solution.html
* [2] http://steveasleep.com/pyglettutorial.html
* [3] http://www.codeskulptor.org
* [4] http://opengameart.org/
