Getting Started
===============

Molo scaffolds a Django application for you with sensible defaults, packages
and configuration to help you get going as soon as possible.

Scaffold a site using Molo
--------------------------

The goal of Molo is to provide a solid base of proven, stable packages that
help Praekelt.org and partners to deliver on project scope::

   $ molo scaffold myapp
   $ cd myapp/
   $ ./manage.py migrate
   $ ./manage.py createsuperuser
   $ ./manage.py runserver

Open the sample site in your browser at http://localhost:8000/ and the CMS
at http://localhost:8000/admin/.

Scaffolding a site in an existing repository
--------------------------------------------

It's not always desirable to create a new directory for an application,
especially when scaffolding an application for a repository that's already
been created. Specifically for that Molo allows a second argument for the
directory.

To scaffold an application called ``myapp`` in the current directory do::

   $ molo scaffold myapp .

Specifying extra requires
-------------------------

Molo in itself is not expected to be enough to deliver on a client request.
During scaffolding use the ``--require`` commandline parameter to include
more libraries that are required for installation::

   $ molo scaffold myapp --require=django-contrib-comments

Adds the `django-contrib-comments` to the generated requirements file which
is read by the generated package's ``setup.py`` file.

Multiple requires can be specified on the command line::

   $ molo scaffold myapp --require=django-contrib-comments \
   >   --require=molo.profiles

Automatically adding installed apps
-----------------------------------

If you're including a Django app chances are you're going to want to
add it to your ``INSTALLED_APPS`` settings as well as adding an entry
to the generated ``urls.py`` file::

   $ molo scaffold myapp --include=django_comments ^comments/

This results in the following ``urls.py`` entry::

   url(r'^comments/',
       include('django_comments.urls',
               namespace='django_comments',
               app_name='django_comments')),

.. note:: multiple includes can be specified on the command line, the format
          is ``--include=<app_name> <regex-for-urls>``

For convenience, here's the full scaffold command for the current plugins::

    $ molo scaffold myapp \
        --require=molo.profiles --include=molo.profiles ^profiles/ \
        --require=django-contrib-comments --include=django_comments ^comments/ \
        --require=molo.commenting --include=molo.commenting ^commenting/ \
        --require=molo.yourwords --include=molo.yourwords ^yourwords/

.. note:: ``molo.profiles`` is a requirement of molo core and is therefore automatically installed when molo is installed.

Molo, Django & settings files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You now have a standard Django application set up for normal development.
The only difference is that your settings are Python modules found in the ``settings/dev.py`` and ``settings/production.py`` files in your applications folder.
Both of these inherit settings from ``settings/base.py``.

To create your own custom settings add a ``local.py`` file in the ``settings``
folder. The ``settings/dev.py`` will automatically include those settings
for your local development environment.

Unpacking Templates from Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes a package's existing templates simply are not enough and need
some amount of customization. Use the ``unpack-templates`` command in the
scaffolded application to unpack a package's templates in your application's
templates directory::

   $ molo scaffold testapp \
   >   --require=molo.profiles \
   >   --include=molo.profiles ^profiles/
   $ pip install -e testapp
   ...

You'll see the default templates that ``molo.core`` ships with available in
the ``templates`` directory::

   $ ls testapp/testapp/templates
   404.html  500.html  base.html core

Now we unpack the ``profiles`` templates directory from the ``molo.profiles``
package into the ``testapp`` package template directory::

   $ molo unpack-templates molo.profiles testapp
   $ ls testapp/testapp/templates
   404.html  500.html  base.html core profiles

The format is::

   $ molo unpack-templates <source package> <target package>

Writing tests
~~~~~~~~~~~~~

Now develop your application and write tests for the features you add.
Running your tests for Django works as you would expect::

   $ ./manage.py test


Testing the Molo scaffolding tool
---------------------------------

If you're interested in working on or contributing to the code that
does the scaffolding then clone this repository from the GitHub repository at
http://github.com/praekelt/molo.

Install the requirement development & testing dependencies::

   $ pip install -r requirements-dev.txt

And then run the full test suite with::

   $ py.test

Pull requests are expected to follow Praekelt's `Ways Of Working`_.

.. _`Ways of Working`: http://ways-of-working.rtfd.org
