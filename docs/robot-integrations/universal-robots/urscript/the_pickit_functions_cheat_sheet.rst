The Pickit functions cheat sheet
=================================

| **Note** This article describes the legacy way of using Pickit with a
  Universal Robot.
| For new systems, please refer to the  `Getting started with the
  Pickit
  URCap <https://support.pickit3d.com/article/75-getting-started-with-the-pick-it-urcap>`__
  article.

Pickit provides many functions to script your Pickit application to a
success. Underneath we provide an overview of the provided functions:

`pickit\_is\_running() <pickit\_is\_running()_>`__,
`pickit\_can\_calibrate() <pickit\_can\_calibrate()_>`__,
`pickit\_save\_scene() <pickit\_save\_scene()_>`__,
`pickit\_find\_calib\_plate() <pickit\_find\_calib\_plate()_>`__,
`pickit\_configure(setup,product) <pickit\_configure(setup, product)_>`__,
`pickit\_look\_for\_object() <pickit\_look\_for\_object()_>`__,
`pickit\_next\_object() <pickit\_next\_object()_>`__,
`pickit\_has\_response() <pickit\_has\_response()_>`__,
`pickit\_object\_found() <pickit\_object\_found()_>`__,
`pickit\_no\_image\_captured() <pickit\_no\_image\_captured()_>`__,
`pickit\_remaining\_objects() <pickit\_remaining\_objects()_>`__,
`pickit\_get\_pose() <pickit\_get\_pose()_>`__

Intro
-----

We differentiate two different kinds of functions:

-  **Blocking functions:** These functions send a command to Pickit
   and waits until a response is received. 
-  **Stopping functions:** These functions force the robot program to
   stop in case it returns false. Note that the return value is never
   used in case the robot program is stopped.
-  **Non-blocking functions**: This is
   `pickit\_look\_for\_object() <#pickit_look_for_object>`__ and
   `pickit\_next\_object() <#pickit_next_object>`__. These functions
   only send a command to Pickit and immediately return. Waiting for a
   response has to happen in another line/function. The motivation for
   that is that the
   `pickit\_look\_for\_object() <#pickit_look_for_object>`__ function
   does not result in an immediate answer due to the detection taking
   time. By having this function non-blocking, the robot or control
   process can do something else before waiting for the response.

Pickit functions
-----------------

pickit\_is\_running()
~~~~~~~~~~~~~~~~~~~~~

Request Pickit if Pickit is in Running state.

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

Request Pickit if Pickit is in Calibration state. (the Robot setup
page is active in the Pickit web interface)

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

Request Pickit to save the latest image and configurations into a
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

Request Pickit to localise the Pickit camera-to-robot calibration
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

Request Pickit to load and use a specific setup and product type.

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

Request Pickit to look for objects.

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

Request Pickit to return the next object stored in the Pickit buffer
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

Check if any objects are present in the Pickit buffer.

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

Check if Pickit was able to capture an image.

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

Check the number of remaining objects in the Pickit buffer.

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

Request Pickit for the pick pose of the first object in the Pickit
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
