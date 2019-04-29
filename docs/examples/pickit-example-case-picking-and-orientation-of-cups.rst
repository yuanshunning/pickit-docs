Pickit example case: Picking and orientation of cups
=====================================================

.. image:: /assets/images/examples/example-case-cups-general.png

This article covers an extensive overview of an actual Pickit
application where picking and orientation is verified during every cycle
of the robot program. We cover the basics of the application as well as
the robot program used in this application.

.. contents::
    :backlinks: top
    :local:
    :depth: 1

Intro
-----

In this application we will try to pick a cylindrical cup form a bin and
perform an orientation check on the cup before putting it next to the
bin.

The bin picking is done by looking first for circles and when no circles
are found, looking for cylinders. 

The orientation of the cups is done by looking for a circle when the cup
was initially detected and picked as a cylinder and looking for a
cylinder when the cup was initially detected and picked as a circle.

So we have already created and saved 2 Pickit setup files and 4 Pickit
product files through the Pickit interface.

Two setup files
~~~~~~~~~~~~~~~

#. One setup file for bin picking (where the blue region of interest box
   is aligned with the bin)
#. One setup file for the orientation check (where the blue region of
   interest box is closer to the camera above the bin)

Four product files
~~~~~~~~~~~~~~~~~~

#. One product file for finding cylinders in the bin
#. One product file for finding circles in the bin
#. One for finding cylinders during the orientation check
#. One for finding circles during the orientation check

Collision prevention is only enabled for the bin picking product files
and not in the product files for the orientation check.

Flowchart
~~~~~~~~~

.. image:: /assets/images/examples/example-case-cups-flow.png

Step by step:
~~~~~~~~~~~~~

Pickit looks for circles and detects 3. 

.. image:: /assets/images/examples/example-case-cups-step-1.png

Pickit will only start to search for cylinders when no circles can be
detected anymore or all detected circles are not reachable to the robot.

Search for cylinders and detects 1. 

.. image:: /assets/images/examples/example-case-cups-step-2.png

After being picked, the product is shown to the camera. Then a region of
interest box (virtual blue box) is marked in the space right in front of
the robot tool. 

.. image:: /assets/images/examples/example-case-cups-step-3.png

In the case that the cup was initially detect as a circle and the robot
is grasping the cup from its bottom side, the cup does not enter the
region of interest and so no detection is made by Pickit.  

.. image:: /assets/images/examples/example-case-cups-step-4.png

In the case that the cup was initially detect as a circle and and the
robot is grasping the cup from its top side the lateral sides of the cup
enter the ROI box, allowing Pickit to see a cylinder. 

.. image:: /assets/images/examples/example-case-cups-step-5.png

If the cup was grasped lying on its side, either its top or bottom side
is shown to the camera in the orientation check. 

If the bottom is showed, Pickit detects a circle.

.. image:: /assets/images/examples/example-case-cups-step-6.png

In the case the other side is showed, Pickit detects nothing, as the
cup lateral sides hide a large part of the circular base.

.. image:: /assets/images/examples/example-case-cups-step-7.png

After a successful orientation check, there are 4 ways to drop
off the cup. Two for cups with the top side pointing up and another two
for cups with the top side pointing down.

.. image:: /assets/images/examples/example-case-cups-step-8.png

A program of 7 steps
--------------------

This application could be build with a robot program which we will split
into 7 major steps. We will explain every step more extensively in the
next chapter.

The 7 steps are:

#. Declare variables and load scripts
#. Move to a starting position
#. Look for an object
#. Pick an object
#. Check orientation of the object and drop object
#. Switch the kind of object Pickit is looking for if no objects are
   safe to pick 
#. Switch the kind of object Pickit is looking for if no objects are
   found 

A generic way of explaining the program
---------------------------------------

Here we explain all the steps of the program in a generic way and
language to introduce the different Pickit commands used for this
application.

All **Pickit specific commands are marked green** and **all waypoints
are marked blue**.

.. image:: /assets/images/examples/example-case-cups-program.png

You can view `a printable version of this generic program
here <https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/attachments/588a247add8c8e73b3e9090a/illustratie-robot-program.pdf>`__.

The Universal Robots program
----------------------------

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

The **pickit_port** and **pickit_ip** must be set to their correct
values to enable communication between the robot and Pickit.

The pose of the next detected object to be picked shall be stored in the
pose variable **pick_pose**. For each pick, it is intended that the
tool briefly goes to an intermediary position above the actual
**pick_pose**, before picking the object. The **pre_pick_offset**
defines this offset and will be used later, adding a negative
translational component to the z-axis of the tool.

