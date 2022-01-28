import json
import random
import re
import unicodedata
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
import string

fonte = ('Comic Sans MS', 12)
FUNDO = 'gray'
FUNDOBOTAO = '#585454'


def define_underscores(palavra):
    n_underscore = len(palavra)
    under = ["_" for _ in range(n_underscore)]
    return under


class Hangman(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.resizable(False, False)
        x = 500
        y = 640
        self.geometry(f"{x}x{y}+"
                      f"{int(self.winfo_screenwidth() / 2 - x / 2) + 1300}+"
                      f"{int(self.winfo_screenheight() / 2 - y / 2)}")
        self.configure(background=FUNDO)

        self.palavras = ['banana', 'amora']
        # ################################################################################################## #
        # DICA
        # ################################################################################################## #
        f_palavra_dica = Frame(self, background=FUNDO)
        f_palavra_dica.pack()

        # Dica
        l_palavra_dica = Label(f_palavra_dica,
                               text='Dica de palavara: ',
                               font=fonte,
                               background=FUNDO)
        l_palavra_dica.pack()

        # Armazena a palavra e a dica
        self.palavra = le_arquivo_palavras_e_escolhe_a_palavra()
        # Exibe a dica
        self.l_dica = Label(f_palavra_dica,
                            text=f"{self.palavra[1]}",
                            font=fonte,
                            background=FUNDO)
        self.l_dica.pack()

        # Cria o que vai esconder a palavra
        self.underscores = define_underscores(self.palavra[0])
        # Exibe a palavra escondida ('underscores')
        self.l_palavra = Label(f_palavra_dica,
                               text=f'{" ".join(self.underscores)}',
                               font=fonte,
                               background=FUNDO)
        self.l_palavra.pack()

        # ################################################################################################## #
        # IMAGEM
        # ################################################################################################## #
        f_imagem = LabelFrame(self, background=FUNDO)
        f_imagem.pack()

        self.img = imagens()
        self.imagem_display = Label(f_imagem,
                                    image=self.img[0][1],
                                    width=440,
                                    height=400,
                                    background=FUNDO)
        self.imagem_display.pack(ipady=20)
        # ################################################################################################## #
        # LETRAS
        # ################################################################################################## #
        self.f_botao_cima = Frame(self, background=FUNDO)
        self.f_botao_baixo = Frame(self, background=FUNDO)
        self.f_botao_cima.pack(pady=4)
        self.f_botao_baixo.pack()
        self.botoes = []
        self.cria_botoes()

        # Erros
        self.erros = 0

    # Cria os botões
    def cria_botoes(self):
        for i, letra in enumerate(string.ascii_uppercase):
            if letra <= "M":
                self.botoes.append(Button(self.f_botao_cima, text=letra, font=fonte, background=FUNDOBOTAO,
                                          command=lambda le=letra: self.valida_palavra(le)))
                self.botoes[i].pack(side=LEFT, pady=2, padx=3)
            else:
                self.botoes.append(Button(self.f_botao_baixo, text=letra, font=fonte, background=FUNDOBOTAO,
                                          command=lambda le=letra: self.valida_palavra(le)))
                self.botoes[i].pack(side=LEFT, pady=2, padx=3)

    # Ao clicar na letra, irá verificar se a letra escolhida está contida na palavra
    def valida_palavra(self, letra):
        # Faz iteração por todos os botões para encontrar a letra pressionada
        for i, le in enumerate(self.botoes):
            # Verifica a letra pressionada
            v_letra = le.cget('text')

            if v_letra == letra:
                # Desabilita o botão pressionado
                self.botoes[i]['state'] = DISABLED
                # Armazena a palavra numa variável local
                palavra = self.palavra[0]

                # Se a letra estiver na palavra
                if v_letra in palavra:
                    # Itera pela palavra para encontra a posição e subistituir o 'underscore'
                    for j, l in enumerate(palavra):
                        # Valida a letra
                        if letra == l:
                            self.underscores[j] = l
                    # Mostra a palavra juntando a palavra do 'underscores'
                    self.l_palavra.config(text=" ".join(self.underscores))
                else:
                    # Faz a contagem dos erros e muda a imagem
                    self.erros += 1
                    if self.erros == 1:
                        self.imagem_display['image'] = self.img[self.erros][1]
                    elif self.erros == 2:
                        self.imagem_display['image'] = self.img[self.erros][1]
                    elif self.erros == 3:
                        self.imagem_display['image'] = self.img[self.erros][1]
                    elif self.erros == 4:
                        self.imagem_display['image'] = self.img[self.erros][1]
                    elif self.erros == 5:  # Total de erros 5
                        self.imagem_display['image'] = self.img[self.erros][1]
                        self.l_palavra.config(text=self.palavra[0])
                        self.l_palavra['fg'] = 'darkred'

                        if messagebox.askquestion("Game over", "Você não acertou a palavra, jogar novamente?") == "yes":
                            self.jogar_novamente()
                        else:
                            self.quit()

        # Valida se a pessoa acertou a palavra
        if self.palavra[0].upper() == "".join(self.underscores):
            self.l_palavra['fg'] = "darkgreen"
            for btn in self.botoes:
                btn['state'] = DISABLED
            # Ao vencer, pergunta se quer jogar novamente
            if messagebox.askquestion("Vitória", "Você venceu, deseja jogar novamente?") == "yes":  # Se, sim.
                # Reseta as variáveis
                self.jogar_novamente()
            else:  # Se, não.
                self.quit()  # Sai da aplicação

    # Jogar novamente
    def jogar_novamente(self):
        self.palavra = le_arquivo_palavras_e_escolhe_a_palavra()
        self.underscores = define_underscores(self.palavra[0])
        self.l_palavra['text'] = " ".join(self.underscores)
        self.l_dica['text'] = self.palavra[1]
        self.imagem_display['image'] = self.img[0][1]
        self.erros = 0
        self.l_palavra['fg'] = 'black'

        for btn in self.botoes:
            btn['state'] = NORMAL


def imagens():
    lista_imagens = []
    for i, x in enumerate('hangman-img'):
        if i <= 5:
            lista_imagens.append((i, ImageTk.PhotoImage(Image.open(f'./hangman-img/hangman - stage {i + 1}.png'))))
    return lista_imagens


def le_arquivo_palavras_e_escolhe_a_palavra():
    with open("Palavras.json", 'r') as arquivo:
        palavra = json.load(arquivo)
        categoria = random.choice(list(palavra.keys()))  # Pega a dica

        palavra_escolhida = random.choice(list(palavra.get(categoria)))  # Usa a dica e pega a lista com as palavras
        pal = unicodedata.normalize("NFD", palavra_escolhida.upper())  # Remove caracteres especiais
        nova = re.sub(r'[\u0300-\u036f]', "", pal)  # Devolve o caracter removido como uma letra normal
        return nova, categoria


if __name__ == '__main__':
    hangman = Hangman()
    hangman.mainloop()
