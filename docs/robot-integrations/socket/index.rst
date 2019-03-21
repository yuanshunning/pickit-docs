The low-level communication structures between a robot and Pick-it on the TCP/IP socket level
=============================================================================================

This article documents the low-level communication structures between a
robot and Pick-it on the TCP/IP socket level. This information is only
required to interface a new robot brand to Pick-it.

1. The protocol
---------------

The robot Pick-it communication is based on TCP/IP socket communication.
Pick-it is the server (slave) and the robot is the client
(master). Hence, the robot is responsible for opening the socket
communication and needs to know:

-  The **IP address** of the Pick-it port labelled ROBOT,
-  The **port number** which is **5001** by default.
-  Pick-it communicates data packages using the **network byte order**
   convention (Big Endian).

|image0|

Above you can find an example of the different behaviour between network
byte order and host byte order.

.. raw:: html

   <div class="callout-yellow">

The robot client sends requests using the `command
message <#command_msg>`__, and the Pick-it server answers with the
`response message <#response_msg>`__. These messages **have a static
size**, and **don’t have a begin and/or end character**. While the
TCP/IP protocol prevents data loss, the robot client implementation is
responsible for keeping track of the boundary between messages by
counting the number of sent/received bytes and comparing with the
expected message size.

There is **no explicit coupling between a command and a response** in
the communication. Therefore, the robot client should not send a second
command before having confirmed that a response to the first command has
been received. It is the responsibility of the client implementation or
the robot program to prevent this from happening.

.. raw:: html

   </div>

The Pick-it server only sends `response messages <#response_msg>`__
after having received an explicit request from the robot client in a
`command message <#command_msg>`__. Apart from this request-response
exchange, Pick-it also expects to receive periodic **robot flange** pose
updates from the client. The rate of these periodic updates depends on
the robot brand, but is typically in the range of 10 to 50 messages per
second. Note that both command requests and robot flange pose updates
use the same message structure, **``robot_to_pickit_data``**, described
in more detail in the `command message <#command_msg>`__ section. The
structure of the response messages, **``pickit_to_robot_data``**, is
described in the `response message <#response%20message>`__ section.

|image1|

A Pick-it data package consists of a number of **int32s** in network
byte order. As such, floating-point data like distances and angles are
multiplied by a factor MULT before being sent as an int32, and are
divided by MULT after being received. This integer conversion factor
**MULT** has the value of **10000**.

For **position** information Pick-it sends and expects to receive values
in **meter** before/after compensating with the MULT factor. For the
**orientation** information it depends on the robot type. For UR
**radians** are used, for ABB **unit quaternions** are used and for the
other brands **degrees** are used. Also here, this is the unit
before/after compensating with the MULT factor. 

2. Command message from robot to Pick-it
----------------------------------------

The data package communicated to Pick-it contains the actual robot pose,
an (optional) robot command and the desired configuration. The latter
allows to request Pick-it to configure according to an existing setup
and product type. What number matches to what file, can be derived from
the Configuration page of the Pick-it web interface.

In summary, the robot is required to send this structure to the Pick-it
Socket Interface:

::

    struct robot_to_pickit_data {
        int32 actual_pose[7];
        int32 command;
        int32 setup;
        int32 product;
        meta_data meta; 
    };

Metadata fields are documented in the  `Message metadata <#metadata>`__
section of this article. The remaining fields are explained below.

.. raw:: html

   <div>

