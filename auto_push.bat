@echo off

cd /d %~dp0

git add .

git commit -m "Auto-commit on %date% at %time%"

git push origin main

pause