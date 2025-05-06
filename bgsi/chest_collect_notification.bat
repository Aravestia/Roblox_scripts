@echo off

cd /d %~dp0

start /min cmd /k "python chest_collect_notification.py"

exit
