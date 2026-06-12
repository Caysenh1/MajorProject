#HANGMAN
import ttkbootstrap as ttk
import random
import tkinter.messagebox as mbox

window = ttk.Window(themename = 'journal')
window.title("HANGMAN")
icon = ttk.PhotoImage(file='hangicon.png')
window.iconphoto(False, icon)
#LOGIC
guess_list = []
guesses = 8
acc = guesses - 1
image_pos = 8 - guesses
#Play Again Funcion
def again():
    global guess_list
    global guesses
    global word
    global fake
    global List
    global acc
    guesses = 8
    acc = guesses - 1
    guessesleft.config(text=f"Guesses Left: {acc}")
    word = random.choice(List)
    guess_list.clear()
    guessed.config(text=guess_list)
    guesses = 8
    print(word)
    fake =["_"] * len(word)
    fake = list(fake)
    WordImg.config(text=fake)
    A.config(state='enabled')
    B.config(state='enabled')
    C.config(state='enabled')
    D.config(state='enabled')
    E.config(state='enabled')
    F.config(state='enabled')
    G.config(state='enabled')
    H.config(state='enabled')
    I.config(state='enabled')
    J.config(state='enabled')
    K.config(state='enabled')
    L.config(state='enabled')
    M.config(state='enabled')
    N.config(state='enabled')
    O.config(state='enabled')
    P.config(state='enabled')
    Q.config(state='enabled')
    R.config(state='enabled')
    S.config(state='enabled')
    T.config(state='enabled')
    U.config(state='enabled')
    V.config(state='enabled')
    W.config(state='enabled')
    X.config(state='enabled')
    Y.config(state='enabled')
    Z.config(state='enabled')
    HangImage.config(image=hangimages[0])
    window.bind("a", lambda event: a1())
    window.bind("b", lambda event: b1())
    window.bind("c", lambda event: c1())
    window.bind("d", lambda event: d1())
    window.bind("e", lambda event: e1())
    window.bind("f", lambda event: f1())
    window.bind("g", lambda event: g1())
    window.bind("h", lambda event: h1())
    window.bind("i", lambda event: i1())
    window.bind("j", lambda event: j1())
    window.bind("k", lambda event: k1())
    window.bind("l", lambda event: l1())
    window.bind("m", lambda event: m1())
    window.bind("n", lambda event: n1())
    window.bind("o", lambda event: o1())
    window.bind("p", lambda event: p1())
    window.bind("q", lambda event: q1())
    window.bind("r", lambda event: r1())
    window.bind("s", lambda event: s1())
    window.bind("t", lambda event: t1())
    window.bind("u", lambda event: u1())
    window.bind("v", lambda event: v1())
    window.bind("w", lambda event: w1())
    window.bind("x", lambda event: x1())
    window.bind("y", lambda event: y1())
    window.bind("z", lambda event: z1())
