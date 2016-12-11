# downloads-my-vines

1) Open the page which contains all of your videos
2) Using the Chrome developer tool, look for the XHR request which downloads the json for the current page info and copy the request as a curl
3) Run curl and save the json into a file (e.g. response1.json)
4) Run this script to download all files in that json: python downloadVids.py response1.json


