# nvidia-haystack

[![PyPI - Version](https://img.shields.io/pypi/v/opea-haystack.svg)](https://pypi.org/project/opea-haystack)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/opea-haystack.svg)](https://pypi.org/project/opea-haystack)

---

**Table of Contents**

- [opea-haystack](#opea-haystack)
  - [Installation](#installation)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

```console
pip install opea-haystack
```

## Contributing

`hatch` is the best way to interact with this project, to install it:

```sh
pip install hatch
```

With `hatch` installed, to run all the tests:

```
hatch run test
```

To only run unit tests:

```
hatch run test -m"not integration"
```

To run the linters `ruff` and `mypy`:

```
hatch run lint:all
```

## License

`opea-haystack` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.
