.. _kuka:

Setting up Pick-it with a KUKA robot
====================================

The setup of Pick-it with an KUKA robot consists of 4 steps:

 1
    `Check controller and software compatibility <#chapter00>`__
 2
    `Setting up the network connection <#chapter01>`__
 3
    `Loading the program files <#chapter02>`__
 4
    `Starting and verifying the communication <#chapter03>`__

Check controller and software compatibility
-------------------------------------------

Pick-it is compatible with controllers as of version **KR-C4** and the
software module **KUKA Connect KRC** for socket communication is
required. The product number for this module is **91B300-020** version
**2.0.14** or later.

Verify if already installed
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To verify whether the **KUKA Connect KRC** module is already installed
on the **KR-C4** controller, go to the **Main Menu**,
then \ **``Help> Info``**. In the **``Info``** screen select the
 **``Options``** tab. The **Main Menu** is reachable by clicking on the
round robot icon:

**|image0|**

If an entry named **Connect** is listed, then the module is installed
and you can skip the next subsection. If the entry is not listed, as in
the image below (right), follow the remaining steps of this section to
install the **KUKA Connect KRC** module.

|image1|

Module installation
~~~~~~~~~~~~~~~~~~~

The **KUKA Connect KRC** module can be purchased directly from KUKA, and
consists of: a set of files that you should copy to a NTFS formatted USB
drive, and a 16-digit license key with the format
**xxxx-xxxx-xxxx-xxxx** that depends on the robot’s serial number.

Generation of temporary license keys by KUKA is possible for validating
an application before the actual purchase of a Pick-it system.

Plug in the USB drive containing the **KUKA Connect KRC** module files
in the external USB port of the **KR-C4** controller cabinet.

|image2|

A user with expert privileges is required to install the module. To
enable expert mode, go to **Main Menu**, then
**``Configuration> User group``** and select the **Expert** group.

|image3|

To install the module, go to **Main Menu**, then
**``Startup> Additional software``**. In the **``Additional software``**
click the **``New software``** button.

|image4|

You should see a list of available modules pending for installation,
including an entry named **``Connect``**. Toggle the checkbox next to
the **``Connect``** module and click install. Confirm the installation
on the pop-up dialog.

|image5|

After preparing the installation, a pop-up dialog will request a
controller restart to complete the installation. Dismiss the pop-up by
clicking OK and click the **``Restart``** button. You can also remove
the USB drive from the **KR-C4** controller cabinet at this point.

|image6|

After restarting, you should see a notification at the top of the screen
indicating that the **``Connect``** module has an invalid license key.

|image7|

To activate the license, go to **Main Menu**, then
**``Configuration> Connect settings``**. In the **``Connect settings``**
screen click the **``License``** button.

|image8|

Enter the 16 digit license key associated to the robot’s serial number
**including dashes** and click **``Activate``**.

|image9|

For the license key activation to take effect, another controller
restart is required. To do so, go to **Main Menu**, then
**``Shutdown``**. In the **``Shutdown``** screen click the
**``Reboot control PC``** button and confirm.

|image10|

SPS file settings
~~~~~~~~~~~~~~~~~

Apart from installing the **KUKA Connect KRC** module, it is necessary
to add one command to the SPS file, which executes in the background of
all robot programs. You need to be in **expert** mode to perform this
operation. To open the SPS file from the navigator, browse to
**``R1> System``**, select the **``sps``** file and click **``Open``**,
as shown in the figure below, left.

Once the file is open, move the cursor to the **``USER PLC``** line and
click on **``Open/close fold``**, and add a line calling the
**``pickitsps()``** function, as shown in the figure below, right.
Finally, close the file to save and exit (orange close icon at left
panel).

|image11|

The **``pickitsps()``** function allows Pick-it to have access to the
robot flange pose, as opposed to the pose of the currently active tool.

|image12|

KUKA KRC settings
~~~~~~~~~~~~~~~~~

