What is the Region of Interest?
===============================

The \ **Region of Interest box (ROI box)** is the 3D region where object
detection takes place. 

In many applications, the field of view of the Pickit camera is greater
than the region where we want to perform object detection. For example,
in a bin picking application we are only interested in the contents of
the bin. In the below image, we compare the camera field of view
(**3D** in the Pickit viewer), with the contents of the ROI box
(**Points** in the Pickit viewer).

.. image:: /assets/images/Documentation/Region-of-interest-example.png

By specifying a correct ROI box, we get \ **faster detection times**, as
Pickit doesn't have to look for objects where they are not expected. In
the above example, object detection with the shown ROI box is between
two and three times faster than on the entire scene.

The ROI box can also be used to \ **prevent unwanted detections**, for
example if two bins are visible to the camera, but we only want to pick
objects from one. Setting the ROI box around one of the bins will ignore
the contents of the other.

For \ **bin picking** applications, the ROI box can be used for \ **bin
representation**, by fitting it to the internal borders of the bin.
Pickit then can (optionally) perform bin collision avoidance and
prevention. Refer to the \ `How can I get a better bin picking
experience <https://support.pickit3d.com/article/81-how-can-i-get-a-better-bin-picking-experience>`__?
article for more information on how to make the best use of the ROI box
for such applications.

The ROI box can be defined and modified from the **Region of
Interest** page of the Pickit web interface, and the points contained
in it can be visualized in the **Points** tab of the viewer.