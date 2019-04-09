Robot-camera calibration
========================

In this step we do a robot-camera calibration. In the previous chapter
we saw that the Pick-it system is able to detect parts in its field of
view. Now Pick-it needs to know where the robot is based so that it can
tell the robot where it needs to move to when an object is detected.
**If you skip this step, the robot will move to a wrong location.**

Follow the steps below to do a robot-camera calibration:

-  Mount the robot-to-camera calibration plate to the flange of the
   robot. Make sure it is well fixed.
-  On the Pick-it interface open the 2D view and the camera(s) tab. In
   this tab select Stationary and Multi poses calibration.
-  On your robot open the example multi pose calibration file supplied
   by Pick-it
-  In this robot program define 5 different waypoints where the robot
   shows the robot-to-camera calibration plate to the camera.\ 
.. image:: /assets/images/First-steps/Robot-camera-calibration.jpg
-  Run the program on the robot.
-  In the Pick-it user interface go to the 3D view and if the updated
   position of the robot base matches the actual position of the robot
   base.
-  Press Save in the Pick-it user interface.
-  Robot-to-camera calibration plate can be dismounted from the robot.

.. tip:: More details about robot-camera calibration can be found in
   the :ref:`calibration` article.