*** install python first (check the previous lessons) ***
pyenv install 3.10.2
in the folder you are working: pyenv local 3.10.2
python -m venv env_3.10.2
then activate the virtual environment
on windows: env_3.10.2/Scripts/activate
on linux: source env_3.10.2/bin/activate

*** install package ***
pip install --upgrade pip-tools pip setuptools
pip-compile --upgrade --generate-hashes --output-file requirements/main.txt requirements/main.in


pip-sync requirements/main.txt