#Win Condition Function
def check():
    global guesses
    global acc
    acc = guesses - 1
    guessesleft.config(text=f"Guesses Left: {acc}")
    if guesses == 1:
        if fake == ["_"] * len(word):
            A.config(state = 'disabled')
            B.config(state = 'disabled')
            C.config(state ='disabled')
            D.config(state='disabled')
            E.config(state='disabled')
            F.config(state = 'disabled')
            G.config(state = 'disabled')
            H.config(state ='disabled')
            I.config(state='disabled')
            J.config(state='disabled')
            K.config(state = 'disabled')
            L.config(state = 'disabled')
            M.config(state ='disabled')
            N.config(state='disabled')
            O.config(state='disabled')
            P.config(state = 'disabled')
            Q.config(state = 'disabled')
            R.config(state ='disabled')
            S.config(state='disabled')
            T.config(state='disabled')
            U.config(state = 'disabled')
            V.config(state = 'disabled')
            W.config(state ='disabled')
            X.config(state='disabled')
            Y.config(state='disabled')
            Z.config(state='disabled')
            mbox.showerror("Game Over", f"How did you lose without getting a single letter!? The word was {word}")
        else:
            A.config(state = 'disabled')
            B.config(state = 'disabled')
            C.config(state ='disabled')
            D.config(state='disabled')
            E.config(state='disabled')
            F.config(state = 'disabled')
            G.config(state = 'disabled')
            H.config(state ='disabled')
            I.config(state='disabled')
            J.config(state='disabled')
            K.config(state = 'disabled')
            L.config(state = 'disabled')
            M.config(state ='disabled')
            N.config(state='disabled')
            O.config(state='disabled')
            P.config(state = 'disabled')
            Q.config(state = 'disabled')
            R.config(state ='disabled')
            S.config(state='disabled')
            T.config(state='disabled')
            U.config(state = 'disabled')
            V.config(state = 'disabled')
            W.config(state ='disabled')
            X.config(state='disabled')
            Y.config(state='disabled')
            Z.config(state='disabled')
            mbox.showerror("Game Over", f"You Lost! The word was: {word}")
    if '_' not in fake:
        if guesses == 8:
            A.config(state = 'disabled')
            B.config(state = 'disabled')
            C.config(state ='disabled')
            D.config(state='disabled')
            E.config(state='disabled')
            F.config(state = 'disabled')
            G.config(state = 'disabled')
            H.config(state ='disabled')
            I.config(state='disabled')
            J.config(state='disabled')
            K.config(state = 'disabled')
            L.config(state = 'disabled')
            M.config(state ='disabled')
            N.config(state='disabled')
            O.config(state='disabled')
            P.config(state = 'disabled')
            Q.config(state = 'disabled')
            R.config(state ='disabled')
            S.config(state='disabled')
            T.config(state='disabled')
            U.config(state = 'disabled')
            V.config(state = 'disabled')
            W.config(state ='disabled')
            X.config(state='disabled')
            Y.config(state='disabled')
            Z.config(state='disabled')
            mbox.showinfo("Game Over", f"You Won without losing a life! WOW!")
        if guesses == 2:
            A.config(state = 'disabled')
            B.config(state = 'disabled')
            C.config(state ='disabled')
            D.config(state='disabled')
            E.config(state='disabled')
            F.config(state = 'disabled')
            G.config(state = 'disabled')
            H.config(state ='disabled')
            I.config(state='disabled')
            J.config(state='disabled')
            K.config(state = 'disabled')
            L.config(state = 'disabled')
            M.config(state ='disabled')
            N.config(state='disabled')
            O.config(state='disabled')
            P.config(state = 'disabled')
            Q.config(state = 'disabled')
            R.config(state ='disabled')
            S.config(state='disabled')
            T.config(state='disabled')
            U.config(state = 'disabled')
            V.config(state = 'disabled')
            W.config(state ='disabled')
            X.config(state='disabled')
            Y.config(state='disabled')
            Z.config(state='disabled')
            mbox.showinfo("Game Over", "You Won with one life remaining! Phew!")
        else:
            A.config(state = 'disabled')
            B.config(state = 'disabled')
            C.config(state ='disabled')
            D.config(state='disabled')
            E.config(state='disabled')
            F.config(state = 'disabled')
            G.config(state = 'disabled')
            H.config(state ='disabled')
            I.config(state='disabled')
            J.config(state='disabled')
            K.config(state = 'disabled')
            L.config(state = 'disabled')
            M.config(state ='disabled')
            N.config(state='disabled')
            O.config(state='disabled')
            P.config(state = 'disabled')
            Q.config(state = 'disabled')
            R.config(state ='disabled')
            S.config(state='disabled')
            T.config(state='disabled')
            U.config(state = 'disabled')
            V.config(state = 'disabled')
            W.config(state ='disabled')
            X.config(state='disabled')
            Y.config(state='disabled')
            Z.config(state='disabled')
            mbox.showinfo("Game Over", f"You Won with {acc} lives remaining!")
    
    

#Letter Specific Functions    
def a():
    global guesses
    if "a" in word:
        for i, let in enumerate(word):
            if let == "a":
                fake[i] = "a"
        
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("a")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    A.config(state='disabled')
    

def b():
    global guesses
    if "b" in word:
        for i, let in enumerate(word):
            if let == "b":
                fake[i] = "b"
            WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("b")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    B.config(state='disabled')
    
def c():
    global guesses
    if "c" in word:
        for i, let in enumerate(word):
            if let == "c":
                fake[i] = "c"
            WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("c")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    C.config(state='disabled')
    
def d():
    global guesses
    if "d" in word:
        for i, let in enumerate(word):
            if let == "d":
                fake[i] = "d"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("d")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    D.config(state='disabled')
def e():
    global guesses
    if 'e' in word:
        for i, let in enumerate(word):
            if let == "e":
                fake[i] = "e"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("e")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    E.config(state='disabled')
def f():
    global guesses
    if 'f' in word:
        for i, let in enumerate(word):
            if let == "f":
                fake[i] = "f"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("f")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    F.config(state='disabled')
def g():
    global guesses
    if 'g' in word:
        for i, let in enumerate(word):
            if let == "g":
                fake[i] = "g"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("g")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    G.config(state='disabled')
def h():
    global guesses
    if 'h' in word:
        for i, let in enumerate(word):
            if let == "h":
                fake[i] = "h"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("h")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    H.config(state='disabled')
