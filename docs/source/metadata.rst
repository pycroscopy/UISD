Metadata
========

Data alone is insufficient for understanding the broader context for scientific information or data.
The data needs to be accompanied with information regarding the measurement instrument, experiment configuration,
sample information, user information, etc. This supplementary information is also referred to as **metadata**.

Metadata are typically structured via key-value pairs such as: ``"user" : "John Doe"``.


The goal must always be to capture as much relevant metadata as possible to support and provide context to data.
Here are some broad categories for metadata:

* Instrument
* Sample
* User
* Comments

Detailed information within each category needs to be captured through a hierarchical schema for easy discoverability.
We recommend structuring the metadata and using the vocabulary using community standards where available.
For example, the `CHiMaD Data and Database <http://chimad.northwestern.edu/news-events/CHiMaD_Data_Database_Efforts.html>`_
efforts aim to develop best practices and community standards for metadata for materials microscopy.
Similarly, the `Open Microscopy Environment <https://www.openmicroscopy.org>`_ (OME) has come up with standards for biological imaging community.

Given that HDF5 files, which are the container of choice for USID, are incapable of accepting nested or hierarchical values for attributes,
we recommend artificially facilitating hierarchy via a dedicated separator character. For example, the following metadata tree:

* Instrument :

  * Type : Scanning Transmission Electron Microscope
  * Vendor : FEI
  * Model : Titan

could be flattened to the following using ``-`` as the separator character:

* Instrument-Type : Scanning Transmission Electron Microscope
* Instrument-Vendor : FEI
* Instrument-Model : Titan