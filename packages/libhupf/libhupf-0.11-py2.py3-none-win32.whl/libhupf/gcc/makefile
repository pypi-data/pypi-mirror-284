VPATH = ../src
.RECIPEPREFIX +=

print-%  : ; @echo $* = $($*)

CC = gcc
#exclude empty.cpp
src = $(filter-out ../src/empty.cpp, $(wildcard ../src/*.cpp))

objdir=$(OUT)
#./release
dllfile=$(objdir)/libhupf.so
_obj1 = $(patsubst %.cpp,%.o,$(src))
obj = $(patsubst %.o,$(objdir)/%.o,$(notdir $(_obj1)))
libs = 

# needs apt-get install gcc-multilib g++-multilib
INCLUDES = -I../inc
CXXFLAGS=-DNDEBUG -DLIBHUPF_EXPORTS -Os -g -s -Wall -Wextra -m32 -Wno-unknown-pragmas -Wno-deprecated-declarations -Wno-parentheses -Wno-unused-function -fopenmp -std=c++11
# -std=c++98 -flto 

#link flags
LDFLAGS = -lstdc++
#-fno-use-linker-plugin 

# rule to generate a dep file by using the C preprocessor
# (see man cpp for details on the -MM and -MT options)
# compiles .c to .o
# $@ = $(output)
# $< = $(input)
$(objdir)/%.o: %.cpp
  @echo "Compiling..."
  $(CC) $(INCLUDES) $(CXXFLAGS) -c $< -o $@

libhupf: $(obj)
  @echo "Linking..."
  $(CC) $(CXXFLAGS) -Wno-maybe-uninitialized $(obj) -shared -o $(dllfile) $(LDFLAGS) $(libs) 
#-Wl,--verbose 
  
#.PHONY: clean, no padding with ifeq!!
clean:  
ifeq ($(OS), Windows_NT)
  del /f /q $(subst /,\,$(obj)) $(subst /,\,$(dllfile))
else
  rm -f $(obj) $(dllfile)
endif

