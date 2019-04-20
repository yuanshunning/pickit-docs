.. _detect-empty-roi:

How to detect an empty ROI
==========================

In this article, you will learn a strategy when Pickit no longer 
detects  objects that allows discriminating between an empty Region of
Interest (ROI) from a ROI that still contains parts that are either
undetected or of a different type than what Pickit is looking for.

These are the steps to follow:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Create a new product file
-------------------------

In the **Configuration** section create a new product file (e.g.
**empty_roi**).

Adjust the detection settings
-----------------------------

Navigate to the  **Detection** page and input the following settings:

-  Detection engine: **Flex**.
-  Group points into clusters: **No clustering**.
-  Reject clusters by cluster size: **Min 200 points**.
   Adjust this number in relation to your part size, as described below
   in :ref:`define-the-minimum-number-of-points`.
-  Fit objects to clusters: **Blob**.

If you run object detection with this product file and Pickit finds
zero objects, the ROI is empty; otherwise, it still has contents inside.

.. _define-the-minimum-number-of-points:

Define the minimum number of points
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Note:: Make sure that your ROI is empty when no objects are present.
   This is especially relevant when the ROI models the inner side of a bin.
   No points belonging to the sides or bottom of the bin should be visible
   in the **Points view** when an empty bin is presented to the camera. 

The following is a strategy for determining the minimum number of points
needed to discriminate if the ROI is empty or not. Generally speaking,
this number should be lower for smaller parts and larger for bigger
parts.

Make sure the product file created above is selected and navigate to
the  **Detection** page and input the following settings:

#. Reject clusters by cluster size: **Min 10 points**.
#. Remove all parts from the ROI.
#. Run object detection. If there are detections, check the number
   of points of the detected blob. If the ROI is truly empty, you should
   get zero detections (zero points).
#. Add one part to the ROI in a position that faces the camera from its
   smallest side (i.e. least visible points).
#. Run object detection and check the number of points of the detected
   part.
#. The minimum number of points should a number between the result of
   steps 3 and 5.

Modify your robot program
-------------------------

If running Pickit object detection with the product file meant to
detect your parts returns zero matches, we can check for an empty ROI:

-  Optional: Retry object detection a few times to confirm that no parts
   are found
-  Switch to the **empty_roi** product and trigger object detection.

   -  If no objects are found, **the ROI is empty**.
   -  If objects are found, **the ROI is not empty** and contains
      undetected parts or parts of a different type than what Pickit
      was looking for.
