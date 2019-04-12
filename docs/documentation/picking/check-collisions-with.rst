Check collisions with
=====================

This setting allows you to discard pick frames that would result in
collision. The pick frames can checked for possible collision with the
bin and/or other objects.

When collision checking yields that a certain object pose will result in
a collision,  the object will be labeled as unpickable and not sent to
the robot. In the Pickit web interface, unpickable objects are
displayed orange in the Objects view and the `detection
grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__.
When clicking on the unpickable object, the modeled tool will appear in
the “Objects” tab of the 3D view to illustrate why the given object is
unpickable.

Bin
---

This option checks if the tool is colliding with the Region of Interest
box. If set the tool is not allowed to hit the sides or bottom of the
region of interest box. If the Region of interest box is set to similar
dimensions as the actual bin, this option is checking for collisions
with the actual bin. A rule of thumb for this to work properly is to set
the dimensions of the region of interest box slightly smaller and
slightly higher than the real bin.

|image0|

Other objects
-------------

This option checks if the tool is colliding with other objects that are
visible in the region of interest. As seen in the image below the object
is not safe to pick because there is another object on top and the tool
would collide with this other object.

|image1|

.. |image0| image:: https://lh5.googleusercontent.com/O5WTyARfx9jMAEe6fxajEh1-NEULjMD8EVptSblNcFbkkivUkhBmbn3gHg2Nqw5E6yjwOyabMaNsrabURy_6F5TSgztEdiwIUBIW3z8D5SSveic_5HNqN1g3LAzOGQ6J0VwcUqa0
   :width: 624px
   :height: 472px
.. |image1| image:: https://lh4.googleusercontent.com/I1dWx5XcL3pQchwDM7PblAgV0QpK7V09V253u24ThAOFuu2haDqQlfqqp9DytqhJZtYdgfj0olcL4G-rkS9SS9KVhmKeFb-tdoyV-P9o5PKB4vIjI0zxB1JPsyPx1d60lDTmv0XB
   :width: 624px
   :height: 467px
