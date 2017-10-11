# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 21:43:36 2017

@author: Gregers
"""

#User inputs
import numpy as np
import pandas as pd

#Volume converter
def convertVolume(V,unitFrom, unitTo):
    L = ["Liter(s)","L"]
    cm3 = ["cm3","Cm3","cm^3","Cm^3"]
    m3 = ["m3","M3","m^3","M^3"]

    #Convert from Liter to cm3 or m3
    if unitFrom in L:
        if unitTo in cm3:
            V = V*1000
        if unitTo in m3:
            V = V/1000
    
    elif unitFrom in cm3:
        if unitTo in L:
            V = V/1000
        if unitTo in m3:
            V = V/1000000
    
    elif unitFrom in m3:
        if unitTo in L:
            V = V*1000
        if unitTo in cm3:
            V = V*1000000
    
    else:
        V=V
    
    return V
    
#Pressure converter
def convertPressure(P, unitFrom, unitTo):
    a = ["Atm","atm"]
    p = ["Pa","pa"]
    t = ["Torr","torr","mmHg"]
    psi = ["Psi","psi"]
    b = ["Bar","bar"]
    
    #Convert from Atm to Pa, Torr, Psi or Bar
    if unitFrom in a:
        if unitTo in p:
            P = P*101325
        if unitTo in t:
            P = P*760
        if unitTo in psi:
            P = P*14.695948775
        if unitTo in b:
            P = P*1.01325
    
    #Convert from Pa to Atm, Torr, Psi or Bar
    elif unitFrom in p:
        if unitTo in a:
            P = P*0.0000098692
        if unitTo in t:
            P = P*0.0075006168
        if unitTo in psi:
            P = P*0.0001450377
        if unitTo in b:
            P = P*0.00001
            
    #Convert from Torr to Atm, Pa, Psi or Bar
    elif unitFrom in t:
        if unitTo in a:
            P = P*0.0013157895
        if unitTo in p:
            P = P*133.32236842
        if unitTo in psi:
            P = P*0.0193367747
        if unitTo in b:
            P = P*0.0013332237
    
    #Convert from Psi to Atm, Pa, Torr or Bar
    elif unitFrom in psi:
        if unitTo in a:
            P = P*0.0680459639
        if unitTo in p:
            P = P*6894.7572932
        if unitTo in t:
            P = P*51.714932572
        if unitTo in b:
            P = P*0.0689475729
    
    #Convert from Bar to Atm, Pa, Torr or Psi
    elif unitFrom in b:
        if unitTo in a:
            P = P*0.9869232667
        if unitTo in p:
            P = P*100000
        if unitTo in t:
            P = P*750.0616827
        if unitTo in psi:
            P = P*14.503773773
    
    else:
        P = P
        
    return P

#Temperature converter
def convertTemperature(T, unitFrom, unitTo):
    K = ["Kelvin", "K"]
    C = ["Celsius", "C"]
    F = ["Fahrenheit", "F"]
    
    #Convert from Kelvin to C or F
    if unitFrom in K:
        if unitTo in C:
            T = T-273.15
        if unitTo in F:
            T = 1.8*T-459.67
    
    #Convert from C to K and F
    elif unitFrom in C:
        if unitTo in K:
            T = T + 273.15
        if unitTo in F:
            T = 1.8*T+32
    
    #Convert from F to K and C
    elif unitFrom in F:
        if unitTo in K:
            T = (T+459.67)/1.8
        if unitTo in C:
            T = (T-32)/1.8
    else:
        T = T
            
    return T

#Check for a parantheses
def parantheses(molecule):
    """
    Calculate the molar mass of the parantheses in a molecule, and also removes
    it and any index behind it
    
    Input = String, molecule with parantheses, ie: Al2(SO4)3
    Output = Int, molar mass of parantheses. String, molecule without parantheses
