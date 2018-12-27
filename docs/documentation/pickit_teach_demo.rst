Pick-it Teach demo
==================

This article will guide you in setting up a simple robot picking demo
with Pick-it Teach. The Teach engine is the Pick-it solution for finding
objects with **complex geometrical shapes** in all kinds of
orientations. In this demo we will be picking electrical plug
shieldings. This demo is set up in four simple steps:

#. Create the setup
#. Configure the Pick-it system
#. Program the robot
#. Happy picking!

1. Create the setup
-------------------

The hardware requirements that are needed to set up this demo are:

-  A Pick-it vision system
-  A robot and gripper, i.e. UR5 and Robotiq gripper
-  An additional computer laptop
-  Electrical plug casings, approximate dimensions 110 x 85 x 22 mm
   (contact support@pickit3d.com to get the parts)
-  Two similar bins, approximate dimensions 400 x 300 x 150 mm

Once you have all the components, you will have to mount the camera and
connect all components.

.. raw:: html

   <div class="callout-yellow">

**Note** The height of the bin can not be bigger than the length of the
gripper fingers. The main reason is that we do not want the robot going
inside the bin to avoid collisions while picking objects.

.. raw:: html

   </div>

1.a Mount the camera
~~~~~~~~~~~~~~~~~~~~

In this particular demo, we mount the Pick-it camera stationary in the
environment. Be sure that the camera is mounted at a proper height with
respect to the working surface, i.e. within the field of view (FOV) of
the camera. For the Pick-it M camera, a mounting height of 700 mm is
advised.

.. raw:: html

   <div class="callout-red">

**Warning** Keep the camera mounting rack *outside* the workspace of the
robot to avoid collisions.

.. raw:: html

   </div>

1.b Connect all the hardware components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Pick-it processor needs to be connected to:

#. The Pick-it camera by USB-connection.
#. Your PC by a local network connection. Use the **YOUR-PC** port on
   the processor.
#. The robot by a local network connection. Use the **ROBOT** port on
   the processor.

These three connections can be seen in the picture below, depicting the
Pick-it ecosystem. Extended guidelines on connecting the system can be
found in \ `this
article <https://support.pickit3d.com/article/74-setting-up-your-pick-it-system>`__.

|image0|

2. Configure the Pick-it system
-------------------------------

Now that every component is connected to the Pick-it system, we are able
to configure Pick-it. Open a chrome web browser on your external PC and
enter the following IP address to access the Pick-it system.

::

    http://192.168.66.1

The Pick-it user interface will now appear. Go to the configuration tab
and create a new setup and product file:

-  **Setup:** teach\_demo\_bin\_left.
-  **Product:** teach\_demo.

Configuring Pick-it comes down to performing these four simple steps:

#. Calibration: Run a robot-camera calibration.
#. Region of interest: Define a region of interest.
#. Detection: Define the objects to search, based on a Pick-it Teach
   model.
#. Picking: Define the picking strategy.

The robot-camera calibration and region of interest settings are stored
in the *setup file* whereas the object model (i.e. Teach engine) and
picking strategies are stored in the *product file*.

2.a Run a robot-camera calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first configuration step consists of the robot-camera calibration.
This calibration teaches Pick-it where the robot base is located w.r.t.
to the camera. This information is used to transform the object
pick-frames into robot coordinates. A detailed description in
robot-camera calibration can be
found \ `here <https://support.pickit3d.com/article/35-how-to-execute-robot-camera-calibration>`__. Do
not forget to save after the calibration is finished.

2.b Define the region of interest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The second step involves to define where Pick-it has to look for
objects. This is done by defining the blue box, or by its official term,
the region of interest (ROI). In total, there are three different
options to set the ROI:

#. By the ROI-markers.
#. By the interactive markers in the 3D-view.
#. By the automatic plane search button.

For this demo, we want the region of interest to coincide properly with
the bin or container. A typical approach here involves using the
markers. Note that height of the blue box should be chosen such that all
objects fit inside. The 3D-view will display all the points inside the
field of view, also shown in the picture below. A thoroughly explained
guide for setting up the region of interest can be
found \ `here <https://support.pickit3d.com/article/42-define-the-boundaries-of-your-application-with-the-roi-box>`__.

|image1|

After adjusting the region of interest, the result should look similar
to the Points-view depicted in the picture below. As reference, one
object is placed in the bin. Be sure again to save the settings when you
are done. Also do not forget to remove the markers.

|image2|

In case you want to use two bins similar to this example, you will have
to make another setup file for the right bin,
i.e. teach\_demo\_bin\_right.

.. raw:: html

   <div class="callout-yellow">

**Note** While setting the ROI-box, make sure to *exclude* points that
not belong to any objects. For example, any points from the bin.

.. raw:: html

   </div>

2.c Define the detection parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The third step consists in setting up the Pick-it Teach engine. The
Teach engine searches objects based on a predefined model. Therefore
does the first step consists in defining these models. Since both the
top and bottom side of our object are different, we will define two
object models by following these steps:

