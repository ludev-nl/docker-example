CC=gcc
CCFLAGS=-O2 -Wall -Wextra
LDD=-lm

all: /build/helloworld

/build/helloworld: main.c
	$(CC) $(CCFLAGS) -o $@ $^ $(LDD)