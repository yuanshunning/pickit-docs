Defining the tool center point (TCP) on a Universal Robot
=========================================================

When using a robot it is very important to define the tool center point
(TCP) exactly in the way you are using it in your application.

The TCP is defined by the exact translational and rotational difference
between the robot flange frame and the tip of the end effector (e.g. a
two finger gripper, a vacuum cup, a welding tool, ...).

Example
-------

|image0|\ In this example there is a translation of 220 mm along the
X-axis between the robot flange and the tip of the end effector and no
translation along the Y and Z axes because the end effector in exactly
below the center of the robot flange. All rotations can be set to 0
because the end effector is round and does not have a clear direction.

On a Universal Robot the TCP needs to defined in the screen as shown
below. Make sure to input the measured values of your own end effector.

|image1|

If robot camera calibration was performed succesfully and TCP was
defined in the right way a pick result should look like the pick in the
green frame. If the TCP was not set in the right way a pick could look
like the pick in the red frame.

|image2|

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58d928e3dd8c8e5c5730e1f1/file-eL29hVd1Hh.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58d924a12c7d3a52b42ef452/file-7dn76kwbAo.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58d92c892c7d3a52b42ef4d1/file-38XZbCZYiN.png

