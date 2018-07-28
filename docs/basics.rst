Data Model and File Format
==========================

**Suhas Somnath**

8/8/2017

In this document we aim to provide a comprehensive overview of the motivation for and specifications of the
**Universal Spectroscopy and Imaging Data** (**USID**) Model and the file format (**h5USID**) used for storing
spectroscopy and imaging data.

Pycroscopy uses the **USID** model and **h5USID** files.

**Dr. Stephen Jesse** conceived the **USID** while **Dr. Suhas Somnath** and **Chris R. Smith** implemented **USID**
into hierarchical data format (**HDF5**) files using python in **pyUSID**

.. contents::

Nomenclature
--------------
Before we start off, lets clarify some nomenclature to avoid confusion.

Data model
~~~~~~~~~~~
Data model refers to the way the data is arranged. This does **not** depend on the implementation in a particular file format

File format
~~~~~~~~~~~~
This corresponds to the kind of file, such as a spreadsheet (.CSV), an image (.PNG), a text file (.TXT) within which information is contained.

Data format
~~~~~~~~~~~~
`data format <https://en.wikipedia.org/wiki/Data_format>`_ is actually a rather broad term. However, we have observed that
people often refer to the combination of a data model implemented within a file format as a ``data format``.

Measurements
~~~~~~~~~~~~
In all measurements, some ``quantity`` such as voltage, resistance, current, amplitude, or intensity is collected
as a function of (typically all combinations of) one or more ``independent variables``. For example, a gray-scale image represents the
quantity - intensity being recorded for all combinations of the variables - row and column. A (simple) spectrum represents
a quantity such as amplitude or phase recorded as a function of a reference variable such as wavelength or frequency.

Data collected from measurements result in N-dimensional datasets where each ``dimension`` corresponds to a variable that
was varied. Going back to the above examples a gray-scale image would be represented by a 2 dimensional dataset whose
dimensions are row and column. Similarly, a simple spectrum wold be a 1 dimensional dataset whose sole dimension would
be frequency for example.

Dimensionality
~~~~~~~~~~~~~~~
* We consider data recorded for all combinations of 2 or more variables as ``multi-dimensional`` datasets or ``Nth order tensors``:

  * For example, if a single value of current is recorded as a function of driving / excitation bias or voltage having B values, the dataset is said to be ``1 dimensional`` and the dimension would be - ``Bias``.
  * If the bias is cycled C times, the data is said to be ``two dimensional`` with dimensions - ``(Bias, Cycle)``.
  * If the bias is varied over B values over C cycles at X columns and Y rows in a 2D grid of positions, the resultant dataset would have ``4 dimensions:`` ``(Rows, Columns, Cycle, Bias)``.
* ``Multi-feature``: As a different example, let us suppose that the ``petal width``, ``length``, and ``weight`` were measured for ``F`` different kinds of flowers. This would result in a ``1 dimensional dataset`` with the kind of flower being the sole dimension. Such a dataset is **not** a 3 dimensional dataset because the ``petal width, length``, and ``weight`` are only different ``features`` for each measurement. Some quantity needs to be **measured for all combinations of** petal width, length, and weight to make this dataset 3 dimensional. Most examples observed in data mining, simple machine learning actually fall into this category

Why should you care?
--------------------

The quest for understanding more about matter has necessitated the
development of a multitude of instruments, each capable of numerous
measurement modalities.

Proprietary file formats
~~~~~~~~~~~~~~~~~~~~~~~~~~

Typically, each commercial instruments generates data files formatted in
proprietary file formats by the instrument manufacturer. The proprietary
nature of these file formats and the obfuscated data model within the files impede scientific progress in the
following ways:

#. By making it challenging for researchers to extract data from these files
#. Impeding the correlation of data acquired from different instruments.
#. Inability to store results back into the same file
#. Inflexibility to accommodate few kilobytes to several gigabytes of data
#. Requiring different versions of analysis routines for each data format
#. In some cases, requiring proprietary software provided with the instrument to access the data

Future concerns
~~~~~~~~~~~~~~~~

#. Several fields are moving towards the open science paradigm which will require journals and researchers to support
   journal papers with data and analysis software
#. US Federal agencies that support scientific research require curation of datasets in a clear and organized manner

Other problems
~~~~~~~~~~~~~~~

#. The vast majority of scientific software packages (e.g. X-array) aim to focus at information already available in
   memory. In other words they do not solve the problem of storing data in a self-describing manner and reading +
   processing this data.
#. There are a few file formatting packages and approaches (Nexus, NetCDF). However, they are typically narrow in scope
   and only solve the data formatting for specific communities
#. Commercial image analysis software are often woefully limited in their capabilities and only work on simple 1, 2, and
   in some cases- 3D datasets. There are barely any software for handling arbitrarily large multi-dimensional datasets.
#. In many cases, especially electron and ion based microscopy, the very act of probing the sample damages the sample.
   To minimize damage to the sample, researchers only sample data from a few random positions in the 2D grid and use
   advanced algorithms to reconstruct the missing data. We have not come across any robust solutions for storing such
   **Compressed sensing / sparse sampling** data. More in the **Advanced Topics** section.

To solve the above and many more problems, we have developed an
**instrument agnostic data model** that can be used to represent data
from any instrument, size, dimensionality, or complexity.

File Format
------------

Requirements
~~~~~~~~~~~~~~
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
~~~~~~~~~~~~
* We found that existing file formats in science such as the `Nexus data format <http://www.nexusformat.org>`_,
  `XDMF <http://www.xdmf.org/index.php/Main_Page>`_, and `NetCDF <https://www.unidata.ucar.edu/software/netcdf/>`_:

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
* The `DREAM.3D <http://dream3d.bluequartz.net/binaries/Help/DREAM3D/nativedream3d.html>`_ is yet another group that uses HDF5
  as the base container to store their data. We are currently evaluating compatibility with and feasibility of their data model.

We found that `HDF5 <http://extremecomputingtraining.anl.gov/files/2015/03/HDF5-Intro-aug7-130.pdf>`_, works best for us compared to the alternatives.
Hence, we have implemented the **USID** model into the HDF5 file format and such file will be referred to as **h5USID** files.

We acknowledge that it is nearly impossible to find the perfect file format and HDF5 too has its fair share of drawbacks.
One common observation among file formats is that a file format optimized for the cloud or cluster computing often does
not perform well (or at all) on HPC due to the conflicting nature of the computing paradigms.
As of this writing, HDF5 is optimized for HPC and not for cloud-based applications.
For cloud-based environments it is beneficial to in fact break up the data into
small chunks that can be individually addressed and used. We think `Zarr <https://zarr.readthedocs.io/en/stable/>`_ and
`N5 <https://github.com/saalfeldlab/n5>`_ would be good alternatives; however, most of these file formats are very much in
their infancy and have not proven themselves like HDF5 has. This being said, the HDF organization
`just announced <https://www.youtube.com/watch?v=3tP3lT5y-QA>`_ a `cloud flavor <https://www.hdfgroup.org/solutions/hdf-cloud/>`_
of HDF5 and we plan to look into this once h5py or other python packages support such capabilities.