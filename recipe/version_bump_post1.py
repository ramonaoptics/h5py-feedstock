diff --git a/h5py/version.py b/h5py/version.py
index 8f47341e..60f04a8f 100644
--- a/h5py/version.py
+++ b/h5py/version.py
@@ -23,7 +23,7 @@ _H5PY_VERSION_CLS = namedtuple("_H5PY_VERSION_CLS",
 
 hdf5_built_version_tuple = _h5.HDF5_VERSION_COMPILED_AGAINST
 
-version_tuple = _H5PY_VERSION_CLS(3, 6, 0, None, None, None)
+version_tuple = _H5PY_VERSION_CLS(3, 6, 0, None, 1, None)
 
 version = "{0.major:d}.{0.minor:d}.{0.bugfix:d}".format(version_tuple)
 if version_tuple.pre is not None:
