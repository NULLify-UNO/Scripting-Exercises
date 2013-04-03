#!/usr/bin/perl --

# Created for NULLify (2013) by Kevin Dolphin for a Perl socket example to SpenceHouse's
# server program.

# Program will open a socket based on localhost:8675 and communicates with a server via IO::Socket
# We will guess a number until we have found the correct random number determined by SpenceHouse's server.

use IO::Socket;
use Modern::Perl;

my ($socket, $count, $response, $low, $high, $guess, $alive);
$high ='1000000000'; $low = 0; $alive = 1; $count = 0 ;
# Max number	      lowest     conn        num guesses

$socket = new IO::Socket::INET(
	PeerHost=>'127.0.0.1', # set IP
	PeerPort=>'8675', # set PORT
	Proto=>'tcp', # set protocol

) or die "Socket creation error\n"; # die if can't create socket

while ($alive){
	$guess = int(($high+$low)/2); # convert to int because abs(), ceil(), and floor() is broken for me
	$socket->send($guess); # send our guess

	$response = <$socket>; # read if high/low/correct

	if ($response =~ /low/ig){
		print "Tried $guess, was low\n";
		$low = $guess;
	}
	if ($response =~ /high/ig){
		print "Tried $guess, too high\n";
		$high = $guess;
	}
	if ($response =~ /correct/ig){
		print "\t!! Correct number was $guess, found in " . ++$count . " guesses.\n"; # Found correct
		print "Closing connection!\n"; # state we're going to close
		$socket->close(); # close our connection
		$alive = 0; # this allows graceful end to the program
	}
	$count++;
}

