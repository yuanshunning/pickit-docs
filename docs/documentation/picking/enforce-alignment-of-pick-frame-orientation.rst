Enforce alignment of Pick frame orientation
===========================================

This setting is used to enforce aligning an object frame with the
reference frame. The newly created aligned frame is the pick frame that
will be sent to the robot. This setting will make sure that one or more
resulting pick frame axes have a parallel or perpendicular axis to the
reference frame axes.

.. raw:: html

   <div class="callout-red">

**Warning** Enforcing a pick frame orientation takes precedence over the
object to reference frame alignment.

.. raw:: html

   </div>

There are multiple alignment options, which will all be discussed in
this article.  

No alignment
------------

No alignment will be done, this option does not modify the pick frame.
This is typically applied if there is only one correct way for the
gripper to approach the object.

Y ⊥ Z
-----

Aligns the Y-axis of the pick frame to be in the XY plane of the
reference frame. This setting allows the pick frames to point as much as
possible upwards when only rotating around his X-axis. This freedom is
typically seen when picking cylinders. As can be seen on the image
below, if the X-axis is the center of rotation, for the gripper to pick
the object it doesn’t matter how the other axises are orientated.

|image0|

See screenshots below to see the effect on a real scene of Pickit. The
image on the left is with no alignment and the image on the right is
with the Y ⊥ Z option.

|image1|

For this to work it is important that the X-axis is in the center of
rotation of the object. For flex cylinders the pick frames have to be
set to default. For Teach this has to be done manually by changing the
pick frame offset.  

Together with this setting an additional offset can be created around
the x-axis if the object is lying close to the side of the bin. Below it
is shown if an object it lying close to the border of the bin an
additional rotation is enforced so that the pick frames tilt away from
the sides of the bin.

|image2|

For this following parameters are used:

-  **Distance from box for avoidance:** Pick frames lying within this
   distance towards the sides of the ROI box are corrected. Set this
   value to 0 to not apply any additional rotation.
-  **Angular modification away from box:** The angle on how much is
   tilted away from the box.
-  **Allowed correction axis deviation:** The angle on how steep the
   object can be towards the side of the ROI box. If an object is in a
   steeper angle the additional tiliting is not applied. E.g. in the
   image below the left object is in angle of 0 degrees and the object
   on the right is in an angle of 20 degrees towards the side of the ROI
   box.
-  **Allowed correction along pick frame Y axis:** For this correction
   to work this value should always be set to 0 degree.

|image3|

Z \|\| Z
--------

This option aligns the Z-axis of the pick frame to be parallel to the Z
axis of the reference frame. In most applications, the Z axis points up
from the table or bin, so this option enforces the pick frame to point
upwards. This is typically used when there is a flexible gripper to pick
the objects, e.g. a vacuum cup to pick cardboard boxes. See image below
for the effect on a real scene in Pickit. The image on the left is with
no alignment, on the right z\|\|z alignment is used. Note that the
X-axis of all pick frames are still pointing in the same orientation.
This correction has no influence on the orientation of the pick frames.

|image4|

Together with this setting an additional offset can be created around
the if the object is lying close to the side of the bin. Below it is
shown if an object it lying close to the border of the bin an additional
rotation is enforced so that the pick frames tilt away from the sides of
the bin.

|image5|

For this following parameters are used:

-  **Distance from box for avoidance:** Pick frames lying within this
   distance towards the sides of the ROI box are corrected. Set this
   value to 0 to not apply any additional rotation.
-  **Angular modification away from box:** The angle on how much is
   tilted away from the box.
-  **Allowed correction axis deviation:** For this correction to work
   this value should always be set to 0 degree.
-  **Allowed correction along pick frame Y axis:** Typically this value
   is set the same as the angular modification away from box. If the
   gripper has different flexibility around his Y-axis than around his
   X-axis this can be set to a lower value.

XYZ \|\| XYZ
------------

This option aligns all three axis of the pick frame with all three axis
of the reference frame. This setting is typically used when there is a
flexible gripper to pick the objects, e.g. a vacuum cup to pick
cardboard boxes. See image below for the effect on a real scene in
Pickit. The image on the left is with no alignment, on the right
XYZ\|\|XYZ alignment is used.

|image6|

The difference with Z\|\|Z alignment is that now also orientation of the
object is lost. The benefit is that if set correctly there is almost no
rotation around the last joint of the robot necessary. This has an
influence on the cycle time of your application.

