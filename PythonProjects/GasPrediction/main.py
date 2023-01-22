import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as skl

def main():
    data = pd.read_csv("gasPrices.csv",sep=",")
    sdata = data[ ["Date", "Price"]]
    print(sdata.head())
    data.plot()
    plt.show()

    regression = skl.LinearRegression()
    
if __name__ == "__main__":
    main()
    