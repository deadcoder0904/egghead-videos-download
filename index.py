from bs4 import BeautifulSoup
import os
import urllib2
import pprint

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'

pp = pprint.PrettyPrinter(indent=4)

url = raw_input(bcolors.OKGREEN + 'Enter the full course or series you want to download : ' + bcolors.ENDC + '\n').split('?')[0]

print(bcolors.OKBLUE + "Visiting... " + bcolors.ENDC + "\n" + bcolors.OKGREEN + url + bcolors.ENDC)

response = urllib2.urlopen(url)
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')
h4 = soup.find_all("h4")

s = ''
c = 0
for item in h4:
	a = item.find("a")
	if a is not None and a.has_attr('href'):
		c = c + 1
		s += a['href'] + '\n'

print(bcolors.OKBLUE + "Downloading "+ str(c) + " files ... " + bcolors.ENDC + "\n")

temp = open('temp.egghead', 'a')
temp.write(s)

os.system("youtube-dl -a temp.egghead")
os.system("rm -rf *.egghead")

for filename in os.listdir("."):
	if filename.find(".mp4") is not -1:
		os.rename(filename, filename[:filename.find(".mp4")+4])