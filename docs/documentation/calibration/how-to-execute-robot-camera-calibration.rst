.. _robot-camera-calibration:

Robot camera calibration
========================

Robot camera calibration is the process where the camera and the robot
learn their relative position towards each other. If done correctly, the
camera can guide the robot to correct positions in the physical
environment. 

Once the camera and robot are mounted, calibration can be done. This
process only needs to be repeated if the the camera is moved relative
to the robot, or visa versa. Pick-it provides two methods of executing
this calibration. Which method to choose depends on how Pick-it is set up
and how it will be used.

If the Pick-it **camera is fixed to an independent structure**, \ `multi
poses <#multipose_fixed>`__ and \ `single pose <#singlepose>`__
calibration can be used \ `depending on the setup <#singlepose>`__.

If the Pick-it  **camera is mounted on the robot**, only `multi
poses <#multipose_mounted>`__ calibration can be used.

The first step in the calibration process are:

#. Selecting the camera mounting type for your application
#. Choosing calibration method

.. warning::
  Wrong or old calibration parameters can lead to unexpected
  motions. Safe motions of the robot must always be checked by the
  operator of the robot itself and can never be guaranteed by Pick-it.

Multi poses calibration
-----------------------

.. _calibration-multi-pose-fixed:

Camera fixed to an independent structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image0|

Clamp the calibration plate to the robot flange or end-effector in
whatever way you can but always make sure the plate  **is rigidly
attached to the flange during the calibration process**. You
can :ref:`attach it to the robot flange <calibration-plate-mounting-on-robot>`,
grab it firmly with a gripper, screw it to a tool or any other way that
it is firmly attached to the robot flange or end-effector.

Find five robot poses that are sufficiently different and that still
allow the camera to see the calibration plate.

|image1|

Next step: `Calculate multi poses calibration <#multipose_calculate>`__

Camera mounted on the robot
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image2|

Place the calibration plate in front of the robot in the center of the
region for picking. Make sure the plate cannot move during the
calibration process. 

Find 5 robot poses (Top, North, East, South, West) that are sufficiently
different and that still allows the camera to see the calibration plate.
Preferably, the calibration plate is as much as possible in the center
of the region where the actual picking will take place. 

|image3|

Next step: `Calculate multi poses calibration <#multipose_calculate>`__

Calculate multi poses calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to the **Calibration** tab in the Pick-it web interface and select
**Multi Poses Calibration**.

Now repeat the following cycle for every pose:  

#. Move the robot to the first pose for calibration.
#. At this point, a request for calibration should be sent.

This request should be sent from the robot using the provided
calibration program. This program can be found under the  **Files** tab
of the Pick-it web interface or under :ref:`robot-integrations`.

After each successful collection of such a pair of transformations, the
interface looks as follows:

|image4|

When this cycle has been done for the 5 poses, click the **Save**
button. 

At the end of the calibration process, all indicators should have a
checkmark. If they do not, consult the log window for instructions.

If something went wrong in the middle of the calibration process, you
can always restart from the beginning by pressing the **Reset
poses** button.

.. note::
  Always  `verify the calibration <#verify>`__ in the 3D view as
  shown below. 

Single pose calibration
-----------------------

Some restrictive conditions on using single pose calibration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Single pose calibration can only be executed when **the camera is not
   mounted on the robot**.
#. Single pose calibration can only be executed **on robots with a
   certain type of flanges**, namely with 50 mm (ISO 9409-1-50-4-M6) and
   31 mm (ISO 9409-1-31.5-4-M5) wide flanges.
#. The calibration plate has to be mounted in a way **the position and
   orientation of the calibration plate** with respect to the robot
   flange \ **is exactly known** and later configured in the Pick-it
   system.

If one of these conditions can not be met, you will need to perform
calibration with `multi poses calibration <#multipose>`__.

Step 1: Install calibration plate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Go to the **Calibration** tab of the Pick-it user interface and
select \ **Single pose calibration**.

Mount the calibration plate to the robot flange directly or by making
use of a tool changer of your choice. Read more on :ref:`Installing the
Pick-it calibration plate on a robot flange or tool
changer <calibration-plate-mounting>`. 

| Position the robot such that the calibration plate can be seen by the
  camera (the “Plate visible” indicator should be green).
| *Preferably, the calibration plate is as much as possible in the
  center of the region where the actual picking will take place. *

.. rubric:: Step 2: Define helper transformation
   :name: helper_transformation

The **helper transformation** is the transformation between the flange
frame of the robot and the calibration plate frame. On the figure below
you can see the defined calibration plate frame. 

|calibration -plate -pickit.jpg|

The helper transformation from the robot flange to the calibration plate
results from the following possible motions: 

#. a possible rotation around the Z-axes
#. a possible translation along Z-axes

