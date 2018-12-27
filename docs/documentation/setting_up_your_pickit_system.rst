Setting up your Pick-it system
==============================

#. `Components <#components>`__
#. `Connecting the cables <#cables>`__
#. `Testing your setup <#test>`__

Components
----------

.. raw:: html

   <div>

An operation Pick-it system consists of 3 mandatory components:

.. raw:: html

   </div>

-  Pick-it processor
-  Pick-it camera
-  Your robot

|image0|\ During the setup, a computer is used to configure the Pick-it
system. After setup and configuration, the computer can be disconnected.

.. raw:: html

   <div>

There are two mandatory connections and two optional connections for the
Pick-it system:

.. raw:: html

   </div>

.. raw:: html

   <div>

-  **Top**\ : The Pick-it processor **can be connected** via a network
   cable to any PC for access to the Pick-it web interface via a Chrome.
-  **Bottom**: The Pick-it camera **must be connected** to the Pick-it
   processor using the provided USB camera cable.
-  **Right**: The Pick-it processor **must be connected** with a network
   cable to the robot or machine controller. This connection allows the
   robot and Pick-it to exchange commands, status information, object
   poses and the robot pose.
-  **Left**\ : The Pick-it processor **can be connected** via a network
   cable to the company network in order to receive remove service from
   a Pick-it engineer over the internet. Alternatively, it can be
   connected to the internet with the Pick-it 3G USB dongle.

.. raw:: html

   </div>

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

Testing your setup
------------------

Connecting to the Pick-it web interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div>

.. raw:: html

   <div>

If you connected your computer directly to the Pick-it processor you can
now connect to the Pick-it interface by surfing to  http://192.168.66.1
to configure your Pick-it setup.

.. raw:: html

   </div>

.. raw:: html

   <div>

If you connected the Pick-it processor to your network you can now
connect to the Pick-it interface by surfing to the IP address that was
assigned by the DHCP server of your network.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   <div>

If you still have questions regarding the connection to the Pick-it web
interface you can always contact 
`support@pickit3d.com <mailto:mailto:support@pickit3d.com>`__.

.. raw:: html

   </div>

.. raw:: html

   </div>

Testing the Robot to Pick-it connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instructions on testing the Robot to Pick-it connection can be found on
the specific instruction page:  `Test robot to Pick-it
connection <http://support.pickit3d.com/article/19-test-pick-it-robot-connection>`__

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/592549520428634b4a33659c/file-Kj7MxzMb03.png

