@echo off
call C:\ProgramData\miniconda3\Scripts\activate.bat info-dynamics

echo Installing basic packages...
python -m pip install matplotlib seaborn pandas numpy scipy scikit-learn

echo Installing factor_analyzer...
python -m pip install factor_analyzer

echo Installing jupyter and notebook...
python -m pip install jupyter notebook

echo.
echo === Installation complete! ===
python -c "import factor_analyzer, pandas, numpy; print('All packages working!')" 