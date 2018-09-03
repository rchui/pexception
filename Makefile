default: test

setup: develop

bdist bdist_wheel build develop install sdist: %:
	python setup.py $@

release:
	python setup.py register
	python setup.py release

test:
	@tox

clean:
	@find . -name \*~ -exec rm -v '{}' +
	@find . -name \*.pyc -exec rm -v '{}' +
	@find . -name __pycache__ -prune -exec rm -vfr '{}' +
	@rm -rf build bdist cover dist sdist
	@rm -rf .tox .eggs
	@find . \( -name \*.orig -o -name \*.bak -o -name \*.rej \) -exec rm -v '{}' +
	@rm -rf distribute-* *.egg *.egg-info *.tar.gz cover junit.xml coverage.xml .cache

.PHONY: default setup test clean
