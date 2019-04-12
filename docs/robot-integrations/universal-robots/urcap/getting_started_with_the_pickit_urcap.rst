Getting started with the Pickit URCap
======================================

Pickit integrates seamlessly with Universal Robots by means of a URCap
plugin. This plugin exposes a set of Pickit specific command blocks
that make the creation of vision-guided programs simple and easy. This
document explains how to install the Pickit URCap plugin and introduces
the functionality it provides.

Some of the benefits of using the Pickit URCap plugin:

-  Less typing and less code.
-  Graphical command interface with in-place documentation.
-  Pickit 2D view available from the UR Teach Pendant.

Pre-requisites
--------------

Pickit
~~~~~~~

| Verify that the installed **Pickit version is 1.8.2 or greater**. The
  software version can be verified at the top left of the web interface.
| When the version is not displayed at the top left of the web interface
  you are running an older version of Pickit which needs to be updated
  first.

|image0|

In order to have your Pickit system updated, you can always contact
your support team:  support@pickit3d.com.

Robot
~~~~~

Verify that you have a supported \ **Polyscope version**.\ ** **\ The
Polyscope versions supported by the Pickit URCap plugin are listed on
our \ `downloads <https://support.pickit3d.com/article/36-pick-it-robot-programs>`__
page. To check the Polyscope version currently installed in your robot,
click the **About** button on the home screen.

|image1|

Installing the Pickit URCap plugin
-----------------------------------

To install the Pickit URCap plugin, follow these steps:

#. `Download </downloads>`__ the Pickit URCap plugin archive containing
   the latest version of the URCap.
#. Unzip the archive and copy its contents to an **empty** USB drive.
#. Insert the drive into the USB port of either the robot controller or
   teach pendant while it is turned on.
#. On the Polyscope home screen, press **Setup Robot**.
   **|image2|**
#. Inside the \ **Setup Robot** menu, press \ **URCaps**.
#. If there's a previous installation of the Pickit URCap plugin
   (appears listed under Active), it should be removed by selecting it
   and pressing **-**.
   Polyscope will indicate that a restart is needed to apply the
   changes. Press the restart button to continue, and after restart head
   back to the  **Setup Robot** menu, **URCaps**, and make sure that
   Pickit is not listed in the Active URCaps.
   |image3|
#. In the \ **Setup Robot** menu, press **URCaps**, then **+
   |image4|**
#. Navigate to the USB drive, and select
   the **``pickit_urcap-[version].urcap``** file.
#. | Polyscope will indicate that a restart is needed to apply the
     changes. Press the restart button to continue.

   |image5|

#. Once Polyscope restarts, the plugin will be deployed and ready to
   use. Make sure your Pickit system is running and connected to the
   robot’s network to continue.

Using the Pickit URCap plugin
------------------------------

To use the Pickit URCap plugin two things must be done: Connect to a
running Pickit system, and write a program that uses Pickit specific
commands.

Connect to a running Pickit system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div>

From the main screen, go to **Program Robot** and select the
**Installation** tab. The configuration screen of the Pickit plugin is
accessible by selecting **Pickit** on the left panel.

.. raw:: html

   </div>

.. raw:: html

   <div>

|image6|

|image7|

#. Make sure that **Enable Pickit plugin** is checked.
#. Set the **IP address** and **hostname** of the Pickit system. The
   hostname of the Pickit system can be found on the top-left of the
   Pickit web interface next to the Pickit logo.
#. Click **Connect to Pickit**

As long as the connection to Pickit has not been established, the
status indicator at the lower left looks like this:

|image8|\ Establishing the connection to Pickit can take a few seconds,
and while this takes place, the status indicator displays:

| |image9|\ When the connection to the Pickit system is successful, the
  status indicator at the lower left should look like this:

|image10|

If you plan to run robot programs that don't use Pickit, you should
disable (not uninstall) the Pickit URCap plugin, by unchecking the
**Enable Pickit plugin** checkbox in the plugin's installation screen.

.. rubric:: Writing programs
   :name: writing_programs

.. raw:: html

   <div>

The Pickit plugin exposes a new set of commands that add to the set of
Polyscope’s existing commands, as well as a number of helper functions
and global variables. A complete description of the interface, and how
to access it from the Polyscope interface can be found in  `The Pickit
URCap
interface <http://support.pickit3d.com/article/80-the-pick-it-urcap-interface>`__
article.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. rubric:: Example programs
   :name: example_programs

The Pickit URCap plugin installation makes available a few example
programs under **``/programs/pickit_samples``** folder of the
robot. The can be also downloaded independently of the
URCap \ `here <https://drive.google.com/open?id=1Gf63Y35NaVxbP4mwc5YUC5SU8u8RYvyO>`__.
These programs are a great way to get familiar with the Pickit URCap
plugin, and can serve as a template to build your own applications. The
following articles provide detailed descriptions of example programs:

-  `Universal Robots URCap example picking
   program <http://support.pickit3d.com/article/76-universal-robots-urcap-example-program>`__

-  ` <http://support.pickit3d.com/article/76-universal-robots-urcap-example-program>`__\ `Robot
   camera calibration with the URCap
   plugin <http://support.pickit3d.com/article/77-robot-camera-calibration-with-the-urcap-plugin>`__

.. rubric:: Running legacy programs with the URCap plugin
   :name: running-legacy-programs-with-the-urcap-plugin

If you have robot programs written for Pickit 1.7 or older, before the
URCap plugin existed, and want to run them without porting them to the
new URCap syntax, please refer to the \ `Running a legacy UR script
program (no URCap
plugin) <https://support.pickit3d.com/article/137-running-a-legacy-ur-script-program-no-urcap-plugin>`__
article.

.. rubric:: 
   :name: section

.. raw:: html

   </div>

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b55dbe82c7d3a03f89ce074/file-81kOf1sljb.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a54cc562c7d3a194367fac2/file-fJB969gmyo.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a54d4802c7d3a194367fb13/file-wxeDBldidi.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a60761e0428635d7f439bee/file-KGcUub1G4D.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a54d49e2c7d3a194367fb14/file-MS3NDhrL8O.png
.. |image5| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a54d4e92c7d3a194367fb15/file-NM7hwAUG1u.png
.. |image6| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a54d5ae042863193800b964/file-vHgpIyHM6r.png
.. |image7| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b55dab00428631d7a893415/file-oVGkP1md8M.png
.. |image8| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b27cb3d0428632c466b0124/file-ygAD4umK5R.png
.. |image9| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b27cb840428632c466b012b/file-pVa0UezvLD.png
.. |image10| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5a5dfd312c7d3a1943684483/file-pvvqxUpaYZ.png

