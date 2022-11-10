class Faculdade:

    def __init__(self, nome, curso):
        self._nome = nome
        self._curso = curso

    def get_curso(self):
        print("A pessoa {} faz faculdade de {}".format(self._nome, self._curso))


f = Faculdade('João', "Eng. Eletrônica")
f.get_curso()
f = Faculdade("Pedro", "Administração")
f.get_curso()
f = Faculdade("Silvia", "Arquitetura")
f.get_curso()
