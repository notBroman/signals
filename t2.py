from scipy import signal
import matplotlib.pyplot as plt

# TO DO
# - create the DT systems automatically from the coeff_list
# - labels & legends in plot
# - plot certain frequency range

if __name__ == '__main__':
    gamma = 100;
    alpha = 0.2
    beta = 100
    freqs = [i/10 for i in range(1,1000000)]

    # continuous time transfer function
    sys = signal.lti([gamma], [1, alpha, beta])
    w, mag, phase = signal.bode(sys, w=freqs)

    #DT transfer function
    T_list = [0.01,0.001,0.0001]
    # create a list of lists with num, den in them
    coeff_list= list()
    for i in range(3):
        t = T_list[i]
        t2 = t*t
        coeff_list.append([[1*gamma*t2,2*gamma*t2,1*gamma*t2],[4+2*alpha*t+beta*t2,-8+2*beta*t2,4-2*alpha*t+beta*t2],t])
    print(coeff_list[0])

    DT_sys_1 = signal.dlti(coeff_list[0][0],coeff_list[0][1], dt = coeff_list[0][2])
    DT_w_1, DT_mag_1, DT_phase_1 = signal.dbode(DT_sys_1)
    dt_sys = signal.cont2discrete(sys,dt= 0.01)
    # print(dt_sys)

    DT_sys_2 = signal.dlti(coeff_list[1][0],coeff_list[1][1],dt = coeff_list[1][2])
    DT_w_2, DT_mag_2, DT_phase_2 = signal.dbode(DT_sys_2)

    DT_sys_3 = signal.dlti(coeff_list[2][0],coeff_list[2][1], dt = coeff_list[2][2])
    DT_w_3, DT_mag_3, DT_phase_3 = signal.dbode(DT_sys_3)


    print(DT_sys_1)
    print(DT_sys_2)
    print(DT_sys_3)

    f1 = plt.figure()
    plt.subplot(211)
    plt.semilogx(w, mag, lw = 1)    # Bode magnitude plot
    plt.semilogx(DT_w_1,DT_mag_1,lw = 1)
    plt.semilogx(DT_w_2,DT_mag_2,lw = 1)
    plt.semilogx(DT_w_3,DT_mag_3,lw = 1)
    plt.grid(visible = 'true',axis = 'both', which = 'both', linestyle='--', figure = f1)
    plt.xlabel("frequency [rad/s]")
    plt.ylabel("Magnitude [dB]")
    plt.subplot(212)
    plt.semilogx(w, phase, lw = 1)  # Bode phase plot
    plt.semilogx(DT_w_1,DT_phase_1, lw = 1)
    plt.semilogx(DT_w_2,DT_phase_2, lw = 1)
    plt.semilogx(DT_w_3,DT_phase_3, lw = 1)
    plt.ylabel("Phase [deg]")
    plt.grid(visible = 'true',axis = 'both', which = 'both', linestyle='--', figure = f1)
    plt.show()

    sys = sys.to_zpk()
