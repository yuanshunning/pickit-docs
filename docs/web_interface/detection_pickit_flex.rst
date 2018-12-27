Detection: Pick-it Flex
=======================

-  `Define the 3D scene <#define>`__
-  `Divide the scene into clusters & reject (some) clusters <#divide>`__
-  `Fit & filter objects <#fit>`__

This article describes how to get started with the Pick-it Flex engine.
The Pick-it Flex engine easily finds geometric shapes (cylinders, boxes,
planes, circles ... ) and can handle a variety of sizes with one
configuration. In the image below an example of a Flex detection is
shown. The Pick-it Flex detection engine has a typical workflow, which
is described step by step in this article.

|image0|

Define the 3D scene
~~~~~~~~~~~~~~~~~~~

The first step of Pick-it Flex is to define where the Pick-it system
should look. The 3D scene is defined by a Region of Interest and the
optimize detection parameters. These detection parameters are explained
in the article  `Explaining the Flex detection
parameters <https://support.pickit3d.com/article/174-explaining-the-flex-detection-parameters>`__.

In the image below an example of a good defined scene is shown. First,
in the 3D view all points within the field of view of the camera are
shown. Second, in the Points view only the points of the parts in the
bin are shown. The table and the bin are filtered out. Also it can be
seen that the space in between points have gotten bigger in the second
view. 

The information shown in the Points view is what will be transferred to
the next step. All other information is not taken into account for the
detection with Pick-it Flex. 

|image1|

Divide the scene into clusters & reject (some) clusters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The next step in the Pick-it Flex detection is rather important. Here
the scene will be divided into different parts(clusters). Each cluster
contains all points that belong to one object in the scene. All clusters
are shown in a different color. 

In the image below the effect of clustering is visualized. The 3D scene
is now divided into 7 different clusters(all shown in a different
color). Also it can be noted that the Clusters view contains less points
than the Points view. This is due to the user defined settings that
certain clusters are rejected. In this case smaller clusters are
rejected(not visualized in the image below). It makes sense to reject
smaller clusters because they often represent noise or partially covered
objects. So these points are then excluded from the following step. 

For the Flex detection to work properly every object should be clustered
apart. A bad example would be one cluster(color) for 2 parts in the
scene. The Pick-it system supports different ways of clustering. All
methods are explained in the  `Explaining the Flex parameters
article <https://support.pickit3d.com/article/174-explaining-the-flex-detection-parameters>`__.

|image2|

Fit & filter objects
~~~~~~~~~~~~~~~~~~~~

The final step of Pick-it flex is to fit a certain geometric shape on
every cluster and to filter out the wrong objects. All accepted objects
can be send back to the robot one by one.

For each cluster that was accepted in the previous step now a shape is
fitted. In the image below we see that each cluster gives rise to a
object. Seven green cylinders and all points in the Region of Interest
are shown in the Objects view. 

In this last step it is decided which objects are accepted as good fits.
These good fits can then be sent back to the robot. Filtering of the
objects is done on their parameters shown in the  `detection
grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__.
An explanation of all these parameters can be found in the
article \ `Explaining the Flex detection
parameters <https://support.pickit3d.com/article/174-explaining-the-flex-detection-parameters>`__.

|image3|

Mentioned articles

What to read next

| ` <https://support.pickit3d.com/article/168-saving-a-snapshot-in-pick-it>`__\ `Explaining
  the Flex detection
  parameters <https://support.pickit3d.com/article/174-explaining-the-flex-detection-parameters>`__
| ` <https://support.pickit3d.com/article/41-attaching-the-roi-box-to-the-robot-base-for-binpicking-objects-from-a-big-bin>`__\ `Pick-it
  detection
  grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__

| `Region of
  Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
| `Detection:
  Pick-it Pattern <https://support.pickit3d.com/article/161-detection-pick-it-pattern>`__
| `Detection:
  Pick-it Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__
| `Picking <https://support.pickit3d.com/article/163-picking>`__

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b583cea2c7d3a03f89cf6f8/file-SIMuw9Wskm.gif
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b5841402c7d3a03f89cf73c/file-IRoavJLk8x.gif
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b5844022c7d3a03f89cf76f/file-d1p1za1ksH.gif
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b5843f10428631d7a8949b9/file-qXBaPoxPBJ.gif

