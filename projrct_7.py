from datetime import date
fname = "btc_usd.csv"
f = open(fname)
dates = []
rates = []
for line in f:
    dt = line.split(";")
    dates.append(dt[0])
    rates.append(dt[1])
f.close()
ratemax = 0
ratemin = 0
rateaverage = 0
i = 0
for rate in rates:
    frate = float(rate)
    rateaverage += frate
    if i == 0:
        ratemax = frate
        ratemin = frate
        datemin = dates[i]
        datemax = dates[i]
    else:
        if frate >= ratemax:
            ratemax = frate
            datemax = dates[i]
        else:
            if frate < ratemin:
                ratemin = frate
                datemin = dates[i]
    i += 1
rateaverage = rateaverage / i
print("Average BTC_USD rate on November 2018: $", rateaverage)
print("The minimum BTC_USD value was fixed on ", datemin, " and amounted to $", ratemin)
print("The maximum BTC_USD value was fixed on ", datemax, " and amounted to $", ratemax)
