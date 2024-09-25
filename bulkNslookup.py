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
    print('- ' + i)    
    result = subprocess.run('nslookup ' + i, shell=True, capture_output=True, text=True)
    cmdResponse = result.stdout
    cmdError = result.stderr
    if int(cmdResponse.find('Name')) == -1:
        print('No FQDN found\r\n')
    else: print(cmdResponse[cmdResponse.find('Name'):])

os.system('pause')