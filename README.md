# translate-with-AWS-lambda


## Create virtual environment
======================

    ubuntu:~/environment/translate-with-AWS-lambda/src (main) $ python3 -m venv ~/.venv
    ubuntu:~/environment/translate-with-AWS-lambda/src (main) $ source ~/.venv/bin/activate
    (.venv) ubuntu:~/environment/translate-with-AWS-lambda/src (main) $ which python3
    /home/ubuntu/.venv/bin/python3  
 
## Install dependencies
======================

    (.venv) ubuntu:~/environment/translate-with-AWS-lambda/src (main) $ pip install ipython
    (.venv) ubuntu:~/environment/translate-with-AWS-lambda/src (main) $ pip install boto3


## Test translate-cli.py
======================

    (.venv) ubuntu:~/environment/translate-with-AWS-lambda/src (main) $ python3  translate-cli.py
    Put in a phrase in any language to translate: on va manger
    Translate phrase: on va manger
    we're going to eat
    (.venv) ubuntu:~/environment/translate-with-AWS-lambda/src (main) $ python3  translate-cli.py --phrase "j'en marre"
    Translate phrase: j'en marre
    I'm tired of
    (.venv) ubuntu:~/environment/translate-with-AWS-lambda/src (main) $ python3  translate-cli.py --help
    Usage: translate-cli.py [OPTIONS]

    Options:
      --phrase TEXT  This is a tool that translates text
      --help         Show this message and exit.
