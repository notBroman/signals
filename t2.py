from scipy import signal
import matplotlib.pyplot as plt

if __name__ == '__main__':
    gamma = 100;
    alpha = 0.2
    beta = 100

    # continuous time transfer function
    sys = signal.TransferFunction([gamma], [1, alpha, beta])
    w, mag, phase = signal.bode(sys)

    #DT transfer function
    T_list = [0.01,0.001,0.0001]
    # create a list of lists with num, den in them
    coeff_list= list()
    for i in range(3):
        t2 = T_list[i]**2
        t = T_list[i]
        coeff_list.append([[1*100*t2,2*100*t2,1*100*t2],[4+0.4*t+100*t2,-8+200*t2,4-0.4*t+100*t2],t])

    DT_sys_1 = signal.dlti([coeff_list[0][0][0],coeff_list[0][0][1],coeff_list[0][0][2]],
                           [coeff_list[0][1][0],coeff_list[0][1][1], coeff_list[0][1][2]],
                           dt = coeff_list[0][2])
    DT_w_1, DT_mag_1, DT_phase_1 = signal.dbode(DT_sys_1)

    plt.figure()
    plt.semilogx(w, mag)    # Bode magnitude plot
    plt.semilogx(DT_w_1,DT_mag_1)
    plt.grid()
    plt.xlabel("frequency [rad/s]")
    plt.ylabel("Magnitude [dB]")
    plt.figure()
    plt.semilogx(w, phase)  # Bode phase plot
    plt.semilogx(DT_w_1,DT_phase_1)
    plt.grid()
    plt.show()

    sys = sys.to_zpk()
