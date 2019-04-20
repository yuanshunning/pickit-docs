How does the Pickit 3D camera works?
====================================

The Pick-it 3D cameras use `structured light <https://en.wikipedia.org/wiki/Structured_light>`__ technology. 
A known pattern is projected on the scene, and the deformations of the pattern as seen by the camera as it hits surfaces determines how far these surfaces are towards the camera. 
This results in a 3D point cloud.

The below image illustrates the structured light principle. 
The red triangle represents the projected pattern, while the green triangle represents where the sensor can detect it. 
When there is an overlap between the two , 3D data in the form a point cloud can be obtained, shown as a thick green line. 
In this case, there is 3D data for the upper part of the circle and for the flat surface below it.

.. image:: /assets/images/faq/Pickit-camera-3d-data.png

All Pick-it 3D camera work according to this principle. 
The M and L camera work with structured infrared light and the M-HD camera works with structured visible light.

What surface of the object gets detected by the camera?
-------------------------------------------------------

From the image above you can see that the camera can't obtain 3D data for the full circle. 
Only the visible upper part is detected. Both the object shape and location (position and orientation) with respect to the camera determine which surfaces will be detected by the camera. 
In this section, two different examples are discussed.

In the image below three circles are placed beneath the camera. 
Here it is shown that the obtained 3D data depends on where objects are located with respect to the camera. 
The detected surfaces are those that have a direct line of sight to both the structured light projector and the sensor (red and green triangles, respectively).

.. image:: /assets/images/faq/Pickit-camera-multiple-objects.png

An interesting situation arises when a rectangular shape gets placed directly beneath the camera, as in the image below. 
In such a case, only the upper side of the rectangle is detected. 
There is no 3D information for the standing sides as they are not visible to the camera.

.. image:: /assets/images/faq/Pickit-camera-box.png

What are the limits of the Pick-it cameras?
-------------------------------------------

There are limits to what the Pick-it cameras can detect. 
In this section, three different scenarios where 3D data from an object cannot be extracted from the scene are explained.

The first scenario is a special case of the rectangle discussed in the previous section of this article. 
Below, the effect of a thin standing edge is shown. The edge itself is rather thin so no 3D data can be obtained on top of it. 
Also, 3D data on the flat surface around the edge is missing where there is only visibility to either the structured light projector (red triangle) or the sensor (green triangle), but not both: The region next to the left side of the edge is visible to the sensor but not to the projector. 
Conversely, the region next to the right side of the edge is visible to the projector but not to the sensor.

.. image:: /assets/images/faq/Pickit-camera-standing-edge.png

The second scenario consists of a transparent object. 
In the image below it can be seen that both the structured light and the sensor pass through the object. 
So 3D data of the flat surface below the object is returned, but no information of the object itself is obtained.

.. image:: /assets/images/faq/Pickit-camera-transparent.png

A third scenario is when the object is reflective. 
The structured light that falls on the object will not be reflected towards the camera but away from it. 
This makes it impossible to obtain 3D information around the object, as shown in the image below.

.. image:: /assets/images/faq/Pickit-camera-reflective.png

The above scenarios exemplify edge cases. 
Often parts are only partially reflective or semi-transparent. 
When in doubt about a part, it is recommended to test it by placing it under the camera, trigger a detection and inspect the point cloud in the **Points** tab of the :ref:`Viewer`. 
If not enough 3D data is shown, know that this can be further optimized. 
For the Pick-it M and L cameras, :ref:`image-fusion` leads to a more stable point cloud. 
For the Pick-it M-HD camera, a different camera preset can be used. 
If still not enough 3D is obtained the parts are too reflective or transparent. 

Does additional lightning help me getting better 3D data?
---------------------------------------------------------

Simple answer: no. 
As explained in the first section of this article the Pick-it 3D cameras are based on the structured light principle. 
For this to work the structured light needs to be the most present in the scene. 
If additional light is added to the scene this can interfere with the known grid. 
This interference leads to worse 3D data.

The M and L camera work with structured infrared light. 
So only other infrared light sources interfere with these cameras. 
The most common infrared light source that causes interference is direct sunlight. 

The M-HD camera works with structured visible light. 
To be less depending on changing light conditions a strong projector is used in this camera. 
Because of this normal changing light conditions in an office or factory don't have much influence on the camera. 
Still, direct sunlight and bright spotlights can cause interference.

.. note:: If the :ref:`color-filter` is used for detections, stable light conditions are necessary.