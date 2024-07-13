import numpy as np
from scipy.sparse.csgraph import laplacian
import simsimd
import faiss


class _KMeans:
    """K-means clustering using FAISS and SimSIMD.

    Parameters:
    -----------
    n_clusters : int
        The number of clusters to form.
    n_iter : int, optional, default=20
        Number of iterations to run the k-means algorithm.
    n_local_trials : int or None, optional, default=None
        Number of seeding trials for centroids initialization.
    random_state : int or None, optional, default=None
        Determines random number generation for centroid initialization.

    Attributes:
    -----------
    cluster_centers_ : numpy.ndarray
        Coordinates of cluster centers.
    labels_ : numpy.ndarray
        Labels of each point (index) in X.

    Methods:
    --------
    fit(X):
        Run k-means clustering on the input data X.
    """

    def __init__(
        self,
        n_clusters,
        n_iter=20,
        n_local_trials=None,
        random_state=None,
    ):
        self.n_clusters = n_clusters
        self.n_iter = n_iter
        self.n_local_trials = n_local_trials
        self.random_state = random_state

    def _init_centroids(self, X):
        rng = np.random.default_rng(self.random_state)

        centroids = np.empty((self.n_clusters, X.shape[1]), dtype=np.float32)
        centroids[0] = X[rng.integers(X.shape[0])]
        dists = np.full(X.shape[0], np.inf)

        if self.n_local_trials is None:
            self.n_local_trials = 2 + int(np.log(self.n_clusters))

        for i in range(1, self.n_clusters):
            current_dists = simsimd.sqeuclidean(X, centroids[i - 1])
            dists = np.minimum(dists, current_dists)

            candidates = rng.choice(
                X.shape[0], size=self.n_local_trials, p=dists / dists.sum()
            )
            candidates_dists = np.array(simsimd.cdist(X, X[candidates], "sqeuclidean"))
            inertias = np.minimum(candidates_dists, dists[:, None]).sum(axis=0)

            best_candidate = candidates[inertias.argmin()]

            centroids[i] = X[best_candidate]

        return centroids

    def fit(self, X):
        """Run k-means clustering on the input data X.

        Parameters:
        -----------
        X : numpy.ndarray
            Input data to cluster.
        """
        index = faiss.IndexFlatL2(X.shape[1])
        kmeans = faiss.Clustering(X.shape[1], self.n_clusters)

        init_centroids = self._init_centroids(X.astype(np.float32))

        kmeans.centroids.resize(init_centroids.size)
        faiss.copy_array_to_vector(init_centroids.ravel(), kmeans.centroids)
        kmeans.niter = self.n_iter
        kmeans.min_points_per_centroid = 0
        kmeans.max_points_per_centroid = -1
        kmeans.train(X.astype(np.float32), index)

        self.cluster_centers_ = faiss.vector_to_array(kmeans.centroids).reshape(
            self.n_clusters, X.shape[1]
        )
        self.labels_ = index.search(X.astype(np.float32), 1)[1].ravel()


class _SpectralClustering:
    """Spectral clustering based on Laplacian matrix.

    Parameters:
    -----------
    n_clusters : int
        The number of clusters to form.
    random_state : int or None, optional, default=None
        Determines random number generation for centroid initialization.

    Attributes:
    -----------
    labels_ : numpy.ndarray
        Labels of each point (index) in the affinity matrix.

    Methods:
    --------
    fit(affinity):
        Fit the spectral clustering model on the affinity matrix.
    """

    def __init__(self, n_clusters, random_state):
        self.n_clusters = n_clusters
        self.random_state = random_state

    def fit(self, affinity):
        """Fit the spectral clustering model on the affinity matrix.

        Parameters:
        -----------
        affinity : numpy.ndarray
            Affinity matrix representing pairwise similarity between points.
        """
        L = laplacian(affinity, normed=True)

        eigvecs = np.linalg.eigh(L)[1]
        eigvecs = eigvecs[:, : self.n_clusters]
        eigvecs /= np.linalg.norm(eigvecs, axis=1)[:, None]
        kmeans = _KMeans(self.n_clusters, random_state=self.random_state)
        kmeans.fit(eigvecs)

        self.labels_ = kmeans.labels_


