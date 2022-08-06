import urllib.request, urllib.error, urllib.parse

url = 'https://questionnaire-148920.appspot.com/swe/data.html'

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')

f = open('dataOutput.html', 'w')
f.write(webContent)
f.close