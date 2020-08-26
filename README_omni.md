# Maya USD Omni Fork #

This document contains information specific to the fork of Maya USD
that you're currently looking at.

## Building ##

Example build steps on macOS:

```
rez-env python-2 boost opensubdiv cmake glew tbb openexr usd-tdg jinja2 googletest maya-2020 openimageio usd_maya_plugins

mkdir build

cd build

cmake ../ -G "Xcode" -DCMAKE_INSTALL_PREFIX=~/tmp/build/maya_usd -DPXR_USD_LOCATION=$REZ_USD_ROOT/osx -DMAYA_LOCATION=$REZ_MAYA_ROOT/osx/Applications/Autodesk/maya2020 -DMAYA_LIBRARY_DIR=$REZ_MAYA_ROOT/osx/Applications/Autodesk/maya2020/Maya.app/Contents/MacOS -DBOOST_ROOT=$REZ_BOOST_ROOT/osx -DTBB_ROOT=$REZ_TBB_ROOT/osx -DMAYAUSD_LIB_ROOT=$REZ_MAYA_USD_ROOT/osx/lib -DMAYAUSD_INCLUDE_ROOT=$REZ_MAYA_USD_ROOT/osx/include -DBoost_NO_BOOST_CMAKE=ON -DBUILD_AL_PLUGIN=ON -DGTEST_ROOT=/usr/local/apps/googletest/1.10.0/osx -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_BUILD_TYPE=Debug

cmake --build . --config Debug --target install
```

To run:

```
export MAYA_MODULE_PATH=$MAYA_MODULE_PATH:~/tmp/build/maya_usd && open -n -a $REZ_MAYA_ROOT/osx/Applications/Autodesk/maya2020/Maya.app
```

## Making a release ##

- Ensure that you have built the following first already within the
  Omni pipeline, in the following order:
      - Boost
      - OpenImageIO
      - Alembic
      - USD
      - Maya USD
      - Maya USD Plugins

- Build maya-usd from the omnithirdparty recipe.
- Now make a release from the `/usr/local/apps/maya-usd/<version>` directory. `rez-env omnilauncher -- rez-deploy`
