What is the Region of Interest?
===============================

The \ **Region of Interest box (ROI box)** is the 3D region where object
detection takes place. 

In many applications, the field of view of the Pick-it camera is greater
than the region where we want to perform object detection. For example,
in a bin picking application we are only interested in the contents of
the bin. In the below image, we compare the camera field of view
(**3D** in the Pick-it viewer), with the contents of the ROI box
(**Points** in the Pick-it viewer).

|image0|

By specifying a correct ROI box, we get \ **faster detection times**, as
Pick-it doesn't have to look for objects where they are not expected. In
the above example, object detection with the shown ROI box is between
two and three times faster than on the entire scene.

The ROI box can also be used to \ **prevent unwanted detections**, for
example if two bins are visible to the camera, but we only want to pick
objects from one. Setting the ROI box around one of the bins will ignore
the contents of the other.

For \ **bin picking** applications, the ROI box can be used for \ **bin
representation**, by fitting it to the internal borders of the bin.
Pick-it then can (optionally) perform bin collision avoidance and
prevention. Refer to the \ `How can I get a better bin picking
experience <https://support.pickit3d.com/article/81-how-can-i-get-a-better-bin-picking-experience>`__?
article for more information on how to make the best use of the ROI box
for such applications.

The ROI box can be defined and modified from the \ **Region of
Interest **\ page of the Pick-it web interface, and the points contained
in it can be visualized in the \ **Points** tab of the viewer.

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb66b22c7d3a0e93671fdc/file-ormnI6ZCCv.png
