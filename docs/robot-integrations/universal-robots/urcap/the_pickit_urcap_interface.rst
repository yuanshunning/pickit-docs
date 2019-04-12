The Pickit URCap interface
===========================

Overview
--------

Pickit integrates seamlessly with Universal Robots by means of a URCap
plugin. This plugin exposes a set of Pickit specific command blocks
that make the creation of vision-guided programs simple and easy. This
article documents the interface of the Pickit URCap plugin. For
installation instructions please refer to the \ `Getting started with
the Pickit
URCap <http://support.pickit3d.com/article/75-getting-started-with-the-pick-it-urcap>`__
article.

 1
    `Global variables <#global_variables>`__
 2
    `Commands <#commands>`__
 3
    `Helper functions <#helper_functions>`__

Global variables
----------------

To use one of the global variables defined by the Pickit plugin, you
need to declare it in the **BeforeStart** section of the program. You
only need to declare the variables you actually use in your program.

+--------------------------------------------------------------------------+
| **pickit\_pose**                                                         |
+==========================================================================+
| Pick pose for the latest detection results sent by Pickit, represented  |
| as a 6D array.                                                           |
| The sequence of commands to get a valid and reachable pick pose is:      |
|                                                                          |
| #. Declare the variable in the **BeforeStart** section of the            |
|    program.\ |image0|                                                    |
| #. In the **Robot Program** section, send a request to Pickit           |
|    using \ **Find object(s)** or **Get next object** command.            |
| #. Wait for detection result using **Get Result** command.               |
| #. Check that a valid detection is available by                          |
|    calling \ **``pickit_object_found()``**.                              |
| #. Check that the robot can reach the pose by                            |
|    calling \ **``pickit_object_reachable()``**.                          |
|                                                                          |
| Refer to the  `Universal Robots URCap example                            |
| program <http://support.pickit3d.com/article/76-universal-robots-urcap-e |
| xample-program>`__                                                       |
| article for a detailed usecase description.                              |
+--------------------------------------------------------------------------+

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **pickit\_pre\_pose**                                                                                                                                                                                                                                                                                                        |
+==============================================================================================================================================================================================================================================================================================================================+
| Pre-pick pose for the latest detection results sent by Pickit, represented as a 6D array.                                                                                                                                                                                                                                   |
| The sequence of commands to get a valid and reachable pre-pick pose is the same as for **``pickit_pose``**. Refer to the documentation of **``pickit_pose``** for more details. For details on how **``pickit_pre_pose``** is computed from **``pickit_pose``**, refer to the documentation of the **Get result** command.   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| **pickit\_dim**                                                          |
+==========================================================================+
| Object dimensions, in meters, for the latest detection results sent by   |
| Pickit, represented as a 3D array.                                      |
| This is how to interpret the array according to the object type:         |
|                                                                          |
| -  **Square** **``[length, length, 0]``**                                |
| -  **Rectangle** **``[length, width, 0]``**                              |
| -  **Circle** **``[diameter, diameter, 0]``**                            |
| -  **Ellipse** **``[length, width, 0]``**                                |
| -  **Cylinder** **``[length, diameter, diameter]``**                     |
| -  **Sphere** **``[diameter, diameter, diameter]``**                     |
| -  **Point** **cloud (Pickit Teach                                      |
|    model)** **``[bbox x, bbox y, bbox z]``**                             |
| -  **Blob** **``[bbox x, bbox y, bbox z]``**                             |
|                                                                          |
| where **``bbox x``** means the size of the bounding box along the        |
| x-axis.                                                                  |
|                                                                          |
| The sequence of commands to get valid object dimensions is the same as   |
| for **``pickit_pose``**. Refer to the documentation of                   |
| **``pickit_pose``** for more details.                                    |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| **pickit\_type**                                                         |
+==========================================================================+
| Object type, as an integer identifier, for the latest detection results  |
| sent by Pickit.                                                         |
| The mapping between object shape and identifier follows:                 |
|                                                                          |
| -  **Square** 21                                                         |
| -  **Rectangle** 22                                                      |
| -  **Circle** 23                                                         |
| -  **Ellipse** 24                                                        |
| -  **Cylinder** 32                                                       |
| -  **Sphere** 33                                                         |
| -  **Point cloud (Pickit Teach model)** 35                              |
|    From version 1.9+ this variable is no longer 35 with the Pickit      |
|    Teach detection engine, but representing the ID Teach model the       |
|    object was detected from.                                             |
| -  **Blob** 50                                                           |
|                                                                          |
| The sequence of commands to get a valid object type is the same as for   |
| **``pickit_pose``**. Refer to the documentation of **``pickit_pose``**   |
| for more details.                                                        |
+--------------------------------------------------------------------------+

