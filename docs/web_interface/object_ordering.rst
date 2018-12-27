Object ordering
===============

This setting defines in which order the objects are returned to the
robot.

-  **Highest product center:** Sort objects with highest product center
   first. This is the most common option.
-  **Lowest product center:** Reverse ordering from 'Highest product
   center'.
-  **Highest product part:** Sort objects with highest volume or surface
   boundary first.
-  **Lowest X value first:** Orders objects based on object center
   position. From small to large X value.
-  **Highest X value first:** Reverse ordering from 'Lowest X value
   first'.
-  **Lowest Y value first:** Orders objects based on object center
   position. From small to large Y value.
-  **Highest Y value first:** Reverse ordering from 'Lowest Y value
   first'.
-  **Biggest product:** Objects are ordered from big to small volume or
   surface.
-  **Pattern along the positive X-axis:** See image below.
-  **Pattern along the negative X-axis:** See image below.
-  **Pattern along the positive Y-axis:** See image below.
-  **Pattern along the negative Y-axis:** See image below.
-  **Highest matching score (Teach only):** Sort objects with the
   highest model matching score first. This only works for the Teach
   detection
-  **Top box first:** Sort objects with the highest product center
   first, but if multiple sides of a box are recognized, the bigger side
   is prefered instead of the smaller.

The pattern sort options are useful for depalletization or pallet
loading applications. The picture below illustrates each option:

|image0|

.. |image0| image:: https://lh5.googleusercontent.com/kqDgJJtwh3VJ9xma5VZozrS9CEDMVco-6L5pwGi0LX8n2ntlpyP9ILqUZeGZP412h_mDz-PbgoRVXnUcOaMggtr276OzJuLkY4WjMzadlyrjkN0oNDeSRMKmxAfzXVYQMwKSR82D
   :width: 624px
   :height: 245px
