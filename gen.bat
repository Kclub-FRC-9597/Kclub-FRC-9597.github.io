@echo off
echo ------Generating HTML files to Docs------
pelican content
echo -------------Moving Files----------------
.\set.bat
@echo on
