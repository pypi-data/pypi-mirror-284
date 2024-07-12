.PHONY: clean

clean:
	rm -rf dist

build: clean
	hatch build

deploy-check:
	pipx run twine check dist/*

deploy-test:
	pipx run twine upload --repository-url=https://test.pypi.org/legacy/ dist/*

deploy: deploy-check
	pipx run twine upload dist/*