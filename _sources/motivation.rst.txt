Motivation
==========

**Suhas Somnath**

8/8/2017

The quest for understanding more about matter has necessitated the development of a multitude of instruments, each
capable of numerous measurement modalities.

The `Center for Nanophase Materials Science (CNMS) <https://www.ornl.gov/facility/cnms>`_ in `Oak Ridge National Laboratory <https://www.ornl.gov>`_
is home to several dozens of cutting-edge
research instruments. Nearly all of these instruments are commercially available instruments, which generate and store
data in different ways. The diversity of data formats was significantly impeding the sharing, correlation, analysis, and curation of data.
These challenges were only exacerbated by the steady and frequent stream of visiting researchers who would visit the CNMS
to conduct their research. As researchers supporting the user facility, we desperately needed a solution for handling data from our instruments.
The sections below describe the challenges and concerns with regards to data structuring, storage, archival, curation, etc. in greater detail.

Proprietary file formats
~~~~~~~~~~~~~~~~~~~~~~~~

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
#. US Federal agencies that support scientific research mandate that the data be stored in a manner that is open, standardized
   and curation-ready in order to meet both the guidelines for data sharing and satisfy the implementation of digital
   data management as outlined by the United States Department of Energy.

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
**instrument agnostic data model** called that can be used to represent data
from any instrument, size, dimensionality, or complexity.