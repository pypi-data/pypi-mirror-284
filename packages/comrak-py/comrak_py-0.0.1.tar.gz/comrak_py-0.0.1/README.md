# README
comrak-py is a python wrapper around the [comrak](https://github.com/kivikakk/comrak) common mark rust port and allows for efficient markdown rendering.

# Building

In order to build the python wheel, you must first have cargo and rustup installed.
```curl https://sh.rustup.rs -sSf | sh```

This python package relies on maturin to build and publish the comrak rust crate
```pip install maturin```

To build a wheel for comrak-py, you can run
```maturin build```

To build comrak-py and install it as a python module, you can run
```maturin develop```
