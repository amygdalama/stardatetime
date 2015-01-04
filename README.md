# stardatetime: datetime for the next generation

stardatetime provides datetime objects converted to Star Trek time.

# Getting Started

Get the current time:

```python
>>> from stardatetime import StarDateTime
>>> StarDateTime.now()
StarDateTime(-307992.1713)
```

Specify a time in Earth time:

```python
>>> StarDateTime(year=2015, month=1, day=1,
                 hour=1, minute=1, second=1, microsecond=1)
StarDateTime(-307999.8839)
```

Create from a `datetime` object:

```python
>>> from datetime import datetime
>>> StarDateTime.from_datetime(datetime.now())
StarDateTime(-307992.1705)
```

# Documentation

# Installation

```bash
$ pip install stardatetime
```
