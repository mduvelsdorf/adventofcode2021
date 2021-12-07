import os

cwd = os.getcwd()
file = open(cwd+"\D1_data")
measurements = []
for line in file:
    measurements.append(int(line.replace("\n","")))
def single_measurement():
    increases = 0
    for i in range(1,len(measurements)):
        if measurements[i] > measurements[i - 1]:
            increases += 1
    return increases

def three_measurement():
    increases = 0
    measurementSum = 0
    for i in range(0,len(measurements)-2):
        newMeasurementSum = measurements[i] + measurements[i + 1] + measurements[i + 2]
        if (not i == 0) and (newMeasurementSum > measurementSum):
            increases += 1
        measurementSum = newMeasurementSum
    return increases

print(single_measurement())
print(three_measurement())