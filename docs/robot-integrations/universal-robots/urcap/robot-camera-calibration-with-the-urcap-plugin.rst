.. _universal-robots-urcap-calibration:

Robot camera calibration
========================

This example program requires the **Pickit URCap** plugin to be installed in your robot.  For installation instructions of both the URCap plugin and the example programs please refer to the :ref:`universal-robots-urcap-installation` article.

Before following these URCap specific instructions in this article, make sure you first understand the process of executing a robot camera calibration as explained on :ref:`robot-camera-calibration`.

`Download the URCap example calibration programs <https://drive.google.com/uc?export=download id=1d_mcLevOZXT94bPC0lga10F3cvCvLUAc>`__ and load them onto your UR controller.

Multi poses calibration
-----------------------

.. image:: /assets/images/robot-integrations/ur/urcap-calibration-1.png

The program starts by opening a pop-up message, informing that multi-poses calibration will be carried out. Before running the program, the user must have the **Calibration** page of the Pickit web interface opened. If this is not the case, it is notified by a pop-up message. Otherwise, the following sequence is repeated five times:

#. Moves the robot to a waypoint

   .. image:: /assets/images/robot-integrations/ur/urcap-calibration-2.png

   All ``MoveJ`` commands are specified with respect to the **tool flange** (as opposed to the TCP).

   While teaching the waypoints, it is recommended to have the **Calibration** page opened in the Pickit interface, where the user can verify whether the calibration plate is visible.

#. The provided program serves as a template only, and the waypoints are not set. They must be taught by the user since they depend on the physical environment and location of the calibration plate. Guidance on how the five waypoints should be taught can be found in the article referenced above.

#. Sends Pickit a calibration request, through the command `Find calibration plate`

   .. image:: /assets/images/robot-integrations/ur/urcap-calibration-3.png
   

In the Calibration page, the user can follow the progress of calibration. 

Single pose calibration
-----------------------

For single pose calibration, the program consists of one single calibration request.

.. image:: /assets/images/robot-integrations/ur/urcap-calibration-4.png
