import os
import numpy as np

def import_ave_time(filename, folder=None):
    assert filename[:6] == "output"
    if folder is None:
        if os.path.exists(filename):
            data = np.loadtxt(filename)
            try:
                time, data = data.T
            except:
                time, data, _ = data.T
            if os.path.exists("data_plot/") is False:
                os.mkdir("data_plot/")
            np.savetxt("data_plot/"+filename[7:], np.vstack([time, data]).T)
        else:
            time, data = np.loadtxt("data_plot/"+filename[7:]).T
    else:
        if os.path.exists(folder+filename):
            data = np.loadtxt(folder+filename)
            try:
                time, data = data.T
            except:
                time, data, _ = data.T
            if os.path.exists("data_plot/") is False:
                os.mkdir("data_plot/")
            np.savetxt("data_plot/"+filename[7:], np.vstack([time, data]).T)
    return time, data

def random_lin_generator(xmin=0, xmax=10, slope=0.3, alpha=0.1, pref = 1, N = 50):
    x = np.linspace(xmin, xmax, N)
    y = slope*x + pref * (np.random.random(len(x))-0.5)*x**alpha
    return x, y

def random_log_generator(xmin=0, xmax=10, slope=0.3, alpha=0.1, pref = 1, N = 50):
    x = np.logspace(xmin, xmax, N)
    y = slope*x + pref * (np.random.random(len(x))-0.5)*x**alpha
    return x, y