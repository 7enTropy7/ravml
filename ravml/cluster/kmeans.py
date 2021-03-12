import ravop.core as R


class KMeans(object):
    def __init__(self, **kwargs):
        self.params = kwargs
        self.points = None
        self.labels = None
        self.k = None

    def set_params(self, **kwargs):
        self.params.update(**kwargs)

    def get_params(self):
        return self.params

    def fit(self, X, k=3, iter=10):
        self.points = X
        self.k = k

        centroids = self.initialize_centroids()

        self.labels = self.closest_centroids(centroids)

        self.update_centroids()

    def initialize_centroids(self):
        return R.random(self.points, size=self.k)

    def closest_centroids(self, centroids):
        centroids = R.expand_dims(centroids, axis=1)
        return R.argmin(R.square_root(R.sum(R.square(R.sub(self.points, centroids)), axis=2)))

    def update_centroids(self):
        indices = R.find_indices(self.labels, values=list(range(self.k)))
        values = R.gather(self.points, indices_list=indices)


if __name__ == '__main__':
    k = KMeans()
    k.set_params(**{"a": "b"})
    k.fit(X=R.Tensor([[2, 3], [5, 6], [5, 7], [6, 8], [7, 2]]))

    from ravcom.utils import inform_server
    inform_server()

