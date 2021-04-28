import numpy
import random
import turtle

M = 100  # Panjang lintasan
p = 0.3  # Probabilitas pengereman
v0 = 0  # kecepatan awal
N = 10  # banyak kendaraan
tmax = 100  # waktu maksimum
vmax = 5  # kecepatan maksimum
dt = 1

posStart = []
lapTime = []
circuitHit = []

lt = []
for t in range(N):
    lt.append(turtle.Turtle())
for i in range(N):
    x = random.randint(0, M)
    posStart.append(x)
    lapTime.append([0, 0])
    circuitHit.append(False)
    lt[i].penup()
    lt[i].setposition(x, 0)
    lt[i].speed(8)


def getJarak(i):
    if (i < N - 1):
        jarak = abs(lt[i + 1].xcor() - lt[i].xcor())
        if lt[i].xcor() <= lt[i + 1].xcor():  # mobil ke i+1 didepan mobil i
            return jarak
        else:
            return M - (jarak)  # mobil ke i didepan mobil i+1
    else:
        jarak = abs(lt[0].xcor() - lt[i].xcor())
        if lt[i].xcor() <= lt[0].xcor():  # mobil awal didepan mobil ke i
            return jarak
        else:
            return M - (jarak)  # mobil ke i didepan mobil awal


def getGas(i):
    vK[i] = min(vK[i] + 1, vmax)
    vK[i] = min(vK[i], getJarak(i) - 1)
    c = numpy.random.uniform(0, 1)
    if (c < p):
        vK[i] = max(0, vK[i] - 1)
    lt[i].forward(vK[i])


def updatePosisi():
    for i in range(N):
        getGas(i)
        posK[i] = lt[i].xcor()
        if (lt[i].xcor() > M):
            lt[i].hideturtle()
            lt[i].goto(lt[i].xcor() - M, 0)
            lt[i].showturtle()
            circuitHit[i] = True
            posK[i] = lt[i].xcor()
        if circuitHit[i] and posK[i] >= posStart[i]:
            lapTime[i][0] += 1
            lapTime[i][1] = lapTime[i][1] + (t - lapTime[i][1])
            circuitHit[i] = False


t = 0
kepadatan = []

screen = turtle.Screen()
screen.delay(1)
vK = [v0] * N
posK = [0] * N
while t <= tmax:
    print(posK)
    updatePosisi()
    t = t + dt
    totCar = 0
    for i in range(N):
        if 80 < posK[i] < 90:
            totCar += 1;
    kepadatan.append(totCar/10);

print("Kepadatan per setiap waktu pada waktu interval di X[80] sampai X[90] : ", kepadatan)

for i in range(len(lapTime)):
    rata = lapTime[i][1] / lapTime[i][0]
    print("kendaraan ke - " + str(i) + " -> " + str(lapTime[i][0]) + " lap / " + str(
        lapTime[i][1]) + " total time = " + str(rata))
