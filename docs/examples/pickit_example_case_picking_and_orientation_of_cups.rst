Pick-it example case: Picking and orientation of cups
=====================================================

|image0|

This article covers an extensive overview of an actual Pick-it
application where picking and orientation is verified during every cycle
of the robot program. We cover the basics of the application as well as
the robot program used in this application.

#. `Intro (flowchart & step by step) <#intro>`__
#. `A program of 7 steps <#steps>`__
#. `A generic way of explaining the robot program <#genericway>`__
#. `The Universal Robots program <#urprogram>`__

1. Intro
--------

In this application we will try to pick a cylindrical cup form a bin and
perform an orientation check on the cup before putting it next to the
bin.

The bin picking is done by looking first for circles and when no circles
are found, looking for cylinders. 

The orientation of the cups is done by looking for a circle when the cup
was initially detected and picked as a cylinder and looking for a
cylinder when the cup was initially detected and picked as a circle.

So we have already created and saved 2 Pick-it setup files and 4 Pick-it
product files through the Pick-it interface.

Two setup files
^^^^^^^^^^^^^^^

#. One setup file for bin picking (where the blue region of interest box
   is aligned with the bin)
#. One setup file for the orientation check (where the blue region of
   interest box is closer to the camera above the bin)

Four product files
^^^^^^^^^^^^^^^^^^

#. One product file for finding cylinders in the bin
#. One product file for finding circles in the bin
#. One for finding cylinders during the orientation check
#. One for finding circles during the orientation check

Collision prevention is only enabled for the bin picking product files
and not in the product files for the orientation check.

Flowchart
~~~~~~~~~

|image1|
~~~~~~~~

Step by step:
~~~~~~~~~~~~~

Pick-it looks for circles and detects 3. 

|image2|

Pick-it will only start to search for cylinders when no circles can be
detected anymore or all detected circles are not reachable to the robot.

Search for cylinders and detects 1. 

|image3|

.. raw:: html

   <div>

After being picked, the product is shown to the camera. Then a region of
interest box (virtual blue box) is marked in the space right in front of
the robot tool. 

.. raw:: html

   </div>

.. raw:: html

   <div>

|image4|

.. raw:: html

   </div>

.. raw:: html

   <div>

In the case that the cup was initially detect as a circle and the robot
is grasping the cup from its bottom side, the cup does not enter the
region of interest and so no detection is made by Pick-it.  

.. raw:: html

   </div>

.. raw:: html

   <div>

|image5|

.. raw:: html

   </div>

.. raw:: html

   <div>

In the case that the cup was initially detect as a circle and and the
robot is grasping the cup from its top side the lateral sides of the cup
enter the ROI box, allowing Pick-it to see a cylinder. 

.. raw:: html

   </div>

.. raw:: html

   <div>

|image6|

.. raw:: html

   </div>

.. raw:: html

   <div>

If the cup was grasped lying on its side, either its top or bottom side
is shown to the camera in the orientation check. 

.. raw:: html

   </div>

.. raw:: html

   <div>

If the bottom is showed, Pick-it detects a circle.

.. raw:: html

   </div>

.. raw:: html

   <div>

|image7|

.. raw:: html

   </div>

.. raw:: html

   <div>

In the case the other side is showed, Pick-it detects nothing, as the
cup lateral sides hide a large part of the circular base.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   <div>

|image8|\ After a successful orientation check, there are 4 ways to drop
off the cup. Two for cups with the top side pointing up and another two
for cups with the top side pointing down.

.. raw:: html

   </div>

.. raw:: html

   <div>

|image9|

.. raw:: html

   </div>

.. raw:: html

   </div>

2. A program of 7 steps
-----------------------

This application could be build with a robot program which we will split
into 7 major steps. We will explain every step more extensively in the
next chapter.

The 7 steps are:

#. Declare variables and load scripts
#. Move to a starting position
#. Look for an object
#. Pick an object
#. Check orientation of the object and drop object
#. Switch the kind of object Pick-it is looking for if no objects are
   safe to pick 
#. Switch the kind of object Pick-it is looking for if no objects are
   found 

3. A generic way of explaining the program
------------------------------------------

Here we explain all the steps of the program in a generic way and
language to introduce the different Pick-it commands used for this
application.

All **Pick-it specific commands are marked green** and **all waypoints
are marked blue**.

|image10|

You can view \ `a printable version of this generic program
here <https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/attachments/588a247add8c8e73b3e9090a/illustratie-robot-program.pdf>`__.

4. The Universal Robots program
-------------------------------