From line 9 untill 16 we assign certain Pickit setup file numbers and
product file numbers to variables. 

On line 19, 21 and 22 scripts containing relevant Pickit functions are
loaded.

2. Move to a starting position
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

      Robot Program
        MoveJ
          actual_pose
          wp_home

Here we **MoveJ** the robot via and intermediate **actual_pose**
position to a waypoint called **wp_home**.

3. Look for an object
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

        Loop pickit_is_running()
          pickit_configure(setup_bin,prod_bin)
          pickit_look_for_object()
          Wait pickit_has_response()

On line 27 a loop that will keep on as long as Pickit is running is
started.

On line 28 the script commands Pickit load the setup file associated
with the variable **setup_bin** and the product file associated with
the variable **prod_bin**. (**pickit_configure**)

On line 29 the commands Pickit to look for objects. (
**pickit_look_for_object()**)

On line 30 we make the robot program to wait until Pickit has send a
response on the  **pickit_look_for_object()** command.
(**pickit_has_response**)

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

If Pickit found an object the command  **pickit_object_found()**
equals true.

On line 32 we declare the variable **pick_pose** equals the just
received **pickit_get_pose**. In other words: **pick_pose** now
equals the pose where Pickit told us the object can be picked.

On line 33 we the variable **pre_pick_pose** as a new pose that equals
the **pick_pose** added with the predefined **pre_pick_offset** (in
this case -10cm in the Z direction). Like this the **pre_pick_pose**
will always be 10cm above the **pick_pose** of a detected object.

On line 34 the robot is commanded to start moving ( **MoveL**) the
robot, but only if the **pre_pick_pose** is within the safety limits
of the robot (= if it is reachable and safe according to the robot).

So if the **pre_pick_pose** is safe the robot moves there.

On line 38 we check if the **pick_pose** provided by Pickit is within
the safety limits of the robot (= if it is reachable and safe according
to the robot).

If this is the case the magnet on the end effector is switched on and
the robot moves to the **pick_pose**. (line 41)

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

First the robot moves to a waypoint **wp_check** via an intermediate
point **wp_pre_check** (lines 44 and 45).

On line 46 the script commands Pickit to load the setup file associated
with the variable **setup_check** and the product file associated with
the variable **prod\_check**.

Then on line 47 the script commands Pickit to look for an object, again
we wait until there is a response of Pickit coming in.

The next step is that the robot moves to a waypoint 
**wp_pre_check** via an intermediate point **wp_pre_drop** (lines
49 and 50).

Now the real logic behind the orientation check starts:

#. If Pickit was looking for a **cylinder** and Pickit **found an
   object** we know it was oriented with the top up and drop it of on
   **wp_cyl_topup** via **wp_pre_topup** (lines 51 to 61)
#. If Pickit was looking for a **cylinder** and Pickit **did not
   find** **an object** we know it was oriented with the top down and
   drop it of on **wp_cyl_topdown** via **wp_pre_topdown**. (line 51
   and 62 to 71)
#. If Pickit was looking for a **circle** and Pickit **found an
   object** we know it was oriented with the top up and drop it of on
   **wp_cir_topup** via **wp_pre_topup**. (lines 72 to 82)
#. If Pickit was looking for a **circle** and Pickit **did not
   find an object** we know it was oriented with the top down and drop
   it of on **wp_cir_topdown** via **wp_pre_topdown**. (line 72 and
   83 to 92)

In all 4 cases we do a short wait of 0.2 seconds, then but the magnet
off, wait again 0.2 seconds and move to  **wp_pre_drop** via an
intermediate waypoint depending on the drop off waypoint.

6. Switch the kind of object Pickit is looking for if no products are safe to pick
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

In the case Pickit found object, but the objects Pickit found are not
safe to be picked (for reason of reachability of safety), we switch the
kind of objects Pickit was looking for. We switch from cylinders to
circles if we were looking for cylinders and form circles to cylinders
if we were looking for circles.

7. Switch the kind of object Pickit is looking for if no products are found
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

          Else
            If prod_bin=prod_cir_bin
              prod_bin=prod_cyl_bin
              prod_check=prod_cir_check
            ElseIf prod_bin=prod_cyl_bin
              prod_bin=prod_cir_bin
              prod_check=prod_cyl_check

In the case Pickit did not find any objects (after the command on line
29), we switch the kind of objects Pickit was looking for. We
switch from cylinders to circles if we were looking for cylinders and
form circles to cylinders if we were looking for circles.

.. code-block:: bash

        pickit_socket_close()