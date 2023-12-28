@echo off
ping up.edu.mx
::ping up.edu.mx
if errorLevel 1 (goto stop) else (goto exit)
:stop
	echo Hubo un error
	pause
:exit