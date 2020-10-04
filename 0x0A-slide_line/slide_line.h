#ifndef SLIDE
#define SLIDE

#include <stdlib.h>
#include <stdio.h>

#define SLIDE_LEFT  1
#define SLIDE_RIGHT 2

int slide_line(int *line, size_t size, int direction);

#endif
