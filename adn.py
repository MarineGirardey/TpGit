#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    documentation here
"""
__author__ = 'Marine Girardey'

# Imports
import re

adn_str="atctgg"

# Test if DNA chain is valid
def is_valid(adn_str):
    if bool(re.search("[zeryuiopqsdfhjklmwxvbn]", adn_str)):
        return(True)
    else:
        return(False)

# Ask for a valid DNA chain if it's not
def get_valid_adn(prompt='chaîne : '):
    adn_input = input(prompt)
    print(adn_input)
    while is_valid(adn_input):
        print("Veuillez entrer une chaîne d'ADN valide")
        adn_input = input(prompt)