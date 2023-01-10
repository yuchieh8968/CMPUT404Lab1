import requests, os

# Q2 Returns version of the requests library installed
print(requests.__version__)

#Curl point 5. Get the google home page
print(requests.get('http://www.google.com'))

#curl point 10. Python script that downloads itself
os.system('curl -i https://raw.githubusercontent.com/yuchieh8968/CMPUT404Lab1/main/main.py')
