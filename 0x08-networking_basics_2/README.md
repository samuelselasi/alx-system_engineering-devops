# 0x08. Networking basics #1
### `DevOps` `Network` `SysAdmin`

![s7kpNYq](https://user-images.githubusercontent.com/85158665/236186259-1fd38b87-fbf8-4aa1-9145-baaffdad81ac.png)

## Resources

**Read or watch**:

* [What is localhost](https://en.wikipedia.org/wiki/Localhost)
* [What is 0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0)
* [What is the hosts file](https://www.makeuseof.com/tag/modify-manage-hosts-file-linux/)
* [Netcat examples](https://www.thegeekstuff.com/2012/04/nc-command-examples/)

**man or help**:

* `ifconfig`
* `telnet`
* `nc`
* `cut`

## General
* What is `localhost/127.0.0.1`: the local computer or device that you are currently using. When you access your own computer through a web browser or other network-based application, you can use either of these terms to refer to the local host.

"127.0.0.1" is a numerical IP address that is assigned to the loopback network interface. This interface allows network software to communicate with itself, which means that you can use "127.0.0.1" to refer to your own computer from within a network-based application.

"localhost" is a hostname that is associated with the loopback network interface. It is typically set to resolve to the IP address "127.0.0.1" by default in most operating systems. So, using "localhost" or "127.0.0.1" is equivalent when referring to the local host.

In summary, "localhost" or "127.0.0.1" refers to the local computer or device that you are currently using, and it allows network software to communicate with itself on that device.
* What is `0.0.0.0`:special IP address that means "all available addresses" or "any address". It is often used in network programming and configuration to indicate a wildcard address that will listen on all available IP addresses.
* What is `/etc/hosts`: a configuration file on Unix and Unix-like operating systems that maps hostnames to IP addresses. It is used to provide a local mapping of hostnames to IP addresses, and can be edited by a system administrator to add or modify mappings or to block access to certain websites.
* How to display your machine’s active network interfaces: 
	* For Linux and macOS:

		* Open a terminal window.
		* Type `ifconfig` and press `Enter`.
		* The output will show a list of active network interfaces, along with their IP addresses, MAC addresses, and other network settings.
	* For Windows:

		* Open a Command Prompt window.
		* Type `ipconfig` and press `Enter`.
		* The output will show a list of active network interfaces, along with their IP addresses, subnet masks, and other network settings.

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass `Shellcheck` (version `0.7.0` via apt-get) without any errors
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks
