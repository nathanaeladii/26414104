$_ = "yabba dabba doo";
if (/abba/) {
    print "It matched!\n";
}

if (/\p{Space}/) {	# 26 different possible characters
    print "The string has some whitespace.\n";
}
if (/\p{Digit}/) {	# 411 different possible characters
    print "The string has a digit.\n";
}
if (/\p{Hex}\p{Hex}/) {
    print "The string has a pair of hex digits.\n";
}
if (/\P{Space}/) {	# Not space (many many characters!)
    print "The string has one or more non-whitespace" .
          "characters.\n";
}

