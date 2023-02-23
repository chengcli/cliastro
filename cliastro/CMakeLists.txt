# Installs cliastro library
#
#   library: libcliastro_debug.o
#   library: libcliastro_release.o
#
# Define the following variables
#
#   CLIASTRO_FOUND
#   CLIASTRO_INCLUDE_DIR
#   CLIASTRO_LIBRARY_DEBUG
#   CLIASTRO_LIBRARY_RELEASE
#
# Normal usage would be:
#
#   include_directories( ${CLIASTRO_INCLUDE_DIR})
#   target_link_libraries( ${CLIASTRO_LIBRARY_DEBUG})
#

file(GLOB _src_files 
  *.cpp
  Jupiter/*.cpp
  Saturn/*.cpp
  )

foreach(build ${BUILD_TYPES})
  string(TOLOWER ${build} buildl)
  add_library(cliastro_${buildl}
    ${_src_files})

  #add_dependencies(cliastro_${buildl} athenapp_${buildl})

  set_target_properties(cliastro_${buildl}
    PROPERTIES
    COMPILE_FLAGS ${CMAKE_CXX_FLAGS_${build}}
    )

  target_include_directories(cliastro_${buildl}
    SYSTEM PRIVATE
    ${CLIMATH_INCLUDE_DIR}
    ${CLIMATH_INCLUDE_DIR}
    ${DEBUGGER_INCLUDE_DIR}
    ${ATHENAPP_INCLUDE_DIR}
    ${CLIUTILS_INCLUDE_DIR}
    ${MPI_CXX_INCLUDE_PATH}
    ${CMAKE_BINARY_DIR}
  )

  target_link_libraries(cliastro_${buildl}
    ${CLIMATH_LIBRARY_${build}}
    ${DEBUGGER_LIBRARY_${build}}
    ${ATHENAPP_LIBRARY_${build}}
    ${CLIUTILS_LIBRARY_${build}}
    ${MPI_CXX_LIBRARIES}
    )

  set(CLIASTRO_LIBRARY_${build} cliastro_${buildl}
    CACHE STRING 
    "cliastro library ${build}")
  mark_as_advanced(CLIASTRO_LIBRARY_${build})
endforeach()

set(CLIASTRO_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/..
  CACHE PATH 
  "cliastro include directory")
set(CLIASTRO_FOUND TRUE CACHE BOOL "FIND CLIASTRO LIBRARY")
mark_as_advanced(CLIASTRO_INCLUDE_DIR)
mark_as_advanced(CLIASTRO_FOUND)
