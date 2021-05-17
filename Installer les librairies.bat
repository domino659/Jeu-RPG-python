echo off 
%@Try%
pip install -r requirements.txt 
%@EndTry%
py -m pip install -r requirements.txt
echo
echo Librairies have been installed
pause
