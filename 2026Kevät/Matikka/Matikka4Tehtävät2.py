import numpy as np
import matplotlib.pyplot as plt
#Kpl 5.3, teht. 8 s. 96: Piirrä funktion kuvaaja.
def tehtone():
    x =np.linspace(-5, -3, 100)
    y = (0*x)+4
    x2=np.linspace(-3, -1, 100)
    y2= (-2*x2)-2
    x3=np.linspace(-1, 1, 100)
    y3= (0*x3)+4
    x4=np.linspace(1, 3, 100)
    y4= (-2*x4)+6
    x5=np.linspace(3, 5, 100)
    y5= (0*x5)+4
    x6=np.linspace(5, 7, 100)
    y6= (-2*x6)+14

    ax = plt.subplot()

    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_aspect('auto')
    ax.set_ylim([0, 4])
    plt.plot(x, y, color='blue')
    plt.plot(x2, y2, color='blue')
    plt.plot(x3, y3, color='blue')
    plt.plot(x4, y4, color='blue')
    plt.plot(x5, y5, color='blue')
    plt.plot(x6, y6, color='blue')
    plt.show()

#Samoin tehtävässä 9
def tehttwo():
    x =np.linspace(-4, 0, 100)
    y = (0.6*x)+3
    x2=np.linspace(0, 4, 100)
    y2= (0*x2)+3
    x3=np.linspace(4, 8, 100)
    y3= (-0.75*x3)+6
    x4=np.linspace(8, 10, 100)
    y4= (0.5*x4)-4

    ax = plt.subplot()

    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_aspect('auto')
    ax.set_ylim([0, 3])
    plt.plot(x, y, color='blue')
    plt.plot(x2, y2, color='blue')
    plt.plot(x3, y3, color='blue')
    plt.plot(x4, y4, color='blue')
    plt.show()

#Kpl 5.4 s 100: Tehtävästä 1 taitanee riittää kuvaajat kohdista a ja b
def tehtthr():
    x =np.linspace(-5, 15, 100)
    y = (x*x)-(4*x)+3
    x2=np.linspace(-5, 15, 100)
    y2= (2*(x2*x2))-(40*x2)+200

    ax = plt.subplot()

    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_aspect('auto')
    ax.set_ylim([-5, 25])
    plt.plot(x, y, color='blue')
    plt.plot(x2, y2, color='blue')
    plt.show()

#Ja lopuksi tehtävän 4 lentorataa kuvaava paraabeli
def tehtfou():
    x =np.linspace(-5, 100, 100)
    y = (-0.0063*(x*x))+(0.55*x)

    ax = plt.subplot()

    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_aspect('auto')
    ax.set_ylim([-5, 25])
    plt.plot(x, y, color='blue')
    plt.show()

inp = input()
if inp == "1":
    tehtone()
if inp == "2":
    tehttwo()
if inp == "3":
    tehtthr()
if inp == "4":
    tehtfou()