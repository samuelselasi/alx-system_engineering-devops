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

![4b995d4f8078b44afa968d68a98035d2bd7e8fac](https://user-images.githubusercontent.com/85158665/236141300-5bf06053-b8ce-4f36-84f6-86012007682e.jpg)

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

[2. MAC and IP address](./2-MAC_and_IP_address)

![1e348ba3bcbb094b02922f821ffeb3d8c5438b7b](https://user-images.githubusercontent.com/85158665/236142926-8939c0e0-ff88-4136-b279-1b49c572af2d.jpg)

**Questions**:

What is a MAC address?

1. The name of a network interface
2. `The unique identifier of a network interface`
3. A network interface

What is an IP address?

1. `Is to devices connected to a network what postal address is to houses`
2. The unique identifier of a network interface
3. Is a number that network devices use to connect to networks

[3. UDP and TCP](./3-UDP_and_TCP)

![3d92e3c4a470f8ecf4c73db511fcbbadaa002e1c](https://user-images.githubusercontent.com/85158665/236146018-43dd7fe4-22ba-437c-ab36-46d30ab3fcc4.jpg)

*Let’s fill the empty parts in the drawing above*.

**Questions**:

* Which statement is correct for the TCP box:

1. `It is a protocol that is transferring data in a slow way but surely`
2. It is a protocol that is transferring data in a fast way and might loss data along in the process

* Which statement is correct for the UDP box:

1. It is a protocol that is transferring data in a slow way but surely
2. `It is a protocol that is transferring data in a fast way and might loss data along in the process`

* Which statement is correct for the TCP worker:

1. `Have you received boxes x, y, z?`
2. May I increase the rate at which I am sending you boxes?

[4. TCP and UDP ports](./4-TCP_and_UDP_ports)

Once packets have been sent to the right network device using `IP` using either `UDP` or `TCP` as a mode of transportation, it needs to actually enter the network device.

If we continue the comparison of a network device to your house, where `IP` address is like your postal address, `UDP` and `TCP` ports are like the windows and doors of your place. A `TCP/UDP` network device has `65535` ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (*but nothing is officially declared*) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:
* **22** for `SSH`
* **80** for `HTTP`
* **443** for `HTTPS`

Note that a specific [IP + port = socket](https://stackoverflow.com/questions/152457/what-is-the-difference-between-a-port-and-a-socket).

Write a Bash script that displays listening ports:

* That only shows listening sockets
* That shows the `PID` and name of the program to which each socket belongs

**Example**:

```
sylvain@ubuntu$ sudo ./4-TCP_and_UDP_ports
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 *:sunrpc                *:*                     LISTEN      518/rpcbind
tcp        0      0 *:ssh                   *:*                     LISTEN      1240/sshd
tcp        0      0 *:32938                 *:*                     LISTEN      547/rpc.statd
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN      518/rpcbind
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      1240/sshd
tcp6       0      0 [::]:33737              [::]:*                  LISTEN      547/rpc.statd
udp        0      0 *:sunrpc                *:*                                 518/rpcbind
udp        0      0 *:691                   *:*                                 518/rpcbind
udp        0      0 localhost:723           *:*                                 547/rpc.statd
udp        0      0 *:60129                 *:*                                 547/rpc.statd
udp        0      0 *:3845                  *:*                                 562/dhclient
udp        0      0 *:bootpc                *:*                                 562/dhclient
udp6       0      0 [::]:47444              [::]:*                              547/rpc.statd
udp6       0      0 [::]:sunrpc             [::]:*                              518/rpcbind
udp6       0      0 [::]:50038              [::]:*                              562/dhclient
udp6       0      0 [::]:691                [::]:*                              518/rpcbind
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     STREAM     LISTENING     7724     518/rpcbind         /run/rpcbind.sock
unix  2      [ ACC ]     STREAM     LISTENING     6525     1/init              @/com/ubuntu/upstart
unix  2      [ ACC ]     STREAM     LISTENING     8559     835/dbus-daemon     /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     9190     1087/acpid          /var/run/acpid.socket
unix  2      [ ACC ]     SEQPACKET  LISTENING     7156     378/systemd-udevd   /run/udev/control
sylvain@ubuntu$
```

[5. Is the host on the network](./5-is_the_host_on_the_network)

![giphy](https://user-images.githubusercontent.com/85158665/236152664-d5a0e1aa-d9fe-4cd0-8771-088ab87e11d8.gif)

The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command `ping` uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.

Write a Bash script that pings an IP address passed as an argument.

**Requirements**:

* Accepts a string as an argument
* Displays Usage: `5-is_the_host_on_the_network {IP_ADDRESS}` if no argument passed
* Ping the IP 5 times

**Example**:

```
sylvain@ubuntu$ ./5-is_the_host_on_the_network 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=12.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=7.83 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=11.3 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=63 time=7.57 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 7.570/10.682/13.679/2.546 ms
sylvain@ubuntu$
sylvain@ubuntu$ ./5-is_the_host_on_the_network
Usage: 5-is_the_host_on_the_network {IP_ADDRESS}
sylvain@ubuntu$
```

It is interesting to look at the time value, which is the time that it took for the ICMP request to go to the `8.8.8.8` IP and come back to my host. The IP `8.8.8.8` is owned by Google, and the quickest roundtrip between my computer and Google was `7.57` ms which is pretty fast, which is a sign that the network path between my computer and Google’s datacenter is in good shape. A slow ping would indicate a slow network.

Next time you feel that your connection is slow, try the `ping` command to see what is going on!
