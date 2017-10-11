# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 00:17:58 2017

@author: Simon Moe Sørensen
"""

from chemDef import *
from sympy import solve
from sympy import Symbol
from units import unit

#Defining our units
gram = unit('g')
mol = unit('mol')
molar = gram/mol
liter = unit("L")
temp = unit("K")
pres = unit("atm")

"""Actual code starts"""

print(
      """================================================================
      
      Welcome to the chemistry calculator 420
      It consists of spaghetti code and runs on dank memes
                  
================================================================""")

while True:
    print("")
    menu = displayMenu(["Calculate the molar mass","Use stoichiometry", "Use the ideal gas equation","Convert units","Quit"])
    
    if menu == 1:
        #User input
        print("")
        print("""
      Please use the following format for your molecule:
      CH3 | H2SO4 | Al2(SO4)3 
              """)
        molecule = inputStr("Please enter your molecule: ")
        
        #Backup of molecule variable
        moleculeBackup = molecule
        
        #Check for parantheses 
        parMolar = 0
        if molecule.find("(") != -1:
            parMolar = parantheses(molecule)[0]
        
            molecule = parantheses(molecule)[1]
        
        #Compute molarmass of molecule (dependent on the parantheses checks)
        molarmass = funcMolarMass(molecule)
        
        #If we found a parantheses, add the molar masses together
        if parMolar != 0:
            molarmass = molarmass+parMolar
        
        #Print molar mass
        if molarmass == 0:
            print("Sorry, the program could not read your molecule")
            print("")
        
        else:
            print("")
            print(" ".join(("The molarmass of",moleculeBackup,"is",str(molar(molarmass)))))
            print("")
    
    elif menu == 2:
        print(
              """
    Please enter the known values for: n = m/M
    where m is mass (in grams), n is the amount of moles and M is the molar mass

    Let the value you wish to solve be 0
    """)
        
        m = inputNumber("Please enter the mass (in grams): ")
        M = inputNumber("Please enter the molar mass: ")
        n = inputNumber("Please enter the amount of moles: ")
        print("")
        
        #Find our variable and solve
        if m == 0:
            #Solve for m
            m = Symbol('x')
            solution = solve(n*M-m,m)[0]
            
            #Print with units
            print("The solution for","m","is",gram(solution))
            
        elif M == 0:
            #Solve for M
            M = Symbol('x')
            solution = solve(m/n-M,M)[0]
            
            #Print with units
            print("The solution for","M", "is",molar(solution))
            
        elif n == 0:
            #Solve for n
            n = Symbol('x')
            solution = solve(m/M-n,n)[0]
            
            #Print in units
            print("The solution for","n", "is",mol(solution))
            
        print("")
        
    elif menu == 3:
        print(
              """
    Please enter the known values for: PV = nRT
    where P is pressure (in atm), V is the volume (in liters), 
    n is the amount of moles, 
    R is the ideal gas constant and T is temperature (in Kelvin)

    Let the value you wish to solve be 0
    """)       
    
        P = inputNumber("Please enter the pressure (in atm): ")
        V = inputNumber("Please enter the volume (in L): ")
        n = inputNumber("Please enter the amount of moles: ")
        T = inputNumber("Please enter the temperature (in Kelvin): ")
        R = 0.0820574587
        print("")
        
        if P == 0:
            #Solve for P
            P = Symbol("X")
            solution = solve((n*R*T)/V-P,P)[0]
            
            #Print with units
            print("The solution for","P","is",pres(solution))

        elif V == 0:
            #Solve for V
            V = Symbol("X")
            solution = solve((n*R*T)/P-V,V)[0]
            
            #Print with units
            print("The solution for","V","is",liter(solution))
        
        elif n == 0:
            #Solve for n
            n = Symbol("X")
            solution = solve((P*V)/(R*T)-n,n)[0]
            
            print("The solution for","n","is",mol(solution))
        
        elif T == 0:
            #Solve for T
            T = Symbol("X")
            solution = solve((P*V)/(n*R)-T,T)[0]
            
            #Print with units
            print("The solution for","T","is",temp(solution))
        
        print("")
        
    elif menu == 4:
        #Ask what units should be converted
        print("")
        while True:
            menu = displayMenu(["Temperature conversion","Pressure conversion","Volume conversion","Back"])
            
            if menu == 1:
                print("")
                print("Can convert between the following units: K, C, F")
                print("")
                T = inputNumber("Please enter the temperature-value: ")
                unitFrom = inputStr("Please enter the unit you convert from: ")
                unitTo = inputStr("Please enter the unit you convert to: ")
                
                tempConvert = (convertTemperature(T, unitFrom, unitTo))
                print("")
                print(str(T)+" "+unitFrom+" is "+str(tempConvert)+" "+unitTo)
                print("")
            
            elif menu == 2:
                print("")
                print("Can convert between the following units: Atm, Pa, Torr, Psi, Bar")
                print("")
                P = inputNumber("Please enter the pressure-value: ")
                unitFrom = inputStr("Please enter the unit you convert from: ")
                unitTo = inputStr("Please enter the unit you convert to: ")
                
                pressureConvert = (convertPressure(P, unitFrom, unitTo))
                print("")
                print(str(P)+" "+unitFrom+" is "+str(pressureConvert)+" "+unitTo)
                print("")
            
            elif menu == 3:
                print("")
                print("Can convert between the following units: L, cm3, m3")
                print("")
                V = inputNumber("Please enter the volume-value: ")
                unitFrom = inputStr("Please enter the unit you convert from: ")
                unitTo = inputStr("Please enter the unit you convert to: ")
                
                volumeConvert = (convertVolume(V, unitFrom, unitTo))
                print("")
                print(str(V)+" "+unitFrom+" is "+str(volumeConvert)+" "+unitTo)
                print("")
            
            elif menu == 4:
                break
        
    elif menu == 5:
        break