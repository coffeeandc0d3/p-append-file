# p-append-file
Appends text to a specified file at the beginning of the file (not the end). 

Best used with an alias shortcut or even better a keyboard shortcut like F1

![append-post1](https://user-images.githubusercontent.com/31811490/159101146-3ab9b2a3-794e-4900-9a1f-ae411711daa0.png)

* [To Install]

  mkdir build 

  cd build

  git clone https://github.com/coffeeandc0d3/p-append-file

  cd p-append-file

* [To Run] (inside ~/build/p-append-file)

  sudo chmod u+x install.sh

  ./install.sh

* [Start Program]

  cd /home/$USER
  
  ./append.sh
  
      -or- (some keyboard shortcuts prefer): 
      
  bash /home/$USER/append.sh 

*Note* 

Program's main driver code is in ~/build/p-append-file/ directory. 
This directory will need to remain unmoved so the append.sh script invokes correct path of python script. *But* you can easily change this by editing the path it targets for the *p-append-file.py*. This is done inside the *append.sh* script :) 

[Tips]

If you have trouble getting $home pathnames found, you'll need to type: */home/$USER/* <filename>

[Todo]

 * If filepath not found, notify and re-prompt user (currently to know if failed, you won't see the 
 'Done!' text, but it's easy to miss that as well. 
  
 * shell-like path-completion to make easier 
  
