from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
html = urlopen("https://github.com/nasa/astrobee/tree/70e3df03ff3f880d302812111d0107f3c14dccc0/communications/ff_msgs/action").read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
all_a = soup.find_all('a')
all_href = [l['href'] for l in all_a]
for i in range(len(all_href)):
  if ".action" in all_href[i]:
    url=re.findall(r"/\w*.action", all_href[i])
    ht=urlopen("https://github.com"+all_href[i]).read().decode('utf-8')
    require=re.findall(r">\w*\s*\w*\s*=\s*-*\w*",ht)
    if(len(require)>0):
      print("\n##",url[1])
      print("\n|Type|Variable|Value|\n|-|-|-|")
    for j in range(len(require)):
      #print(require[j])
      require[j]=require[j].replace(">","")
      require[j]=require[j].replace("=","")
      require[j]=re.sub(r"\s+","|",require[j])
      print("|",require[j],"|")
