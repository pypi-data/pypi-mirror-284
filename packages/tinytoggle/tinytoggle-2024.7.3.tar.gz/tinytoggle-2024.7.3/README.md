# TinyToggle

TinyToggle is a lightweight, dependency-free Python module for implementing feature toggles (also known as feature flags) in your applications. It allows you to easily integrate your own flag evaluation functions, supporting various use cases such as load balancing, named features, and more.

## Features

- Lightweight and dependency-free (uses only Python built-ins)
- Flexible: bring your own flag evaluation function
- Easy to use and integrate into existing projects
- Supports multiple flag types (strings, booleans, etc.)
- Provides a default implementation option

## Installation

You can install TinyToggle using pip:

```
pip install tinytoggle
```

## Usage

Here's a basic example of how to use TinyToggle:

```python
from tinytoggle import TinyToggle

# Define your flag evaluation function
def get_flag_value(parameter):
    # Your logic to retrieve the flag value
    return "blue"

# Create a TinyToggle instance
my_feature = TinyToggle(get_flag_value)

# Define implementations for different flag values
@my_feature.flag("blue")
def blue_implementation():
    print("Blue implementation")

@my_feature.flag("green")
def green_implementation():
    print("Green implementation")

@my_feature.default
def default_implementation():
    print("Default implementation")

# Use the feature
my_feature()  # This will call the appropriate implementation based on the flag value
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Upcoming Features

- [ ] Add logging with JSON export of statistics
- [ ] Implement simple load balancer
- [ ] Add tests

## Acknowledgements

Thanks to all the contributors who have helped to improve TinyToggle.
