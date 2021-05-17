File Format
===========

**Suhas Somnath**

8/8/2017

Requirements
------------
No one really wants yet another file format in their lives. We wanted to adopt a file format that satisfies some basic requirements:

* already widely accepted in scientific research
* support parallel read and write capabilities.
* store multiple datasets of different shapes, dimensionalities, precision and sizes.
* scale very efficiently from few kilobytes to several terabytes
* can be (readily) read and modified using any language including Python, R, Matlab,
  C/C++, Java, Fortran, Igor Pro, etc. without requiring installation of modules that are hard to install
* store and organize data in a intuitive and familiar hierarchical / tree-like
  structure that is similar to files and folders in personal computers.
* facilitates storage of any number of experimental or analysis parameters
  in addition to regular data.
* highly flexible and poses minimal restrictions on how the data can and should be stored.
* readily compatible with high-performance computing (``HPC``) and (soon) cloud-computing.

Candidates
----------
* We found that existing file formats in science such as the `XDMF <http://www.xdmf.org/index.php/Main_Page>`_, and
  `NetCDF <https://www.unidata.ucar.edu/software/netcdf/>`_:

  * were designed for **specific / narrow scientific domains only** and we did not want to shoehorn our data structure into those formats.
  * Furthermore, despite being some of the more popular scientific data formats, it is **not immediately straightforward to read those files**
    on every computer using any programming language. For example - the `Anaconda <https://www.anaconda.com/what-is-anaconda/>`_
    python distribution does not come with any packages for reading these file formats.
* `Adios <https://www.olcf.ornl.gov/center-projects/adios/>`_ is perhaps the ultimate file format for storing petabyte sized data on supercomputers but
  it was specifically designed for simulations, check-pointing, and it trades flexibility, and ease-of-use for performance.
* The `hierarchical data format (HDF5) <https://support.hdfgroup.org/HDF5/doc/H5.intro.html>`_ is the implicitly or explicitly the
  `de-facto standard in scientific research <https://support.hdfgroup.org/HDF5/users5.html>`_.
  In fact, Nexus, NetCDF, and even `Matlab's .mat <https://www.mathworks.com/help/matlab/import_export/mat-file-versions.html>`_
  files are actually (now) just custom flavors of HDF5 thereby validating the statement that HDF5 is the **unanimous the file format of choice**

We acknowledge that it is nearly impossible to find the perfect file format and HDF5 too has its fair share of drawbacks.
For cloud-based environments it is beneficial to in fact break up the data into
small chunks that can be individually addressed and used. We think `Zarr <https://zarr.readthedocs.io/en/stable/>`_ and
`N5 <https://github.com/saalfeldlab/n5>`_ would be good alternatives; however, most of these file formats are very much in
their infancy and have not proven themselves like HDF5 has.

Quick basics of HDF5
--------------------
Information can be stored in HDF5 files in several ways:

* ``Datasets`` allow the storage of data matrices and these are the vessels used for storing the ``main``,
  ``ancillary``, and any extra data matrices
* ``Groups`` are similar to folders in conventional file systems and can be used to store any number of datasets or
  groups themselves
* ``Attributes`` are small pieces of information, such as experimental or analytical parameters, that are stored in
  key-value pairs in the same way as dictionaries in python.  Both groups and datasets can store attributes.
* While they are not means to store data, ``Links`` or ``references`` can be used to provide shortcuts and aliases to
  datasets and groups. This feature is especially useful for avoiding duplication of datasets when two ``main``
  datasets use the same ancillary datasets.