Web interface
=============

When a Pickit system is connected to an additional device and in a
Google chrome web browser following address is typed in 
`http://192.168.66.1 <http://192.168.66.1/>`__, the user interface of
Pickit shown. The user interface looks like the image below. In this
article a general overview of what you can see in this interface is
discussed. The interface is divided into 3 part: top, left and right.

.. image:: /assets/images/First-steps/pickit-webinterface-20.png

.. contents::
    :backlinks: top
    :local:
    :depth: 1

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

.. note:: By default, Pickit enables the **Robot mode** upon startup.

Next to the state the current **Setup** and **Product** file are shown.
More information on these can be found in
the :ref:`Configuration` article.

Then the Settings button is shown. Here the Network and user settings
can be defined. More information about these settings can be found in
the article :ref:`Settings`.

At last the **Robot mode** button is shown. Here you can change from
**Robot mode** to **Idle**. 

.. note:: Only when Pickit is in **Idle** mode parameters can be changed and
   saved.

Left side
---------

Here the Pickit iewer and detection grid
are shown. See the corresponding articles to have an in depth
explanation.

.. toctree::
    :maxdepth: 1

    viewer
    detection-grid

Right side
----------

Here the parameters of the Pickit system can be changed and saved. All
settings and parameters are divided over several tabs. See article of
each tab to have an extensive overview:

-  :ref:`Configuration`
-  :ref:`Cameras`
-  :ref:`Region-of-interest`
-  :ref:`Flex`
-  :ref:`Pattern`
-  :ref:`Teach`
-  :ref:`Picking`
-  :ref:`Files`