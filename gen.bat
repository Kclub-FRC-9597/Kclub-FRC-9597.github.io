set a=%1
@echo off
echo
echo ------Generating HTML files to Docs------
pelican content
echo -------------Moving Files----------------
call set.bat

if "%a%"=="-r" (
	echo -----------Run Servo as required-----------
	pelican --listen
)


@echo on
