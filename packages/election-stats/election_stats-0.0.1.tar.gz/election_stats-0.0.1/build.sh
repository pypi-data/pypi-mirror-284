rm dist/*
python3 -m build
git commit -m "v${$1}"
python3 -m twine upload --repository pypi dist/*