class Gato:
    def __init__(self, tudo):
        self.tudo = tudo

    def __repr__(self):
        return f"{self.nome};{self.idade} ;{self.cor}"
        
    @staticmethod
    def from_string(task_str):
        return Gato(task_str)