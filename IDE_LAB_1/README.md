IDE LABORATORY WORK #1
======================

Command Line Interface; CLI Editors; Setting Server Environment; Version Control Systems
----------------------------------------------------------------------------------------

<br>
##Completed Tasks
######All tasks are done on a Ubuntu Operating System with GIT and VIM installed

   - **Create your own server (ex. virtual machine) (2 pt)**
    
I've installed Virtual Machine with a UBUNTU guest operating system. <br>For installing the server I've used `sudo apt-get install ssh`, therefore I was able to manage the SSH-Server through<br> `sudo service ssh (start | stop | restart)`

   - **Connect to a remote server via SSH**

I've connected to the remote server via Git Bash by using :`ssh username@address` and introducing the password.

   - **Initialize a repository on server**

To initialize a repository on server go to your desired location, and use `git init` command.

   - **Create a file in repository folder, write in your name, save it and commit it**

```
touch <file_name>       # to create a file
vim <file_name>         # open with your CLI editor
                        # in VIM use 'i' to enter insert mode and insert your name
                        # use :wq to write the file and exit
```
Now before commiting we need to check the untracked files using `git status`. If there are present such files, we need to add them to the staging area, this is done by `git add <file_name>` or `git add .` to add all untracked files.
After these steps we are done, and we can commit our data `git commit -m "message"`

   - **Connect to server using public key (1 pt)**

To create s public key, we'll need a key-generator. I've used the same Git Bash with `ssh-keygen` command. Therefore on my local computer were created a public and a private key. So in order to connect with pub key I'll had to send it to the server `scp .ssh/id_rsa.pub student@192.168.158.128: `, and notice that (:) are important.<br>
Now I moved the content of id_rsa.pub  in .ssh/authorized_keys: `cat id_rsa.pub >> .ssh/authorized_keys `.<br>
If some problems appear, we'll need to create the folder manually with some paramers
```
mkdir ~/.ssh
chmod 700 .ssh
```
Now we can connect to the server without password `ssh username@address`

   - **Create 2 more branches with at least one unique committed file per branch (1 pt)**

To create a branch use `git branch <branch_name>`.<br>When we'll create a new branch, the created branch will have all files from the parent branch.<br>To switch onto another branch use `git checkout <branch_name>`.<br>To see the current(active) branch and list of all branches use `git branch`<br><br>Suppose we have a repository already initialized, a master branch with a `test.txt`.
```
git branch copy         # created a copy branch that inherits all master files
                        # now copy has `test.txt` as well
git checkout copy       # switch onto the copy branch
touch copyFile.txt      # creating a file on copy branch
git add .               # adding to the staging area
git commit -m "new file on copy branch"   #commit
```
In the same manner can be created other branches.



