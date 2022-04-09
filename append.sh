#!/bin/sh
cd ~/build/p-append-file/

rm buffer
touch buffer

userPath=`echo /home/$USER/build/p-append-file/buffer`
echo "Append text: (ctrl + d when done)" && cat > $userPath

# Press Ctrl+D to stop recording stuff into file
cat $userPath

python3 p-append-file.py $userPath


