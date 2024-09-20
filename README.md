# PHASE3 FINAL PROJECT : PRODUCTS INVENTORY CLI STORE

## Prerequisites

- For this phase 3 project, you will create a CLI and ORM application in Python. The major learning goals of project include;

    - A CLI application that solves a real-world problem and adheres to best practices.
    - A database created and modified with SQLAlchemy ORM with 3+ related tables.
    - A well-maintained virtual environment using Pipenv.
    - Proper package structure in your application.
    - Use of lists, dicts, and tuples.

## System Requirements

For you to be able to run this program on your local machine, ensure your machine meets the following requirements:

1. Ensure you have an IDE, e.g., VSCode.
2. Ensure you have installed Python3 on your computer. If not, follow the links below:
   - For Windows: [Python3-Installation-Steps:Windows](https://builtin.com/software-engineering-perspectives/how-to-install-python-on-windows)
   - For Linux: [Python3-Installation-Linux](https://docs.python-guide.org/starting/install3/linux/)
   - For Mac: [Python3-Installation-Mac](https://phoenixnap.com/kb/install-python-mac)

3. 8GB and above of RAM
4. Intel Core i5 and above processor

## Installation

Follow the steps below to install the program on your computer:

1. Open your terminal in Ubuntu or the CLI in Windows on your machine.
2. Clone this repository to your machine by running the following command:
    ```console
    $ git clone git@github.com:KhisaBethuel/phase3-Project.git
    ```
3. After cloning, navigate to the project folder:
    ```console
    $ cd phase3-Project
    ```
4. Open the project folder in your IDE by running:
    ```console
    $ code .
    ```
5. Install the dependencies using Pipenv:
    ```console
    $ pipenv install
    ```
6. Set up the database:
    ```console
    $ pipenv run python lib/db/seed.py
    ```

## Running the Program

To run this program, open the `cli.py` file as it is the entry point for the program. You can interact with the application through various inputs to test its functionality. 

Open the terminal and type the following command to see the output:
```console
$ pipenv run python lib/cli.py
```
