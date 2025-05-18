import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import time

st.title("📊Real-Time K-Means Clustering Visualizer - Live Animation")

# Accept both CSV and XLSX files
uploaded_file = st.file_uploader("Upload your data file (CSV or XLSX)", type=["csv", "xlsx"])

def plot_clusters(X, centroids, assignments, iteration, k):
    fig, ax = plt.subplots(figsize=(10, 7))
    colors = plt.cm.get_cmap('tab10', k)
    for cluster in range(k):
        ax.scatter(X[assignments == cluster, 0], X[assignments == cluster, 1], 
                   label=f'Cluster {cluster}', color=colors(cluster))
        ax.scatter(centroids[cluster, 0], centroids[cluster, 1], 
                   s=250, marker='X', c='black', edgecolor='white', linewidth=2)
    ax.set_title(f'Iteration {iteration}', fontsize=16)
    ax.legend(fontsize=12)
    ax.grid(True)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return buf

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            data = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file format!")
            st.stop()

        st.write("Data Preview:")
        st.write(data.head())

        if data.shape[1] < 2:
            st.error("Please upload a file with at least 2 columns for clustering.")
        else:
            X = data.iloc[:, :2].values
            k = st.slider("Number of clusters (k)", min_value=2, max_value=10, value=3)
            max_iter = st.slider("Max iterations", min_value=1, max_value=20, value=10)

            if st.button("Run K-Means Live Animation"):
                centroids = X[np.random.choice(range(len(X)), k, replace=False)]
                assignments = np.zeros(len(X), dtype=int)

                img_placeholder = st.empty()

                for i in range(max_iter):
                    distances = np.linalg.norm(X[:, None] - centroids[None, :], axis=2)
                    assignments = np.argmin(distances, axis=1)

                    buf = plot_clusters(X, centroids, assignments, i+1, k)
                    img_placeholder.image(buf, width=700)

                    time.sleep(1)

                    new_centroids = np.array([
                        X[assignments == c].mean(axis=0) if np.any(assignments == c) else centroids[c]
                        for c in range(k)
                    ])

                    if np.allclose(centroids, new_centroids):
                        st.write(f"Converged after {i+1} iterations!")
                        break
                    centroids = new_centroids

                st.success("K-Means clustering animation completed!")

    except Exception as e:
        st.error(f"Error loading file: {e}")
