Robot-camera calibration
========================

In this step we do a robot-camera calibration. In the previous chapter
we saw that the Pick-it system is able to detect parts in its field of
view. Now Pick-it needs to know where the robot is based so that it can
tell the robot where it needs to move to when an object is detected.
**If you skip this step, the robot will move to a very wrong location.**

Follow the steps below to do a robot-camera calibration:

-  Mount the robot-to-camera calibration plate to the flange of the
   robot. Make sure it is well fixed.
-  On the Pick-it interface open the 2D view and the camera(s) tab. In
   this tab select Stationary and Multi poses calibration.
-  On your robot open the example multi pose calibration file supplied
   by Pick-it
-  In this robot program define 5 different waypoints where the robot
   shows the robot-to-camera calibration plate to the camera.\ |image0|
-  Run the program on the robot.
-  In the Pick-it user interface go to the 3D view and if the updated
   position of the robot base matches the actual position of the robot
   base.
-  Press Save in the Pick-it user interface.
-  Robot-to-camera calibration plate can be dismounted from the robot.

.. raw:: html

   <div class="callout">

   More details about robot-camera calibration can be found in
the \ `Camera(s) <https://support.pickit3d.com/article/158-calibration>`__
article.

.. raw:: html

   </div>

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58b55d852c7d3a576d358fc5/file-y8piF579xc.jpg

