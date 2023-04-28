# 0x05. Processes and signals

### `DevOps` `Shell` `Bash` `Syscall` `Scripting`

## About Bash projects
Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.

## Resources
**Read or watch**:

* [Linux PID](http://www.linfo.org/pid.html)
* [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
* [Linux signal](https://www.educative.io/answers/what-are-linux-signals)
* [Process management in linux](https://www.digitalocean.com/community/tutorials/process-management-in-linux)

**man or help**:

* `ps`
* `pgrep`
* `pkill`
* `kill`
* `exit`
* `trap`

## Requirements

### General

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass `Shellcheck` (version `0.7.0` via `apt-get`) without any error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## More Info
For those who want to know more and learn about all signals, check out [this article](https://www.computerhope.com/unix/signals.htm).

## Tasks

[0. What is my PID](./0-what-is-my-pid)

Write a Bash script that displays its own `PID`.
```
sylvain@ubuntu$ ./0-what-is-my-pid
4120
sylvain@ubuntu$
```
