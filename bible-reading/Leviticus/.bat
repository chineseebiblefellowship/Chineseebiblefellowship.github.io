@echo off
setlocal enabledelayedexpansion

:: 创建目录
mkdir leviticus-chapters

:: 循环创建 HTML 文件
for /L %%i in (1,1,50) do (
    set "chapter=%%i"
    if %%i lss 10 set "chapter=0%%i"
   
)

echo 所有文件已生成。
pause
