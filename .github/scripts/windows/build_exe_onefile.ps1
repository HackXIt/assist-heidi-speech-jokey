# PowerShell script to build Kivy application with Poetry and PyInstaller

Write-Output "listing contents of cwd"
Get-ChildItem -Force | Out-String

Write-Output 'INFO: Beginning execution'

# Download and install Python
Write-Output 'INFO: Downloading Python 3.11.6'
Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe' -OutFile 'python3.11.6.exe'
Write-Output 'INFO: Installing Python'
Start-Process -FilePath '.\python3.11.6.exe' -ArgumentList '/quiet InstallAllUsers=1 IncludePip=1 PrependPath=1 TargetDir=C:\Python311' -Wait -NoNewWindow | Out-String

# Refresh environment variables to recognize newly installed Python
$env:Path = [System.Environment]::GetEnvironmentVariable('Path','Machine')

# Install Poetry
Write-Output 'INFO: Installing Poetry'
pip install poetry

# Set KIVY_GL_BACKEND to angle_sdl2 for compatibility
$env:KIVY_GL_BACKEND = 'angle_sdl2'

# Install dependencies with Poetry
Write-Output 'INFO: Installing dependencies with Poetry'
poetry config virtualenvs.create false
poetry install --only main --no-root

# Create SpeechJokey.spec file
$Target = 'SpeechJokey'
$TargetSpecFile = "$Target.spec"
@"
# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path

block_cipher = None
app_name = 'SpeechJokey'
#win_icon = '.\icon.ico'

a = Analysis(
    ['src\\main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[kivymd_hooks_path],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    Tree('src\\'),
    a.scripts,
    a.binaries,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    name=app_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
"@ | Set-Content $TargetSpecFile

# Remove null bytes from spec file (PyInstaller compatibility issue)
(Get-Content .\$TargetSpecFile) -replace "`0", "" | Set-Content .\$TargetSpecFile

# Build the executable using PyInstaller
Write-Output 'INFO: Building executable with PyInstaller'
poetry run pyinstaller $TargetSpecFile

# Check for build success and output location
if (Test-Path "dist\$Target.exe") {
    Write-Output "INFO: Build successful. Executable located in dist\$Target.exe"
} else {
    Write-Output 'ERROR: Build failed.'
    exit 1
}
