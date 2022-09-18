shimtax - a pluggable codec manager for syntax modifying codecs
===============================================================

Setup
-----

shimtax can be set to be automatically enabled using the CLI.
This will insert a ``.pth`` file in the platlib directory returned by ``sysconfig.get_path("platlib")``.
That file will register the shimtax encoding so you don't have to.

.. code-block:: bash

    $ .venv/bin/shimtax register

The CLI can also remove the ``.pth`` file.

.. code-block:: bash

    $ .venv/bin/shimtax unregister
