#!/usr/bin/env ruby
# A regular expression that matches the output [SENDER],[RECEIVER],[FLAGS] where:
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
