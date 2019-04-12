Settings
========

-  `User settings <#user>`__
-  `Network setting <#network>`__
-  `Upgrade Pickit version <#upgrade>`__

User settings
-------------

Units
~~~~~

|image0|\ This setting allows you to select the length unit of choice
(meters, inches, ...) after which all length values in the interface
will be converted to the newly selected unit.

Automatic detection
~~~~~~~~~~~~~~~~~~~

Here you can choose to automatically trigger a new detection if a
parameter is changed.

Share usage statistics
~~~~~~~~~~~~~~~~~~~~~~

|image1|\ This aggregated data can be used to help create features that
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

|image2|

| By default, this port is set to  Static, which means it's using a
  fixed IP configuration.
| You can set the following IP Configuration options:

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

|image3|\ By default, this port is set to Dynamic, which means it's
requesting an IP address from the DHCP server in your network.

If you prefer to set a Static IP, you can set the following IP
Configuration options:

-  IP Address
-  Subnet mask
-  Gateway

Test connectivity to the internet by pressing the Check button.

Upgrade Pickit version (available from version 1.10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here you can upgrade your Pickit system to latest software version.
Refer to the \ `Pickit systems upgrade
guide <https://support.pickit3d.com/article/196-pick-it-system-software-upgrades>`__
for a step-by-step explanation how to upgrade the software on your
system.

Mentioned articles

What to read next

| 

| `Configuration <https://support.pickit3d.com/article/157-configuration>`__
| `Region of
  Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
| `Detection: Pickit
  Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
| `Detection:
  Pickit Pattern <https://support.pickit3d.com/article/161-detection-pick-it-pattern>`__
| `Detection:
  Pickit Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a8eeb2f04286305fbc9c22a/file-6s4JSgfNcK.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a8eeb432c7d3a080649478b/file-pm8LtL8rjI.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a8f1f8c04286305fbc9c4d0/file-VkC7fYmeap.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a8f20e62c7d3a08064949fc/file-CKo3mzh3On.png

