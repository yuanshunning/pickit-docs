.. _staubli:

Setting up Pickit with Staubli
===============================

This setup manual helps you setup Pickit with a **Staubli robot**.

The setup of **Pickit** with a **Staubli** consists of **4 steps**:

#. `Check Staubli software version <#chapter00>`__
#. `Setup the network connection <#chapter01>`__
#. `Load the program files <#chapter02>`__
#. `Verify communication <#chapter03>`__

--------------

Check Staubli software version
------------------------------

The software version should be at least 7.

To verify this go to  
``MENU`` > ``CONTROL PANEL`` > ``CONTROLLER CONFIGURATION`` > ``VERSION``

|image0|

|image1|

Setup the network connection
----------------------------

Hardware connection
~~~~~~~~~~~~~~~~~~~

The Pickit processor has to be connected to the robot controller using
an Ethernet cable. 

This Ethernet cable should be plugged in:

#. The **ROBOT** port of the **Pickit processor**; 
#. The **robot controller**.

IP configuration
~~~~~~~~~~~~~~~~

To allow communication between Pickit and the robot controller both
must have a different IP address in the same subnet.

By default, the Ethernet port on the Pickit processor labeled ROBOT is
configured to have the following static IP address: **169.254.5.180**
with a subnet mask of **255.255.0.0**.

If this setting is kept, the following has to be done on the robot
controller:

Go to  ``MENU`` > ``CONTROL PANEL`` > ``CONTROLLER CONFIGURATION`` >
``NETWORK`` > ``J204 or J205``

#. Set the IP address of the robot to \ **169.254.5.182** which is an IP
   address in the same subnet as the Pickit IP address;
#. Set the subnet mask to\ ** 255.255.0.0**;

Push Enter to edit. Push F8 OK.

The IP address of the robot can of course not be the same as the IP
address of Pickit.

|image2|

Setup socket
------------

Go to   ``MENU``>  ``CONTROL PANEL``
> \ ``IO`` > ``SOCKETS`` > ``TCP CLIENTS`` > ``NEW``

#. Choose Type: Client
#. Add name: pickit
#. Add the Pickit IP address

|image3|

|image4|

You can test the new socket connection by pushing the Test button.

Test robot connection on Pickit
--------------------------------

Details on testing this connection can be found on:  `Test robot to
Pickit
connection <http://support.pickit3d.com/article/19-test-robot-connection>`__

--------------

Load the program files
----------------------

Loading the program files consists of 2 steps:

#. `Download the right files <#download>`__
#. `Upload the files to the robot <#upload>`__

Download the right files
------------------------

`All program files available for Staubli can be downloaded
here <https://drive.google.com/uc?export-download&id-0BzZKo0Mfhw0RcmJnWWE4LXM4M1k>`__.

Upload the files to the robot
-----------------------------

Upload these files using SRS.

|image5|

--------------

Start and verify communication
------------------------------

Starting and verifying communication consists of 3 steps:

 1
    `Select robot <#select>`__
 2
    `Start communication <#start>`__
 3
    `Verify communication <#verify>`__

Select the right robot
----------------------

Select **Staubli** as the robot type on the Pickit interface. You can
select the robot type under ``Configuration``.

Start communication
-------------------

To start the communication, on the robot you have to select a Pickit
example program. You can test this by using the  *OpenComm* program. 

Verify on the Pickit interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To verify the data packages are received by Pickit: Check for the 
**V** icon next to 'Robot' in the top bar of the Pickit interface.

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58da5f212c7d3a52b42efc64/file-xgLfNUca9b.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58da5f4add8c8e5c5730e996/file-f6GktCCUzZ.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58da62a62c7d3a52b42efc87/file-3TrPwfBQaT.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58da643f2c7d3a52b42efca1/file-zvwgPrS7SB.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58de6933dd8c8e5c5731036d/file-pi1JOBEtv9.png
.. |image5| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58da66eadd8c8e5c5730ea05/file-LCc73gR9iu.png

