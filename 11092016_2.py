#returns array from function
sub numbers{
        if($_[0] == "asc"){ #ascending
                return $fred..$barney;
        }elsif($_[0] == "desc"){ #descending
                return reverse $fred..$barney;
        }
}
$fred = 18; $barney = 25;
@nums = numbers("asc");
print(@nums,"\n");
@nums2 = numbers("desc");
print(@nums2,"\n");

#use array for the param
sub giveMeArray{
        for($i=0;$i<@_;$i++){
                print("I have ",$_[$i],"\n");
        }
}
@arr = (1,3,2);
giveMeArray(@arr);

sub sortNum{
        @new = @_;
        for($i=0;$i<@new;$i++){
                for($j=$i+1;$j<@new;$j++){
                        if($new[$i]>$new[$j]){
                                ($new[$i],$new[$j]) = ($new[$j],$new[$i]);
                        }
                }
        }
        return @new;
}
@ori = (3,1,7,6,4);
@sorted = sortNum(@ori);
print("Ori : ",@ori,"\n");              #3,1,7,6,4
print("Sorted : ",@sorted ,"\n");       #1,3,4,6,7

