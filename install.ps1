$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$base = 'https://aisc-lab.onrender.com'
$root = Join-Path (Get-Location) 'AI_PRACTICALS_EXAM_PACK'
New-Item -ItemType Directory -Force -Path (Join-Path $root 'Code'), (Join-Path $root 'Theory') | Out-Null
foreach ($number in 2..10) {
    $id = '{0:D2}' -f $number
    Invoke-WebRequest -UseBasicParsing "$base/Code/Experiment_$id.py" -OutFile (Join-Path $root "Code\Experiment_$id.py")
    Invoke-WebRequest -UseBasicParsing "$base/Theory/Experiment_$id.txt" -OutFile (Join-Path $root "Theory\Experiment_$id.txt")
}
Write-Host "Downloaded to $root"