KUKA KRC example program
========================

 1
    `Loading the example program <#load_program>`__
 2
    `The example program explained <#program_explained>`__
 3
    `Running the example program <#run_program>`__

This program is part of the KUKA package which you
can download :ref:`here <downloads:KUKA>`.

More details about setting up Pickit with a KUKA robot can be
found :ref:`here <kuka>`.

**Loading the example program**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This article describes an example program illustrating how to perform a
simple picking task with Pickit. The file is called
**``ExampleSimplePicking.src``** are is located in
**``R1> Program> PickIt``**. 

The example program explained
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What follows describes the parts of the example that relate to Pickit.
Lines unrelated to Pickit have been skipped.

.. code-block:: bash

      Pickit_configure(2,3) ; Setup 2 Product 3

Request Pickit to switch to the setup with number 2 and the product
with number 3. These are numbers shown next to the setup and products on
the Pickit CONFIGURATION page:

-  If this line is suppressed, Pickit keeps its current setup and
   product.
-  If the specified setup or product does not exist, the program does
   not proceed.

Make sure that the setup and product passed to
**``pickit_configure()``** are the ones you are expecting, or the robot
may have an unexpected behaviour.

.. code-block:: bash

      Pickit_look_for_object()

      LOOP

        CONTINUE

Trigger Pickit to detect objects and enter the actual program loop. 

.. code-block:: bash

        WAIT FOR Pickit_has_response()

        IF Pickit_object_found() THEN
             
          F_Pick=Pickit_get_pose():F_PickCorrection
          F_PrePick=F_Pick:{X 0.0,Y 0.0,Z 100.0,A 0.0,B 0.0,C 0.0}

Now, the program has to wait until a response from Pickit is received.
If Pickit object detection is successful, we get the object pose
**``F_Pick``** using **``Pickit_get_pose()``**, and apply an ad-hoc
correction offset **``F_PickCorrection``** (zero by default), which
might be useful to compensate for changes to the tool or systematic
errors. Before the actual picking, it is desired that the robot first
stops at a distance above the object (100 mm in the Z direction). This
pre-pick pose is stored in **``F_PrePick``**.

.. code-block:: bash

          ; Check if position is reachable
          BAS(#TOOL,10) ; Suction cup / Tool for picking
          BAS(#BASE,0) 
          PickitAxistest=INVERSE(F_Pick,XHOME, Pickit_ErrStatusCheckPos)

Use inverse kinematics to compute the robot joint values that reach the
object pose **``F_Pick``** for the given base and tool frames. The
**``Pickit_ErrStatusCheckPos``** stores whether the pose is actually
reachable.

.. code-block:: bash

          IF (Pickit_ErrStatusCheckPos==0) THEN

            BAS(#VEL_PTP,30)
            PTP F_PrePick C_DIS
            $VEL.CP=0.1

            ; Trigger gripper cup sucking while robot is moving
            TRIGGER WHEN Path=-20 DELAY=0 DO GrpCupSuck() PRIO=-1

            LIN F_Pick

            $APO.CDIS=10.0
            $VEL.CP=0.3
            LIN_REL {Z 150.0} C_DIS

            M_BinToDrop()
            GrpCupIdle()

            Pickit_look_for_object()
                
            M_DropToBin()

If the object pose is reachable, lines 62-73 perform the object picking
sequence, which consists of a sequence of point-to-point and linear
motions, as well as enabling/disabling vacuum for grasping. Once the
object has been picked, **``Pickit_look_for_object()``** is called to
trigger Pickit to detect objects again, so detection takes place in
parallel to the final **``M_DropToBin()``** motion sequence. This
motivates why the first call of **``Pickit_look_for_object()``** was
outside the actual program loop. 

.. code-block:: bash

          ELSE

            ; Position unreachable for the robot

            IF (Pickit_remaining_objects()>0) THEN
              Pickit_next_object()
            ELSE
              Pickit_look_for_object()
            ENDIF
                
    :      ENDIF

When the object pose is unreachable (line 60 evaluates to false) a new
object pose is required. There are two alternatives:

#. Firstly, If the last call to **``Pickit_look_for_object()``** found
   multiple objects, we can request the next object (lines 86-87). This
   alternative is faster, as it does not incur the overhead of a new
   detection.
#. Alternatively, if there are no remaining detected objects, Pickit is
   triggered to detect objects again in line 89. 

.. code-block:: bash

        ELSE

          ; No Object was found

          ToHome()

         Pickit_look_for_object()
             
       ENDIF
          
      ENDLOOP

If the last call to **``Pickit_look_for_object()``** found no objects
(line 94 is the else statement of line 51), the robot is sent to its
home position and Pickit is triggered to detect objects. As long as
there are no object detections, the infinite loop will keep on trying to
find one.

Running the example program
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Before running the program, it should be verified that **robot camera
  calibration** has been done correctly and that the **tool frame** has
  been defined correctly.
| Please refer to the  `How to execute robot camera
  calibration <http://support.pickit3d.com/article/35-how-to-execute-robot-camera-calibration>`__
  article for more details on how to perform robot camera calibration.
| Example programs for multi-pose and single-pose calibration can be
  found in **``R1> Program> PickIt``**: **``PickitMultiPoseCal.src``**
  and **``PickitSinglePoseCal.src``**, respectively. 

| The example program contains **hard-coded robot poses** that should be
  adapted to every new robot.
| When running a program for the first time, it is advised to do so in
  **manual mode**, and set a **low robot speed**. As such, non-expected
  behaviour (for example due to incorrect programming or wrong
  calibration) can be identified early enough to prevent the robot from
  colliding with surrounding objects or people.

The example program can be run as any other KUKA.KRL program. Please
refer to the **KUKA KR-C4** user manual for further details. Once
running, verify that an object detection is executed on the Pickit side
and that the robot is correctly moving to the object.
