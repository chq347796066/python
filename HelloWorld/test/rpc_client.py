import xmlrpc.client
client_server = xmlrpc.client.Server("http://localhost:7080/")
result = client_server.add(3, 5)
print(result)
