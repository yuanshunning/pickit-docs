Explaining the Flex detection parameters
========================================

.. raw:: html

   <div>

The Pickit Flex vision engine is designed to detect basic geometric
shapes of different sizes, such as cylinders, rectangles, squares,
circles and more.

The parameters for Flex detection are split into five categories:

.. raw:: html

   </div>

#. `Group points into clusters <#group_clusters>`__
#. `Reject clusters <#reject_clusters>`__
#. `Fit objects to clusters <#fit_objects>`__
#. `Filter objects <#filter_objects>`__
#. `Optimize detections <#optimize_detections>`__

The process of detecting objects with the Flex vision engine is all
about step by step testing and fine-tuning parameters until you get a
good result. The parameters for Flex detection are split into five
categories.

Group points into clusters
--------------------------

These parameters affect the clustering (grouping) of points. Clustering
points is a way of grouping points belonging to individual objects. A
good way to detect multiple objects is to try and group points that
belong to the same object. The effect of modifying these parameters can
be visualized in the  **Clusters** view.

There are multiple clustering strategies available, and the choice
initially depends on whether your parts are 
**touching** or **non-touching**. 

-  For **touching parts**,the system looks at the change of surface. If
   a surface change is to abrupt it is considered as a separate cluster.
   An example where this clustering method is used is for touching
   cylinders. In the system a few preset configurations exist, and you
   should experiment with them to determine which works best with your
   parts.
-  For **non-touching parts**, you specify the **clustering distance
   threshold**, which represents the minimum distance to consider
   clusters as separate entities.

Pickit also allows the possibility of **not grouping points into
clusters** at all, and an **expert mode** which is intended mostly for
compatibility with older versions of Pickit. The expert-mode parameters
are such that higher values will typically result in less and/or bigger
clusters, while lower values result in more and/or smaller clusters.

See following article,  `Example: the clustering
methods <https://support.pickit3d.com/article/192-example-the-clustering-methods>`__, to
see examples and use cases for each clustering method.

Reject clusters
---------------

These parameters specify filters for rejecting clusters from object
detection. Clusters can be rejected by setting minimum and maximum
values for their **size in number of points**, or their **physical
size** (length, width and height). Clusters can also be rejected if they
touch the **Region of Interest (ROI) box limits** (top, bottom, and/or
sides).

Rejected clusters are not shown in the  **Clusters** tab of the viewer,
and their count is listed in the detection summary.

|image0|

Fit objects to clusters
-----------------------

These parameters determine the kind of object you want to find. The
effect of modifying them can be visualized in the 
**Objects** view. Below there is a list of all models and a typical
applications where they are used:

-  **Square **\ and \ **rectangle**: cardboard packaging, plastic bags,
   industrial objects
-  **Circle **\ and \ **ellipse**: industrial rings, pipe ends, top of
   soda cans 
-  **Cylinder**: coke cans, tubes, bottles
-  **Sphere**: oranges, footballs
-  **Blob **\ is perfect for detecting objects that can be very well
   clustered but don't have a geometrical shape. Examples for these are
   vegetables and fruit (bananas, peppers ...) and special shaped boxes
   typically on a conveyor belt. 

The image below shows that soda cans can be detected both as cylinders
or circles. Which model is found depends on which side of the is shown
to the camera.

|image1|

The **Object model** specifies the object's geometric shape. For **3D
object models** like cylinders and spheres, one can specify:

-  Whether **internal and/or external surfaces** are desired.
-  The **3D matching tolerance**, used to determine the points that
   confirm the objet model. 

|image2|

For **2D object models**, Pickit first finds flat regions and then
looks for the selected model within them (square, rectangle, circle or
ellipse). One can specify:

-  Whether the shape is solid or has an internal **hole**, like a ring.
-  Whether to look for the shape in the **outer-most contour** only or
   not. This is mostly relevant for ring-like shapes, which have
   internal and external contours.
