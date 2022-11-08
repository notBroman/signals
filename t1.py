from scipy import signal
import matplotlib.pyplot as plt


if __name__ == '__main__':
    R = 80
    C = 280 *10^(-5)
    L1 = 0.01
    L2 = 0.02
    sys = signal.lti([(L1+L2)/R,1],[L2*(L1+L2)/R,C*L1*L2+L1+L2,C*L1*R+L2*(L1+L2)/R,2*L1+L2,R])
    w, mag, phase = signal.bode(sys)

    plt.figure()
    plt.semilogx(w, mag)
    plt.show()
