import nmap
ns = nmap.PortScanner()
print('Version : {}'.format(ns.nmap_version()))
#ipAdd = input('Enter public address to scan ')
#portsFrom = input('Starting port number ')
#portsTo = input('Ending port number ')
#ns.scan(ipAdd,portsFrom+'-'+portsTo,'-v')
ns.scan('192.168.1.1/24','1-1024','-v --version-all')
#print(ns.scaninfo())
#print(ns.csv())
print(ns.scanstats())
#print(ns.all_hosts())
#print(ns['192.168.1.1'].state())
#print(ns['192.168.1.1'].all_protocols())
#print(nsprint(ns['192.168.1.1']['tcp'].keys())
print(ns['192.168.1.1'].has_tcp(80))
