#!/usr/bin/python

###################################
# Name: Gas Mileage Calculator    #
# Company: Black Disc Software    #
# Writer: Sub-Lockdown            #
###################################

#Imports
import os
import json
from math import ceil

# Check to see if folder exists (aka if first start up or removes)
if not os.path.exists('Vehicles'):
    os.makedirs('Vehicles')

# Global Varibles
vehicle = {'Model' : 'Type', 'Reg_MPG' : 0, 'High_MPG' : 0, 'Tank_Size' : 0}
path = os.getcwd() + '/Vehicles'
os.chdir(path)

# The main menu
def start():
    while True:
        global vehicle
        print ("""
        Welcome to the Gas Mileage Calculator
        Please select an option:
        1) Add New Vehicle (NEWV)
        2) Delete Old Vehicle (DELV)
        3) Edit Old Vehicle (EDIT)
        4) Calculate Mileage (CALC)
        5) Exit (EXIT)
        """)
        ans = raw_input('Input Code: ').upper()
        if ans == 'NEWV':
            new_vehicle()
        elif ans == 'DELV':
            delete_vehicle()
        elif ans == 'EDIT':
            edit_vehicle()
        elif ans == 'CALC':
            calculator()
        elif ans == 'EXIT':    
            quit()
        else:
            print "\nUnvalid Choice"

# Creates a vehicle dictionary, along with saving it to a file        
def new_vehicle():
    global vehicle
    while True:
        print "Please enter your vehicle data. (hit ENTER to go back)\n"
        vehicle['Model'] = raw_input('Vehicle Type: ').upper()
        if vehicle['Model'] == '':
            break
        elif os.path.exists(vehicle['Model']):
            print '\n Vehicle already on file \n'
            continue
        vehicle['Reg_MPG'] = float(raw_input('Regular Gas Mileage: '))
        vehicle['High_MPG'] = float(raw_input('Highway Gas Mileage: '))
        vehicle['Tank_Size'] = float(raw_input('Gas Tank Size: '))
        print ("""
        Model: %s
        Regular Gas Mileage: %s
        Highway Gas Mileage: %s
        Gas Tank Size: %s
        """) % (vehicle['Model'], vehicle['Reg_MPG'], vehicle['High_MPG'], vehicle['Tank_Size'])
        ans = raw_input("Is this correct <Y/N>:").upper()
        if ans == 'Y':
            print "Yes"
            with open(vehicle['Model'], 'wb') as fp:
                json.dump(vehicle, fp)
            break
        else:
            print "\n Please Correct \n"

# Deletes a vehicle dictionary file
def delete_vehicle():
    while True:
        print os.listdir(path)
        print "\n Please enter your vehicle data. (hit ENTER to go back) \n"
        delete = raw_input('Delete: ').upper()
        if delete == '':
            break
        elif not os.path.exists(delete):
            print '\n Vehicle not on file \n'
            continue
        print delete
        sure = raw_input('Are you sure you want to delete %s <Y/N>: ' %delete).upper()
        if sure == 'Y':
            print delete
            os.remove(delete)
            break
        else:
            break

# Edits a vehicle dictionary file
def edit_vehicle():
    global vehicle
    load_vehicle()
    if vehicle == '':
        return
    while True:
        print "Please enter your new vehicle data.\n"
        vehicle['Model'] = raw_input('Vehicle Type <Currently: %s>: ' % vehicle['Model']).upper()
        vehicle['Reg_MPG'] = float(raw_input('Regular Gas Mileage <Currently: %s>: ' % vehicle['Reg_MPG']))
        vehicle['High_MPG'] = float(raw_input('Highway Gas Mileage <Currently: %s>: ' % vehicle['High_MPG']))
        vehicle['Tank_Size'] = float(raw_input('Gas Tank Size <Currently: %s>: ' % vehicle['Tank_Size']))
        print ("""
        Model: %s
        Regular Gas Mileage: %s
        Highway Gas Mileage: %s
        Gas Tank Size: %s
        """) % (vehicle['Model'], vehicle['Reg_MPG'], vehicle['High_MPG'], vehicle['Tank_Size'])
        ans = raw_input("Is this correct <Y/N>:").upper()
        if ans == 'Y':
            print "Yes"
            with open(vehicle['Model'], 'wb') as fp:
                json.dump(vehicle, fp)
            break
        else:
            print "\n Please Correct \n"

# Using simple math, calculates optimal gas usage, 
def calculator():
    global vehicle
    load_vehicle()
    if vehicle == '':
        return
    miles = float(raw_input("How Far Are you traveling? "))
    min_gallons = miles/vehicle['High_MPG']
    min_gal_stop = min_gallons/vehicle['Tank_Size']
    if min_gal_stop < 1.0:
        min_gal_stop = 0.0
    else:
        min_gal_stop = ceil(min_gal_stop)
    max_gallons = miles/vehicle['Reg_MPG']
    max_gal_stop = max_gallons/vehicle['Tank_Size']
    if max_gal_stop < 1.0:
        max_gal_stop = 0.0
    else:
        max_gal_stop = ceil(max_gal_stop)
    print ("""
    You will use between:
    Optimal Gas Usage- %s gallons With %s stops
    Maximum  Gas Usage- %s gallons With %s stops
    """) % (min_gallons, min_gal_stop, max_gallons, max_gal_stop)

#Loads a vehicle dictionary from file, to be used with edit_vehicle and calculator functions
def load_vehicle():
    global vehicle
    ans=True
    while ans:
        print os.listdir(path)
        print "\n Please enter your vehicle data. (hit ENTER to go back) \n"
        vehicle = raw_input('Load: ').upper()
        if vehicle == '':
            return vehicle
        elif os.path.exists(vehicle):
            vehicle = json.loads(open(vehicle).read())
            return vehicle
        else:
            print "\n Vehicle does not exist \n"

start()
