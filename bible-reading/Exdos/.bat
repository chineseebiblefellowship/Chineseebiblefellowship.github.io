@echo off
setlocal enabledelayedexpansion

:: 创建目录
mkdir exdos-chapters

:: 循环创建 HTML 文件
for /L %%i in (1,1,50) do (
    set "chapter=%%i"
    if %%i lss 10 set "chapter=0%%i"
    
    echo ^<!DOCTYPE html^> > exdos-chapters/exdos-chapter-!chapter!.html
    echo ^<html lang="zh"^> >> exdos-chapters/exdos-chapter-!chapter!.html
    echo ^<head^> >> exdos-chapters/exdos-chapter-!chapter!.html
    echo ^<meta charset="UTF-8" /^> >> exdos-chapters/exdos-chapter-!chapter!.html
    echo ^<meta name="viewport" content="width=device-width, initial-scale=1.0" /^> >> exdos-chapters/exdos-chapter-!chapter!.html
    echo ^<title^>创世记 第 !chapter! 章^</title^> >> exdos-chapters/exdos-chapter-!chapter!.html
    echo ^</head^> >> exdos-chapters/exdos-chapter-!chapter!.html
    echo ^<body^> >> exdos-chapters/exdos-chapter-!chapter!.html
    echo ^<h1^>创世记 第 !chapter! 章^</h1^> >> exdos-chapters/exdos-chapter-!chapter!.html
    echo ^<p^>这里是创世记第 !chapter! 章的内容。^</p^> >> exdos-chapters/exdos-chapter-!chapter!.html
    echo ^</body^> >> exdos-chapters/exdos-chapter-!chapter!.html
    echo ^</html^> >> exdos-chapters/exdos-chapter-!chapter!.html
)

echo 所有文件已生成。
pause
