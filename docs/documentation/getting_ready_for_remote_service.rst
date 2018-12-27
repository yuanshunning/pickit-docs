Getting ready for remote service
================================

We will cover 3 possible scenarios in this how-to guide. 

 1
    `Connect your Pick-it processor to the internet <#with>`__ (the best
    way to receive complete remote service)
 2
    `Connect your PC (with internet connection) to your Pick-it
    processor <#without>`__ (in case option 1 does not work)
 3
    `There is no internet connection <#no>`__

Connect your Pick-it processor to the internet
----------------------------------------------

The preferred method is to connect your Pick-it processor `via an
Ethernet cable <#ethernet>`__. If this is not possible you can connect
your Pick-it processor `via the 3G USB dongle <#usb>`__.

|image0|

Connecting via Ethernet cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. **Plug in an Ethernet cable** (with internet access) into the LAN
   port of the Pick-it processor.
#. Navigate to the **Network settings**, by clicking on the Settings
   button at the top-right of the web interface.
   |image1|
#. In the \ **Pickit port labeled 'LAN’** section, make sure that the
   **IP address** field has a valid value (blue arrow in image below).

|image2|

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

   <div id="callout_protocol" class="callout">

**Info:** Pick-it uses VPN/TLS over TCP port 443 to establish
connection. The Pick-it Support Server is known as vpn.intermodalics.eu

.. raw:: html

   </div>

Connecting via USB dongle
~~~~~~~~~~~~~~~~~~~~~~~~~

Your Pick-it system was delivered with a USB 3G dongle to connect the
Pick-it system to the internet when  `connecting via
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
^^^^^^

|image3|

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
| Blinking green   | The card has registered to the network but no internet connection could be made.                                                |
|                  | Try reinserting the USB modem and restarting the Pick-it processor. If that doesn’t help, contact a Pick-it support engineer.   |
+------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Solid Green      | The network is available with a successful internet connection. A Pick-it support engineer can now access the system.           |
+------------------+---------------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </div>

Type 2
^^^^^^

|image4|

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
| Solid Green                       | The network is available with a successful internet connection to a 2G network.                                           |
|                                   | A Pick-it support engineer can now access the system but the connection might be too slow to perform a software update.   |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Solid Blue                        | The network is available with a successful internet connection to a 3G network.                                           |
|                                   | A Pick-it support engineer can now access the system but the software update might take up to several hours.              |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Solid Cyan                        | The network is available with a successful internet connection to a 3G+ network.                                          |
|                                   | A Pick-it support engineer can now access the system to perform a software update.                                        |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </div>

Connect your PC (with internet connection) to your Pick-it processor
--------------------------------------------------------------------

In case `connecting your Pick-it processor to the internet <#with>`__ is
not an option or does not work we can provide some remote service
through one of the following options:

-  `TeamViewer <#teamviewer>`__
-  `Video conferencing <#videoconferencing>`__

To receive remote service through one of these option you should always
connect your PC/laptop to the Pick-it processor:

#. **Connect your PC/laptop to the Pick-it processor** with an Ethernet
   cable to the network port labelled ‘Interface’ on your Pick-it
   processor and surf to the Pick-it web
   interface.(\ http://192.168.66.1/)
#. Make sure your **PC/laptop has connection to the internet**, while
   being able to see the Pick-it web interface.

TeamViewer
~~~~~~~~~~

When using TeamViewer installed on your PC, while your PC is connected
to the Pick-it system, **a Pick-it support engineer** can **view** and
**manipulate** your Pick-it web interface.

#. Make sure \ `TeamViewer <https://www.teamviewer.com/>`__ is
   **installed** on your PC/laptop. (`download it
   here <https://www.teamviewer.com/>`__)
#. Open TeamViewer and **send your partner id and password** to the
   Pick-it support engineer.

Video conferencing
~~~~~~~~~~~~~~~~~~

When using a video conferencing tool that allows screen sharing, while
your PC is connected to the Pick-it system,  **a Pick-it support
engineer** can **view** your Pick-it web interface.

#. **Choose a video conferencing tool** such as \ `Google
   Hangouts <https://hangouts.google.com/>`__
   or \ `Skype <https://www.skype.com/>`__.
#. **Contact a Pick-it support engineer** to ask him/her to join the
   video conference.
#. **Share your screen** with the Pick-it support engineer.

There is no internet connection
-------------------------------

The only available option when the is no internet connection on site is
getting service by `saving
snapshots <https://support.pickit3d.com/article/168-saving-a-snapshot-in-pick-it>`__
and sending them to a Pick-it support engineer.

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/592549520428634b4a33659c/file-Kj7MxzMb03.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acca6b604286307509243db/file-bBW4Yzc0ZC.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5accaac604286307509243f9/file-Hk32ec77zf.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5af060e50428631126f1c3b3/file-TAfLPIL4RG.jpg
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5af060872c7d3a3f981f4f79/file-7YOmy0dFqr.jpg

