docs:
	python setup.py upload_docs --upload-dir docs/build/html

upload:
	make clean
	python3 setup.py sdist bdist_wheel && twine upload dist/*

clean:
	python setup.py clean --all
	pyclean .
	rm -rf *.pyc __pycache__ build dist asr.egg-info asr/__pycache__ tests/__pycache__ tests/reports docs/build

test:
	nosetests --with-coverage --cover-erase --cover-package asr --logging-level=INFO --cover-html
	cheesecake_index -n asr -v

count:
	cloc . --exclude-dir=docs,cover,dist,asr.egg-info