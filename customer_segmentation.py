import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess_features(df):
    # Select relevant features for clustering
    features = df[['Quantity', 'UnitPrice']]
    return features

def perform_kmeans(features, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(features)
    clusters = kmeans.predict(features)
    return clusters, kmeans.cluster_centers_

def save_segmented_data(df, clusters, file_path):
    df['Cluster'] = clusters
    df.to_csv(file_path, index=False)

def plot_clusters(features, clusters, cluster_centers):
    plt.scatter(features['Quantity'], features['UnitPrice'], c=clusters, cmap='viridis', marker='o')
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=300, c='red', marker='x')
    plt.xlabel('Quantity')
    plt.ylabel('UnitPrice')
    plt.title('Customer Segmentation using K-means Clustering')
    plt.show()

if __name__ == "__main__":
    # Load the cleaned data
    data_file_path = "cleaned_online_retail_data.csv"
    df = load_data(data_file_path)

    # Preprocess features
    features = preprocess_features(df)

    # Perform K-means clustering
    clusters, cluster_centers = perform_kmeans(features)

    # Save the segmented data
    segmented_data_file_path = "segmented_customers.csv"
    save_segmented_data(df, clusters, segmented_data_file_path)

    # Plot the clusters
    plot_clusters(features, clusters, cluster_centers)
