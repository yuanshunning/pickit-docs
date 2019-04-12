Example: the clustering methods
===============================

-  `Touching parts <#touching>`__
-  `Plane Based Clustering <#plane_based>`__
-  `Non-touching parts <#non-touching>`__

In this article an example of different clustering methods is showed and
discussed. The scene below is used to explain the different clustering
method. In the scene there are 3 shampoo bottles next to each other, 4
boxes randomly on top of each other and 4 electrical plug shieldings
separated from each other.  A snapshot of this scene can be downloaded 
`here <https://drive.google.com/uc?export=download&id=1O_N-cxPfPcg-TQpFimSls3jx3sEwM_RW>`__.
|image0|\ |image1|

Touching parts
--------------

These methods look at the change of surface. If a surface change is too
abrupt it is considered as a separate cluster. On the image below the
results of this clustering method is shown. For the shampoo bottles
three different clusters are formed which is good. For the boxes, the 2
boxes that are aligned but under an angle are not clustered apart. The
transition of the surface is to smooth to filter them apart. For the
electrical plug shieldings multiple clusters per part are formed, which
is not good.

**Best results for:**

-  Rounded parts
-  Cylinders: bottles, gas springs, steel bars,..
-  Balls: tennis balls, oranges,..

|image2|

Plane Based Clustering
----------------------

This method looks for flat surfaces in the scene. If two surfaces have a
different orientation they are considered as separate clusters. On the
image below the results of this clustering method is shown. For the
shampoo bottles multiple clusters are formed, which is not good. For the
boxes all of the boxes are clustered apart andno points are missing at
the edges of the surfaces, which is good. For the electrical plug
shieldings multiple clusters per part are formed, which is not good.

**Best results for:**

-  Flat surfaces
-  Boxes\ |image3|

on-touching parts
-----------------

This method groups points into cluster that are close together. Objects
are clustered apart if there is a physical gap. On the image below the
results of this clustering method is shown. For the shampoo bottles one
big cluster is formed, which is not good. Also the two aligned boxes are
not clustered apart. For the electrical plug shieldings, which are
positioned separated, one cluster per part is formed, which is good.

**Best results for:**

-  (Complex) shapes that are separated\ |image4|

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
| `Picking <https://support.pickit3d.com/article/163-picking>`__

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b7eac860428631d7a8a4d24/file-rt9QKOarBW.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b7eac8e0428631d7a8a4d26/file-idan0aFCHE.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b7eacc62c7d3a03f89e0952/file-8f2kTg9HZB.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b7ead550428631d7a8a4d29/file-uULUv7jLMO.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5b7eada10428631d7a8a4d2d/file-BjE63ZcHTc.png

