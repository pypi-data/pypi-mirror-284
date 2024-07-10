"""This module contains the PrecisionTimer class that wraps the bound C++ timer class and provides a high-level API for
the timer functionality.

The module is exposed to the highest level of the library (through init-based relative imports). All interactions with
the low-level C-API should be carried out through the wrapper class where possible.
"""

from typing import Literal

from ataraxis_base_utilities import console

from ..precision_timer_ext import CPrecisionTimer  # type: ignore


class PrecisionTimer:
    """Provides sub-microsecond-precision interval-timing and blocking / non-blocking delay functionality.

    This is a wrapper for a C++ class that uses 'chrono' library to interface with the highest available precision clock
    of the host system. All methods are implemented in C++, which makes them both significantly faster and more precise
    compared to any pure-python implementation. The class itself operates in nanoseconds, but it automatically converts
    all inputs and outputs from the user-defined precision to nanoseconds and back.

    Notes:
        The actual clock precision depends on the precision and frequency of the system CPU clock that runs this code.
        The class methods mostly have fairly minor overheads ~100 ns, but some OS-based methods used in the class
        (e.g., sleep) may incur longer delays. It is highly advised to test this timer prior to running it in production
        projects to characterize the overhead associated with using different timer methods.

        Use delay_noblock when you want this class to release GIL and delay_block when you do not want this class to
        release GIL.

    Attributes:
        _supported_precisions: A tuple of currently supported precision string-options. Used internally for input
            verification and error-messaging purposes.
        _timer: The inner binding-class generated by nanobind to expose C++ API. Since the class has no stubs at the
            time of writing, the best way to use this library is via the PrecisionTimer (this) wrapper class.

    Args:
        precision: The desired precision of the timer. Accepted values are 'ns' (nanoseconds), 'us' (microseconds),
            'ms' (milliseconds) and 's' (seconds). The argument is case-insensitive.

    Raises:
        ValueError: If the input precision is not one of the accepted options.
    """

    def __init__(self, precision: Literal["ns", "us", "ms", "s"] = "us") -> None:
        self._supported_precisions = ("ns", "us", "ms", "s")

        # Casts to the lower case
        precision = precision.lower()  # type: ignore

        # If the input precision is not supported, raises an error
        if precision not in self._supported_precisions:
            message = (
                f"Unsupported precision argument value ({precision}) encountered when initializing PrecisionTimer "
                f"class. Use one of the supported precision options: {self._supported_precisions}."
            )
            console.error(message=message, error=ValueError)
            raise ValueError(message)  # Fallback should not be reachable

        # Otherwise, initializes the C++ class using the input precision
        self._timer = CPrecisionTimer(precision=precision)

    def __repr__(self) -> str:
        """Generates and returns a string representation of the PrecisionTimer object."""
        representation_string: str = (
            f"PrecisionTimer(precision={self.precision}, elapsed_time = {self.elapsed} {self.precision}.)"
        )
        return representation_string

    @property
    def elapsed(self) -> int:
        """Returns the time passed since the last timer checkpoint (instantiation or reset() call), converted to the
        requested time units.

        The time is automatically rounded to the nearest supported integer precision unit.

        Notes:
            This functionality does not clash with delay functionality of the class. The timer used to delay code
            execution is different from the timer used to calculate elapsed time.
        """
        return self._timer.Elapsed()  # type: ignore

    @property
    def precision(self) -> str:
        """Returns the units currently used by the timer ('ns', 'us', 'ms' or 's')."""
        return self._timer.GetPrecision()  # type: ignore

    @property
    def supported_precisions(self) -> tuple[str, str, str, str]:
        """Returns a tuple that stores all currently supported time unit options."""
        return self._supported_precisions

    def reset(self) -> None:
        """Resets the timer by re-basing it to count time relative to the call-time of this method."""
        self._timer.Reset()

    def delay_noblock(self, delay: int, *, allow_sleep: bool = False) -> None:
        """Delays code execution for the requested period of time while releasing the GIL.

        Use this method to delay code execution while allowing other threads (in multithreaded environments) to run
        unhindered. Defaults to using the non-cpu-releasing busy-wait method due to its higher precision compared to
        the CPU-releasing method.

        Notes:
            Even if sleeping is allowed, the method will only sleep if the duration is long enough to resolve the
            inherent overhead of the sleep() method (~1 ms). Currently, this means it will not run for nanosecond and
            microsecond timers.

            This functionality does not clash with 'elapsed time' functionality of the class. The timer used to delay
            code execution is different from the timer used to calculate elapsed time.

        Args:
            delay: The integer period of time to wait for. The method assumes the delay is given in the same precision
                units as used by the timer (if the timer uses 'us', the method assumes the duration is also in 'us').
            allow_sleep: A boolean flag that allows using CPU-releasing sleep() method to suspend execution for
                durations above 1 millisecond. Defaults to False.
        """
        self._timer.DelayNoblock(delay, allow_sleep)

    def delay_block(self, delay: int, *, allow_sleep: bool = False) -> None:
        """Delays code execution for the requested period of time while maintaining GIL.

        This method is similar to delay_noblock, except it does not release the GIL and, therefore, will prevent any
        other threads from running during the delay duration. Defaults to using the non-cpu-releasing busy-wait method
        due to its higher precision compared to the CPU-releasing method.

        Notes:
            Even if sleeping is allowed, the method will only sleep if the duration is long enough to resolve the
            inherent overhead of the sleep() method (~1 ms). Currently, this means it will not run for nanosecond and
            microsecond timers.

            This functionality does not clash with 'elapsed time' functionality of the class. The timer used to delay
            code execution is different from the timer used to calculate elapsed time.

        Args:
            delay: The integer period of time to wait for. The method assumes the delay is given in the same precision
                units as used by the timer (if the timer uses 'us', the method assumes the duration is also in 'us').
            allow_sleep: A boolean flag that allows using CPU-releasing sleep() method to suspend execution for
                durations above 1 millisecond. Defaults to False.
        """
        self._timer.DelayBlock(delay, allow_sleep)

    def set_precision(self, precision: Literal["ns", "us", "ms", "s"]) -> None:
        """Changes the precision used by the timer to the input string-option.

        This method allows reusing the same timer instance for different precisions, which is frequently more efficient
        than initializing multiple timers or re-initializing a class with a new precision.

        Args:
            precision: The desired precision of the timer. Accepted values are 'ns' (nanoseconds), 'us' (microseconds),
                'ms' (milliseconds) and 's' (seconds). The argument is case-insensitive.

        Raises:
            ValueError: If the input precision is not one of the accepted options.
        """

        # Casts to the lower case
        precision = precision.lower()  # type: ignore

        # If the input precision is not supported, raises an error
        if precision not in self._supported_precisions:
            message = (
                f"Unsupported precision argument value ({precision}) encountered when setting the precision of a "
                f"PrecisionTimer class instance. Use one of the supported precision options: "
                f"{self._supported_precisions}."
            )
            console.error(message=message, error=ValueError)
            raise ValueError(message)  # Fallback should not be reachable

        self._timer.SetPrecision(precision=precision)
