.. _connecting-the-cables:

Connecting the cables
=====================

.. contents::     
    :backlinks: top
    :local:
    :depth: 1

Connect the power cable
~~~~~~~~~~~~~~~~~~~~~~~

The **Pickit processor** has a built-in power supply and needs to be
connected to the power outlet with the provided cable. The Pickit
processor will automatically boot once it's powered.

The Pickit processor can be shut down by pressing the power button
once. The power button is positioned behind the front lid. Powering it
again can be done by pressing the same power button once.

.. note::
  In case the Pickit processor is on and there is a power failure, it
  will restart automatically when power is restored. Pickit will start
  with robot mode enabled.

Connect the camera
~~~~~~~~~~~~~~~~~~

Connect the Pickit camera with the 10m USB cable (CBL-USB-CAM-10) that
is provided with Pickit and plug it into the **CAMERA** labeled USB
port at the back side of the Pickit processor.

When the Pickit camera is connected correctly, there will be a
continuous green light on the front of the Pickit camera. This
indicates that the Pickit camera is operational.


.. note::
  **Important**

  -  A separate power supply for the Pickit camera is not required
  -  A USB hub is not allowed between the Pickit processor and Pickit camera.

Connect the robot or machine controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the provided green 5m UTP network cable (CBL-CAT6-GREEN-5) connect
your robot or machine controller with the **ROBOT** labeled RJ45 port at
the back side of the Pickit processor.

Instructions on the network configuration can be found on the robot
brand specific instruction pages:

-  :ref:`abb`
-  :ref:`fanuc`
-  :ref:`kuka`
-  :ref:`staubli`
-  :ref:`universal-robots`
-  :ref:`yaskawa`

Connect a computer
~~~~~~~~~~~~~~~~~~

There are 2 ways to connect your Pickit processor to a computer. You
can connect it directly with an ethernet cable or connect it to your
network. You can use the provided gray/black 5m UTP network cable
(CBL-CAT6-GRAY-5 / CBL-CAT6-BLACK-5).

A connection with a computer is only required during setup and
configuration. When Pickit is in robot mode a connection with a
computer is not required.

Both connections can be active at the same time and work independently
from each other. It's very common to have Pickit set up this way.

Connecting a computer directly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect a computer to the **YOUR PC** labeled RJ45 port on the Pickit
processor. Your computer will be assigned an IP address by the Pickit
processor. Once connected you can access the Pickit web interface by
browsing to http://192.168.66.1.

Connecting a computer using a network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect the Pickit processor to a network with the **LAN** labeled RJ45
port and connect it to your router or switch. An IP address will be
assigned using the DHCP server of your network. You can now connect to
the Pickit web interface by surfing to the IP address that was assigned
by the DHCP server of your network.

If you want to assign a fixed IP to the Pickit processor you first need
to connect a computer directly to configure a fixed IP.