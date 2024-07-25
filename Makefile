build:
	docker build . -f Dockerfile -t order-service
runlocal:
	docker run -it -v $(PWD):/src -p 8000:8000 --rm --name order-dev order-service uvicorn main:app --host 0.0.0.0 --port 8000
test:
	docker run -it -v $(PWD):/src --rm --name order-test order-service pytest