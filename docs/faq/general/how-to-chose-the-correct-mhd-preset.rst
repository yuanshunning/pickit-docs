.. _how-to-mhd-preset:

How to chose the correct M-HD preset
====================================

The Pickit M-HD camera is a high end camera with many different options on how to capture a point cloud of the scene.
For instance the camera can be optimized to better detect bright parts or to better detect dark parts. 
When set to detect bright parts typically the captured point cloud is darker, to compensate for the brightness of the parts. 
On the contrary when it is set to detect darker parts the point cloud becomes brighter.

This capture was taken with the **Light reflective plastic** setting. 
Here you can clearly see that the bright parts of the plates are detected but the dark parts are not.

.. image:: /assets/images/faq/mhd-preset-lrp.png

This capture was taken with the **Dark non-reflective plastic** setting. 
Here you can clearly see that the dark parts of the plates are detected but the bright parts are not.

.. image:: /assets/images/faq/mhd-preset-dnrp.png

Next to different settings to capture a point cloud the Pickit M-HD camera also has the possibility to trigger multiple captures in a row.
Each capture uses a different setting and the combined image of multiple captures leads to a point cloud which can be better than a single capture.
Taking multiple captures typically leads to a better point cloud but also leads to a longer overal time to capture the point cloud.

This capture was taken with the **Mixed-color plastic** setting.
Here you can see that both the bright and dark parts are detected.

.. image:: /assets/images/faq/mhd-preset-mcp.png

In the Pickit software different presets are available. 
To find the best setting for your application, it is adviced to try different presets and chose the one that gives the best results on your scene.
The result of a certain preset is best visualized in the :ref:`points-view` of the Pickit viewer.

-  **Light reflective plastic** (1 capture): a preset typically used for plastic that is bright and reflective.
-  **Light non-reflective plastic** (1 capture): a preset that is typically used for plastic that is bright and non-reflective.
-  **Dark non-reflective plastic** (1 capture): a preset that is typically used for plastic that is dark and non-reflective.
-  **Dark reflective plastic** (1 capture): a preset that is typically used for for plastic that is reflective and dark.
-  **Mixed-color plastic** (3 captures): a preset that is typically used for mixed-color plastic.
-  **Sandblasted metal** (2 captures): a preset that is typically used for metal that is sandblasted.
-  **Polished metal** (3 captures): a preset that is typically used for for metal that is polished.

.. hint:: Teaching the same model with different settings can help you choose the best setting, typically the preset that leads to the highest number of points in the model is the best preset for this part.
