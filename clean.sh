<<<<<<< HEAD
#autopep8 ./ --recursive --in-place -a
#yapf -ir .
#autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r ./
black .
mypy .
flake8 .
isort --check .
=======
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
>>>>>>> homework6
py.test tests