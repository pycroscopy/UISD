USID in HDF5
=============

**Suhas Somnath**

8/8/2017

Here we discuss guidelines and specifications for implementing the **USID** model into HDF5 files.
While we could impose that the file extension be changed from **.hdf5** to **.h5USID**, we choose to retain
the **.hdf5** extension so that other software are aware of the general file type and can recognize / read them easily.

``Main`` data:
~~~~~~~~~~~~~~

**Dataset** structured as (``positions`` x time or ``spectroscopic`` values)

* ``dtype`` : uint8, float32, complex64, compound if necessary, etc.
* `chunking <https://support.hdfgroup.org/HDF5/doc1.8/Advanced/Chunking/index.html>`__ (**optional**)
  : Chunking is optional and not necessary in h5USID. Typically, HDF5 / ``h5py`` will automatically do a good job of
  deciding implicit chunking such that performance is maximized. If chunking is indeed necessary for your application,
  HDF group recommends that chunks be between 100 kB to 1 MB. We
  recommend chunking by whole number of positions if possible since data is more
  likely to be read by position rather than by specific spectral indices.
* ``compression`` (**optional**): We recommend evaluating the necessity and performance impacts that compression can have on your
  application. In certain cases, compression can result in very long (10 - 20x) longer read and write times. In such cases,
  it may be best to compress only if one does not expect to read / modify the dataset frequently (archival).
* *Required* attributes:

  * ``quantity`` - Single string that explains the data. The physical
    quantity contained in each cell of the dataset – eg –
    'Current' or 'Deflection'
  * ``units`` – Single string for units. The units for the physical
    quantity like 'nA', 'V', 'pF', etc.
  * ``Position_Indices`` - Reference to the position indices dataset
  * ``Position_Values`` - Reference to the position values dataset
  * ``Spectroscopic_Indices`` - Reference to the spectroscopic indices
    dataset
  * ``Spectroscopic_Values`` - Reference to the spectroscopic values
    dataset

Note that we are only storing references to the ancillary datasets. This
allows multiple ``main`` datasets to share the same ancillary datasets
without having to duplicate them.

``Ancillary`` data:
~~~~~~~~~~~~~~~~~~~

``Position_Indices`` structured as (``positions`` x ``spatial dimensions``)

* Dimensions are arranged in ascending order of rate of change. In other
  words, the fastest changing dimension is in the first column and the
  slowest is in the last or rightmost column.
* ``dtype`` : uint32
* Required attributes:

  * ``labels`` - list of strings for the column names like ['X', 'Y']
  * ``units`` – list of strings for units like ['um', 'nm']

* Optional attributes:
  * Region references based on column names

``Position_Values`` structured as (``positions`` x ``spatial dimensions``)

* dimensions are arranged in ascending order of rate of change. In other
  words, the fastest changing dimension is in the first column and the
  slowest is in the last or rightmost column.
* ``dtype`` : float32
* Required attributes:

  * ``labels`` - list of strings for the column names like ['X', 'Y']
  * ``units`` – list of strings for units like ['um', 'nm']

* Optional attributes:
  * Region references based on column names

``Spectroscopic_Indices`` structured as (``spectroscopic dimensions`` x
``time``)

* dimensions are arranged in ascending order of rate of change.
  In other words, the fastest changing dimension is in the first row and
  the slowest is in the last or lowermost row.
* ``dtype`` : uint32
* Required attributes:

  * ``labels`` - list of strings for the column names like ['Bias', 'Cycle']
  * ``units`` – list of strings for units like ['V', ''].
    Empty string for dimensionless quantities

* Optional attributes:
  * Region references based on row names

``Spectroscopic_Values`` structured as (``spectroscopic dimensions`` x
``time``)

* dimensions are arranged in ascending order of rate of change.
  In other words, the fastest changing dimension is in the first row and
  the slowest is in the last or lowermost row.
* ``dtype`` : float32
* Required attributes:

  * ``labels`` - list of strings for the column names like ['Bias', 'Cycle']
  * ``units`` – list of strings for units like ['V', ''].
    Empty string for dimensionless quantities

* Optional attributes:

  * Region references based on row names

Attributes
~~~~~~~~~~
All groups and (at least ``Main``) datasets must be created with the following **mandatory** attributes for better traceability:

-  ``time_stamp`` : '2017\_08\_15-22\_15\_45' (date and time of creation
   of the group or dataset formatted as 'YYYY\_MM\_DD-HH\_mm\_ss' as
   a string)
-  ``machine_id`` : 'mac1234.ornl.gov' (a fully qualified domain name as
   a string)
-  ``pyUSID_version`` : '0.0.1'
-  ``platform`` : 'Windows10....' or something like 'Darwin-17.4.0-x86_64-i386-64bit' (for Mac OS) -
   a long string providing detailed information about the operating system

Groups
~~~~~~~~~~

HDF5 Groups in **h5USID** are used to organize categories of information (raw measurements from instruments, results from data analysis, etc.) in an intuitive manner.

Measurement data
^^^^^^^^^^^^^^^^

-  As mentioned earlier, instrument users may change experimental
   parameters during measurements. Even if these changes are minor, they
   can lead to misinterpretation of data if the changes are not handled
   robustly. To solve this problem, we recommend storing data under **indexed**
   groups named as ``Measurement_00x``. Each time the parameters
   are changed, the dataset is truncated to the point until which data
   was collected and a new group is created to store the upcoming
   new measurement data.
-  Each **channel** of information acquired during the measurement gets
   its own group.
-  The ``Main`` datasets would reside within these channel groups.
-  Similar to the measurement groups, the channel groups are
   named as ``Channel_00x``. The index for the group is incremented
   according to the index of the information channel.
