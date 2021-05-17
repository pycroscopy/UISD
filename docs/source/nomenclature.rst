Nomenclature
============

**Suhas Somnath**

8/8/2017

Lets clarify some nomenclature to avoid confusion.

Data schema
~~~~~~~~~~~
Data schema or model refers to the way the data is arranged. This does **not** depend on the implementation in a particular file format

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
