from skbuild import setup

setup(
    name="libcasm-composition",
    version="2.0a3",
    packages=["libcasm", "libcasm.composition"],
    package_dir={"": "python"},
    cmake_install_dir="python/libcasm",
    include_package_data=False,
)
