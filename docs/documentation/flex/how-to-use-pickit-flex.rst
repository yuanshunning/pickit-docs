How to use Pickit Flex
=======================

This article describes how to get started with the Pickit Flex engine.
The Pickit Flex engine easily finds geometric shapes (cylinders, boxes,
planes, circles ... ) and can handle a variety of sizes with one
configuration. 

Working with Pickit Flex is all about clustering (grouping) of points.
The Pickit camera captures the scene and converts it into points with
depth information (point cloud). For Pickit Flex we need to split this
point cloud into several clusters (`step 3 <#step-3>`__), each cluster
is then used to match a geometrical shape on it (`step 4 <#step-4>`__).

The typical workflow when using the Flex engine is as following:

#. `Choose the vision engine <#step-1>`__
#. `Optimize the 3D image <#step-2>`__
#. `Group points into clusters <#step-3>`__
#. `Reject clusters <#step-4>`__
#. `Fit objects <#step-5>`__
#. `Invalidate objects <#step-6>`__

1. Choose vision engine
-----------------------

On the **Detection** page select **Pickit** **Flex** under the
Detection algorithm option.

2. Optimize the 3D image
------------------------

|image0|

Select the **Points** view, press the **Check** button and make sure
your objects are visible inside the blue ROI box. You can now configure
how many points used for object detection.

-  `Number of Images for
   Fusion <http://support.pickit3d.com/article/30-explaining-the-flex-detection-parameters#fusion>`__
-  `Scene downsampling
   resolution <http://support.pickit3d.com/article/30-explaining-the-flex-detection-parameters#downsampling>`__

` <http://support.pickit3d.com/article/30-explaining-the-flex-detection-parameters#downsampling>`__

|image1|

3. Group points into clusters
-----------------------------

|image2|

Select the **Clusters** view. Clustering points is a way of grouping
points belonging to individual objects. 

-  `No
   clustering <http://support.pickit3d.com/article/30-explaining-the-flex-detection-parameters#no-clustering>`__
   is combining all cloud points into a single cluster. This is mostly
   used with single objects, or to check if there is something to found
   within the blue ROI box.
-  `Distance-based
   clustering <http://support.pickit3d.com/article/30-explaining-the-flex-detection-parameters#distance-based-clustering>`__
   is ideal for clustering non-touching objects of simple geometrical
   shapes.
-  `Normal-based
   clustering <http://support.pickit3d.com/article/30-explaining-the-flex-detection-parameters#normal-based-clustering>`__
   is ideal for clustering touching objects of simple geometrical
   shapes.

Good clustering typically leads to one (or sometimes more) cluster(s)
per physical object under the camera.

4. Reject clusters
------------------

|image3|

Exclude clusters regarding on their size and dimensions. Good practices
for rejecting clusters are:

-  Remove very small clusters that will never allow a good match.
-  In case you have large objects; increase the minimum number of points
   in a cluster.

.. raw:: html

   <div class="callout-yellow">

**Note:** If you have \ **Cluster size in № of pts** set you have to
review your values after modifying the **downsampling** parameter.

.. raw:: html

   </div>

5. Fit objects
--------------

|image4|

|image5|

Define the kind of model you want to find in your cluster. Below we have
a list of typical applications for each object model:

-  **Square** and **rectangle**: cardboard packaging, plastic bags,
   industrial objects
-  **Circle** and \ **ellipse**: industrial rings, pipe ends, top of
   soda cans 
-  **Cylinder**: coke cans, tubes, bottles
-  **Sphere**: oranges, footballs
-  **Blob** is perfect for detecting objects that can be very well
   clustered but don't have a geometrical shape. Examples for these are
   vegetables and fruit (bananas, peppers ...) and special shaped boxes
   typically on a conveyor belt. 

6. Invalidate objects
---------------------

The `Pickit detection
grid <http://support.pickit3d.com/article/57-the-pick-it-detection-grid>`__
is a very helpful tool for improving the reliability of your detections.

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/598482e82c7d3a73488ba4d5/file-qxT6eTJ3eZ.gif
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/598819842c7d3a73488bad4b/file-pqO64ES658.gif
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/598836902c7d3a73488bae18/file-H6bBxgOw8h.gif
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/59883c172c7d3a73488bae43/file-4cLERIpKmZ.gif
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5988380f042863033a1bae8a/file-rCZWjFMDNx.gif
.. |image5| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/598839bf2c7d3a73488bae32/file-ACM2zMi4P6.gif

