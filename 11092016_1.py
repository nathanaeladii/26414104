###file
open(r,">>","myfile.txt") || die("cannot read");
print(r "\nnew lines, nice");
close(r);

open(r,"<","myfile.txt") || die("cannot read");
print("blah ",<r>);
close(r);
