Build a showcase demo with Pattern
==================================

This article will guide you in setting up a simple robot picking demo
with Pickit Pattern. The Pattern vision engine is made for picking
objects with **simple geometrical** **shapes** stacked into an
**organized pattern**. In this demo we are picking cardboard boxes.
Click `here <#picking>`__ to see the video of this demo.

#. `Requirements <#requirements>`__
#. `Your first detection(configuring the Pickit files) <#detection>`__
#. `Calibration <#calibration>`__
#. `Your first pick(program the robot) <#program>`__
#. `Happy picking <#picking>`__

1. Requirements
~~~~~~~~~~~~~~~

The hardware requirements to set up this demo are:

-  A Pickit vision system
-  A robot and gripper, UR5 + vacuum suction cup
-  An additional computer or laptop
-  Cardboard boxes of equal size, i.e. 115 x 65 x 30 mm
   (contact support@pickit3d.com to get exactly these parts).

It is assumed that the Pickit system is mounted around 700 mm above the
table and is running correctly. If you are not sure, please follow step
1-4 from our  `getting
started <https://support.pickit3d.com/article/125-quick-start-7-steps-to-your-first-pick>`__
guide. 

2. Your first detection(Configure the Pickit files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that every component is connected to the Pickit system, we are able
to configure Pickit. Open a chrome web browser on your external PC and
enter the following IP address to access the Pickit system.

::

    http://192.168.66.1

In the Pickit user interface, go to the configuration tab and create
new setup files and a product file:

-  **Setup:** pattern\_demo.
-  **Product:** pattern\_demo.

Configuring the Pickit comes down to three simple steps:

#. Create a scene where you want to pick the parts
#. Define the shape of objects that need to be picked
#. Define a picking strategy

2.a create a scene
^^^^^^^^^^^^^^^^^^

The first step defines where Pickit has to look for objects. This is
done by defining the region of interest (ROI). See the article   `Region
of
Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
on how to define a ROI. 

Below you can see a pictures of a good defined ROI for this application.
All useless information is filtered out(the table and surroundings) only
information of the parts on the table are kept. 

Don't forget to save the settings in the corresponding Setup files.

|image0|

2.b Define the detection parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The second step consists in setting up the Pickit Pattern detection
engine. In this application Pickit will look for fixed sized
rectangular shapes.

See below for images of the results of the clustering and the fitting
step. Below the images all used detection parameters are given. See
following articles on how to use Pickit Pattern and an explanation of
all parameters.

-  `Detection: Pickit
   Pattern <https://support.pickit3d.com/article/161-detection-pick-it-pattern>`__
-  `Explaining the Pattern detection
   parameters <https://support.pickit3d.com/article/175-explaining-the-pattern-detection-parameters>`__

|image1|\ |image2|

In this demo following parameters are used

-  **Clustering:** Non-touching 
-  No \ **rejecting clusters**
-  **Object model:** rectangle
-  **Contour:** inner and outer
-  **3D tolerance:** 15mm
-  **2D tolerance:** 10mm
-  **Expected length:** 115mm
-  **Expected width:** 65mm
-  **Expected orientation:** either X \|\| X or X \|\| Y depending on
   the pattern orientation w.r.t. the reference frame in the 3D-view.
-  **2D contour score:** 45%
-  **2D surface score:** 95%
-  **Fusion:** None
-  **Downsampling:** 1

Don't forget to save the settings. This will update the Product file.

2.c Define the picking parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Finally the picking strategy is defined. For this application no special
strategies are applied. However more information about the picking
strategies can be found in the 
`Picking <https://support.pickit3d.com/article/163-picking>`__ article.

-  **Enforce alignment:** No alignment
-  **Check collision with:** none
-  **Ordering Strategy:** Highest product center

Don't forget to save the settings. This will update the Product file.

3. Calibration
~~~~~~~~~~~~~~

Next step is the robot-camera calibration. This process teaches Pickit
where the robot base is located w.r.t. to the camera. This information
is used to transform the object pick-frames into robot coordinates. A
detailed description in robot-camera calibration can be found  
`here <https://support.pickit3d.com/article/35-how-to-execute-robot-camera-calibration>`__. Do
not forget to save after the calibration is finished.

4. Program the robot
~~~~~~~~~~~~~~~~~~~~

Now Pickit is configured, the only thing left to do is programming the
robot. The robot used in the demo video is a UR5, but a similar program
can be created on any other robot.

The idea of the program is to trigger a detection and take all found
parts one by one. The parts are dropped off on a running conveyor. Since
the boxes are nicely stacked and it is unlikely that a part will move
when one is taken away it is not necessary to trigger a new detection
every time.

-  **The UR robot program:** Download
   link \ `here <https://drive.google.com/uc?export=download&id=1CDlLHGBOY-UKC28ONp_8AvYfquVs0W4V>`__.

|image3|

.. raw:: html

   <div class="callout-red">

**Warning** When using the UR download program in the provided link,
*change the waypoints* to avoid moving the robot to unsafe positions.

.. raw:: html

   </div>

5. Happy picking!
~~~~~~~~~~~~~~~~~

If you followed all steps above, you're ready building your Pickit
product showcase using the Pattern detection engine. Happy picking!

If you need any help with one of the steps above, please contact 
`support@pickit3d.com <mailto:mailto://support@pickit3d.com>`__.

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ad8b23c04286307509297ec/file-ulqiVC6aXr.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ad8b21404286307509297e6/file-JujSd916Lj.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ad8b3272c7d3a0e93677d63/file-u414cFpDJv.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b61cd832c7d3a03f89d3e5a/file-HYsEDLVJUC.png

