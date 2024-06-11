@echo off
:: rem also declare the comments
rem directory where command lives
@REM set COMMAND_ROOT=C:\UserData\Environment\Tools\anaconda_data\envs\ic\Lib\site-packages\PySide6
set COMMAND_ROOT=C:\Users\Dell\.conda\envs\ic\Lib\site-packages\PySide6


:: %1 ui file to use
:: %2 output file to generate
if "%1"=="/?" goto usage 
if "%1"=="" goto input
if not "%1"=="" goto normal

:input
set /p ui_file=Please input the ui file to use: 
set /p gen_file=Please input filename of the file to generate: 
goto command

:usage
echo usage:
echo arg1 - ui file's path
echo arg2 - file path to generate
goto quit

:normal
set ui_file=%1
set gen_file=%2

:command
:: use the command below if configured the PATH variable
:: uic %1 -g python -o %2
%COMMAND_ROOT%/uic %ui_file% -g python -o %gen_file%

:quit
echo program finished!
