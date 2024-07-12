from functools import partial

from tinytoggle import TinyToggle


class UsageFlag:
    def __init__(self):
        self.flag = None

    def get_flag_value(self, parameter: str):
        """Mock function to allow us to change the flag in demo"""
        print(f"Getting flag from vault: {parameter=}")
        return self.flag


usage_flag = UsageFlag()

usage_flag_function = partial(usage_flag.get_flag_value, "optional_flag_parameter")


# def default_implementation():
#     print("Default implementation")


# Define a feature flag
text_to_print_on_screen = TinyToggle(
    usage_flag_function
)  # , default_implementation)  # Uncomment if default required


# Define implementations for different flag values
@text_to_print_on_screen.flag("blue")
def blue_implementation():
    print("Blue implementation")


@text_to_print_on_screen.flag("green")
def green_implementation():
    print("Green implementation")


@text_to_print_on_screen.flag(True)
def true_implementation():
    print("True implementation")


@text_to_print_on_screen.flag(False)
def false_implementation():
    print("False implementation")


@text_to_print_on_screen.default
def default_implementation():
    print("Default implementation")


if __name__ == "__main__":
    for f in ["blue", "green", True, False, "unknown"]:
        usage_flag.flag = f
        print(f"\nFlag is set to: {f}")
        text_to_print_on_screen()  # Calling the same function each time
