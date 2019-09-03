import numpy as np
from prepare_utils import read_raw_all
import argparse
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train classifier')
    parser.add_argument("-d", "--datasets", dest="DATASETS", default=10, type=int, help="number of datasets to prepare")
    parser.add_argument("-i", "--input", dest="IN")
    args = parser.parse_args()

    data_path = args.IN

    for i in range(0, 21, 2):
        data, weights = read_raw_all(kind="CPmix_%s" % str(i).zfill(2), args=args, channel="a1rho", num_particles=8)
        if i == 0:
            data_00 = data
            np.random.seed(123)
            perm = np.random.permutation(len(weights))
            np.save(os.path.join(data_path, "a1rho_raw.data.npy"), data_00)
            np.save(os.path.join(data_path, "a1rho_raw.perm.npy"), perm)
        else:
            np.testing.assert_array_almost_equal(data_00, data)
        np.save(os.path.join(data_path, "a1rho_raw.w_%s.npy" % str(i).zfill(2)), weights)

