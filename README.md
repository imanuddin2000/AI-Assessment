# AI Assessment Submission

This repository contains my solutions for the AI assessment. Below are the details for each part of the test, instructions on how to set up the environment, and steps to run the code.

## Table of Contents
1. [File Structure](#file-structure)
2. [Environment Setup](#environment-setup)
3. [How to Run the Code](#how-to-run-the-code)
4. [Using Visual Studio Code](#using-visual-studio-code)

## File Structure

The repository is structured as follows:

- **ai_solution_design/**: Contains solutions and scripts related to the AI Solution Design Test.
- **ai_technical/**: Contains scripts, the REST API, and test scripts related to the AI Technical Test.
- **AI_Theoretical_Test.ipynb**: A Jupyter Notebook with my responses to the AI Theoretical Test.
- **Programming_Test.ipynb**: A Jupyter Notebook with solutions to the programming test exercises.
- **environment.yml**: Conda environment file to recreate the Python environment used.
- **README.md**: This file, providing setup and usage instructions.

## Environment Setup

### Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution) should be installed.
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/) with the Python extension.

### Steps to Recreate the Environment

1. **Download and Install Miniconda**:
   - If Miniconda is not installed, download it from [here](https://docs.conda.io/en/latest/miniconda.html) and follow the installation instructions for your operating system.

2. **Clone or Download the Repository**:
   - Download the compressed file `AI_Test_YourName.zip` and extract it to your desired directory.

3. **Open a Terminal**:
   - Open the terminal in the extracted folder or use the terminal in Visual Studio Code.

4. **Create the Conda Environment**:
   - Run the following command to create the environment from the `environment.yml` file:

    ```bash
    conda env create -f environment.yml
    ```

5. **Activate the Environment**:
   - After the environment is created, activate it using:

    ```bash
    conda activate your_env_name
    ```

   Replace `your_env_name` with the actual environment name listed in the `environment.yml` file.

6. **Install Additional Dependencies (If Any)**:
   - Some dependencies might not be captured in `environment.yml`. Follow the instructions in each folder’s specific `README` (if any) for additional dependencies.

## How to Run the Code

### AI Theoretical Test

- Open the `AI_Theoretical_Test.ipynb` file in Jupyter Notebook or VS Code.
- Ensure that the correct Conda environment (`your_env_name`) is selected as the Python interpreter.
- Run the cells to see the responses.

### Programming Test

- Navigate to the `Programming_Test` folder.
- Follow the instructions in the folder’s specific README or run the main script using:

    ```bash
    python main_script.py
    ```

   Replace `main_script.py` with the actual filename of the script.

### AI Solution Design and Technical Test

- Navigate to the `ai_solution_design` and `ai_technical` folders.
- Follow the instructions provided in their specific READMEs to run the scripts, REST API, and test cases.

## Using Visual Studio Code

1. **Open the Project in VS Code**:
   - Launch VS Code and open the folder containing the project.

2. **Select the Python Interpreter**:
   - Open the Command Palette by pressing `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac).
   - Type `Python: Select Interpreter` and choose the Conda environment (`your_env_name`).

3. **Run the Code**:
   - Open any script or Jupyter Notebook and run it using the built-in terminal or notebook interface in VS Code.

## Contact Information

If you have any questions or need further assistance, please feel free to contact me at [Your Email Address].

Thank you for reviewing my submission!

