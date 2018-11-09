pip freeze
nosetests --with-coverage --cover-package echarts_china_cities_pypkg --cover-package tests tests  docs/source echarts_china_cities_pypkg && flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
