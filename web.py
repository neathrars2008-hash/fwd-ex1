from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>TCP/IP Protocol Suite</title>
</head>
<body>
  <h1>TCP/IP Protocol Suite</h1>

  <h2>Application Layer</h2>
  <ul>
    <li>HTTP</li>
    <li>HTTPS</li>
    <li>FTP</li>
    <li>SFTP</li>
    <li>SMTP</li>
    <li>POP3</li>
    <li>IMAP</li>
    <li>DNS</li>
    <li>DHCP</li>
    <li>SSH</li>
    <li>Telnet</li>
    <li>SNMP</li>
    <li>NTP</li>
    <li>TFTP</li>
  </ul>

  <h2>Transport Layer</h2>
  <ul>
    <li>TCP</li>
    <li>UDP</li>
    <li>SCTP</li>
  </ul>

  <h2>Internet Layer</h2>
  <ul>
    <li>IPv4</li>
    <li>IPv6</li>
    <li>ICMP</li>
    <li>IGMP</li>
    <li>IPsec</li>
    <li>OSPF</li>
    <li>BGP</li>
    <li>RIP</li>
  </ul>

  <h2>Network Access Layer</h2>
  <ul>
    <li>Ethernet</li>
    <li>Wi-Fi (IEEE 802.11)</li>
    <li>ARP</li>
    <li>RARP</li>
    <li>PPP</li>
    <li>Frame Relay</li>
    <li>ATM</li>
  </ul>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()