#autopep8 ./ --recursive --in-place -a
#yapf -ir .
#autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r ./
black .
mypy .
flake8 .
isort .
py.test tests