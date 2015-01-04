# stardatetime: datetime for the next generation

stardatetime provides datetime objects converted to Star Trek time.

# Getting Started

Get the current time:

:::pycon
>>> from stardatetime import StarDateTime
>>> StarDateTime.now()

Specify a time in Earth time:

:::pycon
>>> StarDateTime(year=2015, month=1, day=1,
                 hour=1, minute=1, second=1)

Specify a time in Star Trek time:

:::pycon
>>> StarDateTime.from_stardatetime(stardatetime=41367.4)

Create from a `datetime` object:

:::pycon
>>> from datetime import datetime
>>> StarDateTime.from_datetime(datetime.now())

Calculate deltas:

:::pycon
>>> StarDateTime.from_stardatetime(41367.4) - StarDateTime.now()

# Documentation

# Installation

:::console
$ pip install stardatetime
