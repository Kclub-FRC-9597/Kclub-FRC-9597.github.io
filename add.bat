@echo off
set /p commit_message=Please enter something:
git add *
git commit -m "%commit_message%"