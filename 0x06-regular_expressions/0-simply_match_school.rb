#!/usr/bin/env ruby
# A regular expression must match School
# It accepts one argument and pass it to a regular expression matching method

puts ARGV[0].scan(/School/).join
