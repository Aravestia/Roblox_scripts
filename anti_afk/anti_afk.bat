@echo off

cd /d %~dp0

start /min cmd /k "python anti_afk.py"

exit
