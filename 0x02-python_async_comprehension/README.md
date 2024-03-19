Overview:
This project, titled "0x02-python_async_comprehension," explores asynchronous comprehension in Python. Asynchronous programming allows tasks to run concurrently, improving performance by leveraging the capabilities of modern computer architectures. Comprehensions are concise and expressive constructs in Python for generating collections such as lists, sets, and dictionaries. This project combines these two concepts to demonstrate how asynchronous programming can be utilized with comprehensions for efficient and streamlined code execution.

Contents:
async_comprehension.py: This file contains examples and demonstrations of asynchronous comprehensions in Python. It showcases how asynchronous operations can be integrated with comprehensions to perform tasks concurrently, thus enhancing performance in certain scenarios.

requirements.txt: This file lists the dependencies required to execute the code in async_comprehension.py. These dependencies can be installed via pip using the command pip install -r requirements.txt.

README.md: This document provides an overview of the project, instructions for executing the code, and any additional information deemed necessary for users or contributors.

Execution:
To execute the code in async_comprehension.py, follow these steps:

Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/Edwinogechi/0x02-python_async_comprehension.git
Navigate to the project directory:
bash
Copy code
cd 0x02-python_async_comprehension
Install the dependencies using pip:
Copy code
pip install -r requirements.txt
Run the script:
Copy code
python async_comprehension.py
Additional Information:
This project is licensed under the MIT License.
Contributions, bug reports, and feedback are welcome. Please feel free to open an issue or submit a pull request on the project's GitHub repository.
For more information or assistance, contact the project maintainer(s) listed in the README.md file or the repository's contributors.
Contributors:
Edwin ogechi




TASKS

0. Async Generator
mandatory
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

1. Async Comprehensions
mandatory
Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.

2. Run time for four parallel comprehensions
mandatory
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