class SpectralBridges:
    """Spectral Bridges clustering algorithm.

    Parameters:
    -----------
    n_clusters : int
        The number of clusters to form.
    n_nodes : int
        Number of nodes or initial clusters.
    M : float, optional, default=1e4
        Scaling parameter for affinity matrix computation.
    n_iter : int, optional, default=20
        Number of iterations to run the k-means algorithm.
    n_local_trials : int or None, optional, default=None
        Number of seeding trials for centroids initialization.
    random_state : int or None, optional, default=None
        Determines random number generation for centroid initialization.

    Methods:
    --------
    fit(X):
        Fit the Spectral Bridges model on the input data X.
    predict(x):
        Predict the nearest cluster index for each input data point x.
    """

    def __init__(
        self,
        n_clusters,
        n_nodes,
        M=1e4,
        n_iter=20,
        n_local_trials=None,
        random_state=None,
    ):
        self.n_clusters = n_clusters
        self.n_nodes = n_nodes
        self.M = M
        self.n_iter = n_iter
        self.n_local_trials = n_local_trials
        self.random_state = random_state

    def fit(self, X):
        """Fit the Spectral Bridges model on the input data X.

        Parameters:
        -----------
        X : numpy.ndarray
            Input data to cluster.
        """
        kmeans = _KMeans(
            self.n_nodes,
            n_iter=self.n_iter,
            n_local_trials=self.n_local_trials,
            random_state=self.random_state,
        )
        kmeans.fit(X)

        affinity = np.empty((self.n_nodes, self.n_nodes))

        X_centered = [
            X[kmeans.labels_ == i] - kmeans.cluster_centers_[i]
            for i in range(self.n_nodes)
        ]

        counts = np.array([X_centered[i].shape[0] for i in range(self.n_nodes)])
        counts = counts[None, :] + counts[:, None]

        segments = kmeans.cluster_centers_[None, :] - kmeans.cluster_centers_[:, None]
        dists = np.einsum("ijk,ijk->ij", segments, segments)
        np.fill_diagonal(dists, 1)

        for i in range(self.n_nodes):
            projs = np.maximum(np.dot(X_centered[i], segments[i].T), 0)
            affinity[i] = np.einsum("ij,ij->j", projs, projs)

        affinity = np.sqrt(affinity + affinity.T) / (np.sqrt(counts) * dists)
        affinity -= 0.5 * affinity.max()

        q10, q90 = np.quantile(affinity, [0.1, 0.9])

        gamma = np.log(self.M) / (q90 - q10)
        affinity = np.exp(gamma * affinity)

        spectralclustering = _SpectralClustering(
            self.n_clusters, random_state=self.random_state
        )
        spectralclustering.fit(affinity)

        self.cluster_centers_ = [
            kmeans.cluster_centers_[spectralclustering.labels_ == i]
            for i in range(self.n_clusters)
        ]

    def predict(self, x):
        """Predict the nearest cluster index for each input data point x.

        Parameters:
        -----------
        x : numpy.ndarray
            Input data points to predict clusters.

        Returns:
        --------
        numpy.ndarray
            Predicted cluster indices for each input data point.
        """
        cluster_centers = np.vstack(self.cluster_centers_)
        cluster_cutoffs = np.cumsum(
            [cluster.shape[0] for cluster in self.cluster_centers_]
        )

        index = faiss.IndexFlatL2(x.shape[1])
        index.add(cluster_centers.astype(np.float32))
        winners = index.search(x.astype(np.float32), 1)[1].ravel()

        labels = np.searchsorted(cluster_cutoffs, winners, side="right")

        return labels
