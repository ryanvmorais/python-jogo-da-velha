#!/bin/bash

# Limpa o terminal antes de iniciar
clear

echo "==========================================="
echo "   INICIANDO JOGO DA VELHA EM PYTHON..."
echo "==========================================="

# Verifica se o comando python3 existe no sistema
if ! command -v python3 &> /dev/null
then
    echo "[ERRO] Python 3 nao encontrado!"
    echo "Por favor, instale o Python usando o gerenciador de pacotes do seu sistema."
    exit
fi

echo "[OK] Python 3 detectado. Preparando o tabuleiro..."
python3 main.py
