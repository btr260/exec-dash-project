# exec-dash-project

# "Robo Advisor" Project


## Program Overview

  1. Synthesizes data from CSV files into a monthly sales report.
  2. Takes user input (from command line) of reporting period of interest from a list of available periods.
  3. Presents total monthly sales and sales by products in chart form and in the command line.



### Repo Setup

Use the GitHub.com online interface to create a new remote project repository called something like "exec-dash". When prompted by the GitHub.com online interface, add a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like `https://github.com/YOUR_USERNAME/exec-dash`.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/exec-dash
```

Create and activate a new Anaconda virtual environment:

```sh
conda create -n dash-env python=3.7 # (first time only)
conda activate dash-env
```

From within the virtual environment, install the required packages specified in the "requirements.txt" file:

```sh
pip install -r requirements.txt
```

From within the virtual environment, run the Python script from the command-line:

```sh
python app/exec-dash.py
```
