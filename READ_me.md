# Excel-CSV Bridge

__The missing ink between human-readable data and machine-ready inputs.__

Machines thrive on `.csv`, but humans and professional workflows rely on `.xlsx`. This tool ensures your Machine Learning models have zero limitations by providing a seamless, lossless conversion bridge.

## Core features

* Excel → CSV : Lossless extraction of raw data for ML model consumption. Requires only the file path.
* CSV → Excel: Professional formatting of model outputs for stakeholders. Supports specific sheet naming to keep data organized.

## Tech stack

* Language: Python 3.11
* Engine: pandas
* Automation: windows Batch scripting; for "one_click" CLI usage

## Setup

1. Environment: Install pandas and openpyxl
2. Path configuration:
   1. Using conda

      ```.bat
      @echo off
      call "C:\Users\USER\miniconda3\Scripts\activate.bat" "C:\Users\USER\miniconda3"
      conda run -n ML python "C:\Path\To\Converter.py" %1 %2
      pause
      ```
   2. Standard Python

      ```.bat
      @echo off
      "C:\Users\USER\AppData\Local\Programs\Python\Python311\python.exe" "C:\Path\To\Converter.py" %1 %2
      pause
      ```

## Usage

Install the requirements; advised with in a virstual environment; Python 13.11 +

Run the tool in your terminal.

__To CSV:__

```powershell
convert data.xlsx
```

__To Excel:__

```powershell
convert data2.csv sheatName1
```

## Project structure

```plaintext
|__ convert.bat
|__ Converter.py
|__ Read_me.md
|__ Requirements.txt
```

## Status

* Initiation  :  24/12/2025
* Developer: Bruno SHEMA | Software Engineer | European University of Lefke
