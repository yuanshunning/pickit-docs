The Pick-it functions cheat sheet
=================================

| **Note** This article describes the legacy way of using Pick-it with a
  Universal Robot.
| For new systems, please refer to the  `Getting started with the
  Pick-it
  URCap <https://support.pickit3d.com/article/75-getting-started-with-the-pick-it-urcap>`__
  article.

Pick-it provides many functions to script your Pick-it application to a
success. Underneath we provide an overview of the provided functions:

`pickit\_is\_running() <#pickit_is_running>`__,
`pickit\_can\_calibrate() <#pickit_can_calibrate>`__,
`pickit\_save\_scene() <#pickit_save_scene>`__,
`pickit\_find\_calib\_plate() <#pickit_find_calib_plate>`__,
`pickit\_configure(setup,product) <#pickit_configure>`__,
`pickit\_look\_for\_object() <#pickit_look_for_object>`__,
`pickit\_next\_object() <#pickit_next_object>`__,
`pickit\_has\_response() <#pickit_has_response>`__,
`pickit\_object\_found() <#pickit_object_found>`__,
`pickit\_no\_image\_captured() <#pickit_no_image_captured>`__,
`pickit\_remaining\_objects() <#pickit_remaining_objects>`__,
`pickit\_get\_pose() <#pickit_get_pose>`__

Intro
-----

.. raw:: html

   <div>

We differentiate two different kinds of functions:

.. raw:: html

   </div>

-  **Blocking functions: **\ These functions send a command to Pick-it
   and waits until a response is received. 
-  **Stopping functions:** These functions force the robot program to
   stop in case it returns false. Note that the return value is never
   used in case the robot program is stopped.
-  **Non-blocking functions**: This is
   `pickit\_look\_for\_object() <#pickit_look_for_object>`__ and
   `pickit\_next\_object() <#pickit_next_object>`__. These functions
   only send a command to Pick-it and immediately return. Waiting for a
   response has to happen in another line/function. The motivation for
   that is that the
   `pickit\_look\_for\_object() <#pickit_look_for_object>`__ function
   does not result in an immediate answer due to the detection taking
   time. By having this function non-blocking, the robot or control
   process can do something else before waiting for the response.

Pick-it functions
-----------------

pickit\_is\_running()
~~~~~~~~~~~~~~~~~~~~~

Request Pick-it if Pick-it is in Running state.

+-----------------+------------------------+-----------+
| **Behaviour**   | **Universal robots**   | **ABB**   |
+=================+========================+===========+
| Blocking        | Yes                    | Yes       |
+-----------------+------------------------+-----------+
| Return value    | Boolean                | Boolean   |
+-----------------+------------------------+-----------+
| Stopping        | No + popup             | No        |
+-----------------+------------------------+-----------+

pickit\_can\_calibrate()
~~~~~~~~~~~~~~~~~~~~~~~~

Request Pick-it if Pick-it is in Calibration state. (the Robot setup
page is active in the Pick-it web interface)

+-----------------+------------------------+-----------+
| **Behaviour**   | **Universal robots**   | **ABB**   |
+=================+========================+===========+
| Blocking        | Yes                    | Yes       |
+-----------------+------------------------+-----------+
| Return value    | Boolean                | Boolean   |
+-----------------+------------------------+-----------+
| Stopping        | No                     | No        |
+-----------------+------------------------+-----------+

pickit\_save\_scene()
~~~~~~~~~~~~~~~~~~~~~

Request Pick-it to save the latest image and configurations into a
file. 

+-----------------+------------------------+-----------+
| **Behaviour**   | **Universal robots**   | **ABB**   |
+=================+========================+===========+
| Blocking        | Yes                    | Yes       |
+-----------------+------------------------+-----------+
| Return value    | Boolean                | Boolean   |
+-----------------+------------------------+-----------+
| Stopping        | No + popup             | No        |
+-----------------+------------------------+-----------+

pickit\_find\_calib\_plate()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request Pick-it to localise the Pick-it camera-to-robot calibration
plate.

+-----------------+------------------------+-----------+
| **Behaviour**   | **Universal robots**   | **ABB**   |
+=================+========================+===========+
| Blocking        | Yes                    | Yes       |
+-----------------+------------------------+-----------+
| Return value    | Boolean                | -         |
+-----------------+------------------------+-----------+
| Stopping        | No + popup             | Yes       |
+-----------------+------------------------+-----------+

