# Static Code Analysis Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Shell command execution using `os.system()` | Security - High | 63 | Executes a shell command, which may introduce command-injection risks. | Removed `os.system()` and replaced it with a normal Python print statement. |
| MD5 hashing | Security - High | 52 | MD5 is unsuitable for security-sensitive hashing. | Replaced `hashlib.md5()` with `hashlib.sha256()`. |
| Unsafe use of `eval()` | Security - Medium | 47 | `eval()` can execute arbitrary Python expressions. | Replaced it with a direct baggage-fee calculation using a surcharge rate. |
| Mutable default argument | Bug | 15 | The default list `baggage_tags=[]` may be shared across function calls. | Changed the default to `None` and initialized a new list inside the function. |
| Hardcoded API secret | Security - Low | 75 | A secret stored directly in source code can be exposed. | Read the secret from the `AIRLINE_API_SECRET` environment variable and avoided printing its value. |
| Insecure random number generation | Security - Low | 56 | The `random` module is not designed for security-sensitive values. | Used the `secrets` module to generate the boarding PIN. |
| Bare exception handler | Security - Low / Code Quality | 31 | A bare `except` silently hides errors and makes debugging difficult. | Replaced it with an explicit check to determine whether the flight exists. |
| File handling without a context manager | Code Quality | 60 | Manually opening and closing a file can leave it open if an error occurs. | Used `with open()` and specified UTF-8 encoding. |
| Incorrect function naming | Code Quality | 15, 27, 35, 45, 51, 55, 59, 66 | Function names did not follow Python's snake_case naming convention. | Renamed functions using snake_case. |
| Missing docstrings | Code Quality | Multiple | The module and functions lacked documentation. | Added a module docstring and function docstrings. |
| Unused imports and variables | Code Quality | 4, 36, 46, 68 | Unused imports and variables reduced code clarity. | Removed unused imports and variables. |
| Comparison with `None` using `==` | Style | 37 | Comparing with `None` using `==` does not follow the recommended Python convention. | Changed the comparison to `is None`. |
| Long lines | Style | 7–9, 23 | Some lines exceeded the recommended line length. | Reformatted long lines to satisfy Flake8. |
| Missing newline at end of file | Style | 87 | The original file did not end with a newline. | Added a final newline. |
