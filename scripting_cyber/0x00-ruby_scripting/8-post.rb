#!/usr/bin/env ruby
require 'net/http'
require 'json'
require 'uri'

def post_request(url, body_params)
  uri = URI.parse(url)
  request = Net::HTTP::Post.new(uri.path, 'Content-Type' => 'application/json')
  request.body = body_params.to_json

  response = Net::HTTP.start(uri.host, uri.port, use_ssl: uri.scheme == 'https') do |http|
    http.request(request)
  end

  puts "Response status: #{response.code} #{response.message}"
  begin
    json_body = JSON.parse(response.body)
    if json_body.empty?
      puts "Response body:\n{}"
    else
      puts "Response body:"
      puts JSON.pretty_generate(json_body)
    end
  rescue JSON::ParserError
    puts "Response body:\n#{response.body}"
  end
end
