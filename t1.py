from scipy import signal
import matplotlib.pyplot as plt


if __name__ == '__main__':
    R = 80
    C = 280 *10^(-5)
    L1 = 0.01
    L2 = 0.02
    sys = signal.lti([C*L1,0,0],[C*L1*L2,C*R*L1, (L1+L2), R])
    w, mag, phase = signal.bode(sys)

    sys = sys.to_zpk()
    zeros = sys.zeros
    poles = sys.poles


    plt.figure()
    plt.scatter(zeros.real, zeros.imag, marker = 'o')
    plt.scatter(poles.real, poles.imag, marker = 'x')
    plt.grid('--')
    plt.show()
