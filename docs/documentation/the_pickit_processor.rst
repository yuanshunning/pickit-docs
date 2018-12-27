The Pick-it processor
=====================

The Pick-it processor is a rack mount computer on which the Pick-it
software is installed. It is responsible for doing all calculations to
detect your objects in a 3D point cloud and send the coordinates to the
robot for picking.

Read \ `this
article <https://support.pickit3d.com/article/74-setting-up-your-pick-it-system>`__
to learn how to set up the processor in your picking application.

Processor version
-----------------

There are currently two hardware versions of the Pick-it processor: 1.0
and 2.0. Both versions look very similar from the outside, but when
taking a closer look, you'll notice that they are equipped with
different hardware components on the inside.

Since many technical specifications stay the same between processor
versions 1.0 and 2.0, the section below only differentiates between the
two processor versions if there is a difference.

What is the version of my Pick-it processor?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways to look up the version of your Pick-it processor:

#. By looking at the back of the processor, you can see if a GTX
   graphics card is installed. If this is the case, the Pick-it
   processor version is 2.0, otherwise, it's 1.0.
#. By looking at the Pick-it software version at the top left of the
   Pick-it interface in your browser. If the software version specifies
   1.x, then your processor version is 1.0, otherwise, it's 2.0.

What is the difference between Pick-it version 1.0 and 2.0?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are the most important differences between Pick-it versions 1.0
and 2.0:

-  From a **hardware** perspective, Pick-it processor 2.0 has a GTX
   graphics card, more powerful CPU and power supply to work with
   the \ `Pick-it M-HD
   camera <https://support.pickit3d.com/article/201-pick-it-m-hd>`__.
   The Pick-it processor 1.0 has no graphics card.
-  From a **software** perspective, Pick-it processor 1.0 runs Pick-it
   software versions 1.x. Pick-it processor 2.0 runs Pick-it software
   versions 2.x. Software version 2.x is the platform that will receive
   the new product updates, while software version 1.x will only receive
   bug fixes and security updates.

Technical specifications
------------------------

The technical specifications in this section apply to both processor
versions 1.0 and 2.0 unless mentioned otherwise.

.. raw:: html

   <div>

.. raw:: html

   <div>

.. raw:: html

   <div>

-  Processor: 6 cores (12 threads) at 3.7 Ghz
-  19-inch server: rack compatible (2U)
-  Temperature: -20°C to 70°C
-  Vibrations: Operating, 5 Grms, 5-500 Hz, 3 axes
-  IP rating: IP54
-  Power supply: 9-32V DC 160W
-  Humidity: ̃95% @ 40°C (non-condensing)

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Processor ports and power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image0|

The front side of the Pick-it processor contains a lid, which can be
opened by rotating the lock handle clockwise. A few ports (which are not
used by Pick-it) and some buttons are located under the lid. In case of
a power failure, while the computer is on, it will restart automatically
when power is restored.

|image1|

All labeled I/O ports and the power connector are placed on the back
side of the processor as shown above. In order to connect the Pick-it
processor to a power supply, use the provided IEC cable (C13).

.. raw:: html

   <div class="callout-red">

**Warning** In case the Pick-it processor is positioned vertically and
sideways, the air inlet shall not stay at the top. This may affect the
ventilation process.

.. raw:: html

   </div>

Power consumption specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pick-it processor 1.0:

-  While turned off: 25 W
-  Booting: 100 W
-  Idle: 60 W
-  Heavy processing: 130 W

Pick-it processor 2.0:

-  While turned off: 25 W
-  Booting: 115 W
-  Idle: 70 W
-  Heavy processing: 160 W

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5aa64e762c7d3a7549518cff/file-8TUd7YX6dk.jpg
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5aa64e6504286374f708ca46/file-UCG7Moyt1M.jpg

