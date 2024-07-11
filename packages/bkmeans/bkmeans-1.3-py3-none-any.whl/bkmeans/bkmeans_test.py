import unittest
import numpy as np
from bkmeans import BKMeans

class TestBKMeans(unittest.TestCase):
    def setUp(self):
        self.data = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
        self.bkmeans = BKMeans(n_clusters=2, random_state=2)

    def test_fit(self):
        self.bkmeans.fit(self.data)
        # assert that cluster_centers is [[10.  2.] [ 1.  2.]] or cluster_centers is [[1.  2.] [ 10.  2.]] up  epsilon=0.0001
        self.assertTrue(np.allclose(self.bkmeans.cluster_centers_, np.array([[10., 2.], [1., 2.]]), atol=0.0001) or np.allclose(self.bkmeans.cluster_centers_, np.array([[1., 2.], [10., 2.]]), atol=0.0001))

    def test_get_error(self):
        self.bkmeans.fit(self.data)
        error = self.bkmeans.get_error(self.data, self.bkmeans.cluster_centers_)
        # assert that error is a vector of length n_clusters
        self.assertEqual(error.shape, (2,))

    def test_predict_equals_labels(self):
        self.bkmeans.fit(self.data)
        labels = self.bkmeans.predict(self.data)
        # assert that labels are [1 1 1 0 0 0] or [0 0 0 1 1 1]
        self.assertTrue(np.all(labels == np.array([1, 1, 1, 0, 0, 0])) or np.all(labels == np.array([0, 0, 0, 1, 1, 1])))
        # assert that labels_ is equal to result of predict
        self.assertTrue(np.all(self.bkmeans.labels_ == labels))

    def test_get_version(self):
        version = BKMeans.get_version()
        self.assertEqual(version, "V1.3")

if __name__ == '__main__':
    unittest.main()
    