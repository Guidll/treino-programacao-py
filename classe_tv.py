class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def power(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True

    def sobe_canal(self):
        self.canal += 1

    def desce_canal(self):
        self.canal -= 1

if __name__ == '__main__': #chamada do proprio arquivo
    televisao = Televisao()
    print('TV está ligada? ',televisao.ligada)
    televisao.power()
    print('TV está ligada? ',televisao.ligada)

    print('No canal: ',televisao.canal)
    televisao.sobe_canal()
    print('No canal: ',televisao.canal)

    televisao.power()
    print('TV está ligada? ',televisao.ligada)