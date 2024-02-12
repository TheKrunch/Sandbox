@echo off
Setlocal enabledelayedexpansion

Rem This sets the pattern that will be replaced.
Set "Pattern=ENCODED"
Set "Replace="

Rem This loops through the current directory
For %%a in (*.mkv) Do (
	Set "File=%%~a"
	Ren "%%a" "!FILE:%Pattern%=%Replace%!"
)
Pause&Exit