#
# This is an example GNUmakefile for my packages
#

# specific names for this package
DICT  = EventFiltersCint
SHLIB = libKalekoAna_EventFilters.so
SOURCES = $(filter-out $(DICT).cxx, $(wildcard *.cxx))
FMWK_HEADERS = LinkDef.h $(DICT).h
HEADERS = $(filter-out $(FMWK_HEADERS), $(wildcard *.h))
OBJECTS = $(SOURCES:.cxx=.o)

# include options for this package
INCFLAGS = -I.                       #Include itself
INCFLAGS += $(shell larlite-config --includes) #larlite
INCFLAGS += $(shell basictool-config --includes) #basictool

# platform-specific options
OSNAME          = $(shell uname -s)
HOST            = $(shell uname -n)
OSNAMEMODE      = $(OSNAME)

include $(LARLITE_BASEDIR)/Makefile/Makefile.${OSNAME}

# set linker flags
LDFLAGS += -L$(shell root-config --libdir)
LDFLAGS += $(shell larlite-config --libs)
LDFLAGS += $(shell basictool-config --libs)

# call the common GNUmakefile
include $(LARLITE_BASEDIR)/Makefile/GNUmakefile.CORE



