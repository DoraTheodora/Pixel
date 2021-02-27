.. Pixel documentation master file, created by
   sphinx-quickstart on Tue Jan  5 19:12:32 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Pixel's documentation!
=================================
.. code-block:: python
   :emphasize-lines: 3,8, 9

   def about_the_project():
      """ About the team """
      developer = "Theodora Litean-Tataru"
      email = "tataru.theodora@yahoo.com"
      date = 2020-2021
      institute = "Institute of Technology Carlow"
      course = "Software Development"
      tutor = "Joseph Kehoe"
      return "Smart speaker with face recognition for elderlies and people with hearing deficiency"
   

Info
----
.. toctree::
   :maxdepth: 5
   :caption: About the software:

   license
   developer

Modules
--------
.. toctree::
   :maxdepth: 5
   :caption: Software:

   modules




Indices and tables
==================

* :ref:`search`