pickit\_configure(setup, product)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request Pick-it to load and use a specific setup and product type.

+-----------------+------------------------+-----------+
| **Behaviour**   | **Universal robots**   | **ABB**   |
+=================+========================+===========+
| Blocking        | Yes                    | Yes       |
+-----------------+------------------------+-----------+
| Return value    | Boolean                | -         |
+-----------------+------------------------+-----------+
| Stopping        | Yes + popup            | Yes       |
+-----------------+------------------------+-----------+

pickit\_look\_for\_object()
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request Pick-it to look for objects.

+-----------------+------------------------+-----------+
| **Behaviour**   | **Universal robots**   | **ABB**   |
+=================+========================+===========+
| Blocking        | No                     | No        |
+-----------------+------------------------+-----------+
| Return value    | -                      | -         |
+-----------------+------------------------+-----------+
| Stopping        | No                     | No        |
+-----------------+------------------------+-----------+

pickit\_next\_object()
~~~~~~~~~~~~~~~~~~~~~~

Request Pick-it to return the next object stored in the Pick-it buffer
which was found before with pickit\_look\_for\_object()

+-----------------+------------------------+-----------+
| **Behaviour**   | **Universal robots**   | **ABB**   |
+=================+========================+===========+
| Blocking        | No                     | No        |
+-----------------+------------------------+-----------+
| Return value    | -                      | -         |
+-----------------+------------------------+-----------+
| Stopping        | No                     | No        |
+-----------------+------------------------+-----------+

pickit\_has\_response()
~~~~~~~~~~~~~~~~~~~~~~~

Check if a response is received after sending
pickit\_look\_for\_object() or pickit\_next\_object().

+-----------------+------------------------+-----------+
| **Behaviour**   | **Universal robots**   | **ABB**   |
+=================+========================+===========+
| Blocking        | Yes                    | Yes       |
+-----------------+------------------------+-----------+
| Return value    | Boolean                | Boolean   |
+-----------------+------------------------+-----------+
| Stopping        | No                     | No        |
+-----------------+------------------------+-----------+

pickit\_object\_found()
~~~~~~~~~~~~~~~~~~~~~~~

Check if any objects are present in the Pick-it buffer.

+-----------------+------------------------+-----------+
| **Behaviour**   | **Universal robots**   | **ABB**   |
+=================+========================+===========+
| Blocking        | No                     | No        |
+-----------------+------------------------+-----------+
| Return value    | Boolean                | Boolean   |
+-----------------+------------------------+-----------+
| Stopping        | No                     | No        |
+-----------------+------------------------+-----------+

pickit\_no\_image\_captured()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check if Pick-it was able to capture an image.

+-----------------+------------------------+-----------+
| **Behaviour**   | **Universal robots**   | **ABB**   |
+=================+========================+===========+
| Blocking        | No                     | No        |
+-----------------+------------------------+-----------+
| Return value    | Boolean                | Boolean   |
+-----------------+------------------------+-----------+
| Stopping        | No                     | No        |
+-----------------+------------------------+-----------+

pickit\_remaining\_objects()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check the number of remaining objects in the Pick-it buffer.

+-----------------+------------------------+-----------+
| **Behaviour**   | **Universal robots**   | **ABB**   |
+=================+========================+===========+
| Blocking        | No                     | No        |
+-----------------+------------------------+-----------+
| Return value    | Integer                | Integer   |
+-----------------+------------------------+-----------+
| Stopping        | No                     | No        |
+-----------------+------------------------+-----------+

pickit\_get\_pose()
~~~~~~~~~~~~~~~~~~~

Request Pick-it for the pick pose of the first object in the Pick-it
buffer. 

+-----------------+--------------------------------------+-----------+
| **Behaviour**   | **Universal robots**                 | **ABB**   |
+=================+======================================+===========+
| Blocking        | No                                   | -         |
+-----------------+--------------------------------------+-----------+
| Return value    | Pose (3 translations, 3 rotations)   | -         |
+-----------------+--------------------------------------+-----------+
| Stopping        | No                                   | -         |
+-----------------+--------------------------------------+-----------+
