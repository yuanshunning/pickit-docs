Which browser or PC can I use to access the Pickit web interface?
==================================================================

The only supported internet browser for Pickit is `Google
Chrome <https://www.google.com/chrome/>`__. 

Note also that the Pickit web interface requires **WebGL** to be able
to show 3D visualizations. In case the 3D views don’t work
out-of-the-box, check your GPU state by going to the following link: 
`chrome://gpu <chrome://gpu/>`__. 
If it doesn’t read "WebGL: Hardware accelerated" in the first list,
this confirms that the 3D views won’t work. To resolve this issue, you
have to:

-  Make sure chrome://flags/#disable-webgl is disabled (there should
   be a link "Enable")
-  If that does not help, try to additionally
   enable chrome://flags/#ignore-gpu-blacklist.

To confirm that this fixes the problem, go to the page 
https://get.webgl.org/ and make sure you see the spinning cube. If
that’s not the case, use a different PC or laptop (with a preferably
stronger graphics card) to access the web interface in order to see the
3D views.