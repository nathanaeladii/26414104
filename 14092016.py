echo 'Single quotes "protect" double quotes'
echo "Well, isn't that \"special\"?"
echo "You have `ls | wc -l` files in `pwd`"
x=100
echo "The value of \$x is $x"
cd; ls
(date; who; pwd) > logfile
sort file | pr -3
vi `grep l ifdef *.cpp`
egrep '(yes|no)' `cat list`


#quoting

name=Arnold
name+=" Robbins" ; echo $name

pets=(blacky rusty)
echo ${pets[*]}

pets+=(raincloud sophie)
echo ${pets[*]}


