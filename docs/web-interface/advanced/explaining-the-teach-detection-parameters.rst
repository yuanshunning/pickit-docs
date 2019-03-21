Explaining the Teach detection parameters
=========================================

.. raw:: html

   <div>

The Pick-it Teach vision engine is designed to detect complex
3D shapes. This article explains its detection parameters. For details
on how to use Pick-it Teach, please refer to the  `How to use Pick-it
Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__
article.

.. raw:: html

   </div>

-  `Define your model(s) <#define>`__

   -  ` <#define>`__\ `Select, re-teach, delete or add
      model <#select>`__
   -  ` <#select>`__\ `Pick frame <#frame>`__
   -  ` <#frame>`__\ `Matching tolerance <#tolerance>`__
   -  ` <#tolerance>`__\ `Minimum matching score <#score>`__

-  `Optimize detections <#optimize>`__

   -  `Image fusion <#fusion>`__
   -  `Scene downsampling resolution <#downsampling>`__
   -  `Detection speed <#speed>`__
   -  `Detection precision <#precision>`__
   -  `Application type <#application-type>`__

Define your model(s)
--------------------

Select, re-teach, delete or add model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image0|\ A list of thaught models is shown accompanied by their ID and
the number of points.By default, there are no models defined.

Add a model
^^^^^^^^^^^

Press the **Add a model** button to add your first model, the points
currently visible within the ROI are now saved into a model. When the
model is successfully created, the model will automatically be shown in
the **Model** view.

Re-teach a model
^^^^^^^^^^^^^^^^

| You can always reteach a model by pressing the **re-teach button** for
  a specific model.
| By pressing this button, the points currently visible within the ROI
  are saved into the model.

**Warning** When re-teaching a specific model, all data the point-cloud
data from the previous model is overwritten. This action cannot be
undone.

Delete a model
^^^^^^^^^^^^^^

| To delete a model, press the delete button for the specific model.
| The action needs to be confirmed in deletion popup.

**Warning** Model ID's will be reassigned after deleting a certain
model. Always check your robot program after deleting models.

**Warning** Model data will be lost after deletion confirmation and
cannot be restored.

Select and visualize a model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A model can be selected by clicking on the row. When the model is
loaded, the model will automatically be shown in the Model view.

Enable or disable a model
^^^^^^^^^^^^^^^^^^^^^^^^^

| Each model can be included or excluded from the detections, this can
  be done by check (Enable model - Default) or uncheck (Disable model).
| When disabling a model, the detection algorithm will completely ignore
  that specific model.

Pick frame
~~~~~~~~~~

By default, Pick-it Teach provides an initial guess for the pick frame,
but this will in general not be the best choice. It's possible to
specify the desired  **pick frame** as a positional and rotational
offset with respect to the object model. The pick frame is the location
where the robot will pick the object. The location of the pick frame can
be visualized from the **Model** view.

|image1|

Matching tolerance
~~~~~~~~~~~~~~~~~~

If the distance between a detected scene point and a point of your model
is below this position tolerance value, then this scene point will
confirm the model point. This parameter has a big impact on the scoring
of the  `Minimum matching score <#score>`__.

|image2|

Minimum matching score
~~~~~~~~~~~~~~~~~~~~~~

Minimum percentage of model points that need to be confirmed by scene
points, for the detected object to be considered valid.

Optimize detections
-------------------

Image fusion
~~~~~~~~~~~~

Image fusion is the combination of multiple camera captures into a
single image. Enabling image fusion can provide **more detail** in
regions that show flickering in the 2D or 3D live streams. Flickering
typically occurs when working with **reflective materials**. There are
three possible fusion configurations: \ **None**, \ **Light
fusion** and **Heavy fusion**.

Image fusion can increase total detection time by up to half a second.
The recommended practice is to use None in the absence of flickering,
and try first Light fusion over Heavy fusion when flickering is
present. 

Scene downsampling resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div>

The downsampling resolution allows reducing the density of the point
cloud. This parameter has a big impact on detection time and accuracy.
More points lead to higher detection times and higher accuracy, fewer
points to lower detection times and lower accuracy.

.. raw:: html

   </div>

