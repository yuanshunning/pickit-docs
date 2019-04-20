Does additional lightning help me getting better 3D data?
=========================================================

Simple answer: no. 
As explained in the article :ref:`how-does-the-pickit-3d-camera-works`, our cameras are based on the structured light principle. 
For this to work the structured light pattern needs to be the most present in the scene. 
If additional light is added to the scene this can interfere with the known grid. 
This interference can lead to worse 3D data.

The M and L camera work with structured infrared light. 
So only other infrared light sources interfere with these cameras. 
The most common infrared light source that causes interference is direct sunlight. 

The M-HD camera works with structured visible light. 
To be less depending on changing light conditions a strong projector is used in this camera. 
Because of this normal changing light conditions in an office or factory don't have much influence on the camera. 
Still, direct sunlight and bright spotlights can cause interference.

.. note:: If the :ref:`color-filter` is used for detections, stable light conditions are necessary.