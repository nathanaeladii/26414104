$_ = "aa11bb";
if (/(.)\111/) {
    print "It matched!\n";
}
if (/(.)\g{1}11/) {
    print "It matched!\n";
}
if (/(.)\g{1}11/) { # relative back reference
    print "It matched!\n";
}
$_ = "xaa11bb";
if (/(.)(.)\g{1}11/) {
    print "It matched!\n";
} 