"""
    parantheses = molecule[molecule.find("(")+1:molecule.find(")")]

    #Molarmass of parantheses
    parMolar = funcMolarMass(parantheses)
    
    #Check for 2 index's behind the parantheses
    if molecule.find(")")+2 < len(molecule) and is_number(molecule[molecule.find(")")+1]) and is_number(molecule[molecule.find(")")+2]):
        index = int(molecule[molecule.find(")")+1]+molecule[molecule.find(")")+2])
    
        #Compute molarmass of parantheses
        parMolar = parMolar * index
        
        #Remove parantheses from molecule
        molecule = molecule.replace(molecule[molecule.find("("):molecule.find(")")+3],"")
        
    #Check for 1 index behind the parantheses
    elif molecule.find(")")+1 < len(molecule) and is_number(molecule[molecule.find(")")+1]):
        index = int(molecule[molecule.find(")")+1])
        
        #Compute molarmass of parantheses
        parMolar = parMolar * index
        
        #Remove parantheses from molecule
        molecule = molecule.replace(molecule[molecule.find("("):molecule.find(")")+2],"")
    return parMolar,molecule

#Check if number is present in string function
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#Function for molar mass 
def funcMolarMass(molecule):
    """
    Calculates the molar mass of a given molecule, without calculations of the parantheses
    
    Input = String, molecule in given form: CH3
    Output = Int, Molar mass of molecule
    """
    #Initial molarmass
    molarmass = 0
    
    #Read atoms
    atoms = pd.read_csv("Atoms.csv")
    
    #Check the molecule for atoms
    #We use i, to loop the molecule
    for i in range(len(molecule)):
        #Defining my array of atoms
        atomArray = np.reshape(np.array([atoms.iloc[:,1]]),-1)
     
        #Check for a 2 letter atom
        if i+1 < len(molecule) and molecule[i]+molecule[i+1] in atomArray:
            #If atom is found, define the spot
            spot = i
    
            #Check if we have an index of 2 digits
            if spot+3 < len(molecule) and is_number(molecule[spot+3]) and is_number(molecule[spot+2]):
                index = int(molecule[(spot+2)]+molecule[(spot+3)])
    
            #Check if we have an index of 1 digit
            elif spot+2 < len(molecule) and is_number(molecule[spot+2]):
                index = int(molecule[(spot+2)])  
                    
            #Else we have an index of 1
            else:
                index = 1
            
            #Get the atomix weight of the atom
            atomSpot = np.where(atomArray == molecule[i]+molecule[i+1])
            
            weight = float(atoms.iloc[int(atomSpot[0]),3])
    
            #Get the total weight of the molecule
            molarmass = (weight*index)+molarmass
        
        #Else check for a 1 letter atom
        elif i < len(molecule) and molecule[i] in atomArray:
            #If atom is found, define the spot
            spot = i
    
            #Check if we have index of 2 digits
            if spot+2 < len(molecule) and is_number(molecule[spot+2]) and is_number(molecule[spot+1]):
                index = int(molecule[(spot+1)]+molecule[(spot+2)])
            
            #Check if we have an index of 1 digit
            elif spot+1 < len(molecule) and is_number(molecule[spot+1]):
                    index = int(molecule[(spot+1)])  
                    
            #Else we have an index of 1       
            else:
                index = 1
            
            #Get the atomic weight of the atom
            atomSpot = np.where(atomArray == molecule[i])
            
            weight = float(atoms.iloc[int(atomSpot[0]),3])
    
            #Get the total weight of the molecule
            molarmass = (weight*index)+molarmass
    
        #End of for-loop i
    
    return molarmass

def displayMenu(options):
    """
    DISPLAYMENU Displays a menu of options, ask the user to choose an item
    and returns the number of the menu item chosen.
    
    Usage: choice = displayMenu(options)
    
    Input options Menu options (array of strings)
    Output choice Chosen option (integer)
    
    
    Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    """
    
    # Display menu options
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
        
    # Get a valid menu choice
    choice = 0
    
    while not(np.any(choice == np.arange(len(options))+1)):
       choice = inputNumber("Please choose a menu item: ")
       
    return choice

def inputNumber(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print("Not valid number. Please try again")
    return num

def inputStr(prompt):
    while True:
        try:
            str = input(prompt)
            break
        except ValueError:
            print("Not a valid string. Please try again")
    return str