The actual used robot program is a program for a Universal Robot.

First we show the whole program and below we again split every step up
into the 7 major steps to explain every aspect of every step.

Whole Universal Robots program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    Program
      Init Variables
      BeforeStart
        pickit_port=5001
        pickit_ip="169.254.5.180"
        actual_pose=get_target_tcp_pose()
        pick_pose=p[0,0,0,0,0,0]
        pre_pick_offset=p[0,0,-0.1,0,0,0]
        setup_bin=354
        setup_check=201
        prod_cir_bin=164
        prod_cyl_bin=299
        prod_cir_check=44
        prod_cyl_check=343
        prod_bin=prod_cir_bin
        prod_check=prod_cyl_check
        pre_pick_ok= False 
        pick_ok= False 
        Script: pickit_functions
        pickit_socket_open()
        Script: pickit_communication
        Script: pickit_transformations
      Robot Program
        MoveJ
          actual_pose
          wp_home
        Loop pickit_is_running()
          pickit_configure(setup_bin,prod_bin)
          pickit_look_for_object()
          Wait pickit_has_response()
          If pickit_object_found()
            pick_pose=pickit_get_pose(False)
            pre_pick_pose=pose_trans(pick_pose, pre_pick_offset)
            MoveL
              pre_pick_ok=is_within_safety_limits(pre_pick_pose)
              If pre_pick_ok
                pre_pick_pose
                pick_ok=is_within_safety_limits(pick_pose)
                If pick_ok
                  Set magnet_ON=On
                  pick_pose
                  Wait: 0.5
              If pre_pick_ok and pick_ok
                wp_pre_check
                wp_check
                pickit_configure(setup_check,prod_check)
                pickit_look_for_object()
                Wait pickit_has_response()
                wp_pre_check
                wp_pre_drop
                If prod_check=prod_cyl_check
                  If pickit_object_found()
                    wp_pre_topup
                    wp_cyl_topup
                    Wait: 0.2
                    Set magnet_ON=Off
                    Wait: 0.2
                    wp_pre_topup
                    wp_pre_drop
                    pickit_configure(setup_bin,prod_bin)
                    pickit_look_for_object()                 
                  Else
                    wp_pre_topdown
                    wp_cyl_topdown
                    Wait: 0.2
                    Set magnet_ON=Off
                    Wait: 0.2
                    wp_pre_topdown
                    wp_pre_drop
                    pickit_configure(setup_bin,prod_bin)
                    pickit_look_for_object()                  
                ElseIf prod_check=prod_cir_check
                  If pickit_object_found()
                    wp_pre_topup
                    wp_cir_topup
                    Wait: 0.2
                    Set magnet_ON=Off
                    Wait: 0.2
                    wp_pre_topup
                    wp_pre_drop
                    pickit_configure(setup_bin,prod_bin)
                    pickit_look_for_object()                 
                  Else
                    wp_pre_topdown
                    wp_cir_topdown
                    Wait: 0.2
                    Set magnet_ON=Off
                    Wait: 0.2
                    wp_pre_topdown
                    wp_pre_drop
                    pickit_configure(setup_bin,prod_bin)
                    pickit_look_for_object() 
              Else
                If pickit_remaining_objects()=0
                  wp_home
                  If prod_bin=prod_cir_bin
                    prod_bin=prod_cyl_bin
                    prod_check=prod_cir_check
                  ElseIf prod_bin=prod_cyl_bin
                    prod_bin=prod_cir_bin
                    prod_check=prod_cyl_check
                Else
                  pickit_next_object()
          Else
            If prod_bin=prod_cir_bin
              prod_bin=prod_cyl_bin
              prod_check=prod_cir_check
            ElseIf prod_bin=prod_cyl_bin
              prod_bin=prod_cir_bin
              prod_check=prod_cyl_check
        pickit_socket_close()

Split up Universal Robots program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Declare variables and load scripts 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    Program
      Init Variables
      BeforeStart
        pickit_port=5001
        pickit_ip="169.254.5.180"
        actual_pose=get_target_tcp_pose()
        pick_pose=p[0,0,0,0,0,0]
        pre_pick_offset=p[0,0,-0.1,0,0,0]
        setup_bin=354
        setup_check=201
        prod_cir_bin=164
        prod_cyl_bin=299
        prod_cir_check=44
        prod_cyl_check=343
        prod_bin=prod_cir_bin
        prod_check=prod_cyl_check
        pre_pick_ok= False 
        pick_ok= False 
        Script: pickit_functions
        pickit_socket_open()
        Script: pickit_communication
        Script: pickit_transformations

