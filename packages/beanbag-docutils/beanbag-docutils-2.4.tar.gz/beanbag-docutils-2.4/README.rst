=====================
Beanbag Doc Utilities
=====================

This is a collection of utilities to help with generating documentation for
Beanbag-related products, including:

* `Review Board`_ - Our widely-used open source code review product.
* RBCommons_ - Our Review Board SaaS.
* Djblets_ - A set of utilities and infrastructure for Django-based projects.
* RBTools_ - Command line tools for Review Board and RBCommons.


.. _Review Board: https://www.reviewboard.org/
.. _RBCommons: https://www.rbcommons.com/
.. _Djblets: https://github.com/djblets/djblets/
.. _RBTools: https://github.com/reviewboard/rbtools/


Sphinx Extensions
=================

Most of the utilities are used with the Sphinx_ documentation system. Amongst
other enhancements, this package offers:

* A parser for the `Beanbag docstring format`_ (a variation on the `Google
  docstring format`_), which we use for Python and JavaScript documentation
* Enhancements for Sphinx's intersphinx_ system to provide per-page
  intersphinx resolution options (useful for pages, such as release notes,
  that need to link to different versions of the same docs, such as Django_ or
  Python)
* Enhancements to ReStructuredText references to let a reference name span
  lines (useful for long Python/JavaScript module/class names)
* Linking code references to GitHub documentation
* High-DPI image embedding
* A role for HTTP status codes
* Access to document-defined metadata in a structured form when parsing
  documents


.. _Beanbag docstring format:
   https://www.notion.so/reviewboard/Standard-Documentation-Format-4388f594d86547cc949b365cda3cf391
.. _Django: https://www.djangoproject.com/
.. _Google docstring format:
   https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings
.. _intersphinx:
   https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
.. _our products: https://www.beanbaginc.com/
.. _ReStructuredText:
   https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
.. _Sphinx: https://www.sphinx-doc.org/


Compatibility
=============

* beanbag-docutils 2.x supports Python 3.6-3.12 and Sphinx 1.8-7.x.
* beanbag-docutils 1.x supports Python 2.7 and 3.6-3.10.


Getting Started
===============

To install the package, run:

.. code-block:: shell

   $ pip install beanbag-docutils


See the documentation_ for usage information.


.. _documentation: https://beanbag-docutils.readthedocs.io/
