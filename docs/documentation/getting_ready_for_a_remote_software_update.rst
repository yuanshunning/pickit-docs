Getting ready for a remote software update
==========================================

To receive an update of the Pick-it software, your Pick-it processor
needs to be connected to the Internet:

-  The preferred method is to connect your Pick-it  processor  `via  an
   Ethernet
   cable <https://secure.helpscout.net/docs/583bfcdbc6979106d37373a0/article/5af03bfa0428631126f1c29e#ethernet>`__. 
-  If this is not possible you can connect your Pick-it processor \ `via
   the 3G USB
   dongle <https://secure.helpscout.net/docs/583bfcdbc6979106d37373a0/article/5af03bfa0428631126f1c29e#usb>`__.

Connecting via Ethernet cable
-----------------------------

#. **Plug in an Ethernet cable** (with Internet access) into the **LAN
   port** of the Pick-it processor.
#. Navigate to the **Network settings**, by clicking on the Settings
   button at the top-right of the web interface.
   |image0|
#. In the \ **Pickit port labeled 'LAN’** section, make sure that the
   **IP address** field has a valid value (blue arrow in the image
   below).

|image1|

If an **IP address** shows up, you are good to go. A Pick-it engineer
can now connect to your system.

If no **IP address** shows up:

-  Double check if the Ethernet cable \ `is attached in the right
   way <#ethernet>`__ to the Pick-it processor and your network;
-  Check with your system administrator if there is a **firewall** on
   your network. If so:

   -  Ask your system administrator to whitelist the ‘LAN’ port’s **MAC
      address** shown in the Network page. (red arrow in the image
      above)
   -  Ask your system administrator to open **TCP 443 port.** (`more
      information on this setting <#callout_protocol>`__)

.. raw:: html

   <div id="callout_protocol" class="callout-blue">

**Info:** Pick-it uses VPN/TLS over TCP port 443 to establish a
connection. The Pick-it software update server is known as
**vpn.intermodalics.eu**.

.. raw:: html

   </div>

Connecting via USB dongle
-------------------------

Your Pick-it system was delivered with a USB 3G dongle to connect the
Pick-it system to the Internet when  `connecting via
Ethernet <#ethernet>`__ is not an option. A Pick-it SIM card is already
inside so this works out of the box. 

.. raw:: html

   <div class="callout-yellow">

**Note:** Since this is a wireless device, it's important that it is
positioned **outside a metal enclosure** (cage of Faraday). In case your
Pick-it system is in such an enclosure, you may use an extension cable
up to 2m to install the remote service modem outside this enclosure.

.. raw:: html

   </div>

.. raw:: html

   <div class="callout-yellow">

**Note:** Depending on **3G reception on site**, a Pick-it support
engineer could view and manipulate the Pick-it web interface, install
product and or setup files and perform updates. If the mobile reception
is bad viewing and manipulating the interface could be impossible. On
slow connections, software updates can take up to several hours.

.. raw:: html

   </div>

Pick-it systems were shipped with 2 different types of USB 3G dongles,
use the images below as a reference to check which type of dongle came
with your Pick-it system.

Type 1
~~~~~~

|image2|

The USB dongle can be plugged into any available USB port of your
Pick-it system. No configuration is required.

.. raw:: html

   <div>

+------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Status LED       | Indication                                                                                                                      |
+==================+=================================================================================================================================+
| Solid red        | The modem is initializing.                                                                                                      |
+------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Blinking red     | Check if a SIM/USIM card is inserted. If it is, try to unplug and replug the modem.                                             |
+------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Blinking green   | The card has registered to the network but no Internet connection could be made.                                                |
|                  | Try reinserting the USB modem and restarting the Pick-it processor. If that doesn’t help, contact a Pick-it support engineer.   |
+------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Solid Green      | The network is available with a successful Internet connection. A Pick-it support engineer can now access the system.           |
+------------------+---------------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </div>

Type 2
~~~~~~

|image3|

The USB dongle can be plugged into any available USB port of your
Pick-it system. No configuration is required.

.. raw:: html

   <div>

+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Status LED                        | Indication                                                                                                                |
+===================================+===========================================================================================================================+
| Blinking green twice (every 3s)   | The USB dongle is powered on.                                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Blinking green once (every 3s)    | The USB dongle is registering with a 2G network.                                                                          |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Blinking blue (every 3s)          | The USB dongle is registering with a 3G/3G+ network.                                                                      |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Solid Green                       | The network is available with a successful Internet connection to a 2G network.                                           |
|                                   | A Pick-it support engineer can now access the system but the connection might be too slow to perform a software update.   |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Solid Blue                        | The network is available with a successful Internet connection to a 3G network.                                           |
|                                   | A Pick-it support engineer can now access the system but the software update might take up to several hours.              |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Solid Cyan                        | The network is available with a successful Internet connection to a 3G+ network.                                          |
|                                   | A Pick-it support engineer can now access the system to perform a software update.                                        |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </div>

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acca6b604286307509243db/file-bBW4Yzc0ZC.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5accaac604286307509243f9/file-Hk32ec77zf.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5af060e50428631126f1c3b3/file-TAfLPIL4RG.jpg
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5af060872c7d3a3f981f4f79/file-7YOmy0dFqr.jpg

