Exercise detection with Pick-it Teach of parts lying flat on a table
====================================================================

This exercise involves using Pick-it Teach. In many applications it is
hard to do bin picking with correct orientation. The reason for this is
that often the distinctive features of the parts are not visible or
partially covered to the camera system. In this exercise the benefit of
multiple steps are discussed. Also parameters to more robustly detect
parts lying flat on a table are discussed.

.. raw:: html

   <div class="callout">

-  **Level:** Advanced
-  **Duration:** < 15 min

.. raw:: html

   </div>

|image0|

Requirement
-----------

Before starting on this exercise we advice you to read following
articles:

-  `Detection: Pick-it
   Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__
-  `Explaining the Teach detection
   parameters <https://support.pickit3d.com/article/173-explaining-the-teach-detection-parameters>`__

.. attention:: For this exercise you need Pick-it version 1.10.x
   If you have a older software version. Please read the following
   `article <https://support.pickit3d.com/article/131-getting-ready-for-a-remote-software-update>`__
   and contact support@pickit3d.com to get an update.


Task
----

In this snapshot parts lying random in a bin are shown. Beside the bin 2
parts lying flat on their side are shown. 

If bin picking with complete orientation of certain parts is proven to
be hard, a multiple step solution can still be applied. In the first
step it is aimed to pick one part from the bin. In this first step
orientation of the part is not important. Then in a second step the
Pick-it system looks again at an isolated part to completely determine
the orientation of that part. 

For this exercise two models of the parts are already taught to the
system. Note that the two models are not the same but are a mirrored
version of each other.

Create a detection strategy for both picking the parts from the bin as
for picking the parts with correct orientation if they are isolated.

**For the bin:**

Region of interest settings: X 60/220mm, Y -145/65mm, Z 10/125mm

Quiz:

-  Is it necessary to use both models?
-  What is a good matching score?

**For the isolated parts:**

Region of interest settings: X -170/50mm, Y -185/100mm, Z 10/125mm

Quiz:

-  What is a good matching score if Parts can overlap is selected?
-  What is a good matching score if Singulated parts is selected?

How to get started
------------------

Follow the next steps to complete the exercise.

#. Download the snapshot file
   `here <https://drive.google.com/uc?export=download&id=1tlBkSm682guvMR_JrdRYcrgYlXP4TFw6>`__
   on your device.
#. Connect your device to your Pick-it processor.
#. In the user interface of Pick-it, go to the Files tab. 
#. Press Upload and select the file.
#. The file can now be found in snapshots/uploads.
#. Finish the exercise.
#. Press the snapshot button on the lower left corner of the view.
#. Name your snapshot 'Solution\_Teach\_2\_CompanyName'.
#. Download the file from the snapshots folder.
#. Send your solution to support@pickit3d.com to receive feedback.

What to read next

| `Exercises through
  snapshots <https://support.pickit3d.com/article/188-exercises-through-snapshots>`__
| `Exercise Region of
  Interest <https://support.pickit3d.com/article/187-exercise-region-of-interest>`__
| `Exercise detection with Pick-it
  Flex <https://support.pickit3d.com/article/190-exercise-detection-with-pick-it-flex>`__
| `Exercise detection with Pick-it
  Pattern <https://support.pickit3d.com/article/191-exercise-detection-with-pick-it-pattern>`__

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b8fe6af0428631d7a8aba05/file-xJGzxZVzhv.png

