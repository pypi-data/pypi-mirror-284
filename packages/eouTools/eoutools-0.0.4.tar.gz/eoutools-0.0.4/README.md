# eouTools
## Requirements
- python >= 3.10 (Required)
- python >= 3.12 (Suggested)
## eouTools.numbers
### isPositive
Syntax: isPositive(n: int | float) -> bool<br>
Alternative: `not isNegative(n)`<br>
Documentation: "Returns whether `n` is positive or not"

### isNegative
Syntax: `isNegative(n: int | float) -> bool`<br>
Alternative: `not isPositive(n)`<br>
Documentation: "Returns whether `n` is negative or not"

### isZero
Syntax: `isZero(n: int | float) -> bool`<br>
Alternative: `n == 0`<br>
Documentation: "Returns whether `n` is zero or not"

## eouTools.decorators
### rename_on_init
Syntax: `@rename_on_init(name: str)`<br>
Documentation: "Rename a function when it is initialized. This may raise unexpected behavior, however"

## eouTools.benchmarking.decorators
### time_func
Syntax: `@time_func`<br>
Documentation: "Time a function. Parse in the keyworded argument `_no_time = True` to get the return instead of the time it took to execute"
### memoize
Syntax: `@memoize`<br>
Documentation: "Create a cache of all results given by a function. run the `.delete_cache()` function to delete the cache. Can be used to speed up certain algorithms such as recursive Fibonacci sequence"