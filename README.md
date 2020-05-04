
# display-timedelta

Simple package for displaying timedeltas for human consumption

Basic usage example

```python
>>> from datetime import timedelta
>>> from display_timedelta import display_timedelta
>>> display_timedelta(timedelta(hours=25, seconds=3))
'1 day, 1 hour, and 3 seconds'
>>> display_timedelta(timedelta(0))
'right now'
```
