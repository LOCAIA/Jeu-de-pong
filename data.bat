@echo off
setlocal

REM Spécifiez le chemin complet vers le fichier main.ini
set "INI_FILE=main.ini"

REM Vérifie si le fichier main.ini existe
if not exist "%INI_FILE%" (
    echo Le fichier main.ini est introuvable.
    exit /b 1
)

REM Charge les informations depuis le fichier main.ini
for /f "tokens=1,* delims==" %%a in ('type "%INI_FILE%" ^| find "="') do (
    set "%%a=%%b"
)

REM Affiche les informations chargées
echo Informations :
echo Nom : %Nom%
echo Version : %Version%
echo Utilisateur : %Utilisateur%
echo Createur : %Createur%
echo Langage Utilise : %LangageUtilise%

echo.
echo Ressources :
echo Appli Principale : %AppliPrincipale%
echo Icon App : %IconApp%
echo Ecran Chargement : %EcranChargement%
echo Page Accueil : %PageAccueil%
echo Page Parametres : %PageParametres%
echo Parametres INI : %ParametresINI%
echo Texture : %Texture%
echo Colision : %Colision%
echo Map : %Map%
echo Map INI : %MapINI%
echo Ecran Chargement Photo : %EcranChargementPhoto%
echo Ecran Menu Photo : %EcranMenuPhoto%

echo.
echo Donne :
echo main XML : %mainXML%
echo conditions XML : %conditionsXML%
echo Lang Fr XML : %LangFrXML%
echo Lang An XML : %LangAnXML%
echo User Progression XML : %UserProgressionXML%



endlocal
echo fin du programme
set /p leave=
