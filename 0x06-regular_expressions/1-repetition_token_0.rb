#!/usr/bin/env ruby
#regular expression that will match the following cases:
# hbn
# hbtn
# hbttn
# hbtttn
# hbttttn
# hbtttttn
# hbttttttn
# It accepts one argument and pass it to a regular expression matching method

puts ARGV[0].scan(/hbt{2,5}n/).join
