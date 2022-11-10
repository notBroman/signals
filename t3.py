from scipy import signal, fft
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    freqs = [i/10 for i in range(1000000)]
    t = np.linspace(0, 1, 20000, endpoint=False)
    x = 2*np.sin(20*np.pi*t) +1.5* np.sin(2000*np.pi*t) - 3* np.cos(5000*np.pi*t)

    # design a  lowpass filter with cut-off freq at 2500 Hz
    lowpass = signal.lti([2500],[1,2500])
    w, mag, phase = signal.bode(lowpass, w=freqs)

    # get impulse response of the system
    b, a =signal.butter(1,2500,'lp',analog=False,output='ba',fs=20000.0)
    x_filtered = signal.lfilter(b,a,x,axis=0)

    # get the power of each freqs signal, before and after filtering
    f_raw, Pxx_den_raw = signal.periodogram(x, 20000)
    f_filt, Pxx_den_filt = signal.periodogram(x_filtered, 20000)

    # plot power per frequency
    plt.figure()
    ax1 = plt.subplot(211)
    plt.semilogx(f_raw,Pxx_den_raw, lw =1)
    plt.grid(which='both')
    plt.xlim([1, 4000])
    plt.ylabel('Power')
    plt.legend(['raw signal'])

    plt.subplot(212, sharex = ax1)
    plt.grid(which='both')
    plt.ylabel('Power')
    plt.xlabel('Frequency [Hz]')
    plt.semilogx(f_filt, Pxx_den_filt,'r',lw=1)
    plt.legend(['filtered signal'])

    plt.figure()
    sig = plt.plot(t, x, lw = 1 )
    sig_filtered = plt.plot(t, x_filtered, lw = 1)
    plt.xlabel('time [s]')
    plt.ylabel('Amplitude [1]')

    plt.legend(['x(t)','x(t) filtered'])

    # plot the amplitude resonse of the designed fiter
    plt.figure()
    ax1 = plt.subplot(211)
    plt.semilogx(w,mag,lw=1)
    plt.xlim([1,1000000])
    plt.grid(which='both')
    plt.ylabel('Amplitude [dB]')

    ax2 = plt.subplot(212, sharex = ax1)
    plt.semilogx(w,phase)
    plt.grid(which='both')
    plt.ylabel('Phase [deg]')
    plt.xlabel('w [Hz]')
    plt.show()
