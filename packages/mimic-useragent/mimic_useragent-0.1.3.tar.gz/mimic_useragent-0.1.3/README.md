# mimic_user_agent

A simple function that returns a random or static fake 'user-agent', Firefox browser only.

# Uso

```python
>>> from mimic_useragent import mimic_user_agent
>>> mimic_user_agent()
'Mozilla/5.0 (X11; Ubuntu; Linux; x86_64; rv:120.0) Gecko/20100101 Firefox/120.0'
>>> mimic_user_agent(seed=10)
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'
```

Receives an `int` parameter for the use of a *seed*, default is `None`.


# Tests

```python
python -m unittest
```