def i():
    global guesses
    if 'i' in word:
        for i, let in enumerate(word):
            if let == "i":
                fake[i] = "i"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("i")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    I.config(state='disabled')
def j():
    global guesses
    if 'j' in word:
        for i, let in enumerate(word):
            if let == "j":
                fake[i] = "j"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("j")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    J.config(state='disabled')
def k():
    global guesses
    if 'k' in word:
        for i, let in enumerate(word):
            if let == "k":
                fake[i] = "k"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("k")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    K.config(state='disabled')
def l():
    global guesses
    if 'l' in word:
        for i, let in enumerate(word):
            if let == "l":
                fake[i] = "l"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("l")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    L.config(state='disabled')
def m():
    global guesses
    if 'm' in word:
        for i, let in enumerate(word):
            if let == "m":
                fake[i] = "m"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("m")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    M.config(state='disabled')
def n():
    global guesses
    if 'n' in word:
        for i, let in enumerate(word):
            if let == "n":
                fake[i] = "n"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("n")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    N.config(state='disabled')
def o():
    global guesses
    if 'o' in word:
        for i, let in enumerate(word):
            if let == "o":
                fake[i] = "o"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("o")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    O.config(state='disabled')
def p():
    global guesses
    if 'p' in word:
        for i, let in enumerate(word):
            if let == "p":
                fake[i] = "p"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("p")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    P.config(state='disabled')
def q():
    global guesses
    if "q" in word:
        for i, let in enumerate(word):
            if let == "q":
                fake[i] = "q"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("q")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    Q.config(state='disabled')
def r():
    global guesses
    if "r" in word:
        for i, let in enumerate(word):
            if let == "r":
                fake[i] = "r"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("r")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    R.config(state='disabled')
def s():
    global guesses
    if "s" in word:
        for i, let in enumerate(word):
            if let == "s":
                fake[i] = "s"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("s")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    S.config(state='disabled')
def t():
    global guesses
    if "t" in word:
        for i, let in enumerate(word):
            if let == "t":
                fake[i] = "t"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("t")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    T.config(state='disabled')
def u():
    global guesses
    if "u" in word:
        for i, let in enumerate(word):
            if let == "u":
                fake[i] = "u"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("u")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    U.config(state='disabled')
def v():
    global guesses
    if "v" in word:
        for i, let in enumerate(word):
            if let == "v":
                fake[i] = "v"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("v")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    V.config(state='disabled')
def w():
    global guesses
    if "w" in word:
        for i, let in enumerate(word):
            if let == "w":
                fake[i] = "w"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("w")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    W.config(state='disabled')
def x():
    global guesses
    if "x" in word:
        for i, let in enumerate(word):
            if let == "x":
                fake[i] = "x"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("x")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    X.config(state="disabled")
def y():
    global guesses
    if "y" in word:
        for i, let in enumerate(word):
            if let == "y":
                fake[i] = "y"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("y")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    Y.config(state='disabled')
def z():
    global guesses
    if "z" in word:
        for i, let in enumerate(word):
            if let == "z":
                fake[i] = "z"
        WordImg.config(text=" ".join(fake))
    else:
        guesses -= 1
        guess_list.append("z")
        guess_list.sort()
        guessed.config(text=guess_list)
        HangImage.config(image=hangimages[min(8 - guesses, 7)])
        HangImage.image = hangimages[min(8 - guesses, 7)]
    Z.config(state='disabled')
#Word List
List = ["cactus", "blanket", "whisper",
        "jungle", "pencil", "thunder",
        "marble", "lantern", "pickle",
        "rocket", "velvet", "pumpkin",
        "hammer", "igloo", "parrot",
        "scooter", "diamond", "canyon",
        "biscuit", "tornado", "backpack",
        "octopus", "sunflower", "treasure",
        "fireworks", "sandcastle", "microwave",
        "watermelon", "snowflake", "toothbrush",
        "elephant", "computer", "backpack",
        "mountain", "pencil", "guitar",
        "chocolate", "rainbow", "adventure",
        "butterfly", "football", "kangaroo",
        "sandwich", "treasure", "dinosaur",
        "volcano", "calendar", "dramatic",
        "airplane", "umbrella", "pineapple"]
word = random.choice(List)
print(word)
#FRAMES
guessesleftFrame = ttk.Frame(window)
guessesleftFrame.pack()
hFrame = ttk.Frame(window)
hFrame.pack()
bFrame1 = ttk.Frame(window)
bFrame1.pack()
bFrame2 = ttk.Frame(window)
bFrame2.pack()
bFrame3 = ttk.Frame(window)
bFrame3.pack()
PlayFrame = ttk.Frame(window)
PlayFrame.pack()
LabFrame=ttk.Frame(window)
LabFrame.pack()
ThemeFrame = ttk.Frame(window)
ThemeFrame.pack()
#Theme Change Logic
def jour():
    window = Window(themename='journal')