#. Isolate the object from the environment.
#. Adjust the ROI-box without saving.
#. Teach the model.

In the first step we will isolate the model physically from the
environment. The picture below depicts two objects presented to the
camera for teaching. The height difference from the bottom to the bin to
the object should be clearly visible. The physical isolation is simply
done by putting a smaller part under the object.

|image3|

The second step involves fitting the ROI-box around the model for
teaching. This is done in the Region of interest tab. The most
convenient method is to use the interactive markers in the 3D-view. For
the top model, the points-view should look like the picture below.

.. raw:: html

   <div class="callout-red">

**Warning** Do not save the local ROI-box for teaching objects since it
is only a temporarily method to teach the object models.

.. raw:: html

   </div>

|image4|

If the model is isolated properly we are ready for the third and final
step, i.e. teaching the model to the Pick-it Teach engine. Go to the
detection tab and define your model(s) drop-down menu, click on the Add
a model button. You can adjust the pick-frame simply by changing the
three translation and rotation parameters. For the other two parameters
choose:

-  **Matching tolerance:** 4 mm, which allows some tolerance on the
   model fit.
-  **Minimum matching score:** 75%, which allows that 25% of the model
   does not have to be visible, i.e. by parts overlapping parts in a
   bin.

Next, optimization of the scene pointcloud is done in the according
drop-down menu:

-  **Fusion:** None.
-  **Downsampling:** 1, 2 or 4 since we do not need all points for a
   proper fit. Check the difference in detection time.
-  **Detection speed:** Normal.

The taught model should look similar to the model in the picture below.

|image5|

When you taught the top model to Pick-it, you can simply add a second
model for the bottom side. You will have to go through the same steps
for a second model. A more thorough guideline about how to teach a model
to Pick-it can be
found \ `here <https://support.pickit3d.com/article/130-how-to-use-pick-it-teach-with-multiple-models>`__.

.. raw:: html

   <div class="callout-yellow">

**Note** The previously taught model is used as reference for the
objects to find. It is therefore important that these objects contain 3D
features. Required geometrical features are:

-  *Height differences* such as the two holes in this object.
-  *Distinctive circumferences* and their location w.r.t. each other,
   such as the conical sides.

If your object does not contain these features, it is maybe not a good
object for Pick-it Teach.

.. raw:: html

   </div>

.. raw:: html

   <div class="callout-red">

**Warning** The green bounding box in the model view must fit the object
model tightly. If this is not the case, undesired points of the
environment slipped into the model and you have to *re-teach* the model.

.. raw:: html

   </div>

2.d Define the picking parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The fourth and last step in setting up the Pick-it system is determining
a detection strategy. 

-  **Enforcements:** none.
-  **Collision prevention:** none. Since we are working with a bin, the
   collision prevention option could however be interesting. This goes
   however out of the scope of this simple demo setup. 
-  **Ordering strategy:** highest product center.

A more detailed description on picking strategies and collision can be
found in \ `this
article <https://support.pickit3d.com/article/54-picking-strategies>`__.

3. Program the robot
--------------------

Now Pick-it is configured, we have to program the robot. The robot
within this demo is a UR5 by Universal Robots. 

-  **The UR robot program:** Download
   link \ `here <https://drive.google.com/uc?export=download&id=1Nzqm_fDFosR59ZeQL8D-RrKCDCNLuytF>`__.

The following \ `landing
page <https://support.pickit3d.com/category/14-universal-robots>`__
contains useful information about using Pick-it with a cobot by
Universal Robots. You will find information about the Pick-it URCap,
writing a simple robot script (comparable to this one) and so on.

|image6|

.. raw:: html

   <div class="callout-yellow">

**Note** When performing random bin picking, *always* trigger a new
detection before picking the next object.

.. raw:: html

   </div>

.. raw:: html

   <div class="callout-red">

**Warning** When using the UR download program in the provided link,
*change the waypoints* to avoid moving the robot to unsafe positions.

.. raw:: html

   </div>

4. Happy picking!
-----------------

If you followed all steps above, you're ready building your Pick-it
product showcase using the Pattern detection engine. Happy picking!

Our support team is open to answer any question or issue that you
encountered while setting up this showcase. Send them an e-mail
at \ `support@pickit3d.com <mailto:mailto://support@pickit3d.com>`__

.. |image0| image:: https://d33v4339jhl8k0.cloudfront.net/docs/assets/583bf3f79033600698173725/images/5b4c9d180428631d7a88f042/file-UTq4Haukhq.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ae1c4b404286328a414941e/file-8vti7bdxIR.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ae1c4ed04286328a4149423/file-ZfS0AdvZ7u.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ae1c95a2c7d3a5063b4e677/file-eXxFZpGIS1.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ae1cb1b2c7d3a5063b4e68b/file-jo1rJB6UTT.png
.. |image5| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ae1cf742c7d3a5063b4e6a8/file-6r7nFUUHtG.png
.. |image6| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5aab8f9f2c7d3a56d887058d/file-jNMkd87wNw.png