Now that the **KUKA Connect KRC** module is installed, we need to
configure it to communicate correctly with the Pick-it system. To do
this, go to **Main Menu**, then **``Configuration> Connect settings``**.
In the **``Connect settings``** screen select the
**``Pickit Settings``** tab and inspect/modify the configuration, as
follows, and as shown in the figure below (right):

|image13|

.. raw:: html

   <div>

**
**

-  **Check correctness the robot IP address. **\ This is a read-only
   value shown for sanity-checking the robot configuration. If you wish
   to change the robot IP address, please refer to the **KUKA KR-C4**
   user manual.
-  **Disable the local UDP port.**
-  **Disable the local TCP port.**
-  **Activate ‘Show dialogs to autocomplete filter’.**
-  **Activate ‘Enable PickIt client connection’.**
-  **Specify the Pick-it server IP address.**

| When communicating with KUKA robots, the Pick-it server IP address
  cannot belong to the following IP ranges:
| **169.254.0.0** to **169.254.255.255
  192.168.0.0** to **192.168.0.255
  172.16.0.0** to **172.16.255.255
  172.17.0.0** to **172.17.255.255
  **\ The default Pick-it server IP is **169.254.5.180**, which belongs
  to the first range, so it must be modified.

Click on the **``Save``** button to store the settings.

.. rubric:: Setting up the network connection
   :name: chapter01

The Pick-it processor has to be connected to the **KUKA KR-C4**
controller using an Ethernet cable. This Ethernet cable should connect:

#. The network port labeled **‘ROBOT’** of the Pick-it PC;
#. The KLI Ethernet port of the KR-C4 controller (also referred to as
   X66). The location of this port may vary depending on the controller
   model. The below images show example locations: Cabinet door (left),
   built-in switch (right).

|image14|

.. rubric:: Loading the program files
   :name: chapter02

There are two sets of files installed in the robot controller that
relate to Pick-it communication:

-  **Pick-it application files.**\ These are example programs that
   illustrate how to perform typical Pick-it operations, like
   robot-camera calibration or object detection for pick and place.
   These are located in **``R1> Program> PickIt``**.
-  **Pick-it interface files.** These are internal files that expose the
   high-level functions used by the application files, and manage
   low-level communication with the Pick-it system. These files are not
   meant for editing and are located in **``R1> TP> Connect> PickIt``**.

The Pick-it application files can be loaded and executed as any other
KUKA.KRL program. Please refer to the **KUKA KR-C4** user manual for
further details.

The examples contained in the Pick-it application files contain
**hard-coded robot poses that should be adapted to every new robot**.
When executing such programs for the first time, please do so in
**manual mode and at low speed** to check for potential collisions.

.. rubric:: Starting and verifying the communication
   :name: chapter03

Before starting the communication, on the Pick-it interface select KUKA
as the robot to communicate with. Next, on the robot side, go to **Main
Menu**, then **``Configuration> Connect settings``**. In the
**``Connect settings``** screen, data being exchanged between the robot
and Pick-it is displayed in the text boxes labeled **``PC -> Robot``**
and **``Robot -> PC``**. You should see data and timestamps be updated
multiple times per second.

|image15|

On the Pick-it side, you can also enable the Log raw data from robot
checkbox to display the raw text messages being sent by the robot.

|image16|

.. raw:: html

   </div>

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/598db351042863033a1be754/file-hIWiAmMSzz.png
   :class: noBdr
