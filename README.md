# 📊 ClusterLens — K-Means Clustering Visualizer with Streamlit & OpenCV

**ClusterLens** is an interactive data visualization tool that demonstrates the working of the K-Means clustering algorithm through a dynamic video-based visualizer. Built using **Streamlit** for the user interface and **OpenCV** for real-time frame generation, this project is designed to help users intuitively understand how clustering works in 2D space.

---

## 🚀 Features

* 📌 **Real-time Visualizer**: Watch the step-by-step clustering process unfold as a video.
* 🎨 **Interactive UI**: Customize the number of clusters, data points, and iterations using an easy-to-use Streamlit interface.
* 🧠 **K-Means Explained Visually**: Observe how data points are assigned to clusters over time and how centroids move.
* 💾 **Downloadable Output**: Option to download the generated clustering video for presentations or educational purposes.

---

## 📷 Demo

> \[Upload a demo video or gif here after testing the full functionality]

---

## 🛠️ Tech Stack

* **Python 3.10**
* **Streamlit** – For web interface and interactivity
* **OpenCV (cv2)** – For frame-by-frame video creation
* **NumPy** – For mathematical operations and random point generation
* **Pandas** – For displaying tabular data if needed

---

## 📂 Folder Structure

```
ClusterLens/
│
├── app.py                # Main Streamlit app
├── requirements.txt     # Project dependencies
├── kmeans_video/       # (Optional) Sample videos or frames
└── README.md            # Project documentation
```

---

## 🖥️ How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/its-kanii/ClusterLens.git
cd ClusterLens
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run ui.py
```

4. Visit the app in your browser at `http://localhost:8501`

---

## 🧪 Requirements

Make sure you have the following installed:

* Python 3.8+
* OpenCV (`cv2`)
* Streamlit
* NumPy

To install everything:

```bash
pip install -r requirements.txt
```

---

## 🧠 Use Cases

* 📚 Teaching or learning clustering in Data Science
* 🧪 Demonstrating unsupervised learning concepts visually
* 📊 Enhancing presentations with clustering animations
* 🎓 Student projects or hackathon demos

---

## 🙌 Acknowledgments

This project was built as part of my Data Science learning journey. Special thanks to the communities supporting open-source tools like Streamlit and OpenCV!

---

## 📌 TODO

* [ ] Add support for more clustering algorithms (DBSCAN, GMM)
* [ ] Enable pause/play controls in the video
* [ ] Upload demo videos
* [ ] Add deployment instructions (Streamlit Cloud / Hugging Face Spaces)

---

## 📫 Let's Connect

If you like this project or want to collaborate on other Data Science visual tools, feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/kanimozhi-kathirvel) or drop a ⭐ on the repo!
