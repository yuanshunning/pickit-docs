Build a showcase demo with Teach
================================

This article will guide you in setting up a simple robot picking
showcase demo with Pickit Teach. The Teach engine is the Pickit
solution for finding objects with **complex geometrical shapes** in all
kinds of orientations. In this demo we will be picking electrical plug
shieldings. Click `here <#picking>`__ to see the video of this demo.

#. `Requirements <#requirements>`__
#. `Your first detection(configuring the Pickit files) <#detection>`__
#. `Calibration <#calibration>`__
#. `Your first pick(program the robot) <#program>`__
#. `Happy picking <#picking>`__

1. Requirements
~~~~~~~~~~~~~~~

The hardware requirements to set up this demo are:

-  A Pickit vision system
-  A robot and gripper, i.e. UR5 and Robotiq gripper
-  An additional computer or laptop
-  Electrical plug casings, approximate dimensions 110 x 85 x 22 mm
   (contact support@pickit3d.com to get the parts)
-  Two similar bins, approximate dimensions 400 x 300 x 150 mm

.. raw:: html

   <div class="callout-yellow">

**Note** the length of the fingers of the gripper should be larger than
the depth of the bin. The main reason is that the head of the robot
stays out of the bin.

.. raw:: html

   </div>

It is assumed that the Pickit system is mounted around 700 mm above the
table and is running correctly. If you are not sure, please follow step
1-4 from our  `getting
started <https://support.pickit3d.com/article/125-quick-start-7-steps-to-your-first-pick>`__
guide. 

2. Your first detection(configuring the Pickit files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that every component is connected to the Pickit system, we are able
to configure Pickit. Open a chrome web browser on your external PC and
enter the following IP address to access the Pickit system.

::

    http://192.168.66.1

In the Pickit user interface, go to the configuration tab and create
new setup files and a product file:

-  **Setup 1:** teach\_demo\_bin\_left
-  **Setup 2:** teach\_demo\_bin\_right
-  **Product:** teach\_demo

Configuring Pickit comes down to three simple steps:

#. Teaching a model of the part you want to pick
#. Create a scene where you want to pick these parts
#. define a picking strategy

The information of the model and picking strategy is stored in the
product file and the information of the scene(s) is stored in the
different setup files.

2.a Teaching the model(s)
^^^^^^^^^^^^^^^^^^^^^^^^^

Here it is assumed that the parts in this demo only have two ways they
can be presented to the camera: either the top is shown or the bottom is
shown. It is assumed that in a random bin, even if a side is shown, that
after a while the part will fall down in the bin and either top or
bottom are shown. Due to this assumption it is sufficient to teach two
models of the part. One model will contain all information of the top of
the part and the second one contains all information of the bottom.

See below for images of both models that are used in the detection tab.
Below the images all detection parameters are given. See following
articles on how to use Pickit Teach and an explanation of all
parameters.

-  `Detection: Pickit
   Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__
-  `Explaining the Teach detection
   parameters <https://support.pickit3d.com/article/173-explaining-the-teach-detection-parameters>`__

|image0|

|image1|\ For both models following parameters are used:

-  **Matching tolerance:** 4mm
-  **Minimum matching score:** 75%
-  **Fusion:** None
-  **Downsampling:** 4
-  **Detection speed:** Normal
-  **Detection precision:** More precise

Note the orientation of the **pick frames** for both models, one is
rotated 90° towards the other. The reason for this is that the gripper
is going to approach the bottom and top under a different orientation.

Don't forget to save the settings. This will update the Product file.

2.b Create the scene(s)
^^^^^^^^^^^^^^^^^^^^^^^

The second step defines where Pickit has to look for objects. This is
done by defining the region of interest (ROI). See the article  `Region
of
Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
on how to define a ROI. 

Below you can see a pictures of a good defined ROI for this application.
All useless information is filtered out(the bin and the table) only
information of the parts in the bin is kept. Also make sure that the ROI
is slightly higher than the real bin.

For this demo two different ROI's are defined, one for each bin. Don't
forget to save the settings in the corresponding Setup files.

|image2| |image3|

2.c Define the picking strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Finally the picking strategy is defined. For this application only bin
collision is checked. This means that Pickit checks if the gripper can
pick the parts without hitting the bin. More information about the
picking strategies can be found in the 
`Picking <https://support.pickit3d.com/article/163-picking>`__ article.

For this demo following parameters are used:

-  **Enforce alignment:** No alignment
-  **Check collision with:** Bin
-  **Ordering Strategy:** Highest product center

Don't forget to save the settings. This will update the Product file.

3. Calibration
~~~~~~~~~~~~~~

Next step is the robot-camera calibration. This process teaches Pickit
where the robot base is located w.r.t. to the camera. This information
is used to transform the object pick-frames into robot coordinates. A
detailed description in robot-camera calibration can be found 
`here <https://support.pickit3d.com/article/35-how-to-execute-robot-camera-calibration>`__. Do
not forget to save after the calibration is finished.

4. Your first pick(Program the robot)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now Pickit is configured, the only thing left to do is programming the
robot. The robot used in the demo video is a UR5, but a similar program
can be created on any other robot.

The idea of this program is to start looking for the parts in one bin.
If one is found the robot moves towards the calculated position, opens
his gripper according which side is found(bottom or top), grasps the
part, get out of the bin and drops it off in the other bin. The parts
are dropped with using the pallet function. This function drops the
parts in different locations of the bin so no stack of parts is
created. The robot starts picking from the other bin either after 8
successful picks or after two unsuccessful detections. 

-  **The UR robot program:** Download
   link \ `here <https://drive.google.com/uc?export=download&id=1Nzqm_fDFosR59ZeQL8D-RrKCDCNLuytF>`__.

|image4|

.. raw:: html

   <div class="callout-yellow">

**Note** When performing random bin picking, *always* trigger a new
detection before picking the next object. The main reason lies in the
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

Following all these previous steps leads to the next Pickit Teach demo
application, happy picking!

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b6075582c7d3a03f89d30a6/file-Z1FeLvCs26.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b6075502c7d3a03f89d30a4/file-OpDijqlR9j.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ae1c4b404286328a414941e/file-8vti7bdxIR.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ae1c4ed04286328a4149423/file-ZfS0AdvZ7u.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b6170d20428631d7a8988c1/file-KEBv6fzuoj.png