.. |image1| image:: https://lh5.googleusercontent.com/HEOuW279eBSXSCrjj_-J7Y5GH9F1zWEB3KUcfypORAyV1iN2orq9gk_Xo4qC07ibV9HxS31v8OlUeEQExNXv3ul0lg12tJEIF8E7xhltodo-RS7MEDcqfmRmhcFeHSZCi3pJeO-L
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/598dba912c7d3a73488be830/file-7nKYl4quBC.png
.. |image3| image:: https://lh4.googleusercontent.com/M0tmwrzyr97yW6b8kGiiCS0fOYN3AEq3kSG-RNzi1Ae-3_1CKuSu2lgGfSqGXGHoiu5YOPMiFiYkMg-zQMJ2jkkMNgtnlvk5ywVgZzUuD6CmAA53aT4wM9ENVbVQ6Q5LaT9Wjt0c
.. |image4| image:: https://lh6.googleusercontent.com/X-RLuOc-5n1Dv9HAqDWfDT9zPLldkrC4whYJN_vFsQ8QG4On4dsqFMVeqYV_xhYiPW5HdJbAJWhDs0v9F49HGpAagr1s5qfXB4yD7YOBL1G5vy5BHVtlylm3dZhfiCwddNFQVma2
.. |image5| image:: https://lh4.googleusercontent.com/q2CEzUAATtewy-8dmrtMlAmGahXInGsqyYx327GuCVmXY5PZFoJMLGetNkXLlv9F_XhcLCpaSLpl92-0c4TYFAMd_A-syJpCYfPOIa-ERV0vipTzcYZEQacWLYRqkvsuBbXfG2Hr
.. |image6| image:: https://lh3.googleusercontent.com/EUICs9LxHMd23dSDtDtv32yX6FGThuado1fUTBKfwGnkJ4Y_zL9mXessCHf7jC7uDuXPE_2Vb6f7cAT_LboQAK7DSjHo6Ug7SJgw6shPqLTW0cRr2VznDoCyo0mucSQd8OJ6xyYU
.. |image7| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/598dbdec042863033a1be7f1/file-E0Gdyqaqyd.png
.. |image8| image:: https://lh6.googleusercontent.com/gdEphYeptKs-DhBhbnZeiTxlWbfEBfDVy-48xhFSFGNYGJXHTCRHR1FUXFIcLlcjoS0h2eBmoNH78U31q1lllOlnQJlIqkgIx6nSWWUE1Q6EcyXy8zYShRhF774vl4_BgIZtBv9I
.. |image9| image:: https://lh3.googleusercontent.com/ulT1LOCf1p_5cnm5TmhmokAnYkSgvONx2sJ3htDTiQwgyeP6HYEgfK3mNh1OQvF-KySBl5FEdXhooITQqnLpjejaYFdfF84nnOvj67GrBxnaVvmAWX2MF4o9jFzYYIuxmJFF4gAl
.. |image10| image:: https://lh6.googleusercontent.com/T8pmNRrrrt-ey5Ykk-9HcBtbzV3gNDZRZlRkg_SmivPl5CLdOa4E0-gvpzAwKhA2pZxmYV0Sc-Y00gy1XHR10A-505qkFFxPLPweo6KWwnbPUhBHiMPV6alsM94imTA8Lz6pskxe
.. |image11| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/598dc1282c7d3a73488be886/file-uRW4lGZcCd.png
   :class: noBdr
.. |image12| image:: https://lh5.googleusercontent.com/2lMqy1osuvMNUQ-Hd-FpRtLFj-Le2L_EWi3DbsVCQrVjnyZFbGPP6HyY5fzOgso7oUGH8RASBUcaKb0EAARe3n0LzJa8g8JgZKXeSFrWfhDRcvtv4CpCOk0NROBQFEEvE2Cccdvf
.. |image13| image:: https://lh6.googleusercontent.com/q0XXskuMWL5Mb0iApmFyPnAQumvDYSX66lHGlT_u19k4CPE0rcNlMZjPSzZywdWzaqKKXN_2G9me9XtkuwjXlwyLfnXmNbcVk1ub-qRhUo-iGg3_WeGdzTt5Ei2XkHnpU_Trxili
.. |image14| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/598dc6a02c7d3a73488be8cd/file-lCsVqNyQ09.png
.. |image15| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/598dcbd12c7d3a73488be913/file-me7AClcPAH.png
.. |image16| image:: https://lh3.googleusercontent.com/-xsVjbkGM_SlhG_iHk13OgApD9D529Uoh_Ah9SgL_KGtTiKDpHulj9dSqXK5tkQ1RA7qXJUdtxMjpW8h3_EQO6yeTDzZE-JoQwIcSzGkkGeLMpcY7ftgeRzj8MJOi24sFqsl0zIg

