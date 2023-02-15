from pyulog import *
import matplotlib.pyplot as plt

def main():
    ulog = ULog("test.ulg")
    data = ulog.get_dataset('actuator_controls_0').data

    fig, ax = plt.subplots()

    # Loop to plot the data
    for i in range(len(data) - 2):
        label = 'control[' + str(i) + ']'
        ax.plot(data['timestamp'], data[label], label=label)

    ax.legend()

    return plt.show()


main()