Commands
--------

.. raw:: html

   <div>

.. raw:: html

   <div>

The Pickit plugin provides a set of commands that add to the set of
Polyscope’s existing commands. They can be accessed from within the 
**Program** tab, under  **Structure** →   **URCaps**, and clicking the 
**Pickit** button.

.. raw:: html

   </div>

.. raw:: html

   </div>

|image1|

To insert a new command, navigate to the **Command** tab select an entry
from the \ **Pickit** **command** drop-down. When a command is
selected, a brief description is shown on the rightmost part of the
page. Some commands require the specification of input parameters.

|image2|

+--------------------------------------------------------------------------+
| **Check if robot mode enabled**                                          |
+==========================================================================+
| Checks whether robot mode is enabled in Pickit.                         |
|                                                                          |
| -  If robot mode is enabled, program execution continues                 |
| -  If robot mode is not enabled, a pop-up is shown requesting the user   |
|    to set Pickit to robot mode.                                         |
|                                                                          |
| Except for **Find calibration plate**, all other Pickit plugin commands |
| require robot mode to be Robot mode is enabled. Robot mode is enabled    |
| from the Pickit web interface.                                          |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| **Select**                                                               |
+==========================================================================+
| Loads the specified setup and product configuration.                     |
| This configuration specifies the behavior of Pickit detections, e.g.    |
| what to look for, in which part of the field of view.                    |
| **Parameters**                                                           |
|                                                                          |
| **Setup** Any of the setup configurations currently available in the     |
| connected Pickit system.                                                |
|                                                                          |
| **Product** Any of the product configurations currently available in the |
| connected Pickit system.                                                |
|                                                                          |
| Available configurations are listed in drop-down menus.                  |
+--------------------------------------------------------------------------+

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Find object(s)**                                                                                                                                                                                                                                                                              |
+=================================================================================================================================================================================================================================================================================================+
| Trigger a Pickit object detection using the currently active setup and product configuration.                                                                                                                                                                                                  |
| The next Pickit command after **Find object(s)** should always be **Get result**, which waits until a response for the detection request is ready.                                                                                                                                             |
| Note that it's valid (and sometimes encouraged) to perform robot motions or other non Pickit actions between calls to **Find object(s)** and **Get result**, for instance                                                                                                                      |
| |image3|\ |image4|\ Refer to the cycle time optimization section of the \ `Universal Robots URCap example program <http://support.pickit3d.com/article/76-universal-robots-urcap-example-program>`__ article for the motivation behind performing robot motions while a Pickit detection is.   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| **Get next object**                                                      |
+==========================================================================+
| Request the next detected object.                                        |
|  A single call to **Find object(s)** might yield the detection of        |
| multiple objects. **Get next object** allows to request the next         |
| available object, if any, without the need of triggering a new detection |
| and the time overhead it entails.                                        |
| The next Pickit command after  **Find object(s)** should always         |
| be \ **Get next object**, which waits until a response for the request   |
| is ready.                                                                |
| |image5|\ It's recommended to use this command only when objects in the  |
| detection region have not moved (significantly) since calling **Find     |
| object(s)**. A good example of when to use **Get next object** is when a |
| detection is unreachable by the robot. An example of when using \ **Get  |
| next object** is not ideal would be the following bin picking scenario:  |
|                                                                          |
| -  Trigger Pickit detection that finds multiple objects.                |
| -  First object is picked. Since objects are randomly placed in bin,     |
|    neighboring objects move and fall into place.                         |
| -  Call **Get next object** and attempt to pick next object. If the next |
|    object is one of the neighboring parts that moved, the pick might     |
|    fail.                                                                 |
|                                                                          |
| When the objects in the detection region have moved, it's better to      |
| re-trigger  **Find object(s)** instead.                                  |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| **Get result**                                                           |
+==========================================================================+
| Wait for Pickit reply with detection results.                           |
| **Get result** should always be the next Pickit command after           |
| a \ **Find object(s)** or **Get next object** request. It blocks until a |
| reply from Pickit is received, and the success of the request can then  |
| be queried by calling **``pickit_object_found()``**. When an object has  |
| been found, the following global variables are populated:                |
|                                                                          |
| -  Object pick pose: **``pickit_pose``**                                 |
| -  Object pre-pick pose: **``pickit_pre_pose``**.                        |
|    This pose is computed by applying an offset to **``pickit_pose``**    |
|    along a specified direction, as specified by the command parameters.  |
| -  Object dimensions: **``pickit_dim``**                                 |
| -  Object type: **``pickit_type``**                                      |
|                                                                          |
| **Parameters**                                                           |
|                                                                          |
| **Pre-pick offset: base frame** **``pickit_pre_pose``** is computed by   |
| applying an offset along the z-axis of the specified frame. Valid        |
| options are object frame or robot base frame.                            |
|                                                                          |
| **Pre-pick offset **\ Offset in mm applied to compute                    |
| **``pickit_pre_pose``**.                                                 |
+--------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Find calibration plate**                                                                                                                                                            |
+=======================================================================================================================================================================================+
| Trigger detection of the robot-camera calibration plate.                                                                                                                              |
| This command requires the Pickit web interface to be in the Calibration page, hence robot mode should be disabled. When Pickit is not in the calibration page, a pop-up is shown.   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Save snapshot**                                                                                                                                                                 |
+===================================================================================================================================================================================+
| Save a snapshot with the latest detection results.                                                                                                                                |
| The saved snapshot can then be loaded or downloaded by going to the Files page on the Pickit web interface and searching for a file whose name contains the capture timestamp.   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Helper functions
----------------

