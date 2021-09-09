#autopep8 ./ --recursive --in-place -a
#yapf -ir .
#autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r ./
echo STARTING BLACK
black .
echo STARTING MYPY
mypy .
echo STARTING FLAKE8
flake8 .
echo STARTING CHECK ISORT
isort --check .
echo STARTING ISORT
isort .
echo RUNNING TESTS
py.test tests