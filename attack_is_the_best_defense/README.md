# Attack is the best defense
##### `DevOps` `Scripting` `Hacking`
## Resources
**Read or watch**:

* [Network sniffing](https://www.lifewire.com/definition-of-sniffer-817996)
* [ARP spoofing](https://www.veracode.com/security/arp-spoofing)
* [Connect to SendGrid’s SMTP relay using telnet](https://docs.sendgrid.com/ui/account-and-settings/troubleshooting-delays-and-latency)
* [What is Docker and why is it popular?](https://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/)
* [Dictionary attack](https://en.wikipedia.org/wiki/Dictionary_attack)

**man or help**:

* `tcpdump`
* `hydra`
* `telnet`
* `docker`

## Tasks

[0. ARP spoofing and sniffing unencrypted traffic](./0-sniffing)

![01c5a1e3f29d290b188d34be5cf534d3255058a7](https://github.com/samuelselasi/alx-system_engineering-devops/assets/85158665/a245aa64-c03a-48de-9787-17abf62639a3)

Security is a vast topic, and network security is an important part of it. A lot of very sensitive information goes over networks that are used by many people, and some people might have bad intentions. Traffic going through a network can be intercepted by a malicious machine pretending to be another network device. Once the traffic is redirected to the malicious machine, the hacker can keep a copy of it and analyze it for potential interesting information. It is important to note that the traffic must then be forwarded to the actual device it was supposed to go (so that users and the system keep going as if nothing happened).

Any information that is not encrypted and sniffed by an attacker can be seen by the attacker - that could be your email password or credit card information. While today’s network security is much stronger than it used to be, there are still some legacy systems that are using unencrypted communication means. A popular one is `telnet`.

In this project, we will not go over ARP spoofing, but we’ll start by sniffing unencrypted traffic and getting information out of it.

[Sendgrid offers](https://sendgrid.com/) is an emailing service that provides state of the art secure system to send emails, but also supports a legacy unsecured way: `telnet`. You can create an account for free, which is what I did, and send an email using `telnet`:

```
sylvain@ubuntu$ telnet smtp.sendgrid.net 587
Trying 167.89.121.145...
Connected to smtp.sendgrid.net.
Escape character is '^]'.
220 SG ESMTP service ready at ismtpd0013p1las1.sendgrid.net
EHLO ismtpd0013p1las1.sendgrid.net
250-smtp.sendgrid.net
250-8BITMIME
250-PIPELINING
250-SIZE 31457280
250-STARTTLS
250-AUTH PLAIN LOGIN
250 AUTH=PLAIN LOGIN
auth login           
334 VXNlcm5hbWU6
VGhpcyBpcyBteSBsb2dpbg==
334 UGFzc3dvcmQ6
WW91IHJlYWxseSB0aG91Z2h0IEkgd291bGQgbGV0IG15IHBhc3N3b3JkIGhlcmU/ISA6RA==
235 Authentication successful
mail from: sylvain@kalache.fr
250 Sender address accepted
rcpt to: julien@google.com
250 Recipient address accepted
data
354 Continue
To: Julien
From: Sylvain
Subject: Hello from the insecure world

I am sending you this email from a Terminal.
.
250 Ok: queued as Aq1zhMM3QYeEprixUiFYNg
quit
221 See you later
Connection closed by foreign host.
sylvain@ubuntu$
```
I wrote the script `user_authenticating_into_server` that performs the authentication steps that I just showed above. Your mission is to execute `user_authenticating_into_server` locally on your machine and, using `tcpdump`, sniff the network to find my password. Once you find it, paste the password in your answer file. **This script will not work on a Docker container or Mac OS, use your Ubuntu vagrant machine or any other Linux machine**.

You can download the script `user_authenticating_into_server` [here](https://intranet.alxswe.com/rltoken/GE_FoAUArlVccQlt7CuBGA)

**DISCLAIMER**: you will probably see `Authentication failed: Bad username / password` in the `tcpdump` trace. It’s normal, we deleted the user to our Sendgrid account. You can’t verify the password found via Sendgrid, only the correction system can!

# Procedure
1. Create a sendgrid account to send email with Telnet from terminal
2. From sendgrid credentials, create program to convert from normal text to base64 encryption and and back
3. Analyze how a message is sent successfully
4. Now use tcpdump to capture network activity on the port used for sendgrid
5. Send another message using another shell so tcpdump can capture its activities
6. Now send another message with sendgrid on the same port in another shell
7. Stop tcpdump after sending the email
8. Download wireshark to analyze the captured network activity
9. You will see your password when you search through(in base64) since you already know what it looks like
10. To find the password of the script provided run the script with tcp dump capturing network activity in another opened shell
11. Now use wireshark the same way and search the same place you found your password
12. Use the decoder to decode from base64 and you have your password!
***I will write a blog on this if sendgrid unbans my IP***



[1. Dictionary attack](./1-dictionary_attack)

Password-based authentication systems can be easily broken by using a dictionary attack (you’ll have to find your own password dictionary). Let’s try it on an SSH account.

* Install Docker on your machine Ubuntu
* Pull and run the Docker image `sylvainkalache/264-1` with the command `docker run -p 2222:22 -d -ti sylvainkalache/264-1`
* Find a password dictionary (you might need multiple of them)
* Install and use `hydra` to try to brute force the account `sylvain` via `SSH` on the Docker container
* Because the Docker container is running locally, `hydra` should access the `SSH` account via IP `127.0.0.1` and port `2222`
* Hint: the password is `11` characters long

Once you found the password, share it in your answer file.

# Procedure
1. Search for a long list of possible passwords to to add to your dictionary
2. Pray the password is in your dictionary
**It took about 8 minutes for my dictionary to crack the password.**

# Still banned!
