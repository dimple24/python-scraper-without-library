
import requests

# Set the URL you want to webscrape from
url = 'https://medium.com/'

# Connect to the URL
response = requests.get(url)

#print(response.status_code)
htmlText = response.text
#print (htmlText)

#split the data
splitList= htmlText.split("href=")
for i in range(1,len(splitList),1):
  splitList1=splitList[i]
  a=""
  #print(len(splitList1))
  for j in range(0,len(splitList1),1):
    if (splitList1[j]==">"):
      break;
    else:
      a=a+splitList1[j]
  f = open("scrapper.txt", "a")
  f.write(a+'\n')
  f.close()
f = open("scrapper.txt", "r")
print(f.read())