-  Depending on the circumstances, the ancillary datasets can be shared
   among channels.

   -  Instead of the main dataset in ``Channel_001`` having references to
      the ancillary datasets in ``Channel_000``, we recommend placing the
      ancillary datasets outside the Channel groups in a area common
      to both channel groups. Typically, this is the
      ``Measurement_00x`` group.

-  This is what the tree structure in the file looks like when
   experimental parameters were changed twice and there are two channels
   of information being acquired during the measurements.
-  Datasets common to all measurement groups (perhaps some calibration
   data that is acquired only once before all measurements)
-  ``Measurement_000`` (group)

   -  ``Channel_000`` (group)

      -  Datasets here

   -  ``Channel_001`` (group)

      -  Datasets here

   -  Datasets common to ``Channel_000`` and ``Channel_001``

-  ``Measurement_001`` (group)

   -  ``Channel_000`` (group)

      -  Datasets here

   -  ``Channel_001`` (group)

      -  Datasets here

   -  Datasets common to ``Channel_000`` and ``Channel_001``

-  ...

Tool (analysis / processing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Each time an analysis or processing routine, referred generally as
   ``tool``, is performed on a dataset of interest, the results are
   stored in new HDF5 datasets within a new HSF5 group.
-  A completely new dataset(s) and group are created even if a minor
   operation is being performed on the dataset. In other words, we **do NOT modify existing datasets**.
-  Almost always, the tool is applied to one (or more) ``main`` datasets (referred to
   as the ``source`` dataset) and at least one of the results is
   typically also a ``main`` dataset. These new ``main`` datasets will
   either need to be linked to the ancillary matrices of the ``source``
   or to new ancillary datasets that will need to be created.
-  The resultant dataset(s) are always stored in a group whose name
   is derived from the names of the tool and the dataset. This makes the
   data **traceable**, meaning that the names of the datasets and
   groups are sufficient to understand what processing or analysis
   steps were applied to the data to bring it to a particular point.
-  The group is named as ``Source_Dataset-Tool_Name_00x``, where a
   ``tool`` named ``Tool_Name`` is applied to a ``main`` dataset named
   ``Source_Dataset``.

   -  Since there is a possibility that the same tool could be applied
      to the very same dataset multiple times, we store the results of
      each run of the tool in a separate group. These groups are
      differentiated by the index that is appended to the name of
      the group.
   -  Note that a ``-`` separates the dataset name from the tool name
      and anything after the last ``_`` will be assumed to be the index
      of the group
   -  Please refer to the advanced topics section for tools that have **more than one**
      ``source`` datasets

-  In general, the results from tools applied to datasets should be
   stored as:

    -  ``Source_Dataset``
    -  ``Source_Dataset-Tool_Name_000`` (group containing results from
       first run of the ``tool`` on ``Source_Dataset``)

       -  Attributes:

          -  all mandatory attributes
          -  ``algorithm``
          -  Other tool-relevant attributes
          -  ``source_000`` - reference to ``Source_Dataset``

       -  ``Dataset_Result0``
       -  ``Dataset_Result1`` ...

    -  ``Source_Dataset-Tool_Name_001`` (group containing results from
       second run of the ``tool`` on ``Source_Dataset``)

-  This methodology is illustrated with an example of applying
   ``K-Means Clustering`` on the ``Raw_Data`` acquired from a measurement:

    -  ``Raw_Data`` (``main`` dataset)
    -  ``Raw_Data-Cluster_000`` (group)
    -  Attributes:

           -  all mandatory attributes
           -  ``algorithm`` : 'K-Means'
           -  ``source_000`` : reference to ``Raw_Data``

    -  ``Label_Indices`` (ancillary spectroscopic dataset with 1 dimension of size 1)
    -  ``Label_Values`` (ancillary spectroscopic dataset with 1 dimension of size 1)
    -  ``Labels`` (Main dataset)

       -  Attributes:

          -  ``quantity`` : 'Cluster labels'
          -  ``units`` : 'a. u.'
          -  ``Position_Indices`` : Reference to ``Position_Indices`` from
             attribute of ``Raw_Data``
          -  ``Position_Values`` : Reference to ``Position_Values`` from
             attribute of ``Raw_Data``
          -  ``Spectroscopic_Indices`` : Reference to ``Label_Indices``
          -  ``Spectroscopic_Values`` : Reference to ``Label_Values``
          -  all mandatory attributes

    -  ``Cluster_Indices`` (ancillary positions dataset with 1 dimension of size equal to number of clusters)
    -  ``Cluster_Values`` (ancillary positions dataset with 1 dimension of size equal to number of clusters)
    -  ``Mean_Response`` (main dataset) <- This dataset stores the endmembers
       or mean response for each cluster

       -  Attributes:

          -  ``quantity`` : copy from the ``quantity`` attribute in
             ``Raw_Data``
          -  ``units`` : copy from the ``units`` attribute in ``Raw_Data``
          -  ``Position_Indices`` : Reference to ``Cluster_Indices``
          -  ``Position_Values`` : Reference to ``Cluster_Values``
          -  ``Spectroscopic_Indices`` : Reference to ``Spectroscopic_Indices``
             from attribute of ``Raw_Data``
          -  ``Spectroscopic_Values`` : Reference to ``Spectroscopic_Values``
             from attribute of ``Raw_Data``
          -  all mandatory attributes

-  Note that the spectroscopic datasets that the ``Labels`` dataset link
   to are not called ``Spectroscopic_Indices`` or
   ``Spectroscopic_Values`` themselves. They only need to follow the
   specifications outlined above. The same is true for the position
   datasets for ``Mean_Response``.
