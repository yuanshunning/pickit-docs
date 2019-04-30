.. _how-to-good-model:

How to teach a good model
=========================

When using Pickit :ref:`Teach` it is important to have a good model. 
This article goes more into depth on how to make sure that good models are taught to the system.

In this article following scene of simple part will be used to explain what is important to pay attention to when teaching a model.

.. image:: /assets/images/faq/how-to-good-model-2d.png

Lets start with showing the good model for this part. In the rest of the article typical mistakes when teaching a model will be discussed.

.. image:: /assets/images/faq/how-to-good-model-good.png

A high quality model has the following characteristics:

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Good 3D features of the object
------------------------------

The detection engine returns the position of parts that look similar to the taught shape.
So a good model for Pickit Teach is a model with many distinctive 3D features. 

For example in the image below only half a model is taught. 
Now this model is fitted twice on each part, because it fits perfectly on both sides.

.. image:: /assets/images/faq/how-to-good-model-half.png

One step further would be to really zoom in on a small part. 
In the image below the taught model is only a small part of the sides. 
This model doesn't have specific 3D features and fits in many places in the scene.

.. image:: /assets/images/faq/how-to-good-model-plane.png

.. note:: This can be expected behaviour for certain applications.

Clean(only points that belong to the object)
--------------------------------------------

When teaching the model it is important that only points that belong to the object are included. 
All other points of the suroundings should be filtered away by the region of interest-box before teaching the model. 
In the example below the region of interest-box was set to a too low value.
Now the ROI markers that are lying next to the part are taken into account as a part of the object.
So whenever a detection is triggered Pickit will look both for the part as for markers lying next to the part.
If these markers are missing in a new scene(which is quite likely) it will have a big effect on the matching score.

.. image:: /assets/images/faq/how-to-good-model-unclean.png

.. note:: The green bounding box around the model visualizes clearly if additional noise points are present in the taught model.
   See the difference between the good model in the beginning of the article and bad model shown here. A good model has a tight bounding box around itself.

It matches what you are looking for
-----------------------------------

In the final example the wrong side of the part was taught. This of course leads to bad detections. 
Before teaching models it is good practice to think about which side is most likely to be shown to the camera in your application.

.. image:: /assets/images/faq/how-to-good-model-wrong.png