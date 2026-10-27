@echo off
setlocal
cd /d "%~dp0"
powershell.exe -NoProfile -Command "$ErrorActionPreference='Stop'; [Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12; try { $base='https://aisc-lab.onrender.com'; $root=Join-Path (Get-Location).Path 'AI_PRACTICALS_EXAM_PACK'; New-Item -ItemType Directory -Force -Path (Join-Path $root 'Code'),(Join-Path $root 'Theory') | Out-Null; foreach($n in 2..10){$id='{0:D2}' -f $n; Invoke-WebRequest -UseBasicParsing ($base+'/Code/Experiment_'+$id+'.py') -OutFile (Join-Path $root ('Code\Experiment_'+$id+'.py')); Invoke-WebRequest -UseBasicParsing ($base+'/Theory/Experiment_'+$id+'.txt') -OutFile (Join-Path $root ('Theory\Experiment_'+$id+'.txt'))} } catch { Write-Error $_; exit 1 }"
if errorlevel 1 goto :failed
echo.
echo Downloaded to "%CD%\AI_PRACTICALS_EXAM_PACK"
pause
exit /b 0
:failed
echo.
echo Download failed. Check your internet connection and try again.
pause
exit /b 1