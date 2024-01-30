![Gojo_Satoru](./images/Gojo_Satoru.jpg)

# HOW TO USE THE SCRIPT

## Clone the repo
    gh repo clone JVAparicio/Jujutsu_Kaisen_url_to_pdf

## SETUP

### To be able to create a virtual environment
    pip install pipenv

### Create a virtual environment with a python version that you already have
    pipenv --python 3.10

### Install the necessary packages
    pipenv install requirements.txt

### Start the virtual environment
    pipenv shell

### Give the scripts the execution permissions
    chmod +x download_jjk_chapter.py



## RUN
### Run the script choosing the output directory and the chapter that you want

    python download_jjk_chapter.py <chapter> <output_directory>

    Example:
    python download_jjk_chapter.py 182 /mnt/e/Projects/Jujutsu_Kaisen/