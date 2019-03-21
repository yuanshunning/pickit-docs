How to use Pick-it Teach with multiple models
=============================================

!This article describes how to get started with the Pick-it Teach
engine. Pick-it Teach is a detection engine in Pick-it which can search
for objects based on a previously shown example object. It is primarily
used to find irregularly shaped objects that don't fit in one of the
basic shape categories, like cylinders, spheres, squares, rectangles,
circles, and ellipses.

How to use Pick-it Teach engine in Pick-it?
===========================================

Using Pick-it Teach is an intuitive two-step process. First, you show
the part to the camera and store one or more models of it. Second, this
stored model is used to find similar parts in a new scene.

The typical workflow when using the Teach engine is as follows:

#. `Teach a model based on your product <#teach_model>`__
#. `Detecting different parts in a new setup <#detecting>`__

Teach a model based on your product
-----------------------------------

Teaching a model of an object is the most important step when setting up
the Pick-it Teach engine to detect your object. The model is the only
thing that is used by Pick-it to search for your objects in a scene, so
a better quality model results in better detections. A high-quality
model has the following characteristics:

#. `It contains as many details of the object as
   possible, <#place_object_under_camera>`__
#. ` <#place_object_under_camera>`__\ `it contains only points that
   belong to the object itself and <#isolate_object>`__
#. ` <#isolate_object>`__\ `it exactly matches the side of the object
   that you want to detect. <#teach_model>`__

Continue reading to learn how to build a high-quality model.

Place the object under the camera
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
box <https://support.pickit3d.com/article/42-define-the-boundaries-of-your-application-with-the-roi-box>`__
(ROI).

Go to the **Region of Interest** tab and modify the region of interest
box boundaries until only points that belong to your objects are inside
the ROI box. Remember that the Points view visualizes only points inside
the ROI. When you're done adapting the boundaries, you're ready to go to
the next step.

.. raw:: html

   <div>

.. rubric:: Adding a model
   :name: adding-a-model

In this step, the actual model will be taught and saved. Go to the
Detection tab and select the Pick-it Teach engine. Open the ‘Define your
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

A **Model row** in the widget contains the following information:
a model ID, a number of points in a model and a set of model actions.
See the \ `model actions <#model_actions>`__ section to see how they
work.

.. rubric:: Adding multiple models
   :name: adding-multiple-models

We just learned how to teach and detect an object model using the
Pick-it Teach detection engine. Now, we will extend this knowledge by
adding more models to your application. 

Using more than one model is useful when the objects in your application
are not always directed the same way to your camera. Think for example
about a bin picking scenario where objects can have any random
orientation with respect to the camera. However, Multiple Models is not
limited to a single object use case, it's possible to add models that
belong to multiple different objects as well.

Multiple Models works in the same way as the single model case: repeat
the steps in the previous sections for every new model that you want to
add. The maximum number of models that Pick-it can search for in one
detection is eight. If you want more models, it’s required to make a new
product file in the Configuration tab.

.. rubric:: Modifying a model
   :name: modifying-a-model

After a model was added, you can perform a set of actions to modify it.
Models can be removed in two ways, by

-  performing a model action and
-  setting model properties.

.. rubric:: ` <>`__\ Model actions
   :name: model-actions

Model actions can be performed by clicking on one of the buttons in the
Model actions column of a model row. There are three types of actions:

-  **Re-teach:** Capture a new point cloud for the model. The model
   number and \ `model properties <#model_properties>`__ will stay the
   same, but the model point cloud and a corresponding number of points
   will be updated with the cloud that is currently in the region of
   interest. Before clicking this button, make sure that the correct
   object side is oriented to the camera and that the region of interest
   only contains points that should belong to your model.
-  | **Delete:** Removes a complete model. The model row will be deleted
     and all related model properties are lost.

   WARNING: When deleting an object, the model ID's of the next objects
   will be deleted. Make sure that the number of your model still
   matches the number in your robot program (see `robot
   program <#robot_program>`__).

-  | **Enable/disable:** Toggles whether Pick-it will search for the
     model or not. This is a useful feature to compare the performance
     of two models of the same side of an object.

   WARNING: Be sure to remove the disabled models before saving your
   final configuration. This is required since the disabled models take
   up computational time.

.. rubric:: ` <>`__\ Model properties
   :name: model-properties

Model properties are the properties that are visible next to the models'
table widget. These properties belong to one model only: the currently
active model. To activate a specific model, you can click on a model
row. The name of the property indicates to which model it belongs.

