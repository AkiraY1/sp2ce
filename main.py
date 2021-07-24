import requests

#url = "https://ipfs.infura.io:5001/api/v0/get?arg=QmSDVs2Quck1UubvPJKmFUjz2gE1UFF8M91JtUHG1dPLie"
#resp = requests.get(url)
#open('cool.pdf', 'wb').write(resp.content)

url = "https://ipfs.infura.io:5001/api/v0/add?arg=QmaQiNTTNjKHwTMTPo8T2vxZB7riR4ssBdKRhNrxqvrhf7"
resp = requests.post(url)
print(resp)