echo STARTING BLACK
black .
echo STARTING MYPY
mypy .
echo STARTING FLAKE8
flake8 homework6
flake8 tests
echo STARTING CHECK ISORT
isort --check .
echo STARTING ISORT
isort .
echo RUNNING TESTS
py.test tests