@echo off
setlocal EnableDelayedExpansion

SET mypath=%~dp0
SET line=py -3 "C:\flip\remove metadata.py"

for %%x in (%*) do (
    copy %%x C:\flip\
 )

cd C:\flip\

echo %line%

%line%

explorer "C:\flip\out"