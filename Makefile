buiid:
	docker build -f Dockerfile -t pest:py .

compose:
	docker-compose up --build

compose-scale:
	docker-compose up --scale flask_cpu=2