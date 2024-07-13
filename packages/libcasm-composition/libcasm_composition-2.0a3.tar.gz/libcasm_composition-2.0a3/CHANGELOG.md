# Changelog

All notable changes to `libcasm-composition` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [2.0a3] - 2024-07-12

### Changed

- Wheels compiled with numpy>=2.0.0


## [2.0a2] - 2024-03-13

### Added

- Build python3.12 wheels

### Changed

- Update libcasm-global dependency to >=2.0.4
- Use index_to_kcombination and nchoosek from libcasm-global 2.0.4

## [2.0a1] - 2023-08-17

This release separates out casm/composition from CASM v1. It creates a Python package, libcasm.composition, that enables using casm/composition and may be installed via pip install, using scikit-build, CMake, and pybind11. This release also includes API documentation for using libcasm.composition, built using Sphinx.

### Added

- Added JSON IO for composition::CompositionConverter
- Added Python package libcasm.composition to use CASM composition converter and calculation methods.
- Added scikit-build, CMake, and pybind11 build process
- Added GitHub Actions for unit testing
- Added GitHub Action build_wheels.yml for Python x86_64 wheel building using cibuildwheel
- Added Cirrus-CI .cirrus.yml for Python aarch64 and arm64 wheel building using cibuildwheel
- Added Python documentation


### Removed

- Removed autotools build process
- Removed boost dependencies
