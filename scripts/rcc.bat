@echo off
:: directory of the "rcc" command
set COMMAND_ROOT=C:\UserData\Environment\Tools\anaconda_data\envs\ic\Lib\site-packages\PySide6

:: %1 ui file to use
:: %2 output file to generate
if "%1"=="/?" goto usage 
if "%1"=="" goto input
if not "%1"=="" goto normal

:input
set /p qrc_file=Please input the "qrc" file to use: 
set /p gen_file=Please input filename of the file to generate: 
goto command

:usage
echo usage:
echo arg1 - qrc file's path
echo arg2 - file path to generate
goto quit

:normal
set qrc_file=%1
set gen_file=%2

:: %1 is the filename of "qrc" file
:: %2 is the filename to generate
:command
rcc -g python %qrc_file% -o %gen_file%

:quit
echo Program finished!
