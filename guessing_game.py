from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os
import random

def start_guessing_game():
    frame_start.pack_forget()  # Esconde a tela inicial
    frame_guessing_game.pack(expand=True, fill='both')  # Mostra a tela do jogo

def back_menu():
    frame_guessing_game.pack_forget() # Esconde a tela do guessing game
    frame_start.pack(expand=True, fill='both') # Mostra a tela inicial


secret_number = random.randint(1,100)
chances = 10

def start_game():
    global secret_number, chances
    secret_number = random.randint(1, 100)
    chances = 10
    label_result.config(text=translate('intro'))
    frame_start.pack_forget()
    frame_guessing_game.pack(expand=True, fill='both')
    restart_button.pack_forget()

def verify_guess():
    global chances
    try:
        guess = int(guess_entry.get())
    except ValueError:
        label_result.config(text=translate('invalid'))
        return


    if guess == secret_number:
        label_result.config(text=translate('win', n=secret_number))
        restart_button.pack(pady=10)
    else:
        chances -= 1
        if chances > 0:
            hint_key = 'hint_more' if guess < secret_number else 'hint_less'
            label_result.config(text=translate(hint_key, c=chances))

        else:
            label_result.config(text=translate('lose', n=secret_number))
            restart_button.pack(pady=10)


translations = {
    'en': {
        'title': "GUESSING GAME",
        'start': "START GUESSING GAME",
        'quit': "QUIT GAME",
        'playing': "YOU'RE PLAYING",
        'back': "BACK",
        'send': "SEND GUESS",
        'restart': "RESTART",
        'intro': "Guess a number between 1 and 100!",
        'win': "Congratulations! You got the number right {n}!",
        'lose': "You lose! The number was {n}.",
        'hint_more': "Wrong! Try a bigger number. You have {c} tries left.",
        'hint_less': "Wrong! Try a minor number. You have {c} tries left.",
        'invalid': "Please enter a valid number.",
        'language': "LANGUAGE"
    },
    'pt': {
        'title': "JOGO DA ADIVINHAÇÃO",
        'start': "COMEÇAR O JOGO",
        'quit': "SAIR DO JOGO",
        'playing': "VOCÊ ESTÁ JOGANDO",
        'back': "VOLTAR",
        'send': "ENVIAR PALPITE",
        'restart': "RECOMEÇAR",
        'intro': "Adivinhe um número entre 1 e 100!",
        'win': "Parabéns! Você acertou o número era {n}!",
        'lose': "Você perdeu! O número era {n}.",
        'hint_more': "Errou! Tente um número maior. Restam {c} tentativas.",
        'hint_less': "Errou! Tente um número menor. Restam {c} tentativas.",
        'invalid': "Por favor, digite um número válido.",
        'language': "IDIOMA"
    }
}

current_lang = 'en'  # ou 'pt'

label_title = None  # variável global para evitar erro de escopo
label_playing_title = None  # Para evitar erro de escopo


def translate(key, **kwargs):
    return translations[current_lang][key].format(**kwargs)

def set_language(lang):
    global current_lang
    current_lang = lang
    update_texts()

def update_texts():
    global title_tk, img_start, img_start_tk, btn_start
    global img_quit, img_quit_tk, btn_quit
    global img_back_tk, send_img_tk
    title_font = ImageFont.truetype("PressStart2P-Regular.ttf", 30)
    
    # Atualiza título da tela inicial
    largura, altura = 1000, 60
    title = Image.new("RGB", (largura, altura), color="#E0FFFF")
    draw = ImageDraw.Draw(title)
    text = translate('title')
    bbox = draw.textbbox((0, 0), text, font=title_font)
    x = (largura - (bbox[2] - bbox[0])) // 2
    y = (altura - (bbox[3] - bbox[1])) // 2
    draw.text((x, y), text, font=title_font, fill="MediumAquamarine")
    title_tk = ImageTk.PhotoImage(title)
    label_title.config(image=title_tk)

    # Remove os botões de idioma ao atualizar o idioma
    #btn_en.place_forget()
    #btn_pt.place_forget()

    # Botão START com fonte retro e imagem
    img_start = Image.new("RGB", (400, 50), color="#4169E1")
    draw_start = ImageDraw.Draw(img_start)
    font_start = ImageFont.truetype("PressStart2P-Regular.ttf", 18)
    draw_start.text((10, 10), translate('start'), font=font_start, fill="white")
    img_start_tk = ImageTk.PhotoImage(img_start)
    btn_start.config(image=img_start_tk, height=50, width=400)
    btn_start.image = img_start_tk

    # Botão QUIT com fonte retro e imagem
    img_quit = Image.new("RGB", (400, 50), color="#8B0000")
    draw_quit = ImageDraw.Draw(img_quit)
    font_quit = ImageFont.truetype("PressStart2P-Regular.ttf", 18)
    draw_quit.text((10, 10), translate('quit'), font=font_quit, fill="white")
    img_quit_tk = ImageTk.PhotoImage(img_quit)
    btn_quit.config(image=img_quit_tk, height=50, width=400)
    btn_quit.image = img_quit_tk

    # Atualiza resultado
    label_result.config(text=translate('intro'))

    # RESTART button text
    restart_button.config(text=translate('restart'))

    # SEND GUESS button
    send_button.config(text=translate('send'), height=2, width=20, relief="flat", font=("PressStart2P", 15))

    btn_start.pack(pady=150)
    btn_quit.pack(pady=10)

    # Atualiza título da tela de jogo
    largura, altura = 600, 60
    title_guessing = Image.new("RGB", (largura, altura), color="#E0FFFF")
    draw = ImageDraw.Draw(title_guessing)
    text = translate('playing')
    bbox = draw.textbbox((0, 0), text, font=title_font)
    x = (largura - (bbox[2] - bbox[0])) // 2
    y = (altura - (bbox[3] - bbox[1])) // 2
    draw.text((x, y), text, font=title_font, fill="MediumAquamarine")
    title_guessing_tk = ImageTk.PhotoImage(title_guessing)
    label_playing_title.config(image=title_guessing_tk)
    label_playing_title.image = title_guessing_tk


