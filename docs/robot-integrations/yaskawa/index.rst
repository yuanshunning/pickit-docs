Setup Pick-it with a Yaskawa robot
==================================

This setup manual helps you setup Pick-it with a Yaskawa robot. The
setup of Pick-it with a Yaskawa robot consists of 4 steps:

 1
    `Check controller and software compatibility <#compatibility>`__
 2
    `Setup the network connection <#network>`__
 3
    `Load the MotoPlus application <#motoplus>`__
 4
    `Start and verify communication <#communication>`__

Check controller and software compatibility
-------------------------------------------

Pick-it is compatible with controllers **FS100,** **DX200** and
**YRC1000**.

.. raw:: html

   <div class="callout-yellow">

The following parameters must be declared on the controller to allow the
correct operation of the application. These settings must be enabled by
Yaskawa:

-  **Ethernet** function set to **1**
-  **MotoPlus** function set to **1**
-  **Macro** function set to **1**
-  **MotoPlus - Number of files** set to **1**
-  **MotoPlus - Number of tasks** set to **5**

.. raw:: html

   </div>

Please contact your local Yaskawa affiliate if you need to connect
multiple devices to the Ethernet port to check compatibility of all this
equipment.

Setup the network connection
----------------------------

Hardware connection
~~~~~~~~~~~~~~~~~~~

The connection between the Yaskawa controller and Pick-it is done over
ethernet. You connect your robot controller to the **ROBOT **\ port on
the Pick-it processor as shown in the diagram below:

|image0|

-  For **DX200** controllers you need to connect the Pick-it processor
   to the **CN104** port.
-  For **FS100** controllers you need to connect the Pick-it processor
   to the **CN2** port.

IP configuration
~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="callout-yellow">

The robot controller should be in  **maintenance mode **\ and the
security mode to \ **management mode** before making these changes.

.. raw:: html

   </div>

Setting the IP address of the robot controller happens in **maintenance
mode** and can be done under **SYSTEM → SETUP → OPTION FUNCTION →
NETWORK** and set the following values:

-  **IP ADDRESS SETTING**: MANUAL SETTING

   -  **IP ADDRESS:** 169.254.5.182
   -  **SUBNET MASK:** 255.255.0.0
   -  **DEFAULT GATEWAY:** 0.0.0.0

Setting the Pick-it IP address on the robot controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The address of Pick-it needs to be entered in a **String**. To do this:

#. Start the robot controller in **normal mode**
#. Go to \ **Main menu → VARIABLE → STRING → S099**
#. Set **S099** to value **169.254.5.180**

Loading the MotoPlus application
--------------------------------

The robot controller should be maintenance mode and the security mode
to management mode before making these changes.

| Before starting, the MotoPlus application should be placed on a USB
  dongle.
| `Download the Pick-it MotoPlus application
  here <https://support.pickit3d.com/article/36-pick-it-robot-programs>`__.

#. Load the correct USB device under \ **SYSTEM → MotoPlus APL. →
   DEVICE**.
#. Open the correct folder where the MotoPlus application is stored
   under \ **SYSTEM → MotoPlus APL. → FOLDER**.
#. Load the MotoPlus application under \ **SYSTEM → MotoPlus APL. →
   LOAD(USER APPLICATION)**. 

Test robot connection on Pick-it
--------------------------------

Details on testing this connection can be found on:  `Test robot to
Pick-it
connection <http://support.pickit3d.com/article/19-test-robot-connection>`__

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ab51daf042863794fbe8cd1/file-f1uO7SanPN.png

