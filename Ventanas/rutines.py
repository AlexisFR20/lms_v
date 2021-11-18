import subprocess



def checkFolders():
    # Verifica y comprueba que existan los folders que se utilizarana en la instalacion
    # cTemp  -> Carpeta temp en disco local c
    # cTApps -> Carpeta Apps en disco local c
    cTemp = " $DIRE = 'C:\\temp'; if ( Test-Path $DIRE ) { echo 'Directory Exists' } else { md C:\\temp }"
    cApps = " $DIRE = 'C:\\Apps'; if ( Test-Path $DIRE ) { echo 'Directory Exists' } else { md C:\\Apps }" 
    subprocess.call('powershell.exe '+ cTemp, shell=True)
    subprocess.call('powershell.exe '+ cApps, shell=True)

def editHost():
    f = open('C:\\Windows\\System32\\drivers\\etc\\hosts', mode = "a")
    f.write("\n\t172.16.11.3\tJUMXLMSL01 #Primario\n\t172.16.11.4\tJUMXLMSL02 #Secundario\n\t172.16.11.8\tJUMXLMSL03 #Flotante")
    f.close
    
def downloadFiles():
    # Descarga cada uno de los componentes a utilizar
    # dGunzip   -> gunzip.exe
    # dWCliente -> WebClient32.zip
    # dPCapc    -> LMS 12.2.prowcapc
    
    dGunzip = "$client = new-object System.Net.WebClient; $client.DownloadFile('http://172.16.11.8/lms/gunzip.exe', 'C:\\temp\\gunzip.exe')"
    
    dWClient= "$client = new-object System.Net.WebClient; $client.DownloadFile('http://172.16.11.8/lms/WebClient32.zip', 'C:\\Apps\\WebClient32.zip')"
    
    #                                                                                                 /versiones/12.2.022/
    dPCapc = "$client = new-object System.Net.WebClient; $client.DownloadFile('http://172.16.11.8/lms/versiones/12.2.022/LMS%2012.2.prowcapc', 'C:\\Apps\\LMS 12.2.prowcapc')"
    lista = list()
    lista.append(dGunzip)
    lista.append(dWClient)
    lista.append(dPCapc)
    for element in lista:
        print(element)
        subprocess.call('powershell.exe '+ element, shell=True)
    
    # Descomprimir WebClient32.zip y eliminar archivo zip restante.
    # Descomprimiendo archivo.
    unzip = "Expand-Archive -Path C:\\Apps\\WebClient32.zip -DestinationPath C:\\Apps\\WebClient32"
    subprocess.call('powershell.exe '+ unzip, shell=True)
    # Borrando archivo zip restante.
    delzip = "Remove-Item C:\\Apps\\WebClient32.zip"
    subprocess.call('powershell.exe '+ delzip, shell=True)



# checkFolders()


# descarga = "$client = new-object System.Net.WebClient; $client.DownloadFile('http://172.16.11.8/lms/gunzip.exe', 'C:\\temp\\gunzip.exe')"



# winscp = "softwarecenter:SoftwareID=ScopeId_C37154BF-A1F4-4B62-B5FF-0CC6F41A762B/Application_a7748e45-eae3-42ae-bc24-999e58c00df7"

# subprocess.call('C:\WINDOWS\CCM\ClientUX\SCClient.exe '+winscp, shell=True)