def puls():
    window.style.theme_use('pulse')

#Theme Change Buttons And Label
ThemeL = ttk.Label(LabFrame, text="THEMES: ",
                   font=("calibri", 20, 'bold'))
ThemeL.pack()
Journal = ttk.Button(ThemeFrame,
                     text='Journal',
                     width=15)
Pulse = ttk.Button(ThemeFrame,
                   text='Pulse',
                     width=15,
                   command=puls)
Flatly = ttk.Button(ThemeFrame,
                    text='Flatly',
                     width=15)
Cosmo = ttk.Button(ThemeFrame,
                   text = 'Cosmo',
                     width=15)
Minty = ttk.Button(ThemeFrame,
                   text='Minty',
                     width=15)
Solar = ttk.Button(ThemeFrame,
                   text='Solar',
                     width=15)
Cyborg = ttk.Button(ThemeFrame,
                    text="Cyborg",
                     width=15)
Vapor = ttk.Button(ThemeFrame,
                   text="Vapor",
                     width=15)
Journal.grid(row=0, column=0, padx=5, pady=5)
Pulse.grid(row=0, column=1, padx=5, pady=5)
Flatly.grid(row=0, column=2, padx=5, pady=5)
Cosmo.grid(row=0, column=3, padx=5, pady=5)
Minty.grid(row=1, column=0, padx=5, pady=5)
Solar.grid(row=1, column=1, padx=5, pady=5)
Cyborg.grid(row=1, column=2, padx=5, pady=5)
Vapor.grid(row=1, column=3, padx=5, pady=5)
#Guessed Letters Label
guessed = ttk.Label(hFrame, text=guess_list,
                    font=("calibri", 18),
                    justify='right')
guessed.pack(side='right')
#guesses left label
guessesleft = ttk.Label(guessesleftFrame, text=f"Guesses Left: {acc}",
                        font=("calibri", 18))
guessesleft.pack()
#HANGMAN IMAGE
hangbase = ttk.PhotoImage(file="hang2.png")
hang1 = ttk.PhotoImage(file="hang3.png")
hang2 = ttk.PhotoImage(file="hang4.png")
hang3 = ttk.PhotoImage(file="hang5.png")
hang4 = ttk.PhotoImage(file="hang6.png")
hang5 = ttk.PhotoImage(file="hang7.png")
hang6 = ttk.PhotoImage(file="hang8.png")
hang7 = ttk.PhotoImage(file='hang9.png')
hangimages = [hangbase, hang1, hang2, hang3,
              hang4, hang5, hang6, hang7]
HangImage = ttk.Label(hFrame, image=hangbase)
HangImage.pack()

#HangMan Word
fakelen = len(word)
WordImg = ttk.Label(hFrame, text=word, font=("Calibri", 30))
WordImg.pack()
fake =["_"] * len(word)

WordImg.config(text=fake)
#combined commands
def a1():
    a()
    check()
    window.unbind("a")
def b1():
    b()
    check()
    window.unbind("b")
def c1():
    c()
    check()
    window.unbind("c")
def d1():
    d()
    check()
    window.unbind("d")
def e1():
    e()
    check()
    window.unbind("e")
def f1():
    f()
    check()
    window.unbind("f")
def g1():
    g()
    check()
    window.unbind("g")
def h1():
    h()
    check()
    window.unbind("h")
def i1():
    i()
    check()
    window.unbind("i")
def j1():
    j()
    check()
    window.unbind("j")
def k1():
    k()
    check()
    window.unbind("k")
def l1():
    l()
    check()
    window.unbind("l")
def m1():
    m()
    check()
    window.unbind("m")
def n1():
    n()
    check()
    window.unbind("n")
def o1():
    o()
    check()
    window.unbind("o")
def p1():
    p()
    check()
    window.unbind("p")
def q1():
    q()
    check()
    window.unbind("q")
def r1():
    r()
    check()
    window.unbind("r")
def s1():
    s()
    check()
    window.unbind("s")
def t1():
    t()
    check()
    window.unbind("t")
def u1():
    u()
    check()
    window.unbind("u")
def v1():
    v()
    check()
    window.unbind("v")
def w1():
    w()
    check()
    window.unbind("w")
def x1():
    x()
    check()
    window.unbind("x")
def y1():
    y()
    check()
    window.unbind("y")
