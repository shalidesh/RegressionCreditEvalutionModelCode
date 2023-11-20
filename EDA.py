import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def scatter(data):
    # Creating a scatter plot
    plt.scatter(data['mileage'], data['price'])

    # Adding labels and title
    plt.xlabel('mileage')
    plt.ylabel('price')
    plt.title('Scatter Plot Example')

    # Display the plot
    plt.show()

def correlation(data):
    
    # Creating a DataFrame
    df = data[['mileage','Age','price']]

    # Compute the correlation matrix
    correlation_matrix = df.corr()

    # Creating a correlation plot
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)

    # Adding title to the plot
    plt.title('Correlation Plot of Numerical Variables')

    # Display the plot
    plt.show()

if __name__=="__main__":
    df=pd.read_csv('notebook\\data\\Preprocessed3W.csv')
    scatter(df)


