@echo off
:: directory of the "rcc" command
@REM set COMMAND_ROOT=C:\UserData\Environment\Tools\anaconda_data\envs\ic\Lib\site-packages\PySide6
set COMMAND_ROOT=C:\Users\Dell\.conda\envs\ic\Lib\site-packages\PySide6

:: %1 ui file to use
:: %2 output file to generate
if "%1"=="/?" goto usage 
if "%1"=="" goto input
if not "%1"=="" goto normal

:input
set /p ui_file=Please input the "qrc" file to use: 
goto command

:usage
echo Usage:
echo arg1 - ui file's path
goto quit

:normal
set ui_file=%1

:: %1 is the filename of "qrc" file
:: %2 is the filename to generate
:command
start %COMMAND_ROOT%\designer %ui_file%

:quit
echo Program finished!