As opposed to commands, that don't have a return value; the Pickit
plugin also exposes a number of helper functions that return useful
information. They typically are used as the expression of a conditional,
such as an **if** statement, and can be selected from the **available
functions drop-down**. 

|image6|

+--------------------------------------------------------------------------+
| **pickit\_object\_found()**                                              |
+==========================================================================+
| Check if the last call to  **Get result** produced valid detection       |
| results.                                                                 |
| **Return**                                                               |
|                                                                          |
| | True if detection results are available.                               |
| | When results are available, the global variables                       |
|   **``pickit_pre_pose``** and **``pickit_pose``** have valid contents.   |
| | This function returns false when Pickit replied with no detection     |
|   results (nominal usecase); or if called without making a request to    |
|   Pickit and collecting the results with **Get result** (should be      |
|   avoided, as it makes no sense).                                        |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| **pickit\_object\_reachable()**                                          |
+==========================================================================+
| Check if the last call to  **Get result** produced reachable pick and    |
| pre-pick poses.                                                          |
| **Return**                                                               |
|                                                                          |
| | True if the global variables **``pickit_pre_pose``** and               |
|   **``pickit_pose``** contain poses that are reachable by the robot.     |
| | Note that **``pickit_object_reachable() == true``** implies            |
|   **``pickit_object_found() == true``**.                                 |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| **pickit\_no\_image\_captured()**                                        |
+==========================================================================+
| Check if object detection was unsuccessful due to a failure to capture a |
| camera image.                                                            |
| When this is the case, it typically indicates a hardware disconnection   |
| issue, such as a loose connector or broken cable. This function can be   |
| used as trigger to send an alarm to a higher level monitoring system.    |
| **Return**                                                               |
|                                                                          |
| True if object detection was unsuccessful due to a failure to capture a  |
| camera image.                                                            |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
| **pickit\_remaining\_objects()**                                         |
+==========================================================================+
| Get the number of remaining object detections.                           |
| After calling **Get result**, this function returns the total number of  |
| object detections minus one, as the first object data is available       |
| through the `global variables <#global_variables>`__. This value is also |
| equal to the number of times **Get next object** can be called. As such, |
| the returned value decreases with each call to **Get next object**.      |
| **Return**                                                               |
|                                                                          |
| Number of remaining object detections available for query.               |
+--------------------------------------------------------------------------+

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a5f2a940428631938010e82/file-I2wchgqD7S.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a72d7852c7d3a4a4198b295/file-J6wnqcXhz3.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a72d7df0428634376cfb3b4/file-rjWnObfV3Z.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a5e0aa12c7d3a1943684512/file-5V8p0WlHg5.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a5e0ad32c7d3a1943684515/file-tPmyJn58Jg.png
.. |image5| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a5e12a5042863193801065f/file-D4zomiCbVr.png
.. |image6| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a72da422c7d3a4a4198b2ae/file-N5oBOwLSx2.png

