num0=float(input('Anna leiviskät.'))
num1=float(input('Anna naulat.'))
num2=float(input('Anna luodit.'))
g=(num2+((num1+(num0*20))*32))*13.3
resultKilogrammat=int(g/1000)
resultGrammat=g-(resultKilogrammat*1000)
print(f"{resultKilogrammat} kilogrammaa ja {resultGrammat} grammaa")