+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field name         | Type / units                     | Comment                                                                                                                                                                                                                          |
+====================+==================================+==================================================================================================================================================================================================================================+
| **actual\_pose**   | **int32[7]**                     | | Actual robot flange pose in robot base frame consisting of position in Cartesian space and orientation in axis angle, quaternion or Euler angles convention. The orientation convention and units depend on the robot brand.   |
|                    | [0-2] : position (m)             | | To populate array elements, each value has to be multiplied by the  **MULT** factor before being sent.                                                                                                                         |
|                    | [3-6] : orientation (rad,o,/)    |                                                                                                                                                                                                                                  |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **command**        | **int32**                        | A single command from robot to Pick-it.                                                                                                                                                                                          |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | RC\_PICKIT\_NO\_COMMAND          | Use when sending a periodic pose update. Pick-it does not reply to these requests.                                                                                                                                               |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | RC\_PICKIT\_FIND\_CALIB\_PLATE   | Trigger the localisation of the Pick-it camera-to-robot calibration plate.                                                                                                                                                       |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | RC\_PICKIT\_LOOK\_FOR\_OBJECTS   | Trigger camera to look for new objects in its current workspace. Pick-it will respond with the amount of objects currently found in the workspace, which may be zero.                                                            |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | RC\_PICKIT\_NEXT\_OBJECT         | Request camera to return next localised object stored in the Pick-it buffer and which was found with RC\_PICKIT\_LOOK\_FOR\_OBJECTS.                                                                                             |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | RC\_PICKIT\_CONFIGURE            | Request Pick-it to load a specific setup and product type.                                                                                                                                                                       |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | RC\_PICKIT\_SAVE\_SCENE          | Request Pick-it to save the latest image as well as the whole configuration into a file for later diagnosis.                                                                                                                     |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **setup**          | **int32**                        | A number matching to a setup known by the Pick-it system.                                                                                                                                                                        |
|                    |                                  | Used only when the command type is RC\_PICKIT\_CONFIGURE.                                                                                                                                                                        |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **product**        | **int32**                        | A number matching to a product type known by the Pick-it system.                                                                                                                                                                 |
|                    |                                  | Used only when the command type is RC\_PICKIT\_CONFIGURE.                                                                                                                                                                        |
+--------------------+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Below are the values for the robot command constants expected by
Pick-it:

.. raw:: html

   </div>

::

        #define RC_PICKIT_NO_COMMAND    -1
        #define RC_PICKIT_CHECK_MODE     0
        #define RC_PICKIT_FIND_CALIB_PLATE   10
        #define RC_PICKIT_LOOK_FOR_OBJECTS   20
        #define RC_PICKIT_NEXT_OBJECT        30
        #define RC_PICKIT_CONFIGURE          40
        #define RC_PICKIT_SAVE_SCENE         50

All command messages (not just periodic pose updates) should contain a
valid **``actual_pose``** field.

3. Response message from Pick-it to robot
-----------------------------------------

Except for the RC\_PICKIT\_CALIBRATE command, each robot command sent to
Pick-it will result in one response message from Pick-it. These messages
contain a Pick-it status value as well as the actual object data for one
object.  

The robot receives this structure from the Pick-it interface:

::

         struct pickit_to_robot_data {
              int32 object_pose[7];
              int32 object_age; 
              int32 object_type;     
              int32 object_dimensions[3]; 
              int32 objects_remaining;
              int32 status;
              meta_data meta;  
         };

Metadata fields are documented in the   `Message metadata <#metadata>`__
section of this article. The remaining fields are explained below.

.. raw:: html

   <div>

