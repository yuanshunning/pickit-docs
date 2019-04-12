Detection: Pickit Teach
========================

-  `Teach a model based on your product <#teach_model>`__
-  `Detecting different parts in a new setup <#detecting>`__

This article describes how to get started with the Pickit Teach engine.
Pickit Teach is a detection engine in Pickit which can search for
objects based on a previously shown example object. It is primarily used
to find irregularly shaped objects that don't fit in one of the basic
shape categories, like cylinders, spheres, squares, rectangles, circles,
and ellipses.

Teach a model based on your product
-----------------------------------

Teaching a model of an object is the most important step when setting up
the Pickit Teach engine to detect your object. The model is the only
thing that is used by Pickit Teach to search for your objects in a
scene, so a better quality model results in better detections. A
high-quality model has the following characteristics:

#. It contains as many details of the object as possible,
#. ` <#place_object_under_camera>`__\ it contains only points that
   belong to the object itself and
#. ` <#isolate_object>`__\ it exactly matches the side of the object
   that you want to detect.

Continue reading to learn how to build a high-quality model.

Placing the object under the camera
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Place your object under the camera and try to put it as close as
possible to the camera to capture the most details while making sure
that the object is lying fully in the field of view of the camera. It's
useful to keep the 2D view open so you see what the camera sees.

|image0|

Isolating the object
~~~~~~~~~~~~~~~~~~~~

Before creating a model of the object, we need to isolate the part from
its surroundings to make sure that only points belonging to the object
are captured in the model. This is done by using the  `Region of
Interest
box <https://support.pickit3d.com/article/159-region-of-interest>`__
(ROI).

Go to the **Region of Interest** tab and modify the region of interest
box boundaries until only points that belong to your objects are inside
the ROI box. When you're done adapting the boundaries, you're ready to
go to the next step.

.. raw:: html

   <div>

.. rubric:: Adding a model
   :name: adding-a-model

In this step, the actual model will be taught and saved. Go to the
Detection tab and select the Pickit Teach engine. Open the ‘Define your
model(s)’ section. Here you will see a widget that allows adding models.

When no models are defined yet, there will be a text stating: “There are
no models currently defined”.

To add a new model, click the **Add a model** button. Before clicking
this button, make sure that the correct object side is oriented to the
camera and that you completed the previous steps. When a new model is
successfully defined, the viewer will open the **Model
tab** automatically and a **Model row** will be added to the models'
widget.

The **Model tab** shows a 3D visual representation of your model, a
model bounding box as a green dashed line and the Pick frame. Note the
number in round brackets in the Model view tab name, this is the model
ID.

.. rubric:: 
   :name: section

A Model row in the widget contains the following information: a model
ID, a number of points in a model and a set of model actions. See
the \ `model
actions <https://secure.helpscout.net/docs/583bfcdbc6979106d37373a0/article/5ace0fe22c7d3a0e9367368b/#model_actions>`__
section to see how they work.

.. rubric:: Adding multiple models
   :name: adding-multiple-models

We just learned how to teach and detect an object model using the
Pickit Teach detection engine. Now, we will extend this knowledge by
adding more models to your application. 

Using more than one model is useful when multiple parts are shown in one
scene, or even to detect multiple sides of one part. Think for example
about a bin picking scenario where objects can have any random
orientation with respect to the camera. 

Multiple Models works in the same way as the single model case: repeat
the steps in the previous sections for every new model that you want to
add. The maximum number of models that Pickit can search for in one
detection is eight. If you want more models, it’s required to make a new
product file in the Configuration tab.

See the article \ `Using the model ID in a robot
program <https://support.pickit3d.com/article/172-using-the-model-id-in-a-robot-program>`__
to learn how to use the detection of multiple models in a robot

.. rubric:: Detecting an object and optimize detections
   :name: detecting

Now that you've added your models, it's time to detect objects. 

Place your objects inside the region of interest box and press the
Detect button. On a successful detection, you will see in the 2D view
that a frame appears on the detected objects and yellow lines indicate
the bounding box. (For the yellow lines enable the "Show model box" in
the Viewer options.)

|image1|

.. raw:: html

   </div>

.. raw:: html

   <div>

In the Objects view, the point cloud models are visualized as a colored
cloud on top of the detected objects. When a detection failed because
for example a threshold parameter was exceeded, the model cloud will be
colored in red.

.. raw:: html

   </div>

.. raw:: html

   <div>

In the Objects table, you can see the detected object dimensions,
matching score and the Model ID that was found. Take a look at this
article to learn how to interpret the  `Detection
grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__.
|image2|

.. raw:: html

   </div>

.. raw:: html

   <div>

If you want to optimize your detections, the article  `Explaining the
Teach detection
parameters <https://support.pickit3d.com/article/173-explaining-the-teach-detection-parameters>`__
goes more in depth on the different parameters of Pickit Teach. We
advice you to experiment with different settings and multiple objects in
different settings(tilted, on top of each other,..)

.. raw:: html

   </div>

.. raw:: html

   <div class="callout-yellow">

**Note** There is a hard limit on the Teach matching time of 5 seconds.
Before applying any optimization, this limit is likely to be reached.

.. raw:: html

   </div>

Mentioned articles

What to read next

| `Explaining the Teach detection
  parameters <https://support.pickit3d.com/article/173-explaining-the-teach-detection-parameters>`__
| `Region of
  Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
| `Pickit detection
  grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__

| `Region of
  Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
| `Detection: Pickit
  Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
| `Detection:
  Pattern <https://support.pickit3d.com/article/161-detection-pick-it-pattern>`__
| `Picking <https://support.pickit3d.com/article/163-picking>`__

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58dd1cdadd8c8e5c5730fc9b/file-TC9h5cgiX1.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5adef38904286328a4147f8e/file-LT4t619UpG.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5adef3cc04286328a4147f91/file-9N8cSlPhV9.png