Here we first start the program (line 1), and then before the actual
start of the program declare some variables and load some scripts.

The **pickit\_port** and **pickit\_ip** must be set to their correct
values to enable communication between the robot and Pick-it.

The pose of the next detected object to be picked shall be stored in the
pose variable **pick\_pose**. For each pick, it is intended that the
tool briefly goes to an intermediary position above the actual
**pick\_pose**, before picking the object. The **pre\_pick\_offset**
defines this offset and will be used later, adding a negative
translational component to the z-axis of the tool.

From line 9 untill 16 we assign certain Pick-it setup file numbers and
product file numbers to variables. 

On line 19, 21 and 22 scripts containing relevant Pick-it functions are
loaded.

2. Move to a starting position
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

      Robot Program
        MoveJ
          actual_pose
          wp_home

Here we **MoveJ** the robot via and intermediate **actual\_pose**
position to a waypoint called **wp\_home**.

3. Look for an object
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

        Loop pickit_is_running()
          pickit_configure(setup_bin,prod_bin)
          pickit_look_for_object()
          Wait pickit_has_response()

On line 27 a loop that will keep on as long as Pick-it is running is
started.

On line 28 the script commands Pick-it load the setup file associated
with the variable **setup\_bin** and the product file associated with
the variable **prod\_bin**. (**pickit\_configure**)

On line 29 the commands Pick-it to look for objects. (
**pickit\_look\_for\_object()**)

On line 30 we make the robot program to wait until Pick-it has send a
response on the  **pickit\_look\_for\_object()** command.
(**pickit\_has\_response**)

4. Pick object
^^^^^^^^^^^^^^

.. code-block:: bash

          If pickit_object_found()
            pick_pose=pickit_get_pose(False)
            pre_pick_pose=pose_trans(pick_pose, pre_pick_offset)
            MoveL
              pre_pick_ok=is_within_safety_limits(pre_pick_pose)
              If pre_pick_ok
                pre_pick_pose
                pick_ok=is_within_safety_limits(pick_pose)
                If pick_ok
                  Set magnet_ON=On
                  pick_pose
                  Wait: 0.5

If Pick-it found an object the command  **pickit\_object\_found()**
equals true.

On line 32 we declare the variable **pick\_pose** equals the just
received **pickit\_get\_pose**. In other words: **pick\_pose** now
equals the pose where Pick-it told us the object can be picked.

On line 33 we the variable **pre\_pick\_pose** as a new pose that equals
the **pick\_pose** added with the predefined **pre\_pick\_offset** (in
this case -10cm in the Z direction). Like this the **pre\_pick\_pose**
will always be 10cm above the **pick\_pose** of a detected object.

On line 34 the robot is commanded to start moving ( **MoveL**) the
robot, but only if the **pre\_pick\_pose** is within the safety limits
of the robot (= if it is reachable and safe according to the robot).

So if the **pre\_pick\_pose** is safe the robot moves there.

On line 38 we check if the **pick\_pose** provided by Pick-it is within
the safety limits of the robot (= if it is reachable and safe according
to the robot).

If this is the case the magnet on the end effector is switched on and
the robot moves to the **pick\_pose**. (line 41)

A wait of 0.5 seconds is added to give the magnet some time to really
grasp the object.

5. Check orientation of object and drop object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

              If pre_pick_ok and pick_ok
                wp_pre_check
                wp_check
                pickit_configure(setup_check,prod_check)
                pickit_look_for_object()
                Wait pickit_has_response()
                wp_pre_check
                wp_pre_drop
                If prod_check=prod_cyl_check
                  If pickit_object_found()
                    wp_pre_topup
                    wp_cyl_topup
                    Wait: 0.2
                    Set magnet_ON=Off
                    Wait: 0.2
                    wp_pre_topup
                    wp_pre_drop
                    pickit_configure(setup_bin,prod_bin)
                    pickit_look_for_object()                 
                  Else
                    wp_pre_topdown
                    wp_cyl_topdown
                    Wait: 0.2
                    Set magnet_ON=Off
                    Wait: 0.2
                    wp_pre_topdown
                    wp_pre_drop
                    pickit_configure(setup_bin,prod_bin)
                    pickit_look_for_object()                  
                ElseIf prod_check=prod_cir_check
                  If pickit_object_found()
                    wp_pre_topup
                    wp_cir_topup
                    Wait: 0.2
                    Set magnet_ON=Off
                    Wait: 0.2
                    wp_pre_topup
                    wp_pre_drop
                    pickit_configure(setup_bin,prod_bin)
                    pickit_look_for_object()                 
                  Else
                    wp_pre_topdown
                    wp_cir_topdown
                    Wait: 0.2
                    Set magnet_ON=Off
                    Wait: 0.2
                    wp_pre_topdown
                    wp_pre_drop
                    pickit_configure(setup_bin,prod_bin)
                    pickit_look_for_object()

