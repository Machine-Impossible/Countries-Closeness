import pandas as pd
import sys

def join():
    mode = sys.argv[1]
    d1 = pd.read_csv('dataset/GII.csv')
    d2 = pd.read_csv('dataset/HDI.csv')
    remaining_csv = ['dataset/INTERNET.csv', 'dataset/POL.csv', 'dataset/PRECIPITATION.csv']

    output = pd.merge(d1, d2, on='Entity', how=mode)

    for i in remaining_csv:
        data = pd.read_csv(i)
        output = pd.merge(output, data, on='Entity', how=mode)

    final_output = output[['Entity', 'GII', 'HDI', 'POL', 'INTERNET', 'PRECIPITATION']]
    final_output["POL"] = final_output["POL"] / 4
    ash = pd.read_csv('dataset/DATA.csv')
    religions = ["Christians", "Muslims", "Unaffiliated", "Hindus", "Buddhists", "folkReligions", "otherReligions", "Jews"]
    for religion in religions:
        ash[religion] = ash[religion] / ash["Population"]

    final_output.round(4)
    final_output = pd.merge(ash, final_output, on='Entity', how=mode)

    final_output.to_csv("dataset/WITHOUT_LANG.csv", index=False)


if __name__ == "__main__":
	join()
