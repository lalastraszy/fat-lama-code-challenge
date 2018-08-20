# Backend Challenge

Install system dependencies
-------------
 - Install python3, see [instructions](https://docs.python-guide.org/starting/install3/osx/).
 - Install virtualenv and activate it, see [instructions](https://docs.python-guide.org/dev/virtualenvs/#virtualenvironments-ref)
 - Install SpatiaLite, see [instruction](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/install/spatialite/)

Running Server
-------------
1. Modify `SPATIALITE_LIBRARY_PATH` in run_server.sh
2. Run below command


    $ ./run_server.sh

Running Tests
-------------
1. Modify SPATIALITE_LIBRARY_PATH in run_tests.sh
2. Run below command


    $ ./run_tests.sh
    
    
Summary on the approach
-------------

I decided to use [Tornado](http://www.tornadoweb.org/en/stable/) framework because it provides reasonable performance and is good for building a very performant web application.
To implemented a localization search logic I used [SpatiaLite](https://www.gaia-gis.it/fossil/libspatialite/index) SQLite extension and [GeoAlchemy2](https://geoalchemy-2.readthedocs.io/en/latest/) library.
To do serializing/deserializing and validation I used [Schematics](https://schematics.readthedocs.io/en/latest/).
