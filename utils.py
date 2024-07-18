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