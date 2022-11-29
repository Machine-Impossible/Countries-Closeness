# Countries Closeness

## Installation

```bash
git clone https://github.com/Machine-Impossible/Countries-Closeness.git
```

Once after cloning the repo, you need to install (or have) the necessary packages in your virtual environment or just globally

```bash
pip3 install pandas numpy seaborn plotly matplotlib scikit-learn fuzzy-c-means 
```
## Dataset URL

```
https://www.kaggle.com/rohan0301/unsupervised-learning-on-country-data
```

## About

The aim of this project is to cluster countries based on the economic and development similarities. We have used and compared various clustering algorithms by their silhoutte score. The clustering algorithms used are,

- K - Means
- DBSCAN
- Fuzzy
- Hierarchial


## K Means


## DBSCAN

It is an density based clustering algorithm. It takes in two parameters eps which the distance to look for points in the cluster and min_samples which is no. of points to consider it as a core point. The min_samples parameter is always greater than equal to the dimension of the dataset which is 9 in our case. Using this and by plotting the k-distance graph we can find the eps parameter. For K-Distance Graph we will be using the KNN method where k = 9.

## Fuzzy


## Hierarchial

## Conclusion

For the gicen dataset hierarchial clustering had the highest silhoutte score thus the better clustering algorithm for this case.

## Contributers

<a href="https://github.com/A-Lokanush">@a-lokanush</a>   :  106120009

<a href="https://github.com/ash20012003">@ash20012003</a>  :  106120017

<a href="https://github.com/CraftyChimera">@CraftyChimera</a> : 106120043

<a href="https://github.com/skandanramesh">@skandanramesh</a> : 106120121