In this step we check the orientation of the picked object by doing some
checks which we explain here.

First the robot moves to a waypoint **wp\_check** via an intermediate
point **wp\_pre\_check** (lines 44 and 45).

On line 46 the script commands Pick-it to load the setup file associated
with the variable **setup\_check** and the product file associated with
the variable **prod\_check**.

Then on line 47 the script commands Pick-it to look for an object, again
we wait until there is a response of Pick-it coming in.

The next step is that the robot moves to a waypoint 
**wp\_pre\_check** via an intermediate point \ **wp\_pre\_drop** (lines
49 and 50).

Now the real logic behind the orientation check starts:

#. If Pick-it was looking for a **cylinder** and Pick-it **found an
   object** we know it was oriented with the top up and drop it of on
   **wp\_cyl\_topup** via **wp\_pre\_topup** (lines 51 to 61)
#. If Pick-it was looking for a **cylinder** and Pick-it **did not
   find** **an object** we know it was oriented with the top down and
   drop it of on **wp\_cyl\_topdown** via **wp\_pre\_topdown**. (line 51
   and 62 to 71)
#. If Pick-it was looking for a **circle** and Pick-it **found an
   object** we know it was oriented with the top up and drop it of on
   **wp\_cir\_topup** via **wp\_pre\_topup**. (lines 72 to 82)
#. If Pick-it was looking for a \ **circle** and Pick-it\ ** did not
   find an object **\ we know it was oriented with the top down and drop
   it of on **wp\_cir\_topdown** via **wp\_pre\_topdown**. (line 72 and
   83 to 92)

In all 4 cases we do a short wait of 0.2 seconds, then but the magnet
off, wait again 0.2 seconds and move to  **wp\_pre\_drop** via an
intermediate waypoint depending on the drop off waypoint.

6. Switch the kind of object Pick-it is looking for if no products are safe to pick
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

              Else
                If pickit_remaining_objects()=0
                  wp_home
                  If prod_bin=prod_cir_bin
                    prod_bin=prod_cyl_bin
                    prod_check=prod_cir_check
                  ElseIf prod_bin=prod_cyl_bin
                    prod_bin=prod_cir_bin
                    prod_check=prod_cyl_check
                Else
                  pickit_next_object()

In the case Pick-it found object, but the objects Pick-it found are not
safe to be picked (for reason of reachability of safety), we switch the
kind of objects Pick-it was looking for. We switch from cylinders to
circles if we were looking for cylinders and form circles to cylinders
if we were looking for circles.

7. Switch the kind of object Pick-it is looking for if no products are found
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

          Else
            If prod_bin=prod_cir_bin
              prod_bin=prod_cyl_bin
              prod_check=prod_cir_check
            ElseIf prod_bin=prod_cyl_bin
              prod_bin=prod_cir_bin
              prod_check=prod_cyl_check

In the case Pick-it did not find any objects (after the command on line
29), we switch the kind of objects Pick-it was looking for. We
switch from cylinders to circles if we were looking for cylinders and
form circles to cylinders if we were looking for circles.

.. code-block:: bash

        pickit_socket_close()

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/588a571f2c7d3a78463056a8/file-j0Uau20DmW.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/588b4256dd8c8e73b3e911d8/file-i0Q7OFfX6A.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/588a22b62c7d3a78463054f1/file-BxLt5GgMVA.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/588a221ddd8c8e73b3e908f3/file-bOJUaD5AR4.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/588a2229dd8c8e73b3e908f4/file-BDzxdnPWOD.png
.. |image5| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/588a2395dd8c8e73b3e90901/file-oc9RgSzBYt.png
.. |image6| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/588a2271dd8c8e73b3e908f7/file-a7fbB755aD.png
.. |image7| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/588a23f52c7d3a7846305502/file-9OhOjw6KzU.png
.. |image8| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/588a236f2c7d3a78463054fb/file-fWM8hzui6A.png
.. |image9| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/588b3df8dd8c8e73b3e911c2/file-kxnGJgruLz.png
.. |image10| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/588a547edd8c8e73b3e90a9b/file-TSVDXyL0rm.png

