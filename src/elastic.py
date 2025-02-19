import numpy as np
import matplotlib.pyplot as mpl

# Define Material Model Class
class MaterialModel:
    def __init__(self, epsilon, E, H, Y0):
        self.epsilon = epsilon # Input strain
        self.E = E # Input Young's Modulus
        self.H = H # Input Hardness Modulus
        self.Y0 = Y0 # Input Yield Stress
        self.check_epsilon()
        self.zero_state()

    # Function to ensure that epsilon is a numpy array
    def check_epsilon(self):
        if not isinstance(self.epsilon, np.ndarray):
            raise ValueError("Epsilon must be an array")

    # Function to ensure that structure begins at 0 stress
    def zero_state(self):
        if not self.epsilon[0] == 0:
            raise ValueError("The initial strain must be 0")

    # Different hardening subclasses use different methods
    # def calculate_stress(self):
        # raise NotImplementedError("Subclasses should implement this method")

class IsotropicHardening(MaterialModel):
    def calculate_stress(self):

        # Initialize Data vectors
        sig = np.zeros(len(self.epsilon))
        Y = self.Y0
        epsilon_p = np.zeros(len(self.epsilon))

        for i in range(1, len(self.epsilon)):
            # Elastic Predictor Step
            Y = self.Y0 + self.H * epsilon_p[i - 1]
            del_sig_trial = self.E * (self.epsilon[i] - self.epsilon[i - 1])
            sig_trial = sig[i - 1] + del_sig_trial
            state = float(abs(sig_trial) - Y)

            if state <= 0:  # elastic
                sig[i] = sig_trial
                epsilon_p[i] = epsilon_p[i - 1]
            else:  # plastic
                del_epsilon_p = state / (self.E + self.H)
                sig[i] = sig_trial - np.sign(sig_trial) * self.E * del_epsilon_p
                epsilon_p[i] = epsilon_p[i - 1] + del_epsilon_p

        return sig

class KinematicHardening(MaterialModel):
    def calculate_stress(self):
        # Initialize Data Vectors
        sig = np.zeros(len(self.epsilon))
        alpha = np.zeros(len(self.epsilon))
        epsilon_p = np.zeros(len(self.epsilon))

        for i in range(1, len(self.epsilon)):
            # Elastic Predictor Step
            sig_trial = sig[i - 1] + self.E * (self.epsilon[i] - self.epsilon[i - 1])
            alpha_trial = alpha[i - 1]
            eta_trial = sig_trial - alpha_trial
            state = float(abs(eta_trial) - self.Y0)

            if state <= 0:  # elastic
                sig[i] = sig_trial
                alpha[i] = alpha_trial
                epsilon_p[i] = epsilon_p[i - 1]
            else:  # plastic
                del_epsilon_p = state / (self.E + self.H)
                sig[i] = sig_trial - np.sign(eta_trial) * self.E * del_epsilon_p
                alpha[i] = alpha[i - 1] + np.sign(eta_trial) * self.H * del_epsilon_p
                epsilon_p[i] += del_epsilon_p

        return sig

def stress_behavior(epsilon, E, H, Y0):
    # Creates instances of model classes
    iso_model = IsotropicHardening(epsilon, E, H, Y0)
    kin_model = KinematicHardening(epsilon, E, H, Y0)

    # Calculate stress states
    stress_isotropic = iso_model.calculate_stress()
    stress_kinematic = kin_model.calculate_stress()

    # Plots the stress strain behavior of the different stress models
    mpl.plot(epsilon, stress_isotropic, label='Isotropic')
    mpl.plot(epsilon, stress_kinematic, label='Kinematic')
    mpl.xlabel('Strain')
    mpl.ylabel('Stress')
    mpl.legend()
    mpl.title('Stress vs. Strain Behavior for different types of hardening')
    mpl.show()

    return stress_isotropic, stress_kinematic
