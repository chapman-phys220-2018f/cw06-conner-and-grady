#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####
# Conner Carnahan and Grady
# Email: carna104@mail.chapman.edu
# Elementary module for CW 5
# PHYS 220
# Septemeber 27, 2018
####

import scipy.constants

class Particle(object):
    """Particle is a class that should have 3 initialized variables: Mass(a float), Position(A triplet of floats), Momentum(A triplet of floats)"""
    mass = 0.0
    position = (0.0,0.0,0.0)
    momentum = (0.0,0.0,0.0)
    def __init__(self, x, y, z):
        """Inits the class, arg1: x position float, arg2: y position float, arg3: z positionfloat"""
        self.position = (x, y, z)
        self.mass = 1.0
        self.momentum = (0.0,0.0,0.0)

    def impulse(self, px,py,pz):
        """changes the momentum by an increment arg1: px, arg2: py, arg3: pz"""
        self.momentum = (self.momentum[0]+px,self.momentum[1]+py,self.momentum[2]+pz)

    def move(self, dt):
        """Moves the particle by a specified amount of time, it is calculated by taking the momentum of the particle and calculating the velocity
        times arg1: dt"""
        self.position = (self.position[0] + (dt/self.mass)*self.momentum[0],self.position[1]+(dt/self.mass)*self.momentum[1],self.position[2]+(dt/self.mass)*self.momentum[2])

class ChargedParticle(Particle):
    charge = 0.0

    def __init__(self, x, y, z):
        """uses the super constructor to construct the class instance
        arg1: x pos (float)
        arg2: y pos (float)
        arg3: z pos (float)
        sets the charge by default to 0"""
        super(Particle,self).__init__(x, y, z)
        self.charge = 0.0
    
class Electron(ChargedParticle):
    """Electron is a subclass of chargedparticle. All instances of electron have a charge of -1.60217662e-19 coulombs and a mass of 9.10938356e-31 kilograms."""    
    
    def __init__(self, x, y, z):
        super(ChargedParticle,self).__init__(x, y, z)
        self.charge = -scipy.constants.e
        self.mass = scipy.constants.m_e
    
class Proton(ChargedParticle):
    """Proton is a subclass of chargedparticle. All instances of proton have a charge of 1.60217662e-19 coulombs and a mass of 1.6726219e-27 kilograms."""
    
    def __init__(self, x, y, z):
        super(ChargedParticle,self).__init__(x, y, z)
        self.charge = scipy.constants.e
        self.mass = scipy.constants.m_p
    
def main(argv):
    pass


