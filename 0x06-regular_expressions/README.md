# 0x06. Regular expression

### `Regex` `DevOps`

#### Background Context
For this project, you have to build your regular expression using `Oniguruma`, a regular expression library that which is used by `Ruby` by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (`regex`), here is the `Ruby` code that you should use, just replace the `regexp` part, meaning the code in between the `//`:
```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

## Resources
**Read or watch**:

* [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
* [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
* [Rubular is your best friend](https://rubular.com/)
* [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
* [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)

## Requirements

### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env ruby`
* All your regex must be built for the `Oniguruma` library

## Tasks

[0. Simply matching School](./0-simply_match_school.rb)

![Screenshot from 2023-05-03 10-13-57](https://user-images.githubusercontent.com/85158665/235890405-1930b7ee-7164-41c9-ae4b-df766598762b.png)

**Requirements**:

* The regular expression must match `School`
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
**Example**:

```
sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```

[1. Repetition Token #0](./1-repetition_token_0.rb)

<img width="959" alt="e7db3c377d46453588fc84f3a975661d142fee91" src="https://user-images.githubusercontent.com/85158665/235893933-b69c3155-1f34-4c6a-90cc-d7f76b111dde.png">

**Requirements**:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

[2. Repetition Token #1](./2-repetition_token_1.rb)

<img width="967" alt="2" src="https://user-images.githubusercontent.com/85158665/235916780-c211c398-8974-4033-bc71-1a7428735c0a.png">

**Requirements**:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

[3. Repetition Token #2](./3-repetition_token_2.rb)

<img width="974" alt="3" src="https://user-images.githubusercontent.com/85158665/235916862-88c7605b-10dc-4022-93f7-bb80c8a49da0.png">

**Requirements**:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

[4. Repetition Token #3](./4-repetition_token_3.rb)

<img width="956" alt="4" src="https://user-images.githubusercontent.com/85158665/235916989-460e6243-89c1-49a2-94d8-a684f574f8d0.png">

**Requirements**:

* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
* Your regex should not contain square brackets

[5. Not quite HBTN yet](./5-beginning_and_end.rb)

**Requirements**:

* The regular expression must be exactly matching a string that starts with `h` ends with `n` and can have any single character in between
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Example**:

```
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$
```

[6. Call me maybe](./6-phone_number.rb)

This task is brought to you by a professional advisor [Neha Jain](https://twitter.com/_nehajain), Senior Software Engineer at LinkedIn.

**Requirement**:

* The regular expression must match a `10` digit phone number

**Example**:

```
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$
```

[7. OMG WHY ARE YOU SHOUTING?](./7-OMG_WHY_ARE_YOU_SHOUTING.rb)

![shouting](https://user-images.githubusercontent.com/85158665/235917118-1f3d1652-1f43-4d38-ad9d-8749e7522055.jpg)

**Requirement**:

* The regular expression must be only matching: capital letters

Example:

```
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$
```
