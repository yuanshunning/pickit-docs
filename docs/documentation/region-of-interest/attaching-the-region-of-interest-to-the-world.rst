Attaching the Region of Interest to the world
---------------------------------------------

Now that you know how to define and modify a ROI box, you need to decide
where it is attached to. The ROI box can be attached to either
the \ **camera** or the \ **robot base**. This distinction is meaningful
for robot-mounted camera scenarios:

Camera
~~~~~~

A ROI box attached to the **camera** moves relative to the robot base as
the robot end-effector (and camera) move.To define the ROI box,
a running connection between Pickit and the robot is not required.

|image7|

Robot base
~~~~~~~~~~

| A ROI box attached to the **robot base** remains stationary relative
  to the robot base as the robot end-effector (and camera) move. 
| This is the recommended attachment for camera-on-robot scenarios. To
  define the ROI box, a running connection between Pickit and the robot
  is **required**.

Refer to the \ `Attach the ROI Box to the robot base for picking objects
from a big
bin <https://support.pickit3d.com/article/41-attaching-the-roi-box-to-the-robot-base-for-binpicking-objects-from-a-big-bin>`__
article for an example application.

|image8|

.. |image7| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acc797704286307509242b1/file-zF0gwfhJ0N.png
.. |image8| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acc79492c7d3a0e93672c9f/file-z7XTnEif5D.png
