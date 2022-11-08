from scipy import signal, fft
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    t = np.linspace(0, 1, 20000, endpoint=False)
    x = 2*np.sin(20*np.pi*t) +1.5* np.sin(2000*np.pi*t) - 3* np.cos(5000*np.pi*t)

    # design a  lowpass filter with cut-off freq at 2500 Hz
    lowpass = signal.lti([2500],[1,2500])
    w, mag, phase = signal.bode(lowpass)

    # get impulse response of the system
    b, a =signal.butter(1,2500,'lp',analog=False,output='ba',fs=20000.0)
    x_filtered = signal.lfilter(b,a,x,axis=0)

    # get the power of each freqs signal, before and after filtering
    f_raw, Pxx_den_raw = signal.periodogram(x, 20000)
    f_filt, Pxx_den_filt = signal.periodogram(x_filtered, 20000)

    # plot power per frequency
    plt.figure()
    plt.subplot(211)
    plt.plot(f_raw,Pxx_den_raw)
    plt.xlim([0, 4000])
    plt.subplot(212)
    plt.plot(f_filt, Pxx_den_filt)
    plt.xlim([0, 4000])

    plt.figure()
    plt.plot(t, x)
    plt.plot(t, x_filtered)

    # plot the amplitude resonse of the designed fiter
    plt.figure()
    plt.semilogx(w,mag,lw=1)
    plt.grid(which='both')
    plt.show()
