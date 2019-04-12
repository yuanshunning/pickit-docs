How can I get a better bin picking experience?
==============================================

This article covers a number of tips and tricks for improving the **bin
picking** experience with Pickit. Some of the tips are specific to
Pickit, while others relate to your hardware setup.

-  Use the ROI box to \ `represent the
   bin <http://support.pickit3d.com/article/42-define-the-boundaries-of-your-application-with-the-roi-box#representation>`__.
   |image0|
-  If picking from a **big bin**, consider using a **robot-mounted
   camera** and \ `attach the ROI box to the robot
   base <http://support.pickit3d.com/article/41-attaching-the-roi-box-to-the-robot-base-for-binpicking-objects-from-a-big-bin>`__.
   A big bin is one whose volume is larger than the camera field of
   view, e.g. very wide, or very deep.
-  When emptying **deep bins** with a robot-mounted camera, **move the
   camera capture pose down** as the bin empties. Keeping the distance
   between camera and objects relatively short produces higher quality
   image captures.
   |image1|
-  In bin picking, each Pickit detection request typically yields
   multiple objects. Select an **object ordering strategy** that places
   higher objects first. In general prefer highest product center over
   highest product part. In the image below object 1 will be picked
   before object 2.
   |image2|
-  Enable \ `collision
   prevention <http://support.pickit3d.com/article/54-picking-strategies-and-collision-prevention-with-pick-it-flex#collision_prevention>`__
   between tool and bin, and between tool and other objects in the bin.
   |image3|
-  Enforce \ `pick frame
   constraints <http://support.pickit3d.com/article/54-picking-strategies-and-collision-prevention-with-pick-it-flex#pick_frame>`__
   to constrain the approach direction and orientation. When enforcing
   alignment constraints it's useful to enable the \ `bin avoidance
   strategy <http://support.pickit3d.com/article/54-picking-strategies-and-collision-prevention-with-pick-it-flex#bin_avoidance>`__
   to improve reachability of objects close to the bin borders.
-  Consider adding an \ `empty bin
   check <http://support.pickit3d.com/article/62-how-to-detect-an-empty-roi>`__
   when no more detections are found.
-  Not related to Pickit but to bin picking in general, use a **slender
   tool** **that is as long as the bin depth**. Leaving bulky parts of
   the tool and the robot outside of the bin at all times greatly
   improves object reachability. This is not always a feasible
   alternative due to application constraints, so it's a good idea to
   consider in early stages of application development.
   |image4|

To conclude, you can take a look at some real bin picking scenarios with
Pickit on the  `videos section of our
website <https://www.pickit3d.com/videos/category/bin-picking>`__.

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a6b6d772c7d3a39e6266646/file-9CnfgLZD2B.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a6b70732c7d3a39e626665b/file-DtNcFSjVCA.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a6b62dd0428632faf623647/file-IwoyjwcCsn.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a6b68fa0428632faf623686/file-1ISsjXN3jE.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a6b6c332c7d3a39e6266633/file-XD5vqS7Q3U.png