|image6|

If the calibration plate is mounted directly to the robot flange, the
translation will always be 0. If something (a tool, a tool changer, ...)
is in between the calibration plate and the robot flange the translation
will not be 0.

All robot brands and types can have varying helper transformations but
here you can find some examples for the case that the calibration plate
is mounted directly to the robot flange:

-  **Universal Robots:** UR3, UR5 and UR10: translation: 0 \| rotation:
   45°
-  **Fanuc:** LR Mate: translation: 0 \| rotation: 135°
-  **KUKA:** KR16: translation: 0 \| rotation: -45°
-  **Staubli:** 0 \| 135°
-  **ABB:** 0 \| -45°
-  **Yaskawa:** 0 \| -45°

Step 3: Send a calibration request from the robot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At this point, a request for calibration should be sent.

This request should be sent from the robot using the provided
calibration program. This program can be found under the **Files** tab
of the Pick-it web interface or on \ `this page about all supported
robot
programs <http://support.pickit3d.com/article/36-pick-it-robot-programs>`__.

Once Pick-it receives the request for calibration from the robot the
robot-camera calibration is calculated. 

**At the end of a successful calibration, all indicators should be
green.** If they do not turn green, consult the log window for
instructions.

|image7|

.. note::
  Always  `verify the calibration <#verify>`__ in the 3D view as
  shown below. 

Verify calibration
==================

Verify the result of the calibration in the 3D view, by looking at the
robot\_base frame and the camera frame locations and their relative
positions. It is recommended to have a look from different viewpoints
to verify that the position and orientation of the robot\_base frame
look correct.

|image8|

|image9|

**SAVE** the new calibration to the current setup file when it looks
correct. Redo calibration if the result does not look correct.

At this point, calibration is done!

The calibration parameters are stored on the Pick-it processor.
Recalibration is only required when the camera is moved or rotated with
respect to the robot. 

Universal Robots
^^^^^^^^^^^^^^^^

If you have a Universal Robots robot, you can additionally visualize a
**virtual 3D robot**, which should make it easier to verify the
correctness of calibration. To do so, follow these steps:

-  Make sure **Pick-it is communicating with the robot**: a Pick-it
   robot program is running and the Robot status indicator at the top of
   the web interface shows a checkmark.\ |image10|
-  Navigate to the **3D view** and click on the **View settings** button
   on the lower right of the viewport.
   |image11|
-  Toggle the **visualize Robot** check mark.
   |image12|

This allows you to intuitively check whether the virtual 3D robot aligns
well with the displayed coordinate frames and captured point cloud. For
example, the following images show a fixed-camera scenario where the
robot is inside the camera view volume. It can be seen how, before
calibration, the robot as seen by the camera does not align with the
virtual 3D robot. After calibration they nicely align. Similarly, the
attached calibration plate (only visible to the camera, not part of the
virtual 3D robot) is correctly aligned with respect to the robot flange
after calibration.

|image13|

|image14|

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58b5590e2c7d3a576d358fb7/file-4pGHdngvBb.jpg
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58b55d852c7d3a576d358fc5/file-y8piF579xc.jpg
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58b55e0e2c7d3a576d358fca/file-E6T17abZCA.jpg
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58b55f7bdd8c8e56bfa810b2/file-yQohfFwFHv.jpg
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a623ae50428632faf61fc14/file-lqVDjp9E8U.png
.. |calibration -plate -pickit.jpg| image:: https://lh6.googleusercontent.com/OBUGYacD05jH4tO9CU6NjT2AWeKpY2CDrB3N6CCpG5plOFv82K3FjUu-l4X-obYuNFRdqbuD7iiBvWvW3nB0QmJiXrsL03e4cLNXTnNllMMwOQ7DwirIzurRbe2HNzI7CnPRhfin
   :width: 311px
   :height: 241px
.. |image6| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58da70fe2c7d3a52b42efd31/file-nAve9RcsKK.png
.. |image7| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a623b2d2c7d3a39e6262dcb/file-GJrWXDdb7k.png
.. |image8| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58a5aa442c7d3a576d353c8b/file-xN5T0VmSzt.png
.. |image9| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58a5aa5cdd8c8e56bfa7bf4d/file-4aqLj3TUUh.png
.. |image10| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a7ac4310428634376cfe3bd/file-SaoIbgAuTx.png
.. |image11| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a7ac4b62c7d3a4a4198e289/file-dbT24C3XPt.png
.. |image12| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a7ac4fa0428634376cfe3c1/file-LgkGLHjkFB.png
.. |image13| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a7ac7fe2c7d3a4a4198e2ae/file-24lkku3k3I.png
.. |image14| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a7ac8340428634376cfe3e4/file-9BDGkvL7UB.png

