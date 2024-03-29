.. _Configuration:

Configuration
=============

On the configuration page, you can manage the setup and product files on
your Pickit system.

-  **Setup** file: contains the Region of Interest (ROI) configuration and
   the camera selection.
-  **Product** file: contains the detection and picking parameters for a
   specific product.

The current loaded setup and product file are always shown in the top
bar as shown in the screenshot below.

.. image:: /assets/images/Documentation/Active-files.png

Loading a setup or product file
-------------------------------

To load a new setup or product file just select them from the list. 

Setup and product files can also be loaded from within your robot
program using the correct Pickit command.

You can rename, download or delete a specific setup or product by pressing :guilabel:`Rename` 
:guilabel:`Download` or :guilabel:`Delete` once the setup or product files are
selected. Note that a setup or product file cannot be renamed or deleted while
being active.

.. image:: /assets/images/Documentation/Configuration-files.png

.. warning::
  Deleted setup and product files cannot be recovered.

Creating a new setup or product file
------------------------------------

To create a new setup or product file, first press the :guilabel:`New` button and fill in the corresponding text
fields and click the :guilabel:`Continue`. Pickit will make a new file with all settings set to the basic default settings.
After creation, the new setup and product file will automatically be
loaded.

.. image:: /assets/images/Documentation/Create-new-setup-file.png

Saving a setup or product file
------------------------------

Once settings are changed in Pickit they can be saved in the correct file. 
The :guilabel:`Save` button for the setup file can be found at the bottom of the Region of Interest tab. 
For the product file the button can be found both at the bottom of the Detection and the Picking tab.

Pressing the :guilabel:`Save` updates the active file with the new data. 
The :guilabel:`Save as` creates a new file with the new data. A name has to be given to this file. 
Pressing :guilabel:`Reset` restores the settings of the last time saved.

.. image:: /assets/images/Documentation/Save-saveas-reset.png
