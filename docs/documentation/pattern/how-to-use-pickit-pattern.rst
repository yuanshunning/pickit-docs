How to use Pickit Pattern
-------------------------

Just like the Flex detection engine, the Pickit
Pattern detection engine has a typical workflow, which is described in
step by step in this article.

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Define the 3D scene
~~~~~~~~~~~~~~~~~~~

The first step of Pickit Pattern is to define where the Pickit system
should look. The 3D scene is defined by a Region of Interest and the
optimize detection parameters. These detection parameters are explained
in the article :ref:`Explaining-the-pattern-detection-parameters`.

In the image below an example of a good defined scene is shown. First,
in the 3D view all points within the field of view of the camera are
shown. Second, in the Points view only the points of the parts  are
shown. The table is filtered out. 

The information shown in the Points view is what will be transferred to
the next step. All other information is not taken into account for the
detection with Pickit Pattern.

.. image:: /assets/images/Documentation/Pattern-3d-points.gif

Divide the scene into clusters & reject (some) clusters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The next step in the Pickit Pattern detection is to divide the scene
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
article :ref:`Explaining-the-pattern-detection-parameters`.

Difference of clustering between Pattern and Flex
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the detection engine Flex it is important that each cluster
represents a different object, see :ref:`Flex`
for more information about the Flex engine. For the Pattern engine one
cluster can contain multiple objects, but the sides of the cluster needs
to be well defined. Because the Pattern engine will use these sides to
start fitting the objects from the sides on.  

.. image:: /assets/images/Documentation/Pattern-points-clusters.gif

Define dimension and orientation of objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this additional step the user defines the size and the orientation of
the objects in the scene. In following article all parameters on how
this can be defined are explained, :ref:`Explaining-the-pattern-detection-parameters`.

Fit & filter objects
~~~~~~~~~~~~~~~~~~~~

The final step of Pickit Pattern is to fit the defined fixed size shape
from the previous step. This fixed size shape is fitted from the sides
of the cluster on. Good fits can be send back to the robot one by one.

In the image below we see four good fits. In the top layer a single
object is fitted. In the bottom layer a shape is fitted in all four
corners. Once all these blocks are removed by the robot, a detection for
the last two blocks is possible. 

| In this last step it is decided which objects are accepted as good
  fits. These good fits can then be sent back to the robot. Filtering of
  the objects is done on their parameters shown in the :ref:`detection-grid`.
  An explanation of all these parameters can be found in the
  article :ref:`Explaining-the-pattern-detection-parameters`. 

.. image:: /assets/images/Documentation/Pattern-clusters-objects.gif