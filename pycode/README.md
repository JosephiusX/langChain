#Setup

##1.[Gpt_Api_Key]

Sign up for free key

##2.[Python_Installation]

* Anaconda gives me access to miniconda which I use to set up environments and install dependancies

##3.[Environment_Setup]

Create a Project directory, navigate to it , creat a conda encironment to be activated. Then We install deps.

in windows terminal:

    mkdir gptLang
    cd gptLang
    conda create -n gptLang_env python langchain openai

in miniconda Prompt:

    conda activate gptLang_env python

back in terminal:

    conda install langchain openai
    touch main.py

pip install python-dotenv

