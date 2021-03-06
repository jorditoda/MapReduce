# MapReduce Project

This is a simple project example on github using the
[MapReduce](https://github.com/jorditoda/MapReduce) library.

[![Build Status](https://travis-ci.org/jorditoda/MapReduce.svg?branch=master)](https://travis-ci.org/jorditoda/MapReduce)
[![codecov](https://codecov.io/gh/jorditoda/MapReduce/branch/master/graph/badge.svg)](https://codecov.io/gh/jorditoda/MapReduce)
[![Code Health](https://landscape.io/github/jorditoda/MapReduce/master/landscape.svg?style=flat)](https://landscape.io/github/jorditoda/MapReduce/master)


## Installing PyActor

Packages required:

    python, python-dev, python-pip

Install with:

    sudo pip install pyactor

Or download the source by cloning [PyActor](https://github.com/pedrotgn/pyactor)'s
repository and installing with:

    sudo python setup.py install

If you clone the repository, you will also have access to the tests and a folder
full of examples. Just check the github page and the documentation for a detailed
tutorial.

## Installing curl

Install with:

    sudo apt-get install curl

## Documentation

As a requirement is important to have installed pyactor and curl.

Is very important to always document your code, as you may know.

To set up your docs at readthedocs.org, follow the guide to build a new documentation project in rst using sphinx: https://docs.readthedocs.io/en/latest/getting_started.html

Then, add a .rst file on the docs directory with the text you want. Reference that file in the index.rst file, so it appears on the docs' content tree.

## Classes:
### CountWordSequencial:

  It counts how many times appears a word in a text.

### WordCounterSequencial:

  It counts all the words in a text.

### Mapper:

  It creates a host and gets registered in the registry class. And starts serving.

### Registry:

```plain
  It creates a host and waits until the mappers and the reducer get registered. It have some functions.
  bind: Register a host in the dictionary.
  unbind: Deletes a host from the dictionary.
  lookup: Returns the proxy associated to the name entered by parameter.
  get_all: Return all the values of the dictionary.
```
### Reduce:

  It creates a host and gets registered in the registry class. And starts serving.

### Master:

  It creates a host and checks that the file we want to read is already downloaded or not. It counts all the lines to divide them to all the mappers. Catch and delete the reduce proxy from the registry list and catch the rest of the proxys to count how many mappers we have. We calculate the number of lines of the text for each mapper. We make a spawn of the reducer and another for the master. After that for all the mappers we do a spawn and send the mapper the information needed for their work (the text, the line_start, the line_finish, the reducer's spawn, the master's spawn, the number of mappers, the time of the starting execution. ) only for the WordCount. After waiting the until the user taps the enter to start the CountWord part and gives to the mappers the same information as before for counting. It serves forever because it waits for the reducer's respond to print it.

### WordCount:

```plain
  wordCount:It counts all the words in a text.
  puntuation: Changes all the punctuation symbols into spaces and the capitals letters to lower letters.
```

### CountWord:

```plain
  countWord: It counts how many times appears a word in a text.
  add: It adds a word into a dictionary if it doesn't exist. If it exists this add one value to the word.
  puntuation: Changes all the punctuation symbols into spaces and the capitals letters to lower letters.  
```

### Echo:

```plain
  echo: It prints a string.
```

### ReduceMapper:

```plain
  addR: It adds a word to the dictionary if it doesn't exists. If the word exists it adds one value to the times it has appeared.
  reduceW: It collects all the words of each mapper in the same dictionary and also returns the time that has used in calculate all of them.
  reduceC: It collects all the word counted of each mapper and returns the time used to do it and the total number of words.
```

## SpeedUp

-**sherlock.txt(6,5MB):**

	WordCounterSequencial: 2,44s
	CountWordSequencial: 2,72s

	4 mappers:
		wordCount: 0,74s
		countWord: 1,68s

	speedup WC: 3,29
	speedup CW: 1,62

-**bible2.txt(8,9MB):**

	WordCounterSequencial: 40,33s
	CountWordSequencial: 43,87s

	4 mappers:
		wordCount: 10s
		countWord: 21,62s

	speedup WC: 4,03
	speedup CW: 2,03

  -**sherlock2.txt(558,1MB):**

  	WordCounterSequencial: 4m 29s
  	CountWordSequencial: 5m 53s

  	4 mappers:
  		wordCount: 1m 17s
  		countWord: 2m 36s

  	speedup WC: 3,49
  	speedup CW: 2,26
