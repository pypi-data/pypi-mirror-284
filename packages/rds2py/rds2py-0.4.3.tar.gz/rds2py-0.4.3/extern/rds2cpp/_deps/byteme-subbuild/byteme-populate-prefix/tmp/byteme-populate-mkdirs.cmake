# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

# If CMAKE_DISABLE_SOURCE_CHANGES is set to true and the source directory is an
# existing directory in our source tree, calling file(MAKE_DIRECTORY) on it
# would cause a fatal error, even though it would be a no-op.
if(NOT EXISTS "/home/runner/work/rds2py/rds2py/extern/rds2cpp/_deps/byteme-src")
  file(MAKE_DIRECTORY "/home/runner/work/rds2py/rds2py/extern/rds2cpp/_deps/byteme-src")
endif()
file(MAKE_DIRECTORY
  "/home/runner/work/rds2py/rds2py/extern/rds2cpp/_deps/byteme-build"
  "/home/runner/work/rds2py/rds2py/extern/rds2cpp/_deps/byteme-subbuild/byteme-populate-prefix"
  "/home/runner/work/rds2py/rds2py/extern/rds2cpp/_deps/byteme-subbuild/byteme-populate-prefix/tmp"
  "/home/runner/work/rds2py/rds2py/extern/rds2cpp/_deps/byteme-subbuild/byteme-populate-prefix/src/byteme-populate-stamp"
  "/home/runner/work/rds2py/rds2py/extern/rds2cpp/_deps/byteme-subbuild/byteme-populate-prefix/src"
  "/home/runner/work/rds2py/rds2py/extern/rds2cpp/_deps/byteme-subbuild/byteme-populate-prefix/src/byteme-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/runner/work/rds2py/rds2py/extern/rds2cpp/_deps/byteme-subbuild/byteme-populate-prefix/src/byteme-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/runner/work/rds2py/rds2py/extern/rds2cpp/_deps/byteme-subbuild/byteme-populate-prefix/src/byteme-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
