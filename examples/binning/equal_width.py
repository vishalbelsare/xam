import matplotlib.pyplot as plt
import numpy as np

from xam.binning import EqualWidthBinner


mu, sigma = 0, 0.1
x = np.random.normal(mu, sigma, 1000)

binner = EqualWidthBinner(n_bins=5)
binner.fit(X=x.reshape(-1, 1))

bins = np.concatenate([
    [np.min(x)],
    binner.cut_points_[0],
    [np.max(x)]
])

plt.hist(x, bins=bins)
plt.show()