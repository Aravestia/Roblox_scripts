@echo off

cd /d %~dp0

start /min cmd /k "python hourly_event_notification.py"

exit
