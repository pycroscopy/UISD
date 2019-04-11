Frequently asked questions
==========================

What do you mean by multidimensional data?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Please refer to our `nomenclature <./nomenclature.html>`_ document

Do you have APIs for creating and reading USID HDF5 files in languages besides python?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
At the moment, we only have tools to read and write USID HDF5 files in python via our sister project - `pyUSID <../pyUSID/about.html>`_.
Given the open-source code of pyUSID and comprehensive documentation available, we believe that it should not be very challenging to work on USID HDF5 in other programming languages.
If you are interested in making an API available for other languages, we would be happy to help in any way we can. Please `get in touch with us <./contact.html>`_.

What is USID not for?
~~~~~~~~~~~~~~~~~~~~~
USID is best suited for large, complex, and multidimensional scientific data.
It is also well suited when research is performed on multiple (especially commercial) instruments that generate data of different dimesionalities, scientific modalities, that will need to be correlated or compared routinely.

USID can seem like an overkill if one is working solely on simple and small data like spectra or images. In such cases, software such as ImageJ might be a better fit.
USID is not the best fit when a database solution with search capabilities. However, it will make it easier when combined with a Database / SDMS

Is it mandatory to store the results of data processing within the same file?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
No, it is not mandatory that the results be stored within the same file as the source dataset(s).
If data are distributed over multiple files, it is the responsibility of the users to manage relationships between the files.
In contrast, storing everything related to a measurement in the same file allows easier tracking of analyses and processing steps, which is why we recommend this strategy.

That being said, if and when a robust `scientific data management software (SDMS) <https://www.olcf.ornl.gov/olcf-resources/rd-project/scientific-data-management-system-sdms/>`_
capable of tracking provenance (results present in file X came from dataset in file Y) was regularly being used to support research,
spreading data over multiple files and managing them would be a lot easier.

How flexible are the rules in USID?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The philosophy of flattening datasets to 2D matrices that are supported by four ancillary matrices is the core aspect of USID.
Beyond this philosophy, the remaining aspects such as the nomenclature of the groups, storing only one raw measurement (and resultant results),
are far more flexible and what we presented in our documentation can be thought of as guidelines rather than strict rules.

How can I reference USID?
~~~~~~~~~~~~~~~~~~~~~~~~~
Please reference our `Arxiv <https://arxiv.org/abs/1903.09515>`_ paper for now.
This manuscript was submitted to Advanced Structural and Chemical Imaging recently and is currently being peer-reviewed.
