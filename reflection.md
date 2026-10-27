# Reflection – Lab 5: Static Code Analysis

## 1. What were the most important issues identified in the original code?

The original flight reservation system contained both security vulnerabilities and code-quality problems. The most serious issues included the use of `eval()`, which can execute potentially unsafe expressions, the use of MD5 for hashing passenger information, and the use of `os.system()` to execute a shell command. Other problems included a mutable default argument, a broad exception handler, an embedded secret token, unused variables, and inconsistent function naming. These issues showed that code can run while still having security and maintainability problems.

## 2. How did Pylint, Bandit, and Flake8 help improve the code?

Each tool helped identify a different category of problems. **Pylint** identified code-quality issues such as missing docstrings, inconsistent naming, unused variables, and poor programming practices. **Bandit** detected potential security risks, including unsafe use of `eval()`, MD5 hashing, and shell command execution. **Flake8** identified style and formatting problems such as long lines, unused imports, and missing newlines. Using all three tools provided a more complete analysis than relying on only one tool.

## 3. What changes were made to fix the identified issues?

I improved the code by replacing `eval()` with a safer baggage-fee calculation, replacing MD5 with SHA-256, and using Python's `secrets` module to generate a boarding PIN. I removed the shell command and used safer file handling with a `with open()` statement and UTF-8 encoding. I also replaced the mutable default list with `None`, handled invalid flight numbers explicitly, used `is None` for comparisons, renamed functions using snake_case, removed unused variables and imports, and added a module docstring. The API secret is now read from an environment variable instead of being hardcoded or printed.

## 4. What did you learn from this lab?

I learned that static code analysis examines source code for potential issues without requiring the program to be executed. I also learned that different tools focus on different aspects of code quality, security, and style. Fixing the reported issues made the program cleaner, safer, and easier to maintain. After making the changes, Pylint improved from **4.00/10 to 10.00/10**, Bandit reported **no issues**, and Flake8 produced an empty report, indicating that it found no remaining violations. This lab taught me that static analysis should be part of the development process, although passing these tools does not guarantee that a program is completely free of bugs or security vulnerabilities.
