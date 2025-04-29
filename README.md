Graph-Based Movie Recommender 🎬🔗

This project implements a **graph-based movie recommendation system** using link prediction algorithms. The system predicts which movies a user might like based on past interactions using graph similarity metrics.

## 📁 Files
- `main.ipynb`: Jupyter Notebook containing the full implementation.
- `dataset.csv`: Input dataset of user-movie interactions.
- `train_dataset.csv`, `test_dataset.csv`: Data splits used for training and testing the model.

## 📌 Project Description

The core idea is to model the user-movie interactions as a **bipartite graph**, where:
- Nodes represent users and movies.
- Edges represent interactions (e.g., watched or rated).

We apply **link prediction techniques** to estimate the likelihood of future user-movie interactions, effectively recommending movies that a user is likely to enjoy.

## 🧠 Techniques Used
- **Graph Construction** using NetworkX
- **Link Prediction Algorithms**:
  - Jaccard Coefficient
  - Adamic-Adar Index
  - Preferential Attachment
  - Resource Allocation Index
- Train/Test splitting per user
- Visualization of sample graphs

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommender-graph.git
   cd movie-recommender-graph

