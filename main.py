# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "40:02"))
# answer: 1:08 AM


# Run unit tests automatically
# main(module='test_module', exit=False)