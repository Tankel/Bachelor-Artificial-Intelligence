@echo off
cls

set /p numero= ¿cuántos archivos quiere crear?
set /p archivo= ¿Como se llamaran los archivos? 
set /p ruta= ¿cual es la ruta?

for /L %%i in (1, 1, %numero%) do (
	copy NUL %ruta%\%archivo%_%%i.txt
)
