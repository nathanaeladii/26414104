line = <STDIN>;
if ($line eq "\n") {
    print "That was just a blank line!\n";
} else {
    print "That line of input was: $line";
}

chomp($line);	# Gets rid of the newline character


chomp($line = <STDIN>);	# Read text without newline
or:
line = <STDIN>;
chomp($line);

