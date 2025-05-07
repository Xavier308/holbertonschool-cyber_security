#!/usr/bin/env ruby
require 'digest'

if ARGV.length != 2
  puts "Usage: #{__FILE__} HASHED_PASSWORD DICTIONARY_FILE"
  exit 1
end

hashed_password = ARGV[0]
dictionary_file = ARGV[1]

begin
  found = false
  File.foreach(dictionary_file) do |word|
    word.strip!
    hash = Digest::SHA256.hexdigest(word)
    if hash == hashed_password
      puts "Password found: #{word}"
      found = true
      break
    end
  end

  puts "Password not found in dictionary." unless found
rescue Errno::ENOENT
  puts "Error: Dictionary file '#{dictionary_file}' not found."
rescue => e
  puts "An error occurred: #{e.message}"
end
