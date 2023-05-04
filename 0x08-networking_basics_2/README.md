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

[0. Change your home IP](./0-change_your_home_IP)

Write a Bash script that configures an Ubuntu server with the below requirements.

**Requirements**:

* `localhost` resolves to `127.0.0.2`
* `facebook.com` resolves to `8.8.8.8`.
* The checker is running on Docker, so make sure to read [this](http://blog.jonathanargentiero.com/docker-sed-cannot-rename-etcsedl8ysxl-device-or-resource-busy/)

**Example**:

```
sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.012 ms
^C
--- localhost ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.012/0.012/0.012/0.000 ms
sylvain@ubuntu$
sylvain@ubuntu$ ping facebook.com
PING facebook.com (157.240.11.35) 56(84) bytes of data.
64 bytes from edge-star-mini-shv-02-lax3.facebook.com (157.240.11.35): icmp_seq=1 ttl=63 time=15.4 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 15.432/15.432/15.432/0.000 ms
sylvain@ubuntu$
sylvain@ubuntu$ sudo ./0-change_your_home_IP
sylvain@ubuntu$
sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.2) 56(84) bytes of data.
64 bytes from localhost (127.0.0.2): icmp_seq=1 ttl=64 time=0.012 ms
64 bytes from localhost (127.0.0.2): icmp_seq=2 ttl=64 time=0.036 ms
^C
--- localhost ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.012/0.024/0.036/0.012 ms
sylvain@ubuntu$
sylvain@ubuntu$ ping facebook.com
PING facebook.com (8.8.8.8) 56(84) bytes of data.
64 bytes from facebook.com (8.8.8.8): icmp_seq=1 ttl=63 time=8.06 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 8.065/8.065/8.065/0.000 ms
```
**In this example we can see that**:

* before running the script, `localhost` resolves to `127.0.0.1` and `facebook.com` resolves to `157.240.11.35`
* after running the script, `localhost` resolves to `127.0.0.2` and `facebook.com` resolves to `8.8.8.8`

If you’re running this script on a machine that you’ll continue to use, be sure to revert `localhost` to `127.0.0.1`. Otherwise, a lot of things will stop working!

[1. Show attached IPs](./1-show_attached_IPs)

Write a Bash script that displays all active `IPv4` IPs on the machine it’s executed on.

**Example**:

```
sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
sylvain@ubuntu$
```

Obviously, the `IPs` displayed may be different depending on which machine you are running the script on.

Note that we can see our `localhost` IP :)

[2. Port listening on localhost](./100-port_listening_on_localhost)

Write a Bash script that listens on port `98` on `localhost`.

**Terminal 0**

Starting my script.
```
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
```

**Terminal 1**

Connecting to `localhost` on port `98` using `telnet` and typing some text.
```
sylvain@ubuntu$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test
```

**Terminal 0**

Receiving the text on the other side.
```
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
Hello world
test
```

For the sake of the exercise, this connection is made entirely within `localhost`. This isn’t really exciting as is, but we can use this script across networks as well. Try running it between your local PC and your remote server for fun!

As you can see, this can come in very handy in a multitude of situations. Maybe you’re debugging socket connection issues, or you’re trying to connect to a software and you are unsure if the issue is the software or the network, or you’re working on firewall rules… Another tool to add to your debugging toolbox!
