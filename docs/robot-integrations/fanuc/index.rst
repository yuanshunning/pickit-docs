Setup Pick-it with a Fanuc robot
================================

This setup manual helps you setup Pick-it with a **Fanuc robot**. The
setup of **Pick-it** with a **Fanuc** **robot** consists of **4 steps**:

 1
    `Check controller and software compatibility <#chapter01>`__
 2
    `Setup the network connection <#chapter02>`__
 3
    `Load the program files <#chapter03>`__
 4
    `Start and verify communication <#chapter04>`__

Check controller and software compatibility
-------------------------------------------

.. raw:: html

   <div class-"callout-yellow">

Pick-it is compatible with controllers as of version **R-J3iB** and the
software module **User Socket Msg** for socket communication is
required. (The product number for this module is A05B-2600-R648)

.. raw:: html

   </div>

To verify if that software module is installed open the Status version
ID page by opening ``MENU > STATUS > Version ID`` and then click the
**ORDER FI** button.

|image0|

Here you can check now if the module is listed as shown below. Note that
also the software version (V8.30P in the above example) can be verified
here.  |image1|

Alternatively, a backup of the controller can be made and the
information on the installed software can be found in the following
file: ~/backup/All Of Above/orderfil.dat.

To get you started as quickly as possible, Pick-it provides:

-  All ASCII files for both the low-level communication as well as an
   example program.  
-  Binaries generated from these ASCII files for software version V8.30.
   In case of using an older software version, you might have to
   recompile the ASCII files first.

.. raw:: html

   <div class-"callout-yellow">

Note that for the version R-J3iB itself, the program names have to be
shortened to at maximum 8 characters.

.. raw:: html

   </div>

--------------

Setup the network connection
----------------------------

Setting up network connection for a Fanuc robot consists of 4 steps:

 1
    `Hardware connection <#hardware>`__
 2
    `IP configuration <#ipconfig>`__
 3
    `Socket configuration <#socket>`__
 4
    `Test robot connection <#test>`__

Hardware connection
~~~~~~~~~~~~~~~~~~~

The Pick-it processor has to be connected to the Fanuc controller using
an Ethernet cable. 

This Ethernet cable should be plugged in:

#. The **ROBOT** port of the **Pick-it processor**; 
#. The **Port 1** port of **Fanuc controller**.

The location of port 1 on the Fanuc  is shown for different controller
types in the images below.

|image2|

|image3|

The Ethernet cable must be fastened by a cable clamp to prevent tension
being applied to the RJ-45 connector, in case the Ethernet cable is
pulled directly. This clamp is also used to ground the cable shield. 

IP configuration
~~~~~~~~~~~~~~~~

To allow communication between Pick-it and the Fanuc controller both
must have an IP address in the same subnet.

By default, the Pick-it ROBOT connection (the Ethernet port on the
Pick-it processor labeled ROBOT) is configured to have the following
static IP address: **169.254.5.180** with a subnet mask of
**255.255.0.0**.

If this setting is kept, the following has to be done at the Fanuc
controller via  ``MENU > SETUP > Host Comm``: 

#. To obtain a static IP, **DHCP** has to be **disabled** on the
   controller.
#. A **static IP should be set** to e.g. 169.254.5.182 which is an IP in
   the same subnet as the Pick-it IP.

|image4|

And select the **TCP/IP protocol**:

|image5|

Next, you have to take the following steps: 

#. **Disable DHCP** by pressing the DHCP button 
#. **Set the correct IP address** and subnet mask for Port#1 
#. **Activate** these new settings via ``NEXT > INIT``

*To verify now if a network connection can be made between Pick-it and
the robot controller, you can create a new host name ‘pickit’ and give
it the Pick-it ROBOT connection IP address. After pressing the PING
button, you should see the following message printed:*

**Ping 169.254.5.180 succeeded**

Socket configuration
~~~~~~~~~~~~~~~~~~~~

Pick-it works through socket communication. To work properly Pick-it has
to act as the **server** for the socket communication. Hence, the robot
controller has to be configured to be **client**.

To do so, select ``Clients`` after pressing ``SHOW`` in the same SETUP
protocols menu used above.

|image6|

Next, select ``DETAIL`` to configure the client C1 as follows:

|image7|

To set the Startup State to **START** you have to use the ``[CHOICE]``
button.

To verify if the configuration of the socket is done correctly, you have
to reboot the controller and go again to ``MENU > SETUP > Host Comm``
and then pressing ``SHOW`` and ``Clients``. You should see the
following:

|image8|

Test robot connection
---------------------

Details on testing this connection can be found on:  `Test robot to
Pick-it
connection <http://support.pickit3d.com/article/19-test-robot-connection>`__

--------------

Load the program files
----------------------

Loading the program files for a Fanuc robot consists of 2 steps:

 1
    `Download the right files <#download>`__
 2
    `Upload the files to the robot <#upload>`__

Additionally we provide  `some extra insights on registers <#karel>`__
used by the Karel program.

Download the right files
------------------------

`All program files available for Fanuc robots can be downloaded
here <https://drive.google.com/uc?export-download&id-0BzZKo0Mfhw0RMDNULWxxY0dvcG8>`__.

The .zip folder contains the following ASCII files:

-  **pick\_it\_communication13\_C.kl**: This a Karel program that cares
   of the low level communication. This files should not be adapted.
-  **EXAMPLE\_PICK\_IT.LS**: This is a Teach Pendant program that shows
   a simple pick application for FANUC using Pick-it.
-  For calibration two Teach Pendant programs are provided
   **MP\_CALIBRATE.LS** for \ `multi poses
   calibration <http://support.pickit3d.com/article/35-how-to-execute-robot-camera-calibration#multipose>`__
   and **CALIBRATE.LS** for \ `single pose
   calibration <http://support.pickit3d.com/article/35-how-to-execute-robot-camera-calibration#singlepose>`__.
-  The other **.LS** file define short Teach Pendant program that
   abstract some of the Pick-it logic into more user readable functions.
   They can also serve as macros that can be called manually. More about
   that later. 

.. raw:: html

   <div class-"callout-blue">

In case of using Fanuc software version v8.30, you can directly use the
binaries available in the downloaded folder. In the other case, you
first have to compile the above files into binaries. 

.. raw:: html

   </div>

.. raw:: html

   <div class-"callout-yellow">

Modifying the pick\_it\_communication13\_C.kl file should only be
considered after talking to a Pick-it support engineer.

.. raw:: html

   </div>

Upload the files to the robot
-----------------------------

Uploading the files can be done using an FTP server or by manually
loading them on the robot using a USB stick mounted to the Teach
Pendant. For the latter, you have to go to
``MENU > FILE > UTIL > Set Device > Select your device:``

|image9|

The uploaded binary files also contain a configuration file for defining
macros: **SYSMACRO.SV**. In case all binaries are loaded correctly, you
can check if the macros are available via ``MENU > SETUP > Macro:``

|image10|

Registers used by the Karel program
-----------------------------------

The Karel program **pick\_it\_communication13\_C.kl**, which takes care
of the low-level communication between the controller and Pick-it, uses
the following IO and registers to pass on data from the low-level
communication to a Teach Pendant application program:

-  Data communicated from Pick-it via the Karel program to the Teach
   Pendant application program:

   -  **R[1]**: the Pick-it status
   -  **PR[1]**: an object pose detected by Pick-it

-  Data communicated from the Teach Pendant application program via the
   Karel program to Pick-it:

   -  **R[2]**: the command for Pick-it
   -  **R[4]**: the desired setup
   -  **R[5]**: the desired product
   -  **R[6]**: Pick-it object dimension x
   -  **R[7]**: Pick-it object dimension y
   -  **R[8]**: Pick-it object dimension z

.. raw:: html

   <div>

.. raw:: html

   <div class-"callout-blue">

To make the Karel programs visible on the Teach Pendant, you have to set
the KAREL\_ENB value to 1 via ``MENU > NEXT > SYSTEM > Sysvars``

.. raw:: html

   </div>

.. raw:: html

   </div>

--------------

Start and verify communication
------------------------------

Starting and verifying communication for a Fanuc robot consists of 2
steps:

 1
    `Start communication <#start>`__
 2
    `Verify communication <#verify>`__

Start communication
-------------------

To start the communication manually, on the robot you have to go to
``MENU > MANUAL FCTNS``, select ``P_OpenCommunication`` and press
``SHIFT+EXEC``.

|image11|

Verify communication
--------------------

Verify on the robot:
^^^^^^^^^^^^^^^^^^^^

In case the communication was started successfully, you can see the
following on the robot Teach Pendant:

**C1\_CONNECTED** is **shown** in the top status barVerify on the
Pick-it interface

|image12|

You can verify the connection from within the Pick-it web interface by
checking if there is a checkmark next to the robot status label in the
top bar.

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/583fe1d9c6979106d3738dbc/file-Y9AuqDqQaq.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/583fe230c6979106d3738dbe/file-JfBlRRIUSv.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/583bfe36903360069817375e/file-VlyXWHAWM4.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/583bfe539033600698173760/file-5qDdj3uOFM.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/583bfec8c6979106d37373ad/file-jRP8F5A0rr.png
.. |image5| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/583bfee89033600698173761/file-C63o6n8Box.png
.. |image6| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/583bff7cc6979106d37373b4/file-gvDb9kImCw.png
.. |image7| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/583bffc19033600698173767/file-2LI0FgLXTb.png
.. |image8| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/583bffe7c6979106d37373be/file-sbMN0grxp2.png
.. |image9| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/583ff420903360069817525d/file-7QvWN6CcKF.png
.. |image10| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/583ff4f5c6979106d3738df1/file-ILANYqSXx4.png
.. |image11| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/583ffa5fc6979106d3738e13/file-v2bB8WuRQq.png
.. |image12| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58cc0a382c7d3a79f5f8d520/file-Mq8WwqjdQ7.png