.. raw:: html

   <div>

In the illustration, you can see an example of setting the scene
downsampling parameter to 1 mm, 4 mm and 10 mm.

.. raw:: html

   </div>

|image3|

Detection speed
~~~~~~~~~~~~~~~

.. raw:: html

   <div>

With this parameter, you can specify how hard Pick-it Teach tries to
find multiple matches. Slower detection speeds are likely to produce
more matches. There are three available options:

.. raw:: html

   </div>

-  **Fast** Recommended for simple scenes with a single or few objects.
-  **Normal** This is the default choice and represents a good
   compromise between a number of matches and detection speed.
-  **Slow** Recommended for scenes with many parts, potentially
   overlapping and in clutter.

| **Example:** Two-step bin picking.
| 1. Pick an individual part from a bin using **Normal** or
  **Slow** detection speed and place it on a flat surface.
| 2. Perform an orientation check for re-grasping using
  **Fast** detection speed, as the part is isolated. Grasp and place in
  final location.

Detection precision
~~~~~~~~~~~~~~~~~~~

Apart from the above choice, you can instruct Pick-it Teach to favor
being **more precise** or to potentially find \ **more objects**. This
choice has a negligible impact on detection times. In most cases,
selecting \ **more precise** yields a good number of matches per
detection run, and is the recommended default.

Application type
~~~~~~~~~~~~~~~~

With the application type setting, an operator can specify how the parts
that need to be detected are placed. By providing this information to
the detection algorithm, the parts can be detected more reliably. Two
cases are distinguished:

-  Parts are overlapping, that is, lying on top of each other at
   irregular angles. This is for instance the case of bin picking
   applications.
-  Parts are lying on a flat surface, without overlapping. This is
   commonly the case on conveyor belts or tables.

If the user chooses the non-overlapping application type, Pick-it will
try to fit the model always with a straight orientation, and never under
an angle. This does not only save processing effort, but also results in
more robust fits. This is especially noticeable when the parts to be
detected have an almost symmetrical shape, with few distinctive 3D
features.

Choose **Parts can overlap** if the parts are lying on top of each
other, tilted in unknown angles. The images below show an example of
this use case.

|image4|

Choose **Singulated parts** if parts are completely lying on a flat
surface. Look at the images below for an example application.

|image5|

Mentioned articles

What to read next

| ` <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__\ `Detection:
  Pick-it Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__\ ` <https://support.pickit3d.com/article/168-saving-a-snapshot-in-pick-it>`__\ ` <https://support.pickit3d.com/article/41-attaching-the-roi-box-to-the-robot-base-for-binpicking-objects-from-a-big-bin>`__

| `Configuration <https://support.pickit3d.com/article/157-configuration>`__
| `Region of
  Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
| `Detection: Pick-it
  Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
| `Detection:
  Pick-it Pattern <https://support.pickit3d.com/article/161-detection-pick-it-pattern>`__
| `Picking <https://support.pickit3d.com/article/163-picking>`__

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b1923140428632c466aa4bd/file-HvTm5oRaq7.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5afb4d5c042863158411cf74/file-NhiK3XQVOe.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5afc25b92c7d3a640ed6e517/file-MNDybwoxST.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58ee1e3edd8c8e5c5731532a/file-pKR4nQsEQv.png
.. |image4| image:: https://lh5.googleusercontent.com/LwBqRBiuk7_pPaMh3kUK_9P50OQPlWMciYWGVlAo_aUQMyagL63UUWlyopivpWSWl17i5zVBy6BUP8GuwsbWh_v29OCDfs569uXi0d-AaEMm4hd1RYxMFv1FaUqktYMa_ysm8Qmz
   :width: 545px
   :height: 171px
.. |image5| image:: https://lh4.googleusercontent.com/sUPD4iwTxEciTwOoyq1N4qnjx3_Snxm8ieexKW4vGR6Z1PaC-anXz4qGMntb6z9pB96fVrZydTZHQv6nkBBOyju5pdfxbV68Sg1J11L9VjQEIXLNCrWXBhgGuZqrPc_SkS8FOFWz
   :width: 423px
   :height: 274px
