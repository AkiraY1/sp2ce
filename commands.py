import requests

#Adding a file
files = {'file': ('myfile', open('hello.txt', 'rb')),}
response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=('1vkBruCKyz5F7MSTPanmTKqKXvK', 'd90e8ac5c76ae2572f7bc4062fded1eb'))
print(response.json())

#Reading a file
response = requests.post('https://ipfs.infura.io:5001/api/v0/cat?arg=QmaQiNTTNjKHwTMTPo8T2vxZB7riR4ssBdKRhNrxqvrhf7', auth=('1vkBruCKyz5F7MSTPanmTKqKXvK', 'd90e8ac5c76ae2572f7bc4062fded1eb'))
print(response.content)

#Downloading file
url = "https://ipfs.infura.io:5001/api/v0/get?arg=QmSDVs2Quck1UubvPJKmFUjz2gE1UFF8M91JtUHG1dPLie"
resp = requests.get(url)
open('cool.pdf', 'wb').write(resp.content)