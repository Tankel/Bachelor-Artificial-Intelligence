@echo off
set /p n= Ingrese el numero de archivos: 
set /p archivo= Ingrese el nombre: 
set /p ruta= Ingrese la ruta: 
FOR /L %%i IN (1,1,%n%) DO (
	copy NUL %ruta%\%archivo%_%%i.txt
)