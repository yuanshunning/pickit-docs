Detection: Pick-it Pattern
==========================

-  `Define the 3D scene <#scene>`__
-  ` <#scene>`__\ `Divide the scene into clusters & reject (some)
   clusters <#clusters>`__
-  `Define dimensions and orientation of objects <#dimensions>`__
-  `Fit & filter objects <#fit>`__

This article describes how to get started with the Pick-it Pattern
engine. The Pick-it Pattern engine is similar towards the Flex detection
engine. Pattern looks for predefined sized objects(boxes, planes,
circles,..).  This allows the Pattern detection engine to solve
applications beyond the limits of the Flex detection engine. The example
that is being used in this article is one of touching aluminum blocks,
see image below. Just like the Flex detection engine, the Pick-it
Pattern detection engine has a typical workflow, which is described in
step by step in this article.

|image0|

Define the 3D scene
~~~~~~~~~~~~~~~~~~~

The first step of Pick-it Pattern is to define where the Pick-it system
should look. The 3D scene is defined by a Region of Interest and the
optimize detection parameters. These detection parameters are explained
in the article  `Explaining the Pattern detection
parameters <https://support.pickit3d.com/article/175-explaining-the-pattern-detection-parameters>`__.

In the image below an example of a good defined scene is shown. First,
in the 3D view all points within the field of view of the camera are
shown. Second, in the Points view only the points of the parts  are
shown. The table is filtered out. 

The information shown in the Points view is what will be transferred to
the next step. All other information is not taken into account for the
detection with Pick-it Pattern.

|image1|

Divide the scene into clusters & reject (some) clusters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The next step in the Pick-it Pattern detection is to divide the scene
into smaller different parts(clusters). Each cluster contains all points
of one layer in the scene. All clusters are shown in a different color.

In the image below the effect of clustering is visualized. The 3D scene
is now divided into 2 different clusters(shown in different colors). In
this step also the rejecting of clusters can be applied. For instance
one of the two planes could be rejected based on the size or dimensions
of the plane. But in this example this is not necessary so no rejecting
is done.

As you can see in the image of the clusters view, there are now thick
points on the side of the clusters. These are contour points and these
need to be well defined for a proper Pattern detection. Parameters that
have an influence on these contour points are explained in following
article  `Explaining the Pattern detection
parameters <https://support.pickit3d.com/article/175-explaining-the-pattern-detection-parameters>`__.

Difference of clustering between Pattern and Flex
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the detection engine Flex it is important that each cluster
represents a different object, see  `Detection: Pick-it
Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
for more information about the Flex engine. For the Pattern engine one
cluster can contain multiple objects, but the sides of the cluster needs
to be well defined. Because the Pattern engine will use these sides to
start fitting the objects from the sides on.  

|image2|

Define dimension and orientation of objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this additional step the user defines the size and the orientation of
the objects in the scene. In following article all parameters on how
this can be defined are explained,  `Explaining the Pattern detection
engine <https://support.pickit3d.com/article/175-explaining-the-pattern-detection-parameters>`__.

Fit & filter objects
~~~~~~~~~~~~~~~~~~~~

The final step of Pick-it Pattern is to fit the defined fixed size shape
from the previous step. This fixed size shape is fitted from the sides
of the cluster on. Good fits can be send back to the robot one by one.

In the image below we see four good fits. In the top layer a single
object is fitted. In the bottom layer a shape is fitted in all four
corners. Once all these blocks are removed by the robot, a detection for
the last two blocks is possible. 

| In this last step it is decided which objects are accepted as good
  fits. These good fits can then be sent back to the robot. Filtering of
  the objects is done on their parameters shown in the  `detection
  grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__.
  An explanation of all these parameters can be found in the
  article \ `Explaining the Pattern detection
  parameters <https://support.pickit3d.com/article/175-explaining-the-pattern-detection-parameters>`__. 
| |image3|

Mentioned articles

What to read next

| `Explaining the Pattern detection
  parameters <https://support.pickit3d.com/article/175-explaining-the-pattern-detection-parameters>`__
| `Detection: Pick-it
  Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
| `Pick-it detection
  grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__

| `Region of
  Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
| `Detection: Pick-it
  Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
| `Detection:
  Pick-it Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__
| `Picking <https://support.pickit3d.com/article/163-picking>`__

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b5ae4eb2c7d3a03f89d0fc1/file-5MYwaY9b55.gif
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b5ae5b60428631d7a896110/file-QKCmLDvFcx.gif
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b5aedeb2c7d3a03f89d100b/file-C6xgZoodom.gif
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b5b03990428631d7a8961b4/file-ontkaSthIq.gif

