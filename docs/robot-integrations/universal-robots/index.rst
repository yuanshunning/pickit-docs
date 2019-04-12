.. _universal-robots:

Set up Pickit with a Universal robot
=====================================

| **Note** This article describes the legacy way of using Pickit with a
  Universal Robot.
| For new systems, please refer to the  `Getting started with the
  Pickit
  URCap <https://support.pickit3d.com/article/75-getting-started-with-the-pick-it-urcap>`__
  article.

This setup manual helps you setup Pickit with a **Universal Robot**.

The setup of **Pickit** with a **Universal** **robot** consists of **3
steps**:

#. `Setup the network connection <#chapter01>`__
#. `Load the program files <#chapter02>`__
#. `Verify communication <#chapter03>`__

--------------

Setup the network connection
----------------------------

Hardware connection
~~~~~~~~~~~~~~~~~~~

The Pickit processor has to be connected to the Universal Robots
controller using an Ethernet cable. 

This Ethernet cable should be plugged in:

#. The **ROBOT** port of the **Pickit processor**; 
#. The **Internet & MODBUS** port of the **UR controller**.

IP configuration
~~~~~~~~~~~~~~~~

To allow communication between Pickit and the Universal
Robots controller both must have an IP address in the same subnet.

By default, the Ethernet port on the Pickit processor labeled ROBOT is
configured to have the following static IP address: **169.254.5.180**
with a subnet mask of **255.255.0.0**.

If this setting is kept, the following has to be done on the Universal
Robots controller via ``Setup Robot`` > ``Setup Network``: 

#. **Disable DHCP** to obtain a static IP;
#. Set the IP address of the robot to **169.254.5.182** which is an IP
   address in the same subnet as the Pickit IP;
#. Set the subnet mask to **255.255.0.0**;
#. Click ``APPLY``.

The IP address of the robot **can not** be the same as the IP address of
Pickit.

|image0|

.. raw:: html

   <div class-"callout">

Default gateway and DNS servers can stay untouched. 

.. raw:: html

   </div>

Test robot connection
---------------------

Details on testing this connection can be found on:   `Test robot to
Pickit
connection <http://support.pickit3d.com/article/19-test-robot-connection>`__

--------------

Load the program files
----------------------

Loading the program files for a Universal Robot consists of 2 steps:

#. `Download the right files <#download>`__
#. `Upload the files to the robot <#upload>`__

Download the right files
------------------------

`All program files available for Universal Robots can be downloaded
here <https://drive.google.com/uc?export-download&id-1VedZYjVvlcyiE4iuqUuF67DsT8545ojU>`__.

Once unzipped, the UR\_Pickit folder contains the following files:

-  **pickit\_communication**: This program is responsible for the low
   level communication between Pickit and the robot;
-  **pickit\_functions**: This program defines basic Pickit functions
   that allow taking Pickit actions via the robot controller;
-  **pickit\_transformations**: This program is responsible for
   computing the transform of the robot’s end-effector with respect to
   the reference frame;
-  **urmagic\_upload\_programs.sh**: This program takes care of the
   automatic uploading of all Pickit related files to the UR
   controller.

The UR\_Pickit folder also contains a few folders, each one
corresponding to a different **Polyscope** software version, containing
robot programs that use the mentioned ASCII files.

.. raw:: html

   <div class-"callout-yellow">

Modifying **pickit\_communication**, **pickit\_functions** or
**Pickit\_transformations** should only be considered after talking to a
**Pickit support engineer**. 

.. raw:: html

   </div>

Upload the files to the robot
-----------------------------

In order to upload these files onto the robot controller, a
USB pendrive containing these files has to be used.

#. **Copy all files** inside the UR\_Pickit folder to the root of the
   USB pendrive;
#. **Insert the USB pendrive** into the USB port of the robot controller
   screen
#. A red “USB” sign appears in the interface, indicating that **the
   upload is in progress**.
   At this moment, all files with extension .urp, .txt, .script,
   .installation and .variables are copied to the /programs folder in
   the original subfolders. 
#. After the upload is complete, **a green “USB” sign shows up**.

--------------

Start and verify communication
------------------------------

Starting and verifying communication consists of 3 steps:

 1
    `Start
    communication <https://secure.helpscout.net/docs/583bfcdbc6979106d37373a0/article/5845417a90336006981766b2#start>`__

 2
    `Verify
    communication <https://secure.helpscout.net/docs/583bfcdbc6979106d37373a0/article/5845417a90336006981766b2#verify>`__

Start communication
-------------------

To start the communication, on the robot you have to select a Pickit
example program which contains the Script instructions for Pickit in
the **BeforeStart** section. You can see an example in the
Robot\_camera\_calibration program:

|image1|

Press 'Play' on the Universal Robot interface, and communication will
start. Communication will stop again once the current robot program
stops.

Verify on the Pickit interface
-------------------------------

To verify the data packages are received by Pickit: Check for the
**V** icon next to 'Robot' in the top bar of the Pickit interface.

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/584e65dd9033602d65f6eb0e/file-0PsWIZrJwk.png
.. |image1| image:: https://lh6.googleusercontent.com/Twwk5VI4Fw2UPVHWRGwAjlArnMa2KVdVx9x5wALONN8KFtmM2Nwn1wVL08b6lne0Xylekg8b6wzKF-17FjjddyLDJ6RjyFb9ew-J_0jg5UB-E8U5DhdVn0D1suGwMC28vvho43g3
   :width: 232px
   :height: 264px
