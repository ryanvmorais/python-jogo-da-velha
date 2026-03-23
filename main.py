import random
import subprocess
import os

class JogoDaVelha:
    def __init__(self):
        self.reiniciar_jogo()

    def exibir_tabuleiro(self):
        # Limpa o console para uma visualização limpa a cada turno
        # 'nt' refere-se ao Windows (New Technology)
        comando_limpar = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run(comando_limpar, shell=True)
        
        print(f"\n {self.tabuleiro[0][0]} | {self.tabuleiro[0][1]} | {self.tabuleiro[0][2]}")
        print("-----------")
        print(f" {self.tabuleiro[1][0]} | {self.tabuleiro[1][1]} | {self.tabuleiro[1][2]}")
        print("-----------")
        print(f" {self.tabuleiro[2][0]} | {self.tabuleiro[2][1]} | {self.tabuleiro[2][2]}\n")

    def reiniciar_jogo(self):
        # Inicializa o tabuleiro como uma matriz 3x3 de espaços vazios
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.status_final = '' # Pode ser 'X', 'O' ou 'Empate'

    def verificar_vitoria_ou_empate(self):
        # Testa as condições para ambos os jogadores
        for jogador in ['X', 'O']:
            # Verifica Linhas e Colunas
            for i in range(3):
                if all(self.tabuleiro[i][j] == jogador for j in range(3)) or \
                   all(self.tabuleiro[j][i] == jogador for j in range(3)):
                    self.status_final = jogador
                    return

            # Verifica Diagonais
            if (self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == jogador) or \
               (self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == jogador):
                self.status_final = jogador
                return

        # Verifica se não há mais espaços vazios (Empate)
        if not any(' ' in linha for linha in self.tabuleiro):
            self.status_final = 'Empate'

    def jogada_do_usuario(self):
        while True:
            try:
                print("Sua vez (X)!")
                linha = int(input('Digite a linha (0, 1 ou 2): '))
                coluna = int(input('Digite a coluna (0, 1 ou 2): '))
                
                if linha in range(3) and coluna in range(3):
                    if self.tabuleiro[linha][coluna] == ' ':
                        self.tabuleiro[linha][coluna] = 'X'
                        break
                    else:
                        print('❌ Essa posição já está ocupada! Tente outra.')
                else:
                    print('⚠️ Coordenada fora do limite! Escolha entre 0 e 2.')
            except ValueError:
                print('⚠️ Entrada inválida! Digite apenas números inteiros.')

    def jogada_da_maquina(self):
        # A máquina só joga se o usuário ainda não tiver vencido
        if self.status_final != '':
            return 
            
        # Identifica todas as posições livres no tabuleiro
        posicoes_livres = [(l, c) for l in range(3) for c in range(3) if self.tabuleiro[l][c] == ' ']
        
        if posicoes_livres:
            linha, coluna = random.choice(posicoes_livres)
            self.tabuleiro[linha][coluna] = 'O'

# --- Execução Principal ---
if __name__ == "__main__":
    jogo = JogoDaVelha()
    
    while True:
        # Loop principal da partida ativa
        while jogo.status_final == '':
            jogo.exibir_tabuleiro()
            jogo.jogada_do_usuario()
            jogo.verificar_vitoria_ou_empate()
            
            if jogo.status_final == '':
                jogo.jogada_da_maquina()
                jogo.verificar_vitoria_ou_empate()

        # Tela de encerramento da partida
        jogo.exibir_tabuleiro()
        if jogo.status_final == 'Empate':
            print("⚖️ Deu Velha! O jogo terminou empatado.")
        else:
            print(f"🎉 Fim de jogo! O vencedor foi: {jogo.status_final}")

        # Opção de Replay
        pergunta = input('\nDeseja jogar novamente? (s/n): ').lower()
        if pergunta == 's':
            jogo.reiniciar_jogo()
        else:
            print("Até a próxima! 👋")
            break
