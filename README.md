# PicoCTF Solution: Decimal-to-ASCII Application

Exercise provided by PicoCTF: https://play.picoctf.org/practice/challenge/156?category=5&page=1

An (overly engineered) application to solve the PicoCTF challenge: 'Nice Netcat...' that can be used for any server outputing decimal outputs or files with decimals to be converted to ASCII. Description of the exercise provided by PicoCTF:
```
There is a nice program that you can talk to by using this command in a shell: $ [Server and Port provided], but it doesn't speak English...
```


## Features

* Make a connection to the server.
* Record the output from the server.
* Convert the output from decimal to ASCII.

### Additional Features

* Takes input of any server and port and saves the output to a file.
* Takes a file as an input and converts the content from Decimal to ASCII.


## Current state

> Complete - all features implemented. 


## Usage

Flags are used to add optional features:
* -h                      : Provides help information for the application. 
* -f [filepath]           : Takes the provided file for conversion. 
* -s [hostname/IP] [Port] : Make a connection to provided server and port to read from.

To run the base application from command line:
```bash
decimal_to_ascii.py -f [filepath]

decimal_to_ascii.py -s [hostname/IP] [Port]

```


## How It Works

The application checks which arguments are given. If a file has been provided, the application reads the contents and save it as a list. This list is then iterated over to convert from decimal to ASCII and then the file string is output to the screen. 
If a server and port are provided, a connection is made and the output from the server is saved to a file and then fed into the same function if a file is provided. 