-  **Model pick frame:** With this setting, you can change the Pick
   frame for each model by specifying a translational or rotational
   offset. For more info on the Pick frame, read.
-  **Model matching parameters:** Take a look at the following articles
   for an explanation on the `matching
   tolerance <https://support.pickit3d.com/article/48-explaining-the-teach-detection-parameters#position_tolerance>`__
   and `minimum matching
   score <https://support.pickit3d.com/article/48-explaining-the-teach-detection-parameters#minimum_3d_model_score>`__.

.. rubric:: Detecting an object and optimize detections
   :name: detecting-an-object-and-optimize-detections

Now that you've added your models, modified them to your needs and
adapted the Pick frame, it's time to try detecting an object. Before
starting, make sure that the **scene downsampling resolution** is set to
*None* in **Optimize detections**. 

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
article to learn how to interpret the  `Objects
table <https://support.pickit3d.com/article/57-the-pick-it-detection-grid>`__.
|image2|

.. raw:: html

   </div>

.. raw:: html

   <div>

Experiment more by triggering more detections, adding more objects,
tilting your objects or stacking them on top of each other. Tune the
minimum matching score and matching tolerance properties until all
detections work reliably.

.. raw:: html

   </div>

.. raw:: html

   <div>

NOTE: There is a hard limit on the Teach matching time of 5 seconds.
Before applying any downsampling, this limit is likely to be reached.
Optimizing the balance between computational speed and accuracy is
discussed in the next section.   

.. raw:: html

   </div>

.. raw:: html

   <div>

.. rubric:: Optimize detection times
   :name: optimize-detection-times

.. rubric:: Scene downsampling resolution
   :name: scene-downsampling-resolution

.. raw:: html

   <div>

Depending on the model and the scenario, the detection time resulting in
a good balance between computational speed and accuracy can vary from
0.5 to 5 seconds. If you want to reduce the detection time, you can look
at the **scene downsampling resolution**. 

.. raw:: html

   </div>

.. raw:: html

   <div>

A model providing a good balance between computational speed and
accuracy is about 500 to 1000 points large. If the size of the model is
too large, you have to increase the scene downsampling resolution to
reduce the number of points in the model. The scene and model are always
downsampled by the same amount.

.. raw:: html

   </div>

.. raw:: html

   <div>

The effect of downsampling can be verified in the Model view for the
model and in the Points view for the scene. 

.. raw:: html

   </div>

**Example scene downsampling resolution:**

-  Scene downsampling resolution None:\ |image3|

-  Scene downsampling resolution 4, the model looks more sparse than the
   one above:\ |image4|

A good value for the scene downsampling resolution depends on the
scenario:

-  Table-top picking: the sole purpose of downsampling the scene is to
   speed up the detection time.
-  Bin picking: the Pick-it camera resolution drops exponentially with
   the distance to the camera. Hence, the downsampling can be used to
   create a more uniform resolution over the whole depth range required
   for covering the bin. If the resolution is uniform, also the
   detection time and the resulting model coverages will be uniform over
   the depth range.

.. raw:: html

   </div>

`An in-depth explanation of the different parameters of Pick-it Teach is
explained in this
article. <https://support.pickit3d.com/article/48-explaining-the-teach-detection-parameters>`__

` <>`__\ Using the model ID in a robot program
----------------------------------------------

Sometimes it's desired to do a different action with a robot depending
on the ID of the detected model. Use cases are:

-  define how to grip an object based on the visible object side or
-  define how to drop off an object based on the visible object side.

Universal Robots with URCap
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A variable **pickit\_type** is available to use after using the Pick-it
URCap **Find object(s)** command\ **.
**\ This variable will represent the **detected model id**.

Universal Robots with non-URCap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When calling **pickit\_look\_for\_object()** in a robot program, an
object named **pickit\_object** will be available. Use the type property
of this object to get the **detected model id**. An example robot
program might look like this:

::

    pickit_look_for_object()
    if pickit_object_found()
      if (pickit_object.type == 1)
        // Use drop off position 2.
      elsif (pickit_object.type == 2)
       // Use drop off position 2.
      endif
    endif

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58dd1cdadd8c8e5c5730fc9b/file-TC9h5cgiX1.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5adef38904286328a4147f8e/file-LT4t619UpG.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5adef3cc04286328a4147f91/file-9N8cSlPhV9.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acf5ec5042863075092587c/file-us0ku6xJcs.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acf5ed4042863075092587e/file-ClV3FmkGpu.png

