#### Hope you like these scripts!

**These are two scripts i made to make it easier for me to create ini files and folders for [unFold repo](https://github.com/Ruben35/More-Icons-unFold-Rainmeter) (+ copy them into the rainmeter skin directory to test them before making a commit/push to Ruben's repo), if you want try them out go right ahead**

For this to work you will require a command line interface that bash is compatable with.
[Linux](https://ubuntu.com/wsl) and [Git-bash](https://git-scm.com/downloads) the ones i use, PowerShell and CMD will work too as well.

Copy both these files into the directory outside More-Icons-unFold-Rainmeter folder.
Run the script in your prefered command line interface with `./run-script.sh`

It will first ask for the button name / the folder name.

**After that the python script starts**
1. Application name 
    + For this use the name you used to create the png files. I wanted to make these scripts to run with as less inputs as possible.
2. Version number. 
    + This is the number for the release of unFold skin you are trying to make the button for.
3. Custom Description or Default Description
    + If you type down DDesc the description will be: The [side] button for [application name]. 
    + If you type down CDesc the description will be: Default description + whichever special message you type down.
4. Path
    + Copy paste the path to the executable or shortcut file of the application you are trying to make this button for.
5. Path #2
    + This is if you want a secondary path (to an executable or shortcut file) to be there for when someone clicks on the button with right mouse button.

And that is all. 