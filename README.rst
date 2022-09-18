shimtax - a pluggable codec manager for Python syntax modifying encodings
=========================================================================

Yes, this is a joke.  But I think it works?  ``*rofl*``  A joke...  that works...

Projects like `Coconut <http://coconut-lang.org/>`__ and `cursed-for <https://github.com/tusharsadhwani/cursed-for>`__ offer new syntax on top of the standard Python syntax.
They achieve this by preprocessing code of their customized form down to standard Python.
One option for this preprocessing is to leverage the `source code encoding <https://docs.python.org/3/tutorial/interpreter.html#source-code-encoding>`__ features of Python.
For example, specifying ``# coding: coconut``, after some other setup, can enable Coconut syntax for that file.
But, what if you need multiple of these syntax modifying encodings?
That's where shimtax comes in and let's you apply multiple other encodings.

..
   TODO: find a pair that actually work

.. code-block:: python

   # coding: shimtax:cursed-for:coconut

   for (i = 0; i < 10; i += 2):
       i |> print

Given that each encoding is offering custom syntax that the others are presumably unaware of, expect many combinations to be order dependent or to simply not work.
Those that simply operate on the code as a string are much more likely to be mixable.
Those that parse the code via a Python syntax parser are likely to fail.

Setup
-----

shimtax can be set to be automatically enabled using the CLI.
This will insert a ``.pth`` file in the platlib directory returned by ``sysconfig.get_path("platlib")``.
That file will register the shimtax encoding so you don't have to.

.. code-block:: console

   $ .venv/bin/shimtax register

The CLI can also remove the ``.pth`` file.

.. code-block:: console

   $ .venv/bin/shimtax unregister

If handling this yourself is preferred, you can use the registration helper function.

.. code-block:: python

   import shimtax

   shimtax.register()
