How to use Pickit Teach
========================

.. raw:: html

   <div>

This article describes how to get started with the Pickit Teach
engine, designed to detect complex 3D shapes. For details on the
individual detection parameters, please refer to the  `Explaining the
Teach detection
parameters <https://support.pickit3d.com/article/48-explaining-the-teach-detection-parameters>`__
article.

.. raw:: html

   </div>

Using Pickit Teach is an intuitive two-step process. First, you show
the part to the camera and store a model of it in the memory of the
processor. Second, this stored model is used to find similar parts in a
new scene.

The typical workflow when using the Teach engine is as follows:

#. `Teach a model based on your product <#chapter01>`__
#. `Detecting different parts in a new setup <#chapter02>`__

Teach a model based on your product
===================================

Initial steps
-------------

Mount the camera above a flat surface that is larger than the footprint
of the object that has to be taught. The optimal camera height is the
height that brings the top of the object to approximately 50-70 cm from
the camera. 

|image0|

It's useful to keep the 2D image view open so you have the most accurate
representation of what the camera sees.

Next, create a new setup file ‘MySetupForTeaching’ and a new product
file ‘MyModel’.

Isolating the part
------------------

Pickit stores a point cloud of the model which will be used to find
similar parts. So it is important that a good point cloud is stored as a
model. A good model contains lots of information on the part and no
information on things that don't belong to the part. Therefore it is
necessary to isolate the part from its surroundings. This is done by
using the \ `Region of Interest
box <https://support.pickit3d.com/article/42-define-the-boundaries-of-your-application-with-the-roi-box>`__
(ROI).

The ROI box is a hard filter which filters out all points lying outside
of this box. Normally, this box defines where Pickit looks for objects,
here, it is used to define which points belong to the model and which
don’t:

#. Go to the Region of Interest tab and define the Region of Interest
   box. 
#. Press the Detect button to take a snapshot in the newly defined
   Region of Interest.
#. Go to the Points view and verify the following:

   #. All parts of the object that are expected to be visible are
      covered by points. The top part might be missing e.g. because the
      top of the Region of Interest box is not high enough.
   #. There should be no other points than the ones belonging to the
      object. Wrong points might appear because the bottom of the Region
      of Interest box is not high enough or because your hand is
      accidentally in the Region of Interest box. 

.. raw:: html

   <div>

Before going to the next step, save the changes to your
‘MySetupForTeaching’ setup file by pressing the SAVE button at the
bottom of the Region of interest page. Note that the model is not yet
saved now.

.. raw:: html

   </div>

Teaching and verifying the model
--------------------------------

In this step, the actual model will be defined and saved. Make sure to
select Pickit Teach as the detection algorithm on the Detection page. 

#. On the **Detection** tab go to the Teach model step and press the
   Teach Model button.
#. In the Product model view, the new model is now displayed. 

   |image1|

#. Finally, you can save the changes to your ‘MyModel’ product file by
   pressing the Save button at the bottom of the Detection page. 

Note that always the full resolution model is saved. Hence, the
downsampling resolution, discussed in the next section, can still be
changed for a model that has been saved already.

Detecting different parts in a new setup
========================================

To start using the product model for actual picking, create a new setup
file ‘MySetup’ on the Configuration page. Next, define the Region of
Interest on the Region of Interest tab according to your scenario and
save it.

Testing different product scenarios
-----------------------------------

Before testing make sure that downsampling is set to none, both in the
Optimize 3D image and the Teach model page. 

#. | Place one object inside the region of interest box and press the
     Detect button.
   | One successfully detected object should appear in the Valid Matches
     view and the matching score should be close to 1.

   |image2|

#. Add a few more objects into the Region of Interest area and press the
   Detect button again. At least one successfully detected object should
   appear in the Valid Matches view and the matching score should still
   be close to 1.

   |image3|

#. Change the orientation of some of the objects into the Region of
   Interest area and press the Detect button again. At least one
   successfully detected object should appear in the Valid Matches view.
   Depending on how much the object orientation varies from the
   orientation at the moment of teaching the model, the matching score
   will be lower, since the number of model points overlapping with the
   scene reduces.\ |image4|
#. In case there is only one red failed fit (see below), but it does
   look like a good fit, you can reduce the minimal model coverage 3D on
   the Filter objects page.

**Note:** There is a hard limit on the Teach matching time of 5 seconds.
Before applying any downsampling, this limit is likely to be reached.
Optimizing the balance between computational speed and accuracy is
discussed in the next section.

Optimize detection time
-----------------------

.. raw:: html

   <div>

Depending on the model and the scenario, the detection time resulting in
a good balance between computational speed and accuracy can vary from
**1 to 5 seconds**. If you want to reduce the detection time, you can
look at downsampling both the model and the scene. 

.. raw:: html

   </div>

.. raw:: html

   <div>

A model providing a good balance between computational speed and
accuracy is about 500 to 1000 points large. If the size of the model is
too large, you have to increase the **Scene downsampling resolution** to
reduces the number of points in the model.

.. raw:: html

   </div>

.. raw:: html

   <div>

The effect of downsampling can be verified in the Product model view for
the model and in the Points view for the scene. 

.. raw:: html

   </div>

.. raw:: html

   <div>

|image5|

A typical value for the **Scene downsampling resolution** is smaller
than 5 mm. Some applications require detecting objects at different
depth ranges, like emptying a bin. Because the Pickit camera resolution
drops exponentially with the distance to the camera, scene downsampling
can be used to create a more uniform resolution over the whole depth
range required for covering the bin. If the resolution is uniform, also
the detection time and the resulting model scores will be uniform over
the depth range.

.. raw:: html

   </div>

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58dd1cdadd8c8e5c5730fc9b/file-TC9h5cgiX1.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58dd2162dd8c8e5c5730fce3/file-95YGNHNQWf.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58dd2184dd8c8e5c5730fce7/file-nw7IGWcj1N.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58dd219bdd8c8e5c5730fcea/file-G5p8YYpyXH.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58dd21badd8c8e5c5730fced/file-NumVMRY7Ai.png
.. |image5| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58dd22632c7d3a52b42f10ea/file-3YWO41zGNa.png

