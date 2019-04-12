Robot camera calibration with the URCap plugin
==============================================

This example program requires the  **Pickit URCap** plugin to be
installed in your robot.  For installation instructions of both the
URCap plugin and the example programs please refer to the \ `Getting
started with the Pickit
URCap <http://support.pickit3d.com/article/75-getting-started-with-the-pick-it-urcap>`__
article.

Before following these URCap specific instructions in this article, make
sure you first understand the process of executing a robot camera
calibration as explained on `How to execute robot camera
calibration <http://support.pickit3d.com/article/35-how-to-execute-robot-camera-calibration>`__.

`Download the URCap example calibration
programs <https://drive.google.com/uc?export=download&id=1d_mcLevOZXT94bPC0lga10F3cvCvLUAc>`__
and load them onto your UR controller.

Multi poses calibration
-----------------------

|image0|

The program starts by opening a pop-up message, informing that
multi-poses calibration will be carried out. Before running the program,
the user must have the **Calibration** page of the Pickit web interface
opened. If this is not the case, it is notified by a pop-up message.
Otherwise, the following sequence is repeated five times:

#. Moves the robot to a waypoint

   |image1|

   All  **``MoveJ``** commands are specified with respect to the **tool
   flange** (as opposed to the TCP).

   While teaching the waypoints, it is recommended to have the
   **Calibration** page opened in the Pickit interface, where the user
   can verify whether the calibration plate is visible.

#. The provided program serves as a template only, and the waypoints are
   not set. They must be taught by the user since they depend on the
   physical environment and location of the calibration plate. Guidance
   on how the five waypoints should be taught can be found in the
   article referenced above.

#. Sends Pickit a calibration request, through the command Find
   calibration plate

   |image2| In the Calibration page, the user can follow the progress of
   calibration. 

Single pose calibration
-----------------------

For single pose calibration, the program consists of one single
calibration request.

|image3|

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a552418042863193800bd1a/file-oSLKIuHQVj.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a5541c6042863193800be2c/file-ZFwTUbVWdk.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a5541f4042863193800be31/file-bU2ENzuzUl.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a552393042863193800bd17/file-kowaUXYWYU.png

