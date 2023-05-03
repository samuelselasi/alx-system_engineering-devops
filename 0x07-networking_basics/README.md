# 0x07. Networking basics #0

### `DevOps` `Network`

## Resources

**Read or watch**:

* [OSI model](https://en.wikipedia.org/wiki/OSI_model)
* [Different types of network](https://www.lifewire.com/lans-wans-and-other-area-networks-817376)
* [LAN network](https://en.wikipedia.org/wiki/Local_area_network)
* [WAN network](https://en.wikipedia.org/wiki/Wide_area_network)
* [Internet](https://en.wikipedia.org/wiki/Internet)
* [MAC address](https://whatismyipaddress.com/mac-address)
* [What is an IP address](https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/)
* [Private and public address](https://www.iplocation.net/public-vs-private-ip-address)
* [IPv4 and IPv6](https://www.webopedia.com/insights/ipv6-ipv4-difference/)
* [Localhost](https://en.wikipedia.org/wiki/Localhost)
* [TCP and UDP](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
* [TCP/UDP ports List](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
* [What is ping /ICMP](https://en.wikipedia.org/wiki/Ping_%28networking_utility%29)
* [Positional parameters](https://wiki.bash-hackers.org/scripting/posparams)

**man or help**:

* `netstat`
* `ping`

## OSI Model
* The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
* It has 7 layers
* It is organized from lowest to highest

## LAN
* A local area network (LAN) is a computer network that interconnects computers within a limited area such as a residence, school, laboratory, university campus or office building
* Used within a limited area such as a residence, school, laboratory, university campus or office building
* Typical geographical size: limited area

## WAN
* A wide area network (WAN) is a telecommunications network that extends over a large geographic area. Wide area networks are often established with leased telecommunication circuits.
* Typical usage: Businesses, as well as schools and government entities, use wide area networks to relay data to staff, students, clients, buyers and suppliers from various locations around the world.
* Typical geographical size: Doesn't matter 

## What is the Internet
* Every machine on the the Internet has a unique number assigned to it, called an IP address
* Two types of IPaddresses: IPv4 and IPv6 Addresses
* In computer networking, localhost is a hostname that refers to the current computer used to access it.
* A subnet is a logical subdivision of an IP network that allows a large network to be divided into smaller, more manageable subnetworks. 
* Why IPv6 was created: IPv6 is the successor to Internet Protocol Version 4 (IPv4). It was designed as an evolutionary upgrade to the Internet Protocol and will, in fact, coexist with the older IPv4 for some time. IPv6 is designed to allow the Internet to grow steadily, both in terms of the number of hosts connected and the total amount of data traffic transmitted.

## TCP/UDP
* Both TCP and UDP are protocols used for sending bits of data—known as packets—over the Internet.
* TCP provides reliability and ensures that all data is received in the correct order, while UDP is faster but does not provide any guarantees about the delivery of data. The choice between TCP and UDP depends on the specific needs of the application and the trade-offs between reliability and speed.
* A port is a communication endpoint that allows a specific type of data to be transmitted and received between a computer or device and the network.
* Memorize SSH, HTTP and HTTPS port numbers:
	* SSH (Secure Shell) typically uses port number 22 for incoming connections. This is the default port number, but it can be changed to a different port number for security reasons.
	* HTTP (Hypertext Transfer Protocol) typically uses port number 80 for incoming connections. This is the default port number for web traffic, but it can also be configured to use a different port number.
What tool/protocol is often used to check if a device is connected to a network
	* HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP and typically uses port number 443 for incoming connections. This port number is also the default for HTTPS traffic, but it can be changed to a different port number if needed.



## Requirements
###General
* Allowed editors: `vi`, `vim`, `emacs`
* All your Bash script files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass `shellcheck` without any error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## More Info
The second line of all your Bash scripts should be a comment explaining what is the script doing

For multiple choice question type tasks, just type the number of the correct answer in your answer file, add a new line for every new answer, example:

What is the most important position in a software company?

1. Project manager
2. Backend developer
3. System administrator
```
sylvain@ubuntu$ cat foo_answer_file
3
sylvain@ubuntu$
```
Source for question 1 [here](https://twitter.com/devopsreact/status/831922429215662080)

## Tasks