def create_lang_button(text, command):
    font_small = ImageFont.truetype("PressStart2P-Regular.ttf", 12)
    img = Image.new("RGB", (180, 40), color="#00BFFF")
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), text, font=font_small, fill="black")
    img_tk = ImageTk.PhotoImage(img)
    btn = Button(frame_start, image=img_tk, command=command, borderwidth=0, bg="#E0FFFF", activebackground="#E0FFFF")
    btn.image = img_tk  # evita que a imagem desapareça
    return btn

window = Tk()  # Define a variável da tela
window.title("Guessing Game Beta 0.1")  # Define o nome da tela

icon_way = os.path.join(os.path.dirname(__file__), "hexagon.ico")  # Define o caminho do ícone da tela
window.iconbitmap(icon_way)  # Define o ícone da tela

window['bg'] = '#E0FFFF'  # Cor da tela
window.geometry("1000x600+300+100")  # Tamanho e posição inicial da tela

pixel_font = ImageFont.truetype("PressStart2P-Regular.ttf", 30)  # Abre o arquivo da fonte utilizada nos textos

# ======================= TELA INICIAL ============================
frame_start = Frame(window, bg="#E0FFFF")
frame_start.pack(expand=True, fill='both')

# Título como imagem
largura, altura = 1000, 60
title = Image.new("RGB", (largura, altura), color="#E0FFFF")
draw = ImageDraw.Draw(title)
text = "GUESSING GAME"
bbox = draw.textbbox((0, 0), text, font=pixel_font)
x = (largura - (bbox[2] - bbox[0])) // 2
y = (altura - (bbox[3] - bbox[1])) // 2
draw.text((x, y), text, font=pixel_font, fill="MediumAquamarine")
title_tk = ImageTk.PhotoImage(title)
label_title = Label(frame_start, image=title_tk, bg="#E0FFFF")
label_title.place(relx=0.5, y=60, anchor='center')

# Botão START
btn_start = Button(frame_start, command=start_guessing_game, bg="#4169E1", relief="flat", font=("PressStart2P", 15), height=2, width=20)


btn_en = create_lang_button("ENGLISH", lambda: set_language('en'))
btn_pt = create_lang_button("PORTUGUÊS", lambda: set_language('pt'))
btn_en.place(relx=0.4, rely=0.5, anchor='center')
btn_pt.place(relx=0.6, rely=0.5, anchor='center')

# Botão QUIT
btn_quit = Button(frame_start, command=window.quit, bg="#8B0000", relief="flat", font=("PressStart2P", 15), height=2, width=20)


# ======================= TELA DO JOGO ============================
frame_guessing_game = Frame(window, bg="#E0FFFF")

largura, altura = 600, 60
title_guessing = Image.new("RGB", (largura, altura), color="#E0FFFF")
draw = ImageDraw.Draw(title_guessing)
text = translate('playing')  # Usa a tradução correta já de início
bbox = draw.textbbox((0, 0), text, font=pixel_font)
x = (largura - (bbox[2] - bbox[0])) // 2
y = (altura - (bbox[3] - bbox[1])) // 2
draw.text((x, y), text, font=pixel_font, fill="MediumAquamarine")
title_guessing_tk = ImageTk.PhotoImage(title_guessing)
label_playing_title = Label(frame_guessing_game, image=title_guessing_tk, bg="#E0FFFF")
label_playing_title.image = title_guessing_tk  # evita garbage collection
label_playing_title.place(relx=0.3, y=30, anchor='n')


# Botão BACK
btn_back = Button(frame_guessing_game, text="BACK", command=back_menu, bg="#8B0000", fg= "white", relief="flat", font=("PressStart2P", 15), height=2, width=20)
btn_back.pack(pady=100)

# Campo para digitar palpite
guess_entry = Entry(frame_guessing_game, font=("PressStart2P", 15), bd=2)
guess_entry.pack(pady=10)

# Botão SEND GUESS
send_button = Button(frame_guessing_game, text="SEND GUESS", command=verify_guess, bg="#00CED1", relief="flat", font=("PressStart2P", 15), height=2, width=20)
send_button.pack(pady=10)

label_result = Label(frame_guessing_game, text="Guess a number between 1 and 100!", font=("PressStart2P", 15), bg="#E0FFFF")
label_result.pack(pady=10)

restart_button = Button(frame_guessing_game, text="RESTART", command=start_game, bg="#00CED1", relief="flat", font=("PressStart2P", 15), height=2, width=20)

window.mainloop()
