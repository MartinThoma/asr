docs:
	python setup.py upload_docs --upload-dir docs/build/html

update:
	python setup.py sdist upload --sign
	sudo pip install asr --upgrade

test:
	nosetests --with-coverage --cover-erase --cover-package asr --logging-level=INFO --cover-html
	cheesecake_index -n asr -v

count:
	cloc . --exclude-dir=docs,cover,dist,asr.egg-info