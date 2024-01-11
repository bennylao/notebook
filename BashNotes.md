# Bash (Mac) Notes 

```bash
ls
```

list control character
```bash
stty -a
```

set erase character to backspace
```bash
stty erase '^?'
```

## Add Path to Mac
1. Copy the path to clipboard. 

2. Open (or create) $HOME/.bash_profile by the command ```nano ~/.bash_profile```

3. Enter ```export PATH=[PATH_TO_DIRECTORY]:$PATH```

4. Press ```Ctrl + X``` and when it asks you to save the file, choose Yes

5. Run ```source $HOME/.bash_profile``` to refresh the current window or restart the terminal

6. Verify that the ```[PATH_TO_DIRECTORY]``` is now in your PATH by running: ```echo $PATH```

