How to execute robot camera calibration with an ABB Yumi robot
==============================================================

When using Pick-it with the YuMi robot, the camera should be **fixed to
an independent structure**. A robot-mounted camera configuration is not
possible due to YuMi payload limitations. Although YuMi is a robot with
two-arms, robot-camera calibration only needs to be performed **for one
arm**. Just be mindful that your calibration program uses a tool frame
**attached to the arm holding the calibration plate**. 

**YuMi does not have a standard robot flange**, as most traditional
robots do for mounting equipment. Therefore only \ `the multi poses
calibration method with the camera fixed to an independent
structure <https://support.pickit3d.com/article/35-how-to-execute-robot-camera-calibration#multipose_fixed>`__
can to be used.

.. raw:: html

   <div>

The YuMi robot has a limited workspace for moving the calibration plate
around. Therefore, **a smaller L-shaped calibration plate needs to be
used**.

.. raw:: html

   </div>

.. raw:: html

   <div>

|image0|
Because it is very important that **this** **plate cannot move with
respect to the gripper**, during calibration \ `you should attach any
piece to the plate that can be grasped firmly by the fingers of your
YuMi gripper <#attach>`__.

.. raw:: html

   <div>

You are free to make holes in the calibration plate as long as they are
not touching the three QR markers.

.. raw:: html

   </div>

.. raw:: html

   <div>

If this is done, you can  `perform the multi poses
calibration <http://support.pickit3d.com/article/35-how-to-execute-robot-camera-calibration#multipose>`__
like with any other robot.

.. raw:: html

   </div>

.. rubric:: Example of attaching a grasping part to the L-shaped plate
   :name: attach

.. raw:: html

   <div>

|image1|

.. raw:: html

   </div>

.. raw:: html

   <div>

|image2|

.. raw:: html

   </div>

.. raw:: html

   </div>

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58bff93f2c7d3a576d35c6e2/file-Cv6a7f42pK.jpg
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58c6642e2c7d3a576d35e3cf/file-JIOpZOBNzp.jpg
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58c664402c7d3a576d35e3d1/file-NsK16II0hP.jpg