def z1():
    z()
    check()
    window.unbind("z")
#BUTTTONNSSSS
A = ttk.Button(bFrame1, text='A', width=5, command=a1)
B = ttk.Button(bFrame1, text='B', width=5, command=b1)
C = ttk.Button(bFrame1, text='C', width=5, command=c1)
D = ttk.Button(bFrame1, text='D', width=5, command=d1)
E = ttk.Button(bFrame1, text='E', width=5, command=e1)
F = ttk.Button(bFrame1, text='F', width=5, command=f1)
G = ttk.Button(bFrame1, text='G', width=5, command=g1)
H = ttk.Button(bFrame1, text='H', width=5, command=h1)
I = ttk.Button(bFrame1, text='I', width=5, command=i1)
J = ttk.Button(bFrame1, text='J', width=5, command=j1)
K = ttk.Button(bFrame2, text='K', width=5, command=k1)
L = ttk.Button(bFrame2, text='L', width=5, command=l1)
M = ttk.Button(bFrame2, text='M', width=5, command=m1)
N = ttk.Button(bFrame2, text='N', width=5, command=n1)
O = ttk.Button(bFrame2, text='O', width=5, command=o1)
P = ttk.Button(bFrame2, text='P', width=5, command=p1)
Q = ttk.Button(bFrame2, text='Q', width=5, command=q1)
R = ttk.Button(bFrame2, text='R', width=5, command=r1)
S = ttk.Button(bFrame2, text='S', width=5, command=s1)
T = ttk.Button(bFrame3, text='T', width=5, command=t1)
U = ttk.Button(bFrame3, text='U', width=5, command=u1)
V = ttk.Button(bFrame3, text='V', width=5, command=v1)
W = ttk.Button(bFrame3, text='W', width=5, command=w1)
X = ttk.Button(bFrame3, text='X', width=5, command=x1)
Y = ttk.Button(bFrame3, text='Y', width=5, command=y1)
Z = ttk.Button(bFrame3, text='Z', width=5, command=z1)

PlayB = ttk.Button(PlayFrame,
                   text="Play Again?",
                   width=20,
                   command=again)

#BUTTTONNSSS PACKED
A.pack(side='left', padx=3, pady=3)
B.pack(side='left', padx=3, pady=3)
C.pack(side='left', padx=3, pady=3)
D.pack(side='left', padx=3, pady=3)
E.pack(side='left', padx=3, pady=3)
F.pack(side='left', padx=3, pady=3)
G.pack(side='left', padx=3, pady=3)
H.pack(side='left', padx=3, pady=3)
I.pack(side='left', padx=3, pady=3)
J.pack(side='left', padx=3, pady=3)
K.pack(side='left', padx=3, pady=3)
L.pack(side='left', padx=3, pady=3)
M.pack(side='left', padx=3, pady=3)
N.pack(side='left', padx=3, pady=3)
O.pack(side='left', padx=3, pady=3)
P.pack(side='left', padx=3, pady=3)
Q.pack(side='left', padx=3, pady=3)
R.pack(side='left', padx=3, pady=3)
S.pack(side='left', padx=3, pady=3)
T.pack(side='left', padx=3, pady=3)
U.pack(side='left', padx=3, pady=3)
V.pack(side='left', padx=3, pady=3)
W.pack(side='left', padx=3, pady=3)
X.pack(side='left', padx=3, pady=3)
Y.pack(side='left', padx=3, pady=3)
Z.pack(side='left', padx=3, pady=3)
#Button Bindings
window.bind("a", lambda event: a1())
window.bind("b", lambda event: b1())
window.bind("c", lambda event: c1())
window.bind("d", lambda event: d1())
window.bind("e", lambda event: e1())
window.bind("f", lambda event: f1())
window.bind("g", lambda event: g1())
window.bind("h", lambda event: h1())
window.bind("i", lambda event: i1())
window.bind("j", lambda event: j1())
window.bind("k", lambda event: k1())
window.bind("l", lambda event: l1())
window.bind("m", lambda event: m1())
window.bind("n", lambda event: n1())
window.bind("o", lambda event: o1())
window.bind("p", lambda event: p1())
window.bind("q", lambda event: q1())
window.bind("r", lambda event: r1())
window.bind("s", lambda event: s1())
window.bind("t", lambda event: t1())
window.bind("u", lambda event: u1())
window.bind("v", lambda event: v1())
window.bind("w", lambda event: w1())
window.bind("x", lambda event: x1())
window.bind("y", lambda event: y1())
window.bind("z", lambda event: z1())
window.bind("<space>", lambda event: again())
PlayB.pack(pady=5)
