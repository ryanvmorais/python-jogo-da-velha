@echo off
title Iniciando Jogo da Velha...
cls

echo ===========================================
echo   VERIFICANDO AMBIENTE PYTHON...
echo ===========================================

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado! 
    echo Por favor, instale o Python em: https://python.org
    pause
    exit
)

echo [OK] Python detectado. Iniciando a partida...
python main.py
pause