+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field name               | Type / units                     | Comment                                                                                                                                                                                                                                     |
+==========================+==================================+=============================================================================================================================================================================================================================================+
| **object\_pose**         | **int32[7]**                     | An object pose expressed relative to the robot base frame consisting of position in cartesian space and orientation in axis angle, quaternion or Euler angles convention. This convention as well as the units depend on the robot brand.   |
|                          | [0-2] : position (m)             | When reading array elements, each value has to be divided by the  **MULT** factor.                                                                                                                                                          |
|                          | [3-6] : orientation (rad, o,/)   |                                                                                                                                                                                                                                             |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **object\_age**          | **int32**                        | The amount of time that has passed between the capturing of the camera data and the moment the object information is sent to the robot.                                                                                                     |
|                          | (seconds)                        | This value has to be divided by the  **MULT** factor.                                                                                                                                                                                       |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **object\_type**         | **int32**                        | The type of object detected at object\_pose                                                                                                                                                                                                 |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_SQUARE             | A square has been detected with center at object\_pose                                                                                                                                                                                      |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_RECTANGLE          | A rectangle has been detected with center at object\_pose                                                                                                                                                                                   |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_CIRCLE             | A circle has been detected with center at object\_pose                                                                                                                                                                                      |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_ELLIPSE            | An ellipse has been detected with center at object\_pose                                                                                                                                                                                    |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_CYLINDER           | A cylinder has been detected with center at object\_pose                                                                                                                                                                                    |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_SPHERE             | A sphere has been detected with center at object\_pose                                                                                                                                                                                      |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_POINT\_CLOUD       | A Pick-it Teach model has been detected                                                                                                                                                                                                     |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_TYPE\_BLOB               | An object without a specified shape has been detected                                                                                                                                                                                       |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **object\_dimensions**   | **int32[3]**                     | **PICKIT\_TYPE\_SQUARE                                                                                                                                                                                                                      |
|                          | [0]: length or diameter (m)      | **\ [0] and [1] contain the side length of the square                                                                                                                                                                                       |
|                          | [1]: width or diameter (m)       |                                                                                                                                                                                                                                             |
|                          | [2]: height (m)                  | | **PICKIT\_TYPE\_RECTANGLE**                                                                                                                                                                                                               |
|                          |                                  | | [0] and [1] respectively contain the length and width of the rectangle                                                                                                                                                                    |
|                          |                                  |                                                                                                                                                                                                                                             |
|                          |                                  | | **PICKIT\_TYPE\_CIRCLE**                                                                                                                                                                                                                  |
|                          |                                  | | [0] and [1] contain the diameter of the circle                                                                                                                                                                                            |
|                          |                                  |                                                                                                                                                                                                                                             |
|                          |                                  | | **PICKIT\_TYPE\_ELLIPSE**                                                                                                                                                                                                                 |
|                          |                                  | | [0] and [1] respectively contain the length and width of the ellipse                                                                                                                                                                      |
|                          |                                  |                                                                                                                                                                                                                                             |
|                          |                                  | | **PICKIT\_TYPE\_CYLINDER**                                                                                                                                                                                                                |
|                          |                                  | | [0] and [1] respectively contain cylinder length and diameter                                                                                                                                                                             |
|                          |                                  |                                                                                                                                                                                                                                             |
|                          |                                  | | **PICKIT\_TYPE\_SPHERE**                                                                                                                                                                                                                  |
|                          |                                  | | [0] and [1] contain the diameter of the sphere                                                                                                                                                                                            |
|                          |                                  |                                                                                                                                                                                                                                             |
|                          |                                  | | **PICKIT\_TYPE\_POINT\_CLOUD**                                                                                                                                                                                                            |
|                          |                                  | | [0], [1] and [2] respectively contain the length, width and height of the point cloud bounding box                                                                                                                                        |
|                          |                                  |                                                                                                                                                                                                                                             |
|                          |                                  | | **PICKIT\_TYPE\_BLOB**                                                                                                                                                                                                                    |
|                          |                                  | | [0], [1] and [2] respectively contain the length, width and height of the blob bounding box                                                                                                                                               |
|                          |                                  |                                                                                                                                                                                                                                             |
|                          |                                  | When reading array elements, each value has to be divided by the  **MULT** factor.                                                                                                                                                          |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **objects\_remaining**   | **int32**                        | Only one object per pickit\_to\_robot\_data message can be communicated. If this field is non-zero, it contains the number of remaining objects that can be sent in next messages to the robot.                                             |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **status**               | **int32**                        | Contains the Pick-it status or a response to previously received robot commands.                                                                                                                                                            |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_COMMAND\_OK              | Generic all nominal response code.                                                                                                                                                                                                          |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_COMMAND\_FAILED          | Generic error response code.The previous command could not be processed. See log messages for diagnostics.                                                                                                                                  |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_OBJECT\_FOUND            | A pick position has been found                                                                                                                                                                                                              |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | PICKIT\_NO\_OBJECTS              | No objects for picking were detected. See status messages for diagnostics.                                                                                                                                                                  |
+--------------------------+----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Below are the values of the Pick-it status constants communicated by
Pick-it:

