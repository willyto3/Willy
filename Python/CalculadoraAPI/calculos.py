import guiAPI
import math


def calculo(hidrometro, temperatura, tipo):
    apiobservado = float(hidrometro)
    temperatura = float(temperatura)

    presion = 0
    S60 = 0.01374979547

    densidad = (141.5 / (apiobservado + 131.5)) * 999.016

    hyc = 1 - (0.00001278*(temperatura-60))-(0.0000000062*(temperatura-60)**2)

    densidad = hyc*densidad

    densidad60 = densidad

    if tipo == "crudo":
        k0 = 341.0957
        k1 = 0
        k2 = 0
        Da = 2

    elif tipo == "refinados":

        if (838.3127 <= densidad60 <= 1163.5):
            k0 = 103.8720
            k1 = 0.2701
            k2 = 0
            Da = 1.3

        elif (787.5195 <= densidad60 < 838.3127):
            k0 = 330.3010
            k1 = 0
            k2 = 0
            Da = 2

        elif (770.3520 <= densidad60 < 787.5195):
            k0 = 1489.0670
            k1 = 0
            k2 = -0.00186840
            Da = 8.5

        elif (610.6 <= densidad60 < 770.3520):
            k0 = 192.4571
            k1 = 0.2438
            k2 = 0
            Da = 1.5

    elif tipo == "lubricantes":
        k0 = 0
        k1 = 0.34878
        k2 = 0
        Da = 1

    tc90 = (temperatura - 32) / 1.8
    t = tc90 / 630
    A1 = -0.148759
    A2 = -0.267408
    A3 = 1.08076
    A4 = 1.269056
    A5 = -4.089591
    A6 = -1.871251
    A7 = 7.438081
    A8 = -3.536296

    dtt = (A1 + (A2 + (A3 + (A4 + (A5 + (A6 + (A7 + A8 * t) * t) * t) * t) * t) * t) * t) * t
    tc68 = tc90 - dtt
    tf68 = 1.8 * tc68 + 32

    i = 0
    spo = 1
    v = math.fabs(spo)

    while i < 15 or v < 0.0001:

        a = (S60 / 2) * ((((k0 / densidad60) + k1) / densidad60) + k2)
        b = (2 * k0 + k1 * densidad60) / \
            (k0 + (k1 + k2 * densidad60) * densidad60)
        de = densidad60 * \
            (1 + ((math.exp(a * (1 + 0.8 * a)) - 1) / (1 + a * (1 + 1.6 * a) * b)))
        alfa60 = k2 + ((k0 / de) + k1) / de

        dt = tf68 - 60.0068749
        ctlc = math.exp(-alfa60 * dt * (1 + 0.8 * alfa60 * (dt + S60)))
        fp = math.exp(-1.9947 + 0.00013427 * tf68 +
                      ((793920 + 2326 * tf68) / de ** 2))
        cpl2 = 1 / (1 - fp * presion * 0.00001)
        ctpl2 = ctlc * cpl2
        dt2 = temperatura - 60
        x = densidad60 * ctpl2
        spo = densidad60 - x
        v = math.fabs(spo)
        e = (densidad / (ctlc * cpl2)) - densidad60
        dtm = 2 * alfa60 * dt2 * (1 + 1.6 * alfa60 * dt2)
        dp = (Da * cpl2 * presion * fp * (7.9392 +
              0.02326 * temperatura)) / (densidad60 ** 2)
        ddensidad60 = e / (1 + dtm + dp)
        i += 1

    densidad60 = densidad60 + ddensidad60
    densidad60 = round(densidad60, 1)

    return densidad60
