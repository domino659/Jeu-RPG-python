echo off 
%@Try%
pip install -r requirements.txt 
%@EndTry%
py -m pip install -r requirements.txt
echo
echo \n Les librairies ont été installées
pause