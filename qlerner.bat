@echo off

REM Check if Python 3.10 is installed
python --version | findstr /i "3.10" >nul && (
    echo Python 3.10 is already installed.
) || (
    echo Installing Python 3.10...
    REM Download the Python installer
    curl https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe -o python-3.10.0-amd64.exe
    REM Install Python 3.10
    start /wait python-3.10.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
    REM Delete the installer
    del python-3.10.0-amd64.exe
)

REM Install pip
echo Installing pip...
python -m ensurepip --default-pip

REM Install requirements
echo Installing requirements...
python -m pip install --upgrade pip -r requirements.txt

REM Start the Flask server
echo Starting Flask server...
set FLASK_APP=qlerner
set FLASK_ENV=development
python -m flask init-db
start http://localhost:5000
python -m flask run --host=0.0.0.0 --port=5000
