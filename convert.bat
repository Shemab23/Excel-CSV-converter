@echo off
call "C:\Users\Shema\miniconda3\Scripts\activate.bat" "C:\Users\Shema\miniconda3"
conda run -n ML python "C:\Users\Shema\Desktop\excel-csv\Converter.py" %1 %2
pause