.. raw:: html

   </div>

::

         #define PICKIT_RUNNING_MODE                0
         #define PICKIT_IDLE_MODE                   1
         #define PICKIT_CALIBRATION_MODE            2

         #define PICKIT_FIND_CALIB_PLATE_OK        10                   
         #define PICKIT_FIND_CALIB_PLATE_FAILED    11                   
         #define PICKIT_OBJECT_FOUND               20
         #define PICKIT_NO_OBJECTS                 21
         #define PICKIT_NO_IMAGE_CAPTURED          22

         #define PICKIT_CONFIG_OK                  40
         #define PICKIT_CONFIG_FAILED              41
         #define PICKIT_SAVE_SCENE_OK              50
         #define PICKIT_SAVE_SCENE_FAILED          51

Below are the values of the object type constants communicated by
Pick-it:

::

        #define PICKIT_TYPE_SQUARE               21
        #define PICKIT_TYPE_RECTANGLE            22
        #define PICKIT_TYPE_CIRCLE               23
        #define PICKIT_TYPE_ELLIPSE              24
        #define PICKIT_TYPE_CYLINDER             32
        #define PICKIT_TYPE_SPHERE               33
        #define PICKIT_TYPE_POINT_CLOUD          35 ## See remark below for Teach on 1.9+ versions
        #define PICKIT_TYPE_BLOB                 50

.. raw:: html

   <div class="callout-yellow">

From version 1.9+, ``PICKIT_TYPE_POINT_CLOUD`` is no longer 35 with the
Pick-it Teach detection engine, but representing the ID Teach model the
object was detected from.

.. raw:: html

   </div>

4. Message metadata
-------------------

To guarantee correct interpretation of the data on both the robot and
the Pick-it side, the following metadata is always sent along with the
structures:

::

        struct meta_data {
            int32 robot_type;
            int32 interface_version;
        };

Each field is explained below. All **int32** are expressed in Network
Byte Format.

.. raw:: html

   <div>

+--------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field name               | Type / units   | Comment                                                                                                                                                |
+==========================+================+========================================================================================================================================================+
| **robot\_type**          | **int32**      | The type of robot Pick-it is connected to:                                                                                                             |
|                          |                | **1:** UNIVERSAL ROBOT → Angle-axis                                                                                                                    |
|                          |                | | **2:** ABB, **GENERIC** → Quaternions (w,x,y,z)                                                                                                      |
|                          |                | | **3:** STAUBLI → Euler Angles (x-y’-z”)                                                                                                              |
|                          |                | | **4:** FANUC, YASKAWA → Fixed Angles (x-y-z)                                                                                                         |
|                          |                | | **5:** KUKA → Euler Angles (z-y’-x”)                                                                                                                 |
|                          |                | | **6:** COMAU → Euler Angles (z-y’-z”)                                                                                                                |
+--------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **interface\_version**   | **int32**      | The version of the robot-Pick-it communication. To get this number, all dots are removed from the actual version number. Example: Version 1.1 -> 11    |
+--------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

To add support for a robot type not adhering to one of the above
conventions, it's recommended to use the **GENERIC** (quaternions)
convention above. The robot-side interface would then take the
responsibility of converting back and forth between the representation
used by Pick-it and the robot.

.. raw:: html

   </div>

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5902f34d2c7d3a057f88a379/file-DAUfHg1N0f.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ac63f772c7d3a0e93670bf5/file-8aIct5CwLA.png
