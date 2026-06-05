#HANGMAN
import ttkbootstrap as ttk
import random
import tkinter.messagebox as mbox

window = ttk.Window(themename = 'journal')
window.title("HANGMAN")
#LOGIC

def a():
    guesses = 8
    if "a" in word:
        a
    if "a" not in word:
        guesses -= 1
        HangImage.config(image)
    A.config(state='disabled')
    
def b():
    if "b" in word:
        print("b")
    B.config(state='disabled')
    
def c():
    if "c" in word:
        c = word.count("c")
        letter = word.find("c")
        letter2 = word.rfind("c")
        wordImg.config(
    C.config(state='disabled')
    
def d():
    if "d" in word:
        print("d")
    D.config(state='disabled')
def e():
    if "e" in word:
        print("e")
    E.config(state='disabled')
def f():
    if "f" in word:
        print("f")
    F.config(state='disabled')
def g():
    if "g" in word:
        print("g")
    G.config(state='disabled')
def h():
    if "h" in word:
        print("h")
    H.config(state='disabled')
def i():
    if "i" in word:
        print("i")
    I.config(state='disabled')
def j():
    if "j" in word:
        print("j")
    J.config(state='disabled')
def k():
    if "k" in word:
        print("k")
    K.config(state='disabled')
def l():
    if "l" in word:
        print("l")
    L.config(state='disabled')
def m():
    if "m" in word:
        print("m")
    M.config(state='disabled')
def n():
    if "n" in word:
        print("n")
    N.config(state='disabled')
def o():
    if "o" in word:
        print("o")
    O.config(state='disabled')
def p():
    if "p" in word:
        print("p")
    P.config(state='disabled')
def q():
    if "q" in word:
        print("q")
    Q.config(state='disabled')
def r():
    if "r" in word:
        print("r")
    R.config(state='disabled')
def s():
    if "s" in word:
        print("s")
    S.config(state='disabled')
def t():
    if "t" in word:
        print("t")
    T.config(state='disabled')
def u():
    if "u" in word:
        print("u")
    U.config(state='disabled')
def v():
    if "v" in word:
        print("v")
    V.config(state='disabled')
def w():
    if "w" in word:
        print("w")
    W.config(state='disabled')
def x():
    if "x" in word:
        print("x")
    X.config(state="disabled")
def y():
    if "y" in word:
        print("y")
    Y.config(state='disabled')
def z():
    if "z" in word:
        print("z")
    Z.config(state='disabled')
#Word List
List = ["cincaini"]
word = random.choice(List)
print(word)
#FRAMES
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
#HANGMAN IMAGE
hangbase = ttk.PhotoImage(file="hang2.png")
hang1 = ttk.PhotoImage(file="hang3.png")
hang2 = ttk.PhotoImage(file="hang4.png")
hang3 = ttk.PhotoImage(file="hang5.png")
hang4 = ttk.PhotoImage(file="hang6.png")
hang5 = ttk.PhotoImage(file="hang7.png")
hang6 = ttk.PhotoImage(file="hang8.png")
hangimages = [hangbase, hang1, hang2, hang3,
              hang4, hang5, hang6]
HangImage = ttk.Label(hFrame, image=hangbase)
HangImage.pack()
#HangMan Word
fakelen = len(word)
WordImg = ttk.Label(hFrame, text=word, font=("Calibri", 30))
WordImg.pack()
if fakelen == 4:
    WordImg.config(text="_ _ _ _")
if fakelen == 5:
    WordImg.config(text="_ _ _ _ _")
if fakelen == 6:
    WordImg.config(text="_ _ _ _ _ _")
if fakelen == 7:
    WordImg.config(text="_ _ _ _ _ _ _")
if fakelen == 8:
    WordImg.config(text="_ _ _ _ _ _ _ _")
if fakelen == 9:
    WordImg.config(text="_ _ _ _ _ _ _ _ _")
if fakelen == 10:
    WordImg.config(text="_ _ _ _ _ _ _ _ _ _")

#BUTTTONNSSSS
A = ttk.Button(bFrame1, text='A', width=5, command=a)
B = ttk.Button(bFrame1, text='B', width=5, command=b)
C = ttk.Button(bFrame1, text='C', width=5, command=c)
D = ttk.Button(bFrame1, text='D', width=5, command=d)
E = ttk.Button(bFrame1, text='E', width=5, command=e)
F = ttk.Button(bFrame1, text='F', width=5, command=f)
G = ttk.Button(bFrame1, text='G', width=5, command=g)
H = ttk.Button(bFrame1, text='H', width=5, command=h)
I = ttk.Button(bFrame1, text='I', width=5, command=i)
J = ttk.Button(bFrame1, text='J', width=5, command=j)
K = ttk.Button(bFrame2, text='K', width=5, command=k)
L = ttk.Button(bFrame2, text='L', width=5, command=l)
M = ttk.Button(bFrame2, text='M', width=5, command=m)
N = ttk.Button(bFrame2, text='N', width=5, command=n)
O = ttk.Button(bFrame2, text='O', width=5, command=o)
P = ttk.Button(bFrame2, text='P', width=5, command=p)
Q = ttk.Button(bFrame2, text='Q', width=5, command=q)
R = ttk.Button(bFrame2, text='R', width=5, command=r)
S = ttk.Button(bFrame2, text='S', width=5, command=s)
T = ttk.Button(bFrame3, text='T', width=5, command=t)
U = ttk.Button(bFrame3, text='U', width=5, command=u)
V = ttk.Button(bFrame3, text='V', width=5, command=v)
W = ttk.Button(bFrame3, text='W', width=5, command=w)
X = ttk.Button(bFrame3, text='X', width=5, command=x)
Y = ttk.Button(bFrame3, text='Y', width=5, command=y)
Z = ttk.Button(bFrame3, text='Z', width=5, command=z)

PlayB = ttk.Button(PlayFrame,
                   text="Play Again?",
                   width=20)

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

PlayB.pack(pady=5)


A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
Y
Z



     
