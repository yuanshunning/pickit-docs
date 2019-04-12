Using the model ID in a robot program
=====================================

Using the model ID in a robot program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes it's desired to do a different action with a robot depending
on the ID of the detected model. Use cases are:

-  define how to grip an object based on the visible object side or
-  define how to drop off an object based on the visible object side.

Universal Robots with URCap
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A variable  **pickit\_type** is available to use after using the Pickit
URCap \ **Find object(s)** command.This variable will represent
the detected model id.

Universal Robots with non-URCap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When calling  **pickit\_look\_for\_object()** in a robot program, an
object named \ **pickit\_object** will be available. Use the type
property of this object to get the detected model id. An example robot
program might look like this:

::

    pickit_look_for_object()
    if pickit_object_found()
      if (pickit_object.type == 1)
        // Use drop off position 2.
      elsif (pickit_object.type == 2)
       // Use drop off position 2.
      endif
    endif

Mentioned articles

What to read next

| 

| `Region of
  Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
| `Detection: Pickit
  Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
| `Detection:
  Pickit Pattern <https://support.pickit3d.com/article/161-detection-pick-it-pattern>`__
| `Detection:
  Pickit Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__
