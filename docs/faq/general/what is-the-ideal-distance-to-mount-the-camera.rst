What is the ideal distance to mount the camera?
===============================================

The distance between the camera and the parts to detect plays an important role in getting high-quality detections out of your Pick-it system. 
The following guidelines will help you to find the camera mounting distance that works best for your application:

-  The distance between the camera and the objects to detect should be within the **minimum and maximum** values documented in the camera specifications.

   -  When objects can be at different heights, such as when emptying a bin, make sure that the closest objects (full bin) are not closer than the minimum distance to the camera, and that the furthest objects (almost empty bin) are not farther away than the maximum distance to the camera.

   -  When objects can be at a height range that exceeds the depth range of the camera, as can happen in depalletizing applications, it is recommended to mount the camera on the robot and to move the detection pose down as the height of the stack decreases. 
      The idea is to preserve a similar distance to the camera for all stack layers.

-  Taking into account the above constraint, the camera should be **as close to the objects as possible**, while still capturing the **desired field of view**.

   -  Moving the camera closer to the objects produces more detailed captures of the scene, which leads to more precise detections.

   -  Moving the camera away from the objects allows capturing a bigger the field of view.

   -  When the application requires a field of view greater than what the camera can provide, as can happen with very wide bins, it is recommended to mount the camera on the robot. 
      The idea is to cover the entire surface using a multiple detection poses.

-  For cameras fixed to an independent structure, make sure that the expected **robot motions don't collide with the camera**. 
   In some cases, it's necessary to reposition the camera to avoid potential collisions.

Detecting cylinders with the Pickit M camera
--------------------------------------------

The graph below shows which cylinder diameter can be reliably detected at which distance with a Pick-it M camera. 
Everything above the green line is considered to be within Pick-it's comfort zone. 
From this graph it can be noted that the closer the camera is mounted the smaller diameters can be detected. 
But the closer the camera is mounted also means a smaller field of view.

.. image:: /assets/images/faq/Cylinder-diameter-vs-camera-distance.png