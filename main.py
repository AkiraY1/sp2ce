import requests

#url = "https://ipfs.infura.io:5001/api/v0/get?arg=QmSDVs2Quck1UubvPJKmFUjz2gE1UFF8M91JtUHG1dPLie"
#resp = requests.get(url)
#open('cool.pdf', 'wb').write(resp.content)

url = "https://ipfs.infura.io:5001/api/v0/add?arg=QmSDVs2Quck1UubvPJKmFUjz2gE1UFF8M91JtUHG1dPLie"
resp = requests.post(url)
print(resp)