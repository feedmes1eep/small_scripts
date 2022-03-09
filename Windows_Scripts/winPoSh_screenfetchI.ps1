#Requires -RunAsAdministrator
if (!(Get-Command git -ea SilentlyContinue)) {Write-Host "Install Git and rerun script"; Start-Process "shell:Appsfolder\Microsoft.MicrosoftEdge_8wekyb3d8bbwe!MicrosoftEdge" "https://git-scm.com/downloads"; exit}
$cd = Get-Location
$exp = Get-ExecutionPolicy
if ((Out-String -InputObject $exp) -ne "Unrestricted") {Set-ExecutionPolicy Unrestricted}
$psm1p = ($env:PSModulePath -split ";").Get(0)
if (!(Test-Path $psm1p)) {New-Item $psm1p -ItemType Directory}
Set-Location $psm1p
$UsePath = (Split-Path $PROFILE | Join-Path -ChildPath Modules); if(!(Test-Path $UsePath)) {New-Item $UsePath -Type Directory -Force | Out-Null}; Set-Location $UsePath
git clone https://github.com/AkariiinMKII/Windows-screenFetch
if (!(Test-Path $PROFILE)) {New-Item $PROFILE -Type File -Force | Out-Null}
Add-Content -Path $PROFILE -Value "Import-Module Windows-screenFetch";
screenfetch
Remove-Variable cd, exp, UserPath, psm1p
Set-Location $cd