@echo off
setlocal
set "CN_LAB_INSTALL_DIR=%~dp0CN_LAB"
powershell.exe -NoProfile -Command "$ErrorActionPreference='Stop'; $ProgressPreference='SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12; $base='https://aisc-lab.onrender.com'; $root=$env:CN_LAB_INSTALL_DIR; $files=@('README.txt','Ports_and_Run_Instructions.txt','PDFs/Experiment_02_TCP_IP_Utility_Commands.pdf','PDFs/CN_Practical_Theory_Experiments_02-10.pdf','PDFs/Experiment_03_DNS_with_Cisco_Packet_Tracer.pdf','PDFs/Experiment_04_Hub_and_Switch_Topology.pdf','PDFs/Practical_05_Static_Routing_GNS3.pdf','PDFs/Experiment_07_EIGRP_Dynamic_Routing_GNS3.pdf','PDFs/Experiment_08_TCP_Client_Server_Sockets.pdf','PDFs/Experiment_09_UDP_File_Transfer.pdf','PDFs/Experiment_10_Wireshark_Packet_Analysis.pdf','Code/Experiment_08_TCP_Server.py','Code/Experiment_08_TCP_Client.py','Code/Experiment_09_UDP_Receiver.py','Code/Experiment_09_UDP_Sender.py'); foreach($f in $files){$p=Join-Path $root ($f -replace '/','\'); New-Item -ItemType Directory -Force -Path (Split-Path $p) | Out-Null; Invoke-WebRequest -UseBasicParsing -Uri ($base+'/'+$f) -OutFile $p; Write-Host 'Downloaded' $f}; Write-Host 'Files saved in' $root"
if errorlevel 1 goto failed
echo.
echo CN Lab files downloaded.
echo Press any key to close.
pause >nul
exit /b 0
:failed
echo.
echo Download failed. Check the link and internet connection, then try again.
echo Press any key to close.
pause >nul
exit /b 1
