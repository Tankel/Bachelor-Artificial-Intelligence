@echo off

set Num= 1 2 3 4 5

FOR %%i IN (1,1,%i%) DO (
	echo %%i
)

FOR /L %%i IN (%num%) DO (
	echo Numero %%i
)

FOR /D %%v in (*) DO (
	echo %%v
)