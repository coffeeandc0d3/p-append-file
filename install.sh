#!/bin/sh

# copy the append.sh to user $HOME
userPath=`echo /home/$USER`
cp append.sh $userPath

cd $userPath

# Let user run the driver script
sudo chmod u+x append.sh

# Done 
echo "->Done! To run type: ./append.sh in ${userPath}"
printf "\n-> [Note] Recommended to setup as a keyboard shortcut or alias :)	 " 
printf "\n-> ! [Keep p-append-file.py in ${userPath}/build/p-append-file ]"
