.. _Settings:

Settings
========

.. contents::
    :backlinks: top
    :local:
    :depth: 1

User settings
-------------

Units
~~~~~

.. image:: /assets/images/Documentation/Settings-units.png

This setting allows you to select the length unit of choice
(meters, inches, ...) after which all length values in the interface
will be converted to the newly selected unit.

Automatic detection
~~~~~~~~~~~~~~~~~~~

Here you can choose to automatically trigger a new detection if a
parameter is changed.

Share usage statistics
~~~~~~~~~~~~~~~~~~~~~~

.. image:: /assets/images/Documentation/Settings-share-usage-statistics.png

This aggregated data can be used to help create features that
can give you a better understanding of what’s happening across your
entire application.

You benefit when this setting is ON because this data could be used to
help build better tools and provide guidance that can help you analyze
your application. Application data lets you know where you stand in your
application and it’s performance and may uncover important trends or
problems.

Network settings
----------------

Pickit port labeled ROBOT
~~~~~~~~~~~~~~~~~~~~~~~~~~

This port has the purpose of connecting your Pickit processor to the
robot controller or PLC.

.. image:: /assets/images/Documentation/Settings-port-labeled-robot.png

By default, this port is set to  Static, which means it's using a
fixed IP configuration.
You can set the following IP Configuration options:

-  IP Address (Default value: 169.254.5.180)
-  Subnet mask (Default value: 255.255.0.0)
-  Gateway

If you prefer to get an IP Address from a DHCP server you set this port
to Dynamic. 

Test the connection to your robot by entering the IP of your robot
controller or PLC and check if it can be reached by the Pickit
processor.

Pickit port labeled LAN
~~~~~~~~~~~~~~~~~~~~~~~~

This port has the purpose of connecting your Pickit processor to a
network. 

.. image:: /assets/images/Documentation/Settings-port-labeled-lan.png

By default, this port is set to Dynamic, which means it's
requesting an IP address from the DHCP server in your network.

If you prefer to set a Static IP, you can set the following IP
Configuration options:

-  IP Address
-  Subnet mask
-  Gateway

Test connectivity to the internet by pressing the Check button.

Upgrade Pickit version
~~~~~~~~~~~~~~~~~~~~~~

Here you can upgrade your Pickit system to latest software version.
Refer to the :ref:`Pickit-system-software-upgrade`
for a step-by-step explanation how to upgrade the software on your
system.