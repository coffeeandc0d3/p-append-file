# p-append-file
Appends text to a specified file at the beginning of the file (not the end). 

Best used with an alias shortcut or even better a keyboard shortcut like F1

![append-post1](https://user-images.githubusercontent.com/31811490/159094836-530c6691-e986-479e-8af9-6ce876a168c8.png)

* [To Install]

mkdir build 

cd build

git clone https://github.com/coffeeandc0d3/p-append-file

cd p-append-file

* [To Run] (inside ~/build/p-append-file)

sudo chmod u+x install.sh

./install.sh

[Start Program]

cd /home/$USER
./append.sh

*Note* Program's main driver code is in ~/build/p-append-file/ directory. 
This directory will need to remain unmoved so the append.sh script invokes correct path of python script. *But* you can easily change this by changing the path it targets the p-append-file.py. This is done inside the *append.sh* script :) 

[Tips

If you have trouble getting pathnames found, you'll likely need to type: *~/* or */home/$USER/* <filename>
