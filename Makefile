.PHONY: build publish test

build:
    poetry build

publish:
    poetry publish

clean:
    rm -rf dist

test:
    pytest