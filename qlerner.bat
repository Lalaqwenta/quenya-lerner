@echo off

:: Check if Docker is installed
where docker >nul 2>&1
if %errorlevel% neq 0 (
    echo Docker not found. Installing Docker...
    powershell -Command "Invoke-WebRequest -Uri https://get.docker.com/builds/Windows/x86_64/docker-latest.exe -OutFile docker.exe"
    docker.exe --version >nul 2>&1 || set PATH=%PATH%;%cd%
)

:: Pull the Docker image
docker pull lalaqwenta/quenya-lerner

:: Run the Docker container
start /b docker run -p 5000:80 lalaqwenta/quenya-lerner

:: Open browser
start http://localhost:5000
