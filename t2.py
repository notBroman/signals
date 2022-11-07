from scipy import signal
import matplotlib.pyplot as plt

if __name__ == '__main__':
    gamma = 100;
    alpha = 0.2
    beta = 100

    sys = signal.TransferFunction([gamma], [1, alpha, beta])
    w, mag, phase = signal.bode(sys,n=1000000)

    plt.figure()
    plt.semilogx(w, mag)    # Bode magnitude plot
    plt.grid()
    plt.xlabel("frequency [rad/s]")
    plt.ylabel("Magnitude [dB]")
    plt.figure()
    plt.semilogx(w, phase)  # Bode phase plot
    plt.grid()
    plt.show()

    sys = sys.to_zpk()
    print(sys)
