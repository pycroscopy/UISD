.. USID documentation master file, created by
   sphinx-quickstart on Wed Jun 27 10:37:14 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Universal Spectroscopy and Imaging Data  (USID)
===============================================

About
-----
USID is an open, community-driven, self-describing, and standardized schema for representing imaging and spectroscopy data of any size, dimensionality,
precision, instrument of origin, or modality. While the abstract USID schema can in theory be paired with any file format,
it performs best within Hierarchical Data Format Files (HDF5) which have become the de-facto standard in scientific research.
The combination of USID within HDF5 files is refered to as **h5USID**.

The flexible and open nature of both HDF5 and USID elevates USID data stored in HDF5 files to be curation-ready and therefore
both meet the guidelines for data sharing issued to federally funded agencies and satisfy the implementation of digital data
management as outlined by the United States Department of Energy. Traceability and reproducibility of both the experiments as
well as the data processing routines in h5USID are captured through comprehensive and consistent metadata stored as attributes
where appropriate, in addition to links created between the data source and the analysis results within the HDF5 file.
Despite the fact that it was developed independently, h5USID already satisfies most of the requirements of FAIR principles
and we intend to make necessary changes to satisfy all the recommendations put forward in the FAIR principles.

Related projects
----------------
* `pyUSID <../pyUSID/about.html>`_ provides a convenient python interface to read and write to h5USID files.

* `pycroscopy <../pycroscopy/about.html>`_  has several tools for `translating <../pycroscopy/translators.html>`_ data
  from proprietary files generated from popular scanning probe and scanning transmission electron microscopes into h5USID files

More information
----------------
We encourage you to go through the `motivation <./motivation.html>`_ for USID, read more about `USID <./usid_model.html>`_,
and see why it is best paired with `HDF5 <./file_format.html>`_.
We have a few `hands-on <./auto_examples/index.html>`_ to illustrate how a few common data types can be represented in USID.
We also provide `detailed specifications <./h5_usid>`_ on how the data and metadata are structured in h5USID files.
We also have some guidelines on capturing contextual `metadata <./metadata.html>`_ to support the data.

Should you have any questions, please feel free to `get in touch with us <./contact.html>`_

Site index
----------
.. currentmodule:: index

.. autosummary::
   :template: module.rst

.. toctree::
   :maxdepth: 1

   index
   motivation
   nomenclature
   usid_model
   file_format
   auto_examples/index
   h5_usid
   metadata
   advanced_topics
   faq
* :ref:`search`
