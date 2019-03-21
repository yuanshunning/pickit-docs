Connecting the cables
---------------------

#. `Connect the power cable <#power-cable>`__
#. `Connect the camera <#camera>`__
#. `Connect the robot or machine controller <#robot>`__
#. `Connect a computer <#computer>`__

Connect the power cable
~~~~~~~~~~~~~~~~~~~~~~~

The **Pick-it processor** has a built-in power supply and needs to be
connected to the power outlet with the provided cable. The Pick-it
processor will automatically boot once it's powered.

The Pick-it processor can be shut down by pressing the power button
once. The power button is positioned behind the front lid. Powering it
again can be done by pressing the same power button once.

In case the Pick-it processor is on and there is a power failure, it
will restart automatically when power is restored. Pick-it will start
with robot mode enabled.

Connect the camera
~~~~~~~~~~~~~~~~~~

Connect the Pick-it camera with the 10m USB cable (CBL-USB-CAM-10) that
is provided with Pick-it and plug it into the **CAMERA** labeled USB
port at the back side of the Pick-it processor.

When the Pick-it camera is connected correctly, there will be a
continuous green light on the front of the Pick-it camera. This
indicates that the Pick-it camera is operational.

.. raw:: html

   <div class="callout-yellow">

**Important**

-  A separate power supply for the Pick-it camera is not required
-  A USB hub is not allowed between the Pick-it processor and Pick-it
   camera.

.. raw:: html

   </div>

Connect the robot or machine controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div>

Using the provided green 5m UTP network cable (CBL-CAT6-GREEN-5) connect
your robot or machine controller with the **ROBOT** labeled RJ45 port at
the back side of the Pick-it processor.

.. raw:: html

   </div>

Instructions on the network configuration can be found on the robot
brand specific instruction pages:

-  `Setup Pick-it with an ABB
   robot <http://support.pickit3d.com/article/55-setup-pick-it-with-an-abb-robot>`__
-  `Setup Pick-it with a Fanuc
   robot <http://support.pickit3d.com/article/6-setup-pick-it-with-a-fanuc-robot>`__
-  `Setup Pick-it with a Kuka
   robot <http://support.pickit3d.com/article/64-setting-up-pick-it-with-a-kuka-robot>`__
-  `Setup Pick-it with a Staubli
   robot <http://support.pickit3d.com/article/45-set-up-pick-it-with-a-staubli-robot>`__
-  `Setup Pick-it with a Universal Robots
   robot <http://support.pickit3d.com/article/13-set-up-pick-it-with-a-universal-robot>`__

Connect a computer
~~~~~~~~~~~~~~~~~~

There are 2 ways to connect your Pick-it processor to a computer. You
can connect it directly with an ethernet cable or connect it to your
network. You can use the provided gray/black 5m UTP network cable
(CBL-CAT6-GRAY-5 / CBL-CAT6-BLACK-5).

A connection with a computer is only required during setup and
configuration. When Pick-it is in running mode a connection with a
computer is not required.

Both connections can be active at the same time and work independently
from each other. It's very common to have Pick-it set up this way.

Connecting a computer directly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect a computer to the **YOUR PC** labeled RJ45 port on the Pick-it
processor. Your computer will be assigned an IP address by the Pick-it
processor. Once connected you can access the Pick-it web interface by
browsing to  http://192.168.66.1.

Connecting a computer using a network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect the Pick-it processor to a network with the **LAN** labeled RJ45
port and connect it to your router or switch. An IP address will be
assigned using the DHCP server of your network. You can now connect to
the Pick-it web interface by surfing to the IP address that was assigned
by the DHCP server of your network.

If you want to assign a fixed IP to the Pick-it processor you first need
to  `connect your computer directly <#connect-computer-directly>`__
to \ `configure a fixed IP <>`__.