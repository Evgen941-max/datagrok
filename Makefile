buiid:
	docker build -f Dockerfile -t pest:py .

compose:
	docker-compose up --build