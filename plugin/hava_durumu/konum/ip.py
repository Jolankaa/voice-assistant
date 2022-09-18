import http.client
import socket
conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 2dMupB4Lh50j0KxMhXToLm:1a1DbEQR6kh5FRFB5uvyOT"
    }
ip = socket.gethostbyname(socket.gethostname())
conn.request("GET", f"/ip/ipToLocation?data.ip={ip}", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))