I can not connect to the Pickit web interface on Windows. What to do?
======================================================================

In case the Pickit web interface cannot be reached when surfing to
**http://192.168.66.1** using **Google Chrome**, the following actions
can be taken:

-  Click the Windows button on your keyboard + R to open a run dialog
-  Enter ``cmd`` and you will see a black command line dialog
-  Enter the following command: ``ping 192.168.66.1``
-  You should start receiving continuous ping replies:

.. image:: /assets/images/faq/Ping-pickit-web-interface.png

-  If instead of replies you are getting "Request timed out" messages,
   try to disable possible active WiFi connections on your
   laptop/computer, and try again.
-  If that doesn't resolve the problem, please enter the following
   command: ``ipconfig``
-  The output of this command should look similar to what is shown
   below. If that is not the case, please make a screenshot of the
   output and send it
   to `support@pickit3d.com <mailto:mailto:support@pickit3d.com>`__

.. image:: /assets/images/faq/ipconfig.png