import math
class Particle:
    "Class representing a genric partilce"
    def __init__(self,mass,charge,name,momentum=0.):
        """
        Arguments:
        mass:mass particle Mev/c^2
        charge: charge in electronvolt
        name: particle name
        momentum :
        """
        self.mass= mass
        self.charge= charge
        self.name= name
        self.momentum= momentum

    def print_info(self):
        """ Print particle info in a nice, formatted way"""
        message = 'Particle "{}": mass = {:.3f} MeV/c^2, charge = {} e, '\
                  'momentum = {:.3f} MeV/c'
        print(message.format(self.name, self.mass, self.charge, self.momentum))

    @property
    def energy(self):
        """partcile energy"""
        return math.sqrt(self.mass**2+self.momentum**2)

    @energy.setter
    def energy(self,energy):
        """Set particle energy"""
        if energy< self.mass:
            print('Cannot set the enrgy to a value lower than mass')
        else:
            self.momentum=math.sqrt(energy**2-self.mass**2)

proton=Particle(938.272, +1 ,'Proton')
print(proton.mass)

"""
muon=Particle(105.6,charge= -1,name= 'Muon')
print(muon.print_info())
print('Particle energy:{:.2f} MeV'.format(muon.energy))

muon.energy=200# fake attribute = Property
print('Particle energy:{:.2f} MeV'.format(muon.energy))
muon.momentum =10# real attribute
print('Particle momentum:{:.2f} '.format(muon.momentum))
"""



class Proton(Particle):
    """ Class describing a Proton"""

    NAME = 'Proton'
    MASS = 938.272 # MeV /c^2
    CHARGE = +1. # e

    def __init__(self, momentum=0.):
        "super() does not need self infact super()=siper(Proton,self) "
        #super().__init__(self.MASS, self.CHARGE,self.NAME, momentum)
        #super().__init__(938.272, +1 ,'Proton', momentum)
        Particle.__init__(self,self.MASS, self.CHARGE,self.NAME, momentum)




proton = Proton(momentum=200.)
#proton.print_info()
print(proton.mass)
