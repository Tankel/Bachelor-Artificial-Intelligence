@echo off
set /p dia= Captura el dia: 
set /p mes= Captura el mes: 
if %dia% == 24 echo Hoy es 24
if %mes% == 12 goto Diciembre
	echo Falta aun para Navidad
	goto Salida
:Diciembre
	echo ¡Feliz navidad!
:Salida
	echo Salida jajaj
