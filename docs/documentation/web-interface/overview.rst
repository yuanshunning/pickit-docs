Overview
========

-  `Top bar <#top>`__
-  `Left side <#left>`__
-  `Right side <#right>`__

When a Pickit system is connected to an additional device and in a
Google chrome web browser following address is typed in 
`http://192.168.66.1 <http://192.168.66.1/>`__, the user interface of
Pickit shown. The user interface looks like the image below. In this
article a general overview of what you can see in this interface is
discussed. The interface is divided into 3 part: top, left and right.

|image0|

Top bar
-------

Starting from left to right. First the logo of Pickit shown. Next to
the logo the name of the system is given, typically this is pc-XXXXX.
Next to the name the current software version of your system is shown.

Next are the Pickit connection status:

-  **Robot**: An active robot communication is indicated by **✓**,
   otherwise **∅**.
-  **Cam**: A camera connection is indicated by **✓**, otherwise **∅**.
-  **App**: The Pickit application correctly working is indicated by
   **✓**, otherwise **∅**.

Then the current operational mode is shown. The Pickit system has 4
main operational modes:

-  **Running**: Pickit is ready to receive commands from the robot and
   to send localization results to the robot. You can only run a robot
   program with Pickit when this state is activated. 
-  **Check**: Pickit is doing a single object detection without sending
   the result to a connected robot. This allows testing the object
   detection without any robot or machine connected. 
-  **Testing**: Pickit is continuously detecting objects without
   sending the result to a connected robot. This mode allows testing the
   object detection without any robot or machine connected. 
-  **Idle**: No commands from the robot are accepted.

.. raw:: html

   <div class="callout-yellow">

By default, Pickit enables the **Robot mode** upon startup.

.. raw:: html

   </div>

Next to the state the current **Setup** and **Product** file are shown.
More information on these can be found in
the \ `Configuration <https://support.pickit3d.com/article/157-configuration>`__
article.

Then the Settings button is shown. Here the Network and user settings
can be defined. More information about these settings can be found in
the article 
`Settings <https://support.pickit3d.com/article/182-settings>`__.

At last the **Robot mode** button is shown. Here you can change from
**Robot mode** to **Idle**. 

.. raw:: html

   <div class="callout-yellow">

Only when Pickit is in **Idle** mode parameters can be changed and
saved.

.. raw:: html

   </div>

Left side
---------

Here the  `Pickit
viewer <https://support.pickit3d.com/article/156-views>`__
and \ `detection
grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__
are shown. See the corresponding articles to have an in depth
explanation.

Right side
----------

Here the parameters of the Pickit system can be changed and saved. All
settings and parameters are divided over several tabs. See article of
each tab to have an extensive overview:

-  `Configuration <https://support.pickit3d.com/article/157-configuration>`__
-  `Camera(s) <https://support.pickit3d.com/article/158-calibration>`__
-  `Region of
   Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
-  ` <https://support.pickit3d.com/article/159-region-of-interest>`__\ `Detection:
   Pickit
   Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
-  `Detection: Pickit
   Pattern <https://support.pickit3d.com/article/161-detection-pick-it-pattern>`__
-  `Detection: Pickit
   Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__
-  ` <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__\ `Picking <https://support.pickit3d.com/article/163-picking>`__
-  `Files <https://support.pickit3d.com/article/164-files>`__