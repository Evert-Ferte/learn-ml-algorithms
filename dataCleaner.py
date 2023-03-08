import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
import warnings

# Function that calculates the percentage of missing values
def calc_percent_NAs(df):
    nans = pd.DataFrame(df.isnull().sum().sort_values(ascending=False)/len(df), columns=['percent']) 
    idx = nans['percent'] > 0
    return nans[idx]

df = pd.read_csv('pump_sensor_data.csv')
# df.info()

df = df.drop_duplicates()
del df['sensor_15']

# Let's convert the data type of timestamp column to datatime format
df_tidy = df
df_tidy['date'] = pd.to_datetime(df_tidy['timestamp'])
del df_tidy['timestamp']

# print(calc_percent_NAs(df).head(10))

# Extract the readings from the BROKEN state of the pump
broken = df[df['machine_status'] == 'BROKEN']
df2 = df.drop(['machine_status'], axis=1)
names = df2.columns

# Plot time series for a sensor with the BROKEN state
# name = 'sensor_00'
# _ = plt.figure(figsize=(18,3))
# _ = plt.plot(broken[name], linestyle='none', marker='X', color='red', markersize=12)
# _ = plt.plot(df[name], color='blue')
# _ = plt.title(name)
# plt.show()

# Extract the names of the numerical columns
df['date'].values.astype('float ')
x = df[names]
scaler = StandardScaler()
pca = PCA()
pipeline = make_pipeline(scaler, pca)
pipeline.fit(x)

# Plot the principal components against their inertia
features = range(pca.n_components_)
_ = plt.figure(figsize=(15, 5))
_ = plt.bar(features, pca.explained_variance_)
_ = plt.xlabel('PCA feature')
_ = plt.ylabel('Variance')
_ = plt.xticks(features)
_ = plt.title("Importance of the Principal Components based on inertia")
plt.show()

# Calculate with the 2 principal components
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDF = pd.DataFrame(data=principalComponents, columns=['pc1', 'pc2'])
