@echo off
cls
echo POSITIVES
for %%i in (01 02 03 04 05 06) do (
echo.
for /f %%j in (func_tests\pos_%%i_args.txt) do (
app.exe func_tests\pos_%%i_in.txt %%j > func_tests\pos_out.txt
)
fc func_tests\pos_out.txt func_tests\pos_%%i_out.txt
if %errorlevel% equ 0 (echo PASSED) else (echo FAILED)
echo.
pause
)

cls
echo NEGATIVES
for %%i in (01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17) do (
echo.
for /f %%j in (func_tests\neg_%%i_args.txt) do (
app.exe func_tests\neg_%%i_in.txt %%j > func_tests\neg_out.txt
)
fc func_tests\neg_out.txt func_tests\neg_%%i_out.txt
if %errorlevel% equ 0 (echo PASSED) else (echo FAILED)
echo.
pause
)