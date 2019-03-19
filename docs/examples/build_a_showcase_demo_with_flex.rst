Build a showcase demo with Flex
===============================

This article will guide you in setting up a simple robot picking demo
with Pick-it Flex. The Flex vision engine is the vision engine for
finding objects with **simple geometrical shapes** in **random
orientations**. In this demo we are picking simple steel
cylinders. Click \ `here <#picking>`__ to see the video of this demo.

#. `Requirements <#requirements>`__
#. `Your first detection(configuring the Pick-it files) <#detection>`__
#. `Calibration <#calibration>`__
#. `Your first pick(program the robot) <#program>`__
#. `Happy picking <#picking>`__

1. Requirements
~~~~~~~~~~~~~~~

The hardware requirements to set up this demo are:

-  A Pick-it vision system
-  A robot and gripper, UR5 + double-lined magnetic gripper
-  An additional computer or laptop
-  Steel cylinders of 105 x 42 mm (diameters greater than 30 mm are
   advised)
-  A sturdy bin, dimensions 400 x 600 x 150 mm

First we create the hardware setup. This includes mounting the camera
and connecting all components.

.. raw:: html

   <div class="callout-yellow">

**Note** the length of the gripper should be larger than the depth of
the bin. The main reason is that the head of the robot stays out of the
bin.

.. raw:: html

   </div>

It is assumed that the Pick-it system is mounted around 700 mm above the
table and is running correctly. If you are not sure, please follow step
1-4 from our   `getting
started <https://support.pickit3d.com/article/125-quick-start-7-steps-to-your-first-pick>`__
guide. 

2. Your first detection(configuring the Pick-it files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that every component is connected to the Pick-it system, we are able
to configure Pick-it. Open a chrome web browser on your external PC and
enter the following IP address to access the Pick-it system.

::

    http://192.168.66.1

In the Pick-it user interface, go to the configuration tab and create
new setup files and a product file:

-  **Setup:** flex\_demo.
-  **Product:** flex\_demo.

Configuring the Pick-it comes down to three simple steps:

#. Create a scene where you want to pick the parts
#. Define the shape of objects that need to be picked
#. Define a picking strategy

The information of the shape and picking strategy is stored in the
product file and the information of the scene is stored in the setup
file.

2.a Create the scene
^^^^^^^^^^^^^^^^^^^^

The first step defines where Pick-it has to look for objects. This is
done by defining the region of interest (ROI). See the article  `Region
of
Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
on how to define a ROI. 

Below you can see a pictures of a good defined ROI for this application.
All useless information is filtered out(the bin and the table) only
information of the parts in the bin are kept. Also make sure that the
ROI is slightly higher than the real bin.

Don't forget to save the settings in the corresponding Setup files.

|image0|

|image1|

2.b Define the detection parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The second step consists in setting up the Pick-it Flex detection
engine. In this application Pick-it will look for cylindrical shapes in
the scene. 

See below for images of the results of the clustering and the fitting
step. Below the images all used detection parameters are given. See
following articles on how to use Pick-it Flex and an explanation of all
parameters.

-  `Detection: Pick-it
   Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
-  `Explaining the Flex detection
   parameters <https://support.pickit3d.com/article/174-explaining-the-flex-detection-parameters>`__\ |image2|

|image3|

In this demo following parameters are used:

-  **Clustering:** Touching - Preset A
-  No **rejecting clusters**
-  **Object model:** Cylinder
-  **Surface:** external only
-  **3D tolerance:** 5mm
-  Filtering: 400 < **Points** < 500000
-  Filtering: 100mm < **Length** < 110mm
-  Filtering: 38mm < **Diameter** < 46mm
-  **3D scene score:** 90%
-  **Fusion:** None
-  **Downsampling: **\ 1

Don't forget to save the settings. This will update the Product file.

2.c Define the picking strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Finally the picking strategy is defined. For this application bin
collision is checked. This means that Pick-it checks if the gripper can
pick the parts without hitting the bin. Also  the pick frames are
orientated on the top surface of the cylinders. More information about
the picking strategies can be found in the 
`Picking <https://support.pickit3d.com/article/163-picking>`__ article.

For this demo following parameters are used:

-  **Pick strategy:** Surface top
-  **Enforce alignment:** No alignment
-  **Check collision with:** Bin
-  **Ordering Strategy:** Highest product center

Don't forget to save the settings. This will update the Product file.

3. Calibration
~~~~~~~~~~~~~~

Next step is the robot-camera calibration. This process teaches Pick-it
where the robot base is located w.r.t. to the camera. This information
is used to transform the object pick-frames into robot coordinates. A
detailed description in robot-camera calibration can be found 
`here <https://support.pickit3d.com/article/35-how-to-execute-robot-camera-calibration>`__. Do
not forget to save after the calibration is finished.

4. Your first pick(Program the robot)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now Pick-it is configured, the only thing left to do is programming the
robot. The robot used in the demo video is a UR5, but a similar program
can be created on any other robot.

The idea of the program is to pick 5 parts and drop these off side by
side. After 5 cylinders are picked the program stops and a pop-up
appears. After the parts are taken away the program starts all over
again. 

-  **The UR robot program:** Download
   link \ `here <https://drive.google.com/uc?export=download&id=1JhTG1n5DSZauU7sXV6Z0JXjZYLRb7HUf>`__.

|image4|

.. raw:: html

   <div class="callout-yellow">

**Note** When performing random bin picking, *always* trigger a new
detection before picking the next object. The main reason lies in the
fact that the environment can change when an objects are picked and this
could lead to undesired miss-picks.

.. raw:: html

   </div>

.. raw:: html

   <div class="callout-red">

**Warning** When using the UR download program in the provided link,
*change the waypoints* to avoid moving the robot to unsafe positions.

.. raw:: html

   </div>

5. Happy picking!
~~~~~~~~~~~~~~~~~

Following all these previous steps leads to the next Pick-it Flex demo
application, happy picking!

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ae089b42c7d3a5063b4dd94/file-N07wxn0nrw.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ae088ee2c7d3a5063b4dd90/file-umdtf5TwpF.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ae0908f2c7d3a5063b4dde7/file-3kxVAYZ2kX.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ae09f992c7d3a5063b4deac/file-vNRKmvPg2U.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acf620c2c7d3a0e93674192/file-7fk4iZV1W4.png

