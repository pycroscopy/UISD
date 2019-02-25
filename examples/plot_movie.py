"""
================================================================================
05. Movie / Stack of 2D images
================================================================================

**Suhas Somnath**

2/02/2018

**This example illustrates how data representing a movie, time series, or a stack of images can be represented in
Universal Spectroscopic and
Imaging Data (USID) schema and stored in a Hierarchical Data Format (HDF5) file, also referred to as the h5USID file.**
The data for this example is a sequence of 2D grayscale scan images acquired from a Scanning Transmission Electron
Microscope (STEM). While USID offers a clear and singular solution for representing most data, videos fall under a gray
area and can be represented in `two ways <../usid_model.html#videos>`_. Here, we will explore the two ways for
representing movie or time series data.

This document is intended as a supplement to the explanation about the `USID data model <../usid_model.html>`_

Please consider downloading this document as a Jupyter notebook using the button at the bottom of this document.

Prerequisites:
--------------
We recommend that you read about the `USID data model <../usid_model.html>`_

We will be making use of the ``pyUSID`` package at multiple places to illustrate the central point. While it is
recommended / a bonus, it is not absolutely necessary that the reader understands how the specific ``pyUSID`` functions
work or why they were used in order to understand the data representation itself.
Examples about these functions can be found in other documentation on pyUSID and the reader is encouraged to read the
supplementary documents.

Import all necessary packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The main packages necessary for this example are ``h5py`` and ``matplotlib`` in addition to ``pyUSID``:
"""

from __future__ import print_function, division, unicode_literals
import subprocess
import sys
import os
from warnings import warn
import h5py


def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


try:
    # This package is not part of anaconda and may need to be installed.
    import wget
except ImportError:
    warn('wget not found.  Will install with pip.')
    import pip
    install('wget')
    import wget

# Finally import pyUSID.
try:
    import pyUSID as usid
except ImportError:
    warn('pyUSID not found.  Will install with pip.')
    import pip
    install('pyUSID')
    import pyUSID as usid

########################################################################################################################
# Download the dataset
# ---------------------
# As mentioned earlier, this image is available on the USID repository and can be accessed directly as well.
# Here, we will simply download the file using ``wget``:
h5_path = 'temp.h5'
url = 'https://raw.githubusercontent.com/pycroscopy/USID/master/data/STEM_movie_WS2.h5'
if os.path.exists(h5_path):
    os.remove(h5_path)
_ = wget.download(url, h5_path, bar=None)

########################################################################################################################
# Open the file
# -------------
# Lets open the file and look at its contents using
# `pyUSID.hdf_utils.print_tree() <../../pyUSID/auto_examples/beginner/plot_hdf_utils_read.html#print-tree>`_

h5_file = h5py.File(h5_path, mode='r')
usid.hdf_utils.print_tree(h5_file)

########################################################################################################################
# Notice that this file has two `Measurement` groups, each having seemingly identical contents. We will go over the
# contents of each of these groups to illustrate the two ways one could represent movie data.

for key, val in usid.hdf_utils.get_attributes(h5_file).items():
    print('{} : {}'.format(key, val))


# In[4]:


h5_main = usid.hdf_utils.get_all_main(h5_file)[-1]
print(h5_main)


# In[8]:


print('N-dimensional shape:\t{}'.format(h5_main.get_n_dim_form().shape))
print('Dimesion names:\t\t{}'.format(h5_main.n_dim_labels))


# In[9]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[10]:


usid.plot_utils.use_nice_plot_params()
h5_main.visualize()


# In[11]:


fig, axes = usid.plot_utils.plot_map_stack(h5_main.get_n_dim_form(), 
                                           reverse_dims=True, 
                                           subtitle='Time step:', 
                                           title_yoffset=0.94, 
                                           title='Movie Frames')


# In[12]:


print('Position Indices:')
print('-------------------------')
print(h5_main.h5_pos_inds)
print('\nPosition Values:')
print('-------------------------')
print(h5_main.h5_pos_vals)


# In[14]:


fig, all_axes = plt.subplots(ncols=2, nrows=2, figsize=(8, 8))

for axes, h5_pos_dset, dset_name in zip(all_axes,
                                        [h5_main.h5_pos_inds, h5_main.h5_pos_vals],
                                        ['Position Indices', 'Position Values']):
    axes[0].plot(h5_pos_dset[()])
    axes[0].set_title('Full dataset')
    axes[1].set_title('First 2048 rows only')
    axes[1].plot(h5_pos_dset[:2048])
    for axis in axes.flat:
        axis.set_xlabel('Row in ' + dset_name)
        axis.set_ylabel(dset_name)
        axis.legend(h5_main.pos_dim_labels)

for axis in all_axes[1]:
    usid.plot_utils.use_scientific_ticks(axis, is_x=False, formatting='%1.e')
    axis.legend(h5_main.pos_dim_descriptors)

fig.tight_layout()


# In[16]:


for key, val in usid.hdf_utils.get_attributes(h5_main.h5_pos_inds).items():
    print('{}\t: {}'.format(key, val))


# In[17]:


print('Spectroscopic Indices:')
print('-------------------------')
print(h5_main.h5_spec_inds)
print('\nSpectroscopic Values:')
print('-------------------------')
print(h5_main.h5_spec_vals)


# In[19]:


fig, axes = plt.subplots(ncols=2, figsize=(8, 4))
for axis, data, title, y_lab in zip(axes.flat,
                                    [h5_main.h5_spec_inds[()].T, h5_main.h5_spec_vals[()].T],
                                    ['Spectroscopic Indices', 'Spectroscopic Values'],
                                    ['Index', h5_main.spec_dim_descriptors[0]]):
    axis.plot(data)
    axis.set_title(title)
    axis.set_xlabel('Row in ' + title)
    axis.set_ylabel(y_lab)

fig.tight_layout()


# In[20]:


for key, val in usid.hdf_utils.get_attributes(h5_main.h5_spec_inds).items():
    print('{}\t: {}'.format(key, val))


# In[21]:


h5_file.close()
# os.remove(h5_path)

