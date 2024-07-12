Decorator for implementing singleton pattern

## Usage

To install, add `pygleton` module to your project. Then add
`from pygleton import singleton` to your file.

There are two ways to use the decorator: without repetetive `__init__()` calls
and with them (you do not want this unless you know what are you doing).

### Main scenario: call init only the first time

Do not pass any parameter to the decorator:

```python
@singleton()
class Foo:
    ...
```

Now, when you do `Foo(...)` for the first time, object instance will be created,
and `Foo` init method would be called. Any subsequent `Foo(...)` calls will
return the same instance, and `Foo.__init__` will be completely ignored.

### I know what I am doing: I want to call init every time

Pass truthy value to `recall_init` parameter of the decorator:

```python
@singleton(recall_init=True)
class Foo:
    ...
```

Now, when you do `Foo(...)` for the first time, object instance will be created,
and all subsequent `Foo(...)` calls will return the same instance. However,
**init method will be called every time.**

### Usage example

See test file.

## Development

The project uses poetry (highly recommended) and you should know your way
around. The supplied `Makefiles` allows to run linters, check formatting, and
run tests (100% coverage is required!) simply by typing `make`. Everything
should pass.
