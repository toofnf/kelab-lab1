.PHONY: docker-run

IMAGE_NAME = lab1-docker
IMAGE_TAG_GOOD = good
IMAGE_TAG_BAD = bad
PYTHON_BASE_VERSION = 3.10
PYTHON_IMAGE = slim-buster
PORT ?= 9000
PORT_BAD ?= 9001

docker-run-good: # Build and run service in Docker
	docker build \
		--build-arg PYTHON_BASE_VERSION=$(PYTHON_BASE_VERSION) \
		-t $(IMAGE_NAME):$(IMAGE_TAG_GOOD) \
		-f docker/Dockerfile \
		.
	docker run --rm -it \
		-p $(PORT):$(PORT) \
		$(IMAGE_NAME):$(IMAGE_TAG_GOOD)

docker-run-bad: # Build and run service in Docker
	docker build \
		-t $(IMAGE_NAME):$(IMAGE_TAG_BAD) \
		-f docker/Dockerfile-bad \
		.
	docker run --rm -it \
		-p $(PORT_BAD):$(PORT_BAD) \
		$(IMAGE_NAME):$(IMAGE_TAG_BAD)

