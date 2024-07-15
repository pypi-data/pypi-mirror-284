# ruff: noqa: D104


# start delvewheel patch
def _delvewheel_patch_1_7_1():
    import ctypes
    import os
    import platform
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'moocore.libs'))
    is_conda_cpython = platform.python_implementation() == 'CPython' and (hasattr(ctypes.pythonapi, 'Anaconda_GetVersion') or 'packaged by conda-forge' in sys.version)
    if sys.version_info[:2] >= (3, 8) and not is_conda_cpython or sys.version_info[:2] >= (3, 10):
        if os.path.isdir(libs_dir):
            os.add_dll_directory(libs_dir)
    else:
        load_order_filepath = os.path.join(libs_dir, '.load-order-moocore-0.0.9999')
        if os.path.isfile(load_order_filepath):
            with open(os.path.join(libs_dir, '.load-order-moocore-0.0.9999')) as file:
                load_order = file.read().split()
            for lib in load_order:
                lib_path = os.path.join(os.path.join(libs_dir, lib))
                kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
                if os.path.isfile(lib_path) and not kernel32.LoadLibraryExW(ctypes.c_wchar_p(lib_path), None, 0x00000008):
                    raise OSError('Error loading {}; {}'.format(lib, ctypes.FormatError(ctypes.get_last_error())))


_delvewheel_patch_1_7_1()
del _delvewheel_patch_1_7_1
# end delvewheel patch

from ._moocore import (
    ReadDatasetsError,
    avg_hausdorff_dist,
    eaf,
    eafdiff,
    epsilon_additive,
    epsilon_mult,
    filter_dominated,
    filter_dominated_within_sets,
    get_dataset_path,
    groupby,
    hypervolume,
    igd,
    igd_plus,
    is_nondominated,
    normalise,
    pareto_rank,
    read_datasets,
    vorobDev,
    vorobT,
    whv_hype,
)

from importlib.metadata import version as _metadata_version

__version__ = _metadata_version(__package__ or __name__)
# Remove symbols imported for internal use
del _metadata_version


__all__ = [
    "ReadDatasetsError",
    "avg_hausdorff_dist",
    "eaf",
    "eafdiff",
    "epsilon_additive",
    "epsilon_mult",
    "filter_dominated",
    "filter_dominated_within_sets",
    "get_dataset_path",
    "groupby",
    "hypervolume",
    "igd",
    "igd_plus",
    "is_nondominated",
    "normalise",
    "pareto_rank",
    "read_datasets",
    "vorobDev",
    "vorobT",
    "whv_hype",
]
