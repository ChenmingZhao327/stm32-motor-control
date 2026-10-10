import serial
import matplotlib.pyplot as plt
ser = serial.Serial("COM5", 115200, timeout=1)
rpm_history = []
target_history = []
time_history = []

plt.ion()  
fig, ax = plt.subplots()
ax.set_xlabel('Time (s)')
ax.set_ylabel('RPM')
ax.set_title('RPM vs Target RPM')
rpm_line, = ax.plot(time_history, rpm_history, label='RPM')
target_line, = ax.plot(time_history, target_history, label='Target RPM')
ax.legend()
plt.show()

while 1:
    data = ser.readline()
    if data:
        line = (data.decode('utf-8').rstrip())
        if line == "START":
            rpm_history.clear()
            target_history.clear()
            time_history.clear()
            continue
        try:
            target,rpm,duty = map(float,line.split(','))
        except ValueError:
            continue
        print(target,rpm,duty)
        rpm_history.append(rpm)
        target_history.append(target)
        time_history.append(len(rpm_history) * 0.1)
        rpm_line.set_data(time_history, rpm_history)
        target_line.set_data(time_history, target_history)

        ax.relim()
        ax.autoscale_view()
        plt.pause(0.01)

        

        