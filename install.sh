venvDir='venv'
[ -d "$venvDir" ] || python -m venv "$venvDir"
source "$venvDir"/bin/activate
pip install -r requirements.txt