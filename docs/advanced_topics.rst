Advanced topics
===============

**Suhas Somnath**

8/8/2017

Region references
-----------------
These are references to sections of a ``main`` or ``ancillary`` dataset that make it easy to access data specific to a
specific portion of the measurement, or each column or row in the ancillary datasets just by their alias (intuitive
strings for names).

We have observed that the average **USID** user does not tend to use region references as much as we thought they
might. Therefore, we do not require or enforce that region references be used

Processing on multiple ``Main`` datasets
----------------------------------------
One popular scientific workflow we anticipate involves the usage of multiple ``source`` datasets to create results.
By definition, this breaks the current nomenclature of HDF5 groups that will contain results. This will be addressed by
restructuring the code in such a way that the results group could be named as: ``Multi_Dataset-Tool_Name_000``. To improve
the robustness of the solution, we have already begun storing the necessary information as attributes of the HDF5
results groups. Here are the attributes of the group that we expect to capture the references to all the datasets along
with the name of the tool while relaxing the restrictions on the aforementioned nomenclature:

* ``tool`` : <string> - Name of the tool / process applied to the datasets
* ``num_sources``: <unsigned integer> - Number of source datasets that take part in the process
* ``source_000`` : <HDF5 object reference> - reference to the first source dataset
* ``source_001`` : <HDF5 object reference> - reference to the second source dataset ...

We would have to break the list of references to the source datasets into individual attributes since h5py / HDF5
currently does not allow the value of an attribute to be a list of object references.

Sparse Sampling / Compressed Sensing
------------------------------------
In many cases, especially electron and ion based microscopy, the very act of probing the sample damages the sample.
In order to minimize damage to the sample, researchers only sample data from a few random positions in the 2D grid of
positions and use advanced algorithms to reconstruct the missing data. This scientific problem presents a data storage
challenge. The naive approach would be to store a giant matrix of zeros with only a available positions filled in.
This is highly inefficient since the space occupied by the data would be equal to that of the complete (non-sparse)
dataset.

For such sparse sampling problems, we propose that the indices for each position be identical and still range from ``0``
to ``N-1`` for a dataset with ``N`` randomly sampled positions. Thus, for an example dataset with two position dimensions,
the indices would be arranged as:

+-------+-------+
|   X   |   Y   |
+=======+=======+
|  0    |   0   |
+-------+-------+
|  1    |   1   |
+-------+-------+
|  2    |   2   |
+-------+-------+
|  .    |   .   |
+-------+-------+
|  N-2  |  N-2  |
+-------+-------+
|  N-1  |  N-1  |
+-------+-------+

However, the position values would contain the actual values:

+-------+-------+
|   X   |   Y   |
+=======+=======+
|  9.5  |  1.5  |
+-------+-------+
|  3.6  |  7.4  |
+-------+-------+
|  5.4  |  8.2  |
+-------+-------+
|  .    |   .   |
+-------+-------+
|  1.2  |  3.9  |
+-------+-------+
|  4.8  |  6.1  |
+-------+-------+

The spectroscopic ancillary datasets would be constructed and defined in the traditional methods since the sampling in
the spectroscopic dimension is identical for all measurements.

The vast majority of the existing features including signal filtering, statistical machine learning algorithms, etc. in
child packages like pycroscopy could still be applied to such datasets.

By nature of its definition, such a dataset will certainly pose problems when attempting to reshape to its N-dimensional
form among other things. Pycroscopy currently does not have any scientific algorithms or real datasets specifically
written for such data but this will be addressed in the near future. This is section is presented to show that we
have indeed thought about such advanced problems as well when designing the universal data structure.

Provenance over multiple HDF5 files
-----------------------------------
We are exploring strategies to accomdoate situations where data products are spread over multiple (smaller) HDF5 files.