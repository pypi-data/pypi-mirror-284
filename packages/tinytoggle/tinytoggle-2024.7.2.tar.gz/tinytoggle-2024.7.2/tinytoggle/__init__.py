#!/usr/bin/env python3
from functools import partial
from typing import Any, Callable, Dict


class TinyToggle:
    def __init__(
        self, flag_func: partial, default_impl: Callable | None = None
    ):  # Uncomment to require default
        self.flag_func = flag_func
        self.flags: Dict[Any, Callable] = {}
        self.default_impl: Callable | None = default_impl

    def flag(self, flag_value: Any) -> Callable:
        """Wrapper to pass the flag_value to the FlagFeature Dict"""

        def decorator(func: Callable) -> Callable:
            """Callable func passed from the decorator, called via flag wrapper. flag_value is in scope"""
            self.flags[flag_value] = func
            return func

        return decorator

    def default(self, func: Callable) -> Callable:
        """Implement a default function"""
        self.default_impl = func
        return func

    def __call__(self, *args, **kwargs) -> Any:
        """When the object is called, __call__ will get the flag from the flag_func and call the
        correct implementation with whatever args and kwargs are given for that call.
        """
        flag_value = self.flag_func()
        implementation = self.flags.get(flag_value, self.default_impl)
        if implementation is None:
            raise ValueError(f"No implementation found for flag value: {flag_value}")
        return implementation(*args, **kwargs)
