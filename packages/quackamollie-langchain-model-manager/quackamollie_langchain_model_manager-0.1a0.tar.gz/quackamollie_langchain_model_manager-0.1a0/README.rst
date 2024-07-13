====================================
Quackamollie Langchain Model Manager
====================================

:Name: Quackamollie Langchain Model Manager
:Package name: quackamollie-langchain-model-manager
:Description: Model manager compatible with Langchain models for Quackamollie Telegram chat bot
:Version: 0.1a0
:Main page: https://gitlab.com/forge_of_absurd_ducks/quackamollie/lib/model_managers/quackamollie_langchain_model_manager
:PyPI package: https://pypi.org/project/quackamollie-langchain-model-manager/
:Docker Image: registry.gitlab.com/forge_of_absurd_ducks/quackamollie/lib/model_managers/quackamollie_langchain_model_manager:0.1a0
:Documentation: https://langchain-model-manager-forge-of-absurd-ducks-qu-910c28e8f82e0a.gitlab.io/
:Build Status:
    :Master: |master_pipeline_badge| |master_coverage_badge|
    :Dev: |dev_pipeline_badge| |dev_coverage_badge|

.. |master_pipeline_badge| image:: https://gitlab.com/forge_of_absurd_ducks/quackamollie/lib/model_managers/quackamollie_langchain_model_manager/badges/master/pipeline.svg
   :target: https://gitlab.com/forge_of_absurd_ducks/quackamollie/lib/model_managers/quackamollie_langchain_model_manager/commits/master
   :alt: Master pipeline status
.. |master_coverage_badge| image:: https://gitlab.com/forge_of_absurd_ducks/quackamollie/lib/model_managers/quackamollie_langchain_model_manager/badges/master/coverage.svg
   :target: https://gitlab.com/forge_of_absurd_ducks/quackamollie/lib/model_managers/quackamollie_langchain_model_manager/commits/master
   :alt: Master coverage status

.. |dev_pipeline_badge| image:: https://gitlab.com/forge_of_absurd_ducks/quackamollie/lib/model_managers/quackamollie_langchain_model_manager/badges/dev/pipeline.svg
   :target: https://gitlab.com/forge_of_absurd_ducks/quackamollie/lib/model_managers/quackamollie_langchain_model_manager/commits/dev
   :alt: Dev pipeline status
.. |dev_coverage_badge| image:: https://gitlab.com/forge_of_absurd_ducks/quackamollie/lib/model_managers/quackamollie_langchain_model_manager/badges/dev/coverage.svg
   :target: https://gitlab.com/forge_of_absurd_ducks/quackamollie/lib/model_managers/quackamollie_langchain_model_manager/commits/dev
   :alt: Dev coverage status

----

Project description
===================
Quackamollie is a Telegram chat bot in Python using the library `aiogram` to serve LLM models running locally using Ollama.
This package is a model manager exposing Langchain models for the Quackamollie project.
It contains:

 - a model manager `LangchainQuackamollieModelManager` class implementing abstract functions of `MetaQuackamollieModelManager`

Learn more about Quackamollie on the project main page : https://gitlab.com/forge_of_absurd_ducks/quackamollie/quackamollie


Requirements
============

Virtual environment
------------------------------
- Setup a virtual environment in python 3.10

.. code-block:: bash

   make venv
   # or
   python3 -m venv venv

- Activate the environment

.. code-block:: bash

   source venv/bin/activate

- If you want to deactivate the environment

.. code-block:: bash

   deactivate


Tests
=====

Tests requirements
------------------
- Install test requirements

.. code-block:: bash

   make devtools
   # or
   pip install tox

Run pytest
----------
- Run the tests

.. code-block:: bash

   tox

Run lint
--------
- Run the lintage

.. code-block:: bash

   tox -e lint


Documentation
=============

- To auto-generate the documentation configuration

.. code-block:: bash

   tox -e gendocs

- To generate the documentation in Html

.. code-block:: bash

   tox -e docs

- An automatically generated version of this project documentation can be found at `here <https://langchain-model-manager-forge-of-absurd-ducks-qu-910c28e8f82e0a.gitlab.io/>`_


Install
=======
- Install the application from sources

.. code-block:: bash

   make install
   # or
   pip install .

- Or install it from distribution

.. code-block:: bash

   pip install dist/quackamollie-langchain-model-manager-0.1a0.tar.gz

- Or install it from wheel

.. code-block:: bash

   pip install dist/quackamollie-langchain-model-manager-0.1a0.whl

- Or install it from PyPi repository

.. code-block:: bash

   pip install quackamollie-langchain-model-manager  # latest
   # or
   pip install "quackamollie-langchain-model-manager==0.1a0"


Docker
======
- To build the application docker

.. code-block:: bash

   docker build --network=host -t quackamollie_langchain_model_manager:0.1a0 .

- The official Docker image of this project is available at: registry.gitlab.com/forge_of_absurd_ducks/quackamollie/lib/model_managers/quackamollie_langchain_model_manager

- You can pull the image of the current release:

.. code-block:: bash

   docker pull registry.gitlab.com/forge_of_absurd_ducks/quackamollie/lib/model_managers/quackamollie_langchain_model_manager:latest  # or dev
   # or
   docker pull registry.gitlab.com/forge_of_absurd_ducks/quackamollie/lib/model_managers/quackamollie_langchain_model_manager:0.1a0


Running the model manager
=========================
`quackamollie-langchain-model-manager` package is automatically discovered, through entrypoints, by the command tool line named `quackamollie`.
Therefore, once installed, you should automatically see models managed by this model manager in Telegram `/settings` command.

You can install models for this model manager by simply pulling them using the `ollama <https://ollama.com/>`_ command:

.. code-block:: bash

   ollama pull llama3

For details on how to run the Quackamollie project, please refer to the `Quackamollie's project main page <https://gitlab.com/forge_of_absurd_ducks/quackamollie/quackamollie>`_.


Authors
=======

- **QuacktorAI** - *Initial work* - `quacktorai <https://gitlab.com/quacktorai>`_


Contributing
============
Currently, contributions are frozen because the project is still in very early stages and I have yet to push the whole architecture.

For more details on the general contributing mindset of this project, please refer to `CONTRIBUTING.md <CONTRIBUTING.md>`_.


Credits
=======

Section in writing, sorry for the inconvenience.
