# Import libraries
import requests
import threading


# Set the URL you want to webscrape from
url = 'https://medium.com/'

# Connect to the URL
response = requests.get(url)

#print(response.status_code)
htmlText = response.text
#print (htmlText)

#split the data
splitList= htmlText.split('href="')
for i in range(1,len(splitList),1):
  a=""
  for k in range(0,len(splitList[i]),1):
      splitList1=splitList[i][k]
      if (splitList1  =='"'):
        break;
      else:
        a=a+splitList1
  
  f = open("scrapper.txt", "a")
  f.write(a+'\n')
  f.close()
f = open("scrapper.txt", "r")
print(f.read())
class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        print_data(self.name, self.counter)
        print ("Exiting " + self.name)

def print_data(threadName, counter):
    datafields = []
    file = open('scrapper.txt', "r") 
    for line in file: 
      print (line)
      today = line
      datafields.append(today)
      print ("%s[%d]: %s" % ( threadName, counter, datafields[0] ))

# Create new threads
thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)
thread3 = myThread("Thread", 3)
thread4 = myThread("Thread", 4)
thread5 = myThread("Thread", 5)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()


print ("Exiting the Program!!!")
