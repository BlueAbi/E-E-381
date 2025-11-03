import csv, statistics, matplotlib.pyplot as plt

years = range(2001, 2021)

def truncate(num, n):                 ## truncate to n decimal places
    return int(num * 10 ** n) / 10 ** n

def calc_probabability(data, year, low=200000, high=300000) :
    prices = [float(row[1]) for row in data if int(row[0]) == year]
    if not prices :
        return 0

    count_in_range = sum(1 for p in prices if low <= p <= high)
    probability =  count_in_range / len(prices)
    return round(probability, 3)

def plot_probability(data) :
    probs = []
    for i in years :
        p = calc_probabability(data, i)
        probs.append(p)
        print(f"{i}: Probability = {p: .3f}")

    plt.figure(figsize=(10, 5))
    plt.bar(years, probs, color="mediumseagreen", edgecolor="black")
    plt.xlabel("Year")
    plt.ylabel("Probability")
    plt.title("Probability of Sale Prices from $200k–$300k by Year (2001–2020)")
    plt.xticks(list(years))
    plt.ylim(0, 1)  # since probability maxes at 1
    plt.tight_layout()
    plt.show()

def calc_stats(data, year) :
    values = [float(row[1]) for row in data if int(row[0]) == year]
    if values :
        mean = statistics.mean(values)
        ##print(f"Average price of a house in {year} was ${truncate(mean, 2)}.")
        stdev = statistics.stdev(values) if len(values) > 1 else 0
        print(f"Standard deviation of houses in {year} was ${truncate(stdev, 2)}.")
        return truncate(mean, 2), truncate(stdev, 2)
    else :
        return 0, 0

def plot_stats(data) :
    means = []
    stdevs = []

    for i in years :
        mean, stdev = calc_stats(data, i)
        means.append(mean)
        stdevs.append(stdev)

    ## PLOT 1: MEANS
    plt.figure(figsize=(10,5))
    plt.bar(years, means, color="steelblue", edgecolor="black")
    plt.xlabel("Year")
    plt.ylabel("Average Price ($)")
    plt.title("Average Housing Prices by Year from 2001-2020")
    plt.xticks(list(years))
    plt.tight_layout()
    plt.show()

    ## PLOT 2: STANDARD DEVIATIONS
    plt.figure(figsize=(10,5))
    plt.bar(years, stdevs, color="steelblue", edgecolor="black")
    plt.xlabel("Year")
    plt.ylabel("Standard Deviations ($)")
    plt.title("Standard Deviation of Housing Prices from the Average by Year from 2001-2020")
    plt.xticks(list(years))
    plt.tight_layout()
    plt.show()


with open("Sales_01_20.csv", newline="") as f :
    reader = csv.reader(f)   ## skip the first line in the csv
    next(reader)
    data = list(reader)

plot_stats(data)
plot_probability(data)