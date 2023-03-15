class Triangulo():
    def __init__(self,ladoa,ladob,ladoc):
        self.ladoa = ladoa
        self.ladob = ladob
        self.ladoc = ladoc

    def calcularPerimetro(self):
        calculo = self.ladoa + self.ladob + self.ladoc
        print (calculo)

    def maiorlado(self):
        self.ladoa
        self.ladob
        self.ladoc
        maiorlado = 0
        if self.ladoa > self.ladob or self.ladoa > self.ladoc:
            maiorlado = self.ladoa
        elif maiorlado < self.ladob:
            maiorlado = self.ladob
        elif maiorlado < self.ladoc:
            maiorlado = self.ladoc
        else:
            print('Os lados são iguais!')
        print(maiorlado)

Triangulo1 = Triangulo (100,150,300)

Triangulo1.calcularPerimetro()
Triangulo1.maiorlado()
