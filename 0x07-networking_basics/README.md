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

[0. OSI model](./0-OSI_model)

OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:

* **The lowest level**: layer `1` which is for transmission on physical layers with electrical impulse, light or radio signal
* **The highest level**: layer `7` which is for application specific communication like SNMP for emails, HTTP for your web browser, etc

Keep in mind that the OSI model is a **concept**, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.

![4e6a0ad87a65d7054248 (1)](https://user-images.githubusercontent.com/85158665/236139808-c2327303-8d89-4187-824f-e61903d75c5b.png)

**In this project we will mainly focus on**:

* The `Transport` layer and especially `TCP/UDP`
* On the `Network` layer with `IP` and `ICMP`

The image bellow describes more concretely how you can relate to every level.

![0fc96bd99faa7941b18bcae4c5f90c6acd11791d](https://user-images.githubusercontent.com/85158665/236139935-7d4bd967-ae9b-42b8-8ba3-7ee413be9aa1.jpg)

**Questions**:

What is the OSI model?

1. Set of specifications that network hardware manufacturers must respect
2. `The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology`
3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

How is the OSI model organized?

1. Alphabetically
2. `From the lowest to the highest level`
3. Randomly

[1. Types of network](./1-types_of_network)


LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

**Questions**:

What type of network a computer in local is connected to?

1. Internet
2. WAN
3. `LAN`

What type of network could connect an office in one building to another office in a building a few streets away?

1. Internet
2. `WAN`
3. LAN

What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

1. `Internet`
2. WAN
3. LAN

