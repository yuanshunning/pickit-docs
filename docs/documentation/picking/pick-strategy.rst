Pick strategy
=============

.. note::
  This setting is only available for **cylinder** and **sphere** detections with the **Flex engine**.

This setting allows you to move the pick frame to the real surface of
the detected object instead of the center of the object. The possible
options are:

-  Default: The default object frame will be used, which is a frame in
   the center of the cylinder or sphere. This option does not modify the
   pick frame.
-  Surface top: The pick frame will move to the center at the top
   surface of the object.
-  Surface visible: The pick frame will move to the center of the
   visible part of the object. This setting is useful to avoid
   collisions when the detected object is partially covered by another
   object.
-  End circle: The pick frame will be moved to the highest circular end
   of the cylinder.

.. note::
  The resulting pick frame axes will not necessarily be parallel to one of the reference frame axes. If you want this, use the **Enforce alignment of pick frame orientation** option.

The picture below shows an example of a spherical and cylindrical object
respectively:

|image0|

.. |image0| image:: https://lh4.googleusercontent.com/SXNC32lpmOOQUbN5kqeZxB2JSzYEdbQXyCuZTARG2-xnk3JMCgDTpD-yQ2lgu6k2SCAda-WqmNk_fTnd-G44msaacWCppKQjCnN4aIlTlmIIwy4m0o0vSxseAJmpS3fZvAYLz-Of
   :width: 624px
   :height: 1317px
