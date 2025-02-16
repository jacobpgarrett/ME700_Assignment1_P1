import numpy as np
import sympy as sp
import matplotlib.pyplot as mpl

def check_epsilon(epsilon):
    if not isinstance(epsilon, np.ndarray):
        raise ValueError('Epsilon must be an array')

def zero_state(epsilon):
    if not epsilon[0] == 0:
        raise ValueError('The initial strain must be 0')

def isotropic(epsilon, E, H, Y0):

    '''

    This function computes the isotropic stress-strain behavior of a linear element
    with isotropic hardening.  It returns the stress as a function of strain.

    Inputs:
    epsilon: strain
    E: Young's modulus
    H: hardening modulus
    Y0: initial yield stress
    
    Output:
    sig: stress

    '''
    
    #


    # Define initial state
    sig = np.zeros(len(epsilon)) # Initialize stress vector
    Y = Y0 # Initial yield stress
    epsilon_p = np.zeros(len(epsilon)) # Initialize plastic strain vector

    # Loop through each strain increment
    for i in range(1, len(epsilon)):
        Y = Y0+H*epsilon_p[i-1] # Updated yield stress

        # Elastic Predictor Step
        del_sig_trial = E*(epsilon[i]-epsilon[i-1]) # Test change in stress assuming elastic
        sig_trial = sig[i-1]+del_sig_trial # Stress after strain increment
        state = float(abs(sig_trial)-Y) # Check if over or under yield
        
        if state <= 0: # elastic
            sig[i] = sig_trial # Stress is equal to trial stress
            epsilon_p[i] = epsilon_p[i-1]
        else: # plastic
            del_epsilon_p = state/(E+H) # Plastic strain increment
            sig[i] = sig_trial - np.sign(sig_trial)*E*del_epsilon_p # Stress after plastic strain
            epsilon_p[i] = epsilon_p[i-1]+del_epsilon_p # Total plastic strain
            
    
    return sig # Returns stress vector

def kinematic(epsilon, E, H, Y0):
    '''

    This function computes the kinematic stress-strain behavior of a linear element
    with kinematic hardening.  It returns the stress as a function of strain.

    Inputs:
    epsilon: strain
    E: Young's modulus
    H: hardening modulus
    Y0: initial yield stress

    Output:
    sig: stress

    '''

    # Define initial state of 0
    sig = np.zeros(len(epsilon)) # Initialize stress vector
    alpha = np.zeros(len(epsilon)) # Initialize back stress vector
    epsilon_p = np.zeros(len(epsilon)) # Initialize plastic strain vector

    for i in range(1, len(epsilon)):

        # Elastic Predictor Step
        sig_trial = sig[i-1] + E*(epsilon[i]-epsilon[i-1])
        alpha_trial = alpha[i-1]
        eta_trial = sig_trial-alpha_trial
        state = float(abs(eta_trial)-Y0)
        
        if state <= 0: # elastic
            sig[i] = sig_trial
            alpha[i] = alpha_trial
            epsilon_p[i] = epsilon_p[i-1]
        else: # plastic
            del_epsilon_p = state/(E+H)
            sig[i] = sig_trial-np.sign(eta_trial)*E*del_epsilon_p
            alpha[i] = alpha[i-1]+np.sign(eta_trial)*H*del_epsilon_p
            epsilon_p[i] = epsilon_p[i] + del_epsilon_p

    return sig

def stress_behavior(epsilon, E, H, Y0):
    '''
    This function takes strain and material properties as inputs and plots the stress-strain behavior of the material.
    It will plot and return the stress behavior for different types of hardening models (isotropic and kinematic).

    Inputs:
    epsilon: strain
    E: Young's modulus
    H: hardening modulus
    Y0: initial yield stress

    Output:
    stress_isotropic: stress-strain behavior for isotropic hardening
    stress_kinematic: stress-strain behavior for kinematic hardening
    '''

    mpl.close() # Closes open MatPlotLib windows

    check_epsilon(epsilon)

    zero_state(epsilon)

    stress_isotropic = isotropic(epsilon, E, H, Y0) # Computes stress for given strains using isotropic hardening
    stress_kinematic = kinematic(epsilon, E, H, Y0) # Computes stress for given strains using kinematic hardening

    # Plots stress-strain curves
    mpl.plot(epsilon, stress_isotropic, label='Isotropic')
    mpl.plot(epsilon, stress_kinematic, label='Kinematic')
    mpl.xlabel('Strain')
    mpl.ylabel('Stress')
    mpl.legend()
    mpl.show()
    mpl.title('Stress vs. Strain Behavior for different types of hardening')

    return stress_isotropic, stress_kinematic
