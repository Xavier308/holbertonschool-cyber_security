#!/usr/bin/env ruby

require 'json'

def merge_json_files(file1_path, file2_path)
  # Read and parse the first JSON file
  file1_content = File.read(file1_path)
  data1 = JSON.parse(file1_content)

  # Read and parse the second JSON file
  file2_content = File.read(file2_path)
  data2 = JSON.parse(file2_content)

  # Merge the two JSON objects (append data1 to data2)
  merged_data = data2 + data1

  # Write the merged data back to file2
  File.write(file2_path, JSON.pretty_generate(merged_data))

  puts 'Merged JSON written to file.json'

end