-  The \ **3D matching tolerance**, used to determine the points that
   confirm flat regions.
-  The **2D matching tolerance**, used to determine the points that
   confirm the object model.

|image3|

Filter objects
--------------

These parameters specify filters for rejecting detected
objects. Rejected objects are shown in the  **Objects** view and in
the \ `detection
grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__
as invalid.

Similar to how we reject clusters, objects can be rejected by setting
minimum and maximum values for their  **size in number of points**, or
their \ **physical size** (length, width, diameter). Additionally,
objects can be rejected depending on the value of the different matching
scores, explained below.

2D contour score
~~~~~~~~~~~~~~~~

****\ This score only applies to 2D shapes and represents the percentage
of the\ ** 2D model contour** that is covered with points within the
**2D matching tolerance**.

|image4|

2D surface score
~~~~~~~~~~~~~~~~

This score only applies to 2D shapes, and represents the percentage of
the **2D shape surface** that is covered with points taking into account
the **2D and 3D matching tolerance**. 

|image5|

3D scene score
~~~~~~~~~~~~~~

This score applies to all shapes, and represents the percentage of the
**cluster surface** that confirms the \ **chosen object model**.

The example below is for **cylinders** (in yellow, shown from the side),
but this score can be given for every object shape.

.. raw:: html

   <div>

|image6|

.. raw:: html

   </div>

Optimize detections
-------------------

These parameters affect the number of points of the captured point cloud
used for object detection. The effect of modifying these parameters can
be visualized in the **Points** view.

Image fusion
~~~~~~~~~~~~

Image fusion is the combination of multiple camera captures into a
single image. Enabling image fusion can provide  **more detail** in
regions that show flickering in the 2D or 3D live streams. Flickering
typically occurs when working with **reflective materials**. There are
three possible fusion configurations: **None**, **Light fusion** and
**Heavy fusion**.

Image fusion can increase total detection time by up to half a second.
The recommended practice is to use None in the absence of flickering,
and try first Light fusion over Heavy fusion when flickering is
present. 

Scene downsampling resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div>

The downsampling resolution allows reducing the density of the point
cloud. This parameter has a big impact on detection time, and to a
lesser extent on detection accuracy. More points lead to higher
detection times and higher accuracy, fewer points to lower detection
times and lower accuracy.

.. raw:: html

   </div>

.. raw:: html

   <div>

In the illustration, you can see an example of setting the scene
downsampling parameter to 1 mm, 4 mm and 10 mm.

.. raw:: html

   </div>

.. raw:: html

   <div>

|image7|

.. raw:: html

   </div>

Mentioned articles

What to read next

| `Pickit detection
  grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__
| `Example: the clustering
  methods <https://support.pickit3d.com/article/192-example-the-clustering-methods>`__

| `Region of
  Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
| `Detection: Pickit
  Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
| `Detection:
  Pickit Pattern <https://support.pickit3d.com/article/161-detection-pick-it-pattern>`__
| `Detection:
  Pickit Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__
| `Picking <https://support.pickit3d.com/article/163-picking>`__

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a8d3bd104286305fbc9b172/file-ra6obvfgNo.png
.. |image1| image:: https://d33v4339jhl8k0.cloudfront.net/docs/assets/583bf3f79033600698173725/images/598839bf2c7d3a73488bae32/file-ACM2zMi4P6.gif
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a8ea3fe2c7d3a0806494520/file-09pPUAlpwi.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a8ea49404286305fbc9bf81/file-uAlPwdCfWv.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a8e98b72c7d3a08064944b1/file-ztsDnqL5cP.png
.. |image5| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a8e98da2c7d3a08064944b2/file-l1Q6bhAOaQ.png
.. |image6| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a8e99402c7d3a08064944b4/file-5Gvzj8MDlB.png
.. |image7| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58ee1e3edd8c8e5c5731532a/file-pKR4nQsEQv.png

