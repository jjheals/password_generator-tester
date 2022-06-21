# password_generator-tester

This script will prompt the user to set up and gather information on what task to perform and the needed parameters. It can perform a few tasks:

1. Generate a new random password based on given parameters
2. Generate a new text file with X amount of new passwords based on given parameters
3. Test the strength of a given password 
    - Will compare against the rockyou.txt password list, if asked

I decided to create this script to get some extra practice in python. It helped me develop better iteration and overall programming skills, including how to limit runtime. I did research on how to handle exceptions, which is something I've done in other languages but not much in python up until now. Because of the user input of this script, I got more experience in thinking through the possible cases and handling bad input. There are definitely some places where the script could break if the user puts in bad enough input, so it's not by any means perfect, but I decided to leave these holes for now as I work towards completing more complex projects so I can see my progress and learning journey better. I also was able to use some modules I don't typically work with (random, string). Overall it was a very beneficial project and one of my more involved ones so far. 

--> Note: Github does not allow me to upload files larger than 25MB. The rockyou.txt even when compressed is over double this threshold, so if you want to try that part of the script yourself you will need to download the rockyou.txt file from another source. I downloaded it from https://github.com/brannondorsey/naivehashcat/releases/download/data/rockyou.txt but there are plenty of other places to get it. 