Together with this setting an additional offset can be created around
the if the object is lying close to the side of the bin. Below it is
shown if an object it lying close to the border of the bin an additional
rotation is enforced so that the pick frames tilt away from the sides of
the bin.

|image7|

-  **Distance from box for avoidance:** Pick frames lying within this
   distance towards the sides of the ROI box are corrected. Set this
   value to 0 to not apply any additional rotation.
-  **Angular modification away from box:** The angle on how much is
   tilted away from the box.
-  **Allowed correction axis deviation:** For this correction to work
   this value should always be set to 0 degree.
-  **Allowed correction along pick frame Y axis:** Typically this value
   is set the same as the angular modification away from box. If the
   gripper has different flexibility around his Y-axis than around his
   X-axis this can be set to a lower value.

Short overview
--------------

**No alignment:** if the there is no tolerance for the gripper to pick
the part.

**Y⊥Z:** For cylindrical parts.

**Z\|\|Z:** If the gripper has enough compliance to pick the parts
straight upwards.

**XYZ\|\|XYZ:** If the gripper has compliance to pick the objects
straight upwards and orientation of the parts is not important.

.. |image0| image:: https://lh3.googleusercontent.com/s92rRAN86rSr3zrkQwdsw2A4tgnSFpXa2Qgr7wA6UKHuAMppJTWfGeasJv5t-tor5lf3T0pK3w7FtszdLNajXTdiX7ZqwLsg7cUQJTw00bOHKF28eoDZEoUte4rV_N7gMEiCZnA5
   :width: 358px
   :height: 310px
.. |image1| image:: https://lh4.googleusercontent.com/kjr9eNyjIm66OrfzSu2dt-2pusHR7aZPJUaP3mCh7cqAhks3kII09KFhgw8SH2Gh86Uh-h9632rFI3MChXD5PifKALqQe86g7DtGJHYq7Ysq2nTgVdc74KLYYFrkFxR_WKixo7v7
   :width: 624px
   :height: 251px
.. |image2| image:: https://lh4.googleusercontent.com/Mi_slcGykLRYmOG1_QUqCMz3LTmfhl0aHOlk0Z4tJ2HdvSzKvDqpA6qTw4ATEGJeMvz4xCvUHIsv_N2CWgtYVF6GAvadu6gMSNnx-_VRiVwQXKsKRuT5qtDhFglGlQWYw6i0hSgX
   :width: 624px
   :height: 251px
.. |image3| image:: https://lh4.googleusercontent.com/WAJVz3wh6RoQ5vaOWd2VOZcUVge3aK3EqwAXe0WCmeqbKLIxU_HO6fIBkr6iKAAeqmCxOWaCZk3ZRRZfFapA_esevQWr27fLAuIl_R9Mv4TboNbDmXdkvzTWsX7QH-dn8pO_w-Vz
   :width: 534px
   :height: 344px
.. |image4| image:: https://lh6.googleusercontent.com/ftXCqjVuuNs6FdzCSlaHHE_30ydtx2cCzUH01J8mYHXHQ48GZhWqMT8TznnP3EsqQ0dAEboU_0l9CENQsJLS1cFJ2KmCQpWq_CN9KHgrrI-yWIkat3p-9p-pNwOXG29XlbOtnFXs
   :width: 624px
   :height: 236px
.. |image5| image:: https://lh5.googleusercontent.com/lvvxmtEGGptk9s3U7O66z3pcci7I8BSPVsplpEFPzigjKfn7BsB_lu75_8tZWJe1N7aPAxkbjOPK6--J-98t0Vv7Ep1ED_FAjJC1_tGtleChpH4KU6I6Y_cZLrTW5Bk40889-4n7
   :width: 624px
   :height: 236px
.. |image6| image:: https://lh5.googleusercontent.com/6aELmO8TNodgIURO9JBOMmKMTvwk8NwCjUVD5qPeK9YOoSN_rUoV1UJtcRnshWqKTczCKKdMrjVdmHNUpUvO92yMkDnKp47vjNvZe5ygTr3D8fveiIy5Z-t_lkncEyRLG2fDIo-q
   :width: 624px
   :height: 231px
.. |image7| image:: https://lh4.googleusercontent.com/77fgZUq8FN6G0eqAIZWrFpQRF80MKYgOFd69BolObENE9eBOzMyec4tR6dwzCaFaBMuLDibtTdo1_etE5iKRvTkz9FPI4d2QabPiB6_EMaO6m9W7YxO-seNWSf8PV9YXFhKUtuOk
   :width: 624px
   :height: 231px
