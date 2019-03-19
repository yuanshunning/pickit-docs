Setting up Pick-it with ABB
===========================

The setup of Pick-it with an ABB robot consists of 4 steps:

#. `Check controller and software compatibility <#chapter00>`__
#. `Setup the network connection <#chapter01>`__
#. `Load the program files <#chapter02>`__
#. `Test communication <#chapter03>`__

Check controller and software compatibility
-------------------------------------------

| Pick-it is compatible with controllers as of version IRC5 with
  RobotWare 5 or 6 and furthermore, Pick-it needs the following
  controller modules
|     • 616 PC interface
|     • 623-1 Multitasking

To check this compatibility,  open RobotStudio and follow next steps:

|image0|

|image1|

|image2|

If you don't have the right software version or module please contact
your local ABB distributor.

Setup the network connection
----------------------------

Hardware connection
~~~~~~~~~~~~~~~~~~~

The Pick-it processor has to be connected to the robot controller using
an Ethernet cable. 

This Ethernet cable should be plugged in:

#. The \ **ROBOT** port of the Pick-it processor; 
#. The \ **WAN** port of the robot controller.

IP configuration
~~~~~~~~~~~~~~~~

Open RobotStudio and follow next steps:

|image3|

|image4|

Set the IP address of the controller preferably to 
**169.254.5.182** which is an IP address in the same subnet as the
Pick-it IP and set the subnet mask to \ **255.255.0.0**.

The IP address of the robot can not be the same as the IP address of
Pick-it.

After these steps restart form the Flex pendant. (assuming you have no
write acces yet)

|image5|

Load the program files
----------------------

Download the right files
~~~~~~~~~~~~~~~~~~~~~~~~

`All program files available for an ABB robot can be downloaded
here <https://drive.google.com/uc?export-download&id-1-rLxMBKSnh-2JDbfjX3tPL-iYFBOLfoA>`__.

Upload the files to the robot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upload these files using File Transfer.

|image6|\ Request write access.

-  Manual mode: press 'Grant' on the Flex pendant
-  Automatic mode: not necessary

|image7|

Load parameters from controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image8|

Select the **Pickit SYS.cfg** file. This will load the required system
modules. 

For the ABB YuMi select the **Pickit SYS YuMi.cfg** file.

|image9|

Restart the controller.

|image10|

Test robot connection on Pick-it
--------------------------------

Details on testing this connection can be found on:  `Test robot to
Pick-it
connection <http://support.pickit3d.com/article/19-test-robot-connection>`__

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/590c7e260428634b4a32e286/file-f56PmHV3cI.jpg
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/590c7e300428634b4a32e287/file-Nfgs4ow6CZ.jpg
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/590c7e412c7d3a057f88d5bc/file-WZMatCUU5l.jpg
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/590c7ed10428634b4a32e295/file-RM2G5RR7C9.jpg
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/590c7ee32c7d3a057f88d5c6/file-JoOqek3Szq.jpg
.. |image5| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/590c80330428634b4a32e2ac/file-cupCsLxHzb.jpg
.. |image6| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/590c818e0428634b4a32e2c4/file-xqdxVIq3NH.jpg
.. |image7| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/590c81e90428634b4a32e2ca/file-6duraR4IT6.jpg
.. |image8| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/590c823a2c7d3a057f88d5fd/file-nHbzT0ufu6.jpg
.. |image9| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/590c829d2c7d3a057f88d602/file-KVIyNZZCIh.jpg
.. |image10| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/590c82a72c7d3a057f88d604/file-uoanS4ELIo.jpg

