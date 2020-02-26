# pygrocydm
[![Build Status](https://travis-ci.com/BlueBlueBlob/pygrocydm.svg?branch=master)](https://travis-ci.com/BlueBlueBlob/pygrocydm)
[![CodeFactor](https://www.codefactor.io/repository/github/blueblueblob/pygrocydm/badge)](https://www.codefactor.io/repository/github/blueblueblob/pygrocydm)
[![Coverage Status](https://coveralls.io/repos/github/BlueBlueBlob/pygrocydm/badge.svg?branch=master)](https://coveralls.io/github/BlueBlueBlob/pygrocydm?branch=master)

## Installation



## Usage
Import the package: 
```python
from pygrocydm import GrocyDataManager
```

Obtain a grocy instance:
```python
gdm = GrocyDataManager("https://example.com", "GROCY_API_KEY")
```
or
```python
gdm = GrocyDataManager("https://example.com", "GROCY_API_KEY", port = 9192, verify_ssl = True)
```

