# Daily-Learnings
This is my daily learnings technically

27-11-2025

Today morning started with the sonic and the complete summary of this operating system is

This is a operating system for networking devices.
The simple way is that I will get a networking device without any operating system in it.
Basically the network devices of different vendors comes with their own operating system.
Example the cisco switch will have the cisco internetworking operating system and juniper devices comes with junos operating system.
But what is the significance of this sonic from those.
The first advantage is that I can get any hardware no matter which vendor is providing it.
After buying it I will install this sonic in it and then i can use it for my networking requirements.
This is as simple as I will buy the dell laptop and I will install windows in it or I will use linux distributions.
Now this installed operating system will do my tasks no matter which hardware it is.

In linux we have kernel where it helps us to do the most of the tasks will be achieved through this kernel.
I will give instructions to my os like ubuntu or kali linux now this os will communicate with the kernel and then kernel will communicate this to hardware then it will get the  response and then it will give it to os and then this os will give the response back to the application from where it received.
This is how the communication will happen across this linux kernel.
In the same way in sonic we will have a switch abstraction layer which will receive all the instructions throught the cli and then this will communicate with the hardware or chip and then the response will be given.

The another major difference between the traditional network operting systems and this operting system is that this is a containerized archietectre.
Basically when I talk about containers i am talking about the microservice architecture.
This sonic follows this architecture where as the other NOS follows monolithic architecture.
The difference is that in the monolithic the processes that are present in the os will communicate each other directly but in the  microservices architecture the communication will happen through this redis database in this sonic os.
The communication happens through the Redis database, which runs inside a Docker container.
The advantage with this architecture is that if a contaner goes down it will not affect other services till it get reloaded or getting up and running.
Each service like bgp, ospf and snmp etc will have it's own container.
The configurations will be slightly different fromt the traditional network operatiing systems.
These configurations need to be there in database.

To do the vlan configuration the commands that we use in sonic are
    sudo config vlan add 10
This adds the vlan 10 to the configDB

    sudo config vlan member add  -u 10 <port/interface>
This command will add the port ethernet1 is an access port 
Here -u indicates untagged.

    sudo config vlan member add 10 <port/interface>
Now this will do the port as a trunked port.
And one more thing is that we are using config in all of our commands where we directly communicating with this configDB whatever we are writing is being reflected in this redis database.
This is how we create and assign vlan in the sonic NOS.

    sudo config vlan member del 10 Ethernet1 
This is to remove the port <port/interface> from the vlan 10


After learning this I have started learning the basic shell scripting.
Basically this shell scripting will automate the the process instead of doing things manually.
If suppose I need to create some 100 files in a folder and this needs to be done in many vms it will take some time if i am simply using touch command for 100 times.
Instead I can have a shell script and then i can use this in all my vms and that's it I have saved so much time and done the tasks in short time.

#!/bin/bash
#this is a comment line now I am creating a variable for the target directory

target_dir="folder1" 
file_start="file" 
#these 2 are variables one is for my target directory and then another one is to start my file with suffix file

#let's create the target directory
mkdir -p $target_dir

#now we have a directory I need 100 files for that I will take a for loop and then I will iterate it till 100.
for I in {1..100}
do
    filename="$file_start$i.txt"
    touch "$target_dir/$filename"
done 
echo "the creation is done"

"#!/bin/bash"  this is called shebang where it tell to use the interpreter bash which is present in the bin folder no matter which os it is.
Not only bash there are sh, ksh, dash etc
"-p" is used while creating a folder which means that if the folder is already there with the specified name then it will continue without any errors.
The for loop will start at 1 and for the range it uses {} braces and inside that we will give the range.
It will initialize with 1 and ends at 100
In first iteration it will have 1 as I and the "do" indicates that the start of the logic 
In first line after do I have a variable basically it is for the file name.
In this variable the file will start with the value stored in the variable file_start that is file in this script and then it uses the value of I stored in it and then it uses .txt as a static string.
The significance of this "$" is it indicates the interpreter that don't use the text that is there instead use the value in it.
Then  after having this filename now I will use touch command to create an empty file inside the target folder that is folder1 and the filename will be file1 for iteration and it will change over the iterations.
After this "done" indicates the end of that iteration and then it will continue with the next iteration.
After for loop  I have used this echo command to say that the process is done and it is similar to the printing we use in other programming languages.

After this to run this bash script we use command 
sh f<ilename> or ./<filename>

The filename needs to have the extension ".sh" for these shell scripts in the same way we use .py for python, .java for java etc.

If we haven't enabled the permissions then the access will be denied for that we need to use the "chmod" command to enable them.
Basically 4 is to read, 2 is to write and 1 is to execute
If we use 444 now we have given permissions to just read the file not for writing and executing for all the 3 groups 
Like we have -,---,---,--- the first bit is for the file or directory if it is "-" it is a file or "d" for directory.
The second three bits for the one who creates that folder or the file, next three for group of users we need to give accress and last one is for all the other users.
We can enable the permissions based on our requirements.

For this shell script simply I can use 
chmod 777 <filename> 
It enables all permissions for all users.

Now if we run the script will be executed and then this script can be used in all the vms.
If we use the sh then the default interpreter that is there to execute the shell scripts will be used else if we use ./ we need to have the permissions enabled.
This is how this bash script will automate so much in less time.

This is all about today...

Thank you
Lavakumar H N
