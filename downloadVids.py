from sys import argv
import json
import urllib

script, filename = argv

txt = open(filename)

json_string = txt.read()

parsed_json = json.loads(json_string)

i = 0
for record in parsed_json['data']['records']:
  created = record['created']
  url = record['videoUrls'][0]['videoUrl']
  testfile = urllib.URLopener()
  print "downloading file %d %s" % (i , created+".mp4")
  testfile.retrieve(url, created+".mp4")
  i += 1

