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
    sys = signal.lti([0,0,gamma], [1, alpha, beta])
    w, mag, phase = signal.bode(sys, w=freqs)

    #DT transfer function
    T_list = [0.01,0.001,0.0001]
    # create a list of lists with num, den in them
    coeff_list= list()
    #for i in range(3):
    #    t = T_list[i]
    #    coeff_list.append([[1*gamma*t,0,0],[-alpha+beta*t,alpha-1,1],t])
    #print(coeff_list[0])

    #DT_sys_1 = signal.dlti(coeff_list[0][0],coeff_list[0][1], dt = coeff_list[0][2])
    #DT_w_1, DT_mag_1, DT_phase_1 = signal.dbode(DT_sys_1)
    dt_sys = sys.to_discrete(dt=0.01,method='impulse')
    dt_w, dt_mag, dt_phase = signal.dbode(dt_sys,n=20000000)
    print(dt_sys)

    dt_sys_2 = sys.to_discrete(dt=0.001, method='impulse')
    dt_w2, dt_mag2, dt_phase2 = signal.dbode(dt_sys_2,n=2000000)

    print(dt_sys_2)
    dt_sys_3 = sys.to_discrete(dt=0.0001, method='impulse')
    dt_w3, dt_mag3, dt_phase3 = signal.dbode(dt_sys_3,n=2000000)

    print(dt_sys_3)
    #DT_sys_2 = signal.dlti(coeff_list[1][0],coeff_list[1][1],dt = coeff_list[1][2])
    #DT_w_2, DT_mag_2, DT_phase_2 = signal.dbode(DT_sys_2)

    #DT_sys_3 = signal.dlti(coeff_list[2][0],coeff_list[2][1], dt = coeff_list[2][2])
    #DT_w_3, DT_mag_3, DT_phase_3 = signal.dbode(DT_sys_3, w =freqs)


    #print(DT_sys_1)
    #print(DT_sys_2)
    #print(DT_sys_3)

    f1 = plt.figure()
    ax1 =plt.subplot(211)
    plt.semilogx(w, mag, lw = 1)    # Bode magnitude plot
    plt.semilogx(dt_w,dt_mag,lw = 1)
    plt.semilogx(dt_w2,dt_mag2,lw = 1)
    plt.semilogx(dt_w3,dt_mag3,lw = 1)
    plt.grid(visible = 'true',axis = 'both', which = 'both', linestyle='--', figure = f1)
    plt.ylabel("Magnitude [dB]")
    ax2 = plt.subplot(212, sharex=ax1)
    plt.semilogx(w, phase, lw = 1)  # Bode phase plot
    plt.semilogx(dt_w,dt_phase, lw = 1)
    plt.semilogx(dt_w2,dt_phase2, lw = 1)
    plt.semilogx(dt_w3,dt_phase3, lw = 1)
    plt.ylabel("Phase [deg]")
    plt.grid(visible = 'true',axis = 'both', which = 'both', linestyle='--', figure = f1)
    plt.legend(['CT','T=0.01','T=0.001','T=0.0001'])
    plt.xlabel("frequency [Hz]")
    plt.xlim([0.1,1000000])
    plt.show()

    sys = sys.to_zpk()
