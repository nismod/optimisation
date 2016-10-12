==========
nismod_opt
==========

This is the documentation of **nismod_opt**.

Installing Python, required modules and nismod_opt
================================================

By far the easiest and recommended way to obtain a working Python installation
including the required Python modules is to use the `Miniconda distribution
<http://conda.pydata.org/miniconda.html>`_,
which does not come with any pre-included packages, downloading packages only
as required.

Once you have Miniconda installed, you can create a new Python 3.5 environment
called "nismod_opt" with all the necessary modules with the following command
(see the note on Windows below if this command causes an error)::

   $ conda create -n nismod_opt python=3.5 pip --yes

Then, you need to activate the "nismod_opt" environment. On Linux and Mac OS X::

   $ source activate nismod_opt

On Windows::

   $ activate nismod_opt

Finally, install nismod_opt with the Python package installer pip,
which will also automatically install Pyomo (and any other remaining
dependencies not installed already)::

   $ pip install nismod_opt

.. _windows_install_note:

.. Note::

   nismod_opt has been tested on Windows 7 and Windows 8 and should generally
   work, but running Python software on Windows can be trickier than on
   Linux or Mac OS:

Installing a solver
===================

You need at least one of the solvers supported by Pyomo installed.
GLPK or Gurobi are recommended and have been confirmed to work with nismod_opt.
Refer to the documentation of your solver on how to install it.
Some details on GLPK and Gurobi are given below.
Another commercial alternative is
`CPLEX <http://ibm.com/software/integration/optimization/cplex-optimization-studio/>`_.

GLPK
----

`GLPK <https://www.gnu.org/software/glpk/>`_ is free and open-source,
but can take too much time and/or too much memory on larger problems.

If using Anaconda, GLPK can be easily installed into the "nismod_opt"
environment (make sure the environment has been activated as shown above)::

   $ conda install -c cachemeorg glpk=4.47

More recent versions of GLPK cause problems with Pyomo and should not be used
for now. To install GLPK manually,
refer to the `GLPK website <https://www.gnu.org/software/glpk/>`_.

Gurobi
------

`Gurobi <http://www.gurobi.com/>`_ is commercial but significantly faster
than GLPK, which is relevant for larger problems.
It needs a license to work, which can be obtained for free for academic use
by making an account on gurobi.com.

On Windows and Linux, Gurobi can be installed via conda::

    $ conda install -c gurobi gurobi

On Mac OS X, it has to be downloaded manually from the
`Gurobi website <http://www.gurobi.com/>`_.

After installing, log on to gurobi.com and obtain a (free or paid) license,
then activate it on your system via the instructions given online
(using the ``grbgetkey`` command).

Contents
========

.. toctree::
   :maxdepth: 2

   License <license>
   Authors <authors>
   Changelog <changes>
   Module Reference <api/modules>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
