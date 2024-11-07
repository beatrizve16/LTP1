from motor import Motor
from pneu import Pneu

class Veiculo(Motor, Pneu):
    def status(self):
        return f"{Motor.status(self)} e {Pneu.status(self)}"
