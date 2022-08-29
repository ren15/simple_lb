.PHONY: $(MAKECMDGOALS)

test:
	bash scripts/test_1.sh

docker_build:
	bash scripts/docker_build.sh

docker_run_server:
	bash scripts/docker_run_server.sh

docker_run_client:
	bash scripts/docker_run_client.sh
	