@echo off
call C:\ProgramData\miniconda3\Scripts\activate.bat info-dynamics
python -c "import sys; print('Python path:', sys.executable)"
echo.
echo Installing ipykernel...
python -m pip install ipykernel --no-deps
echo.
echo Installing jupyter kernel...
python -m ipykernel install --user --name info-dynamics --display-name "Information Dynamics" 