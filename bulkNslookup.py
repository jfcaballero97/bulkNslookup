import os,re, subprocess, time, ipaddress

fqdnList = []

def addFQDN():
    while True:
        fqdn = input("Introduce the FQDN (press enter to scape):").replace(" ", "")
        if fqdn == "":
            break
        fqdn = re.split(r'[,;]', fqdn)
        for i in fqdn:
                fqdnList.append(str(i))

addFQDN()
os.system('cls')
print('Results:\r\n')

for i in fqdnList:
    responseIPs = [] 
    print('\r\n- ' + i)    
    result = subprocess.run('nslookup ' + i, shell=True, capture_output=True, text=True)
    cmdResponse = result.stdout
    cmdError = result.stderr

    if int(cmdResponse.find('Name')) == -1:
        print('No FQDN found\r\n')
    else:
         cmdResponse = cmdResponse[cmdResponse.find('Name'):]
         print(cmdResponse)
         if cmdResponse.find('Address: ')+len('Address: ') != -1:
              aux = cmdResponse[cmdResponse.find('Address: ')+len('Address: '):]
              aux = re.split(r'[^0-9.]+', aux)
         else:
            aux = cmdResponse[cmdResponse.find('Addresses: ')+len('Addresses: '):]
            aux = re.split(r'[^0-9.]+', aux)
         for i in aux:
             try:
                 ipaddress.ip_address(i)
                 responseIPs.append(i)
             except ValueError:
                 error = i + ' is not a valid IP'
		
         isPublic = False
         for ip in responseIPs:
              if ipaddress.IPv4Address(ip).is_private == False:
                   isPublic = True
         if isPublic: print('Public IPs have been found in the FQDN.')
		
         else: print('Everything is private ;)')

os.system('pause')
