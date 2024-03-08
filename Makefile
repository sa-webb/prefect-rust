.PHONY:
	dev, run

dev:
	maturin develop

run:
	python main.py