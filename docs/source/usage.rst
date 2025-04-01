Usage
=====

.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']


These variables are incorporated into the SBML reaction components in units of milligrams per gram of dry weight (mg/gDW). An upper bound on the total modeled protein is configured, and reaction fluxes are coupled to protein requirements according to the following general formulation:

.. math::

       \min_{x \in R^n} f(x)

subject to

.. math::

       gxyz_L \leq grx(x) \leq gxxx_{Udd}

       x_L \leq  x  \leq x_U




The *flux* is expressed in mmol/gDW, *kcat* denotes the turnover number in 1/h, *stoic* signifies the number of protein copies in the catalyzing enzyme, *n_AS* indicates the number of active sites in the enzyme, *\[P]* represents the protein concentration in mg/gDW, 





