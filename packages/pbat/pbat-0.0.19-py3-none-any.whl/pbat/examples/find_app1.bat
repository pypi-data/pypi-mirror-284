@echo off
rem This file is generated from find_app1.pbat, all edits will be lost
if exist "C:\curl\bin\curl.exe" set CURL=C:\curl\bin\curl.exe
if exist "C:\Git\mingw64\bin\curl.exe" set CURL=C:\Git\mingw64\bin\curl.exe
if exist "C:\Program Files\Git\mingw64\bin\curl.exe" set CURL=C:\Program Files\Git\mingw64\bin\curl.exe
if not defined CURL (
echo CURL not found
exit /b
)
echo ok


