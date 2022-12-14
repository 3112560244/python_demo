import http.client

conn = http.client.HTTPConnection("39.105.0.57:8080")

uid =7777

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n7745\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"prodid\"\r\n\r\n0101\r\n-----011000010111000001101001--\r\n\r\n"

headers = { 'content-type': "multipart/form-data; boundary=---011000010111000001101001" }

conn.request("GET", "/kill/k", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))