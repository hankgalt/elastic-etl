
# install
install:
	@echo "installing requirements"
	pip3 install --upgrade pip && pip install -r requirements.txt

# build service proto
.PHONY: build-proto
build-proto:
	@echo "building latest proto"
	scripts/build-proto.sh $(TARGET)

# start server
.PHONY: start-server
start-server:
	@echo "starting gRPC server"
	python3 src/server.py

# run client
.PHONY: run-client
run-client:
	@echo "running client to test server"
	python3 client/route_guide_client.py

# check tests
.PHONY: check-tests
check-tests:
	@echo "check test runr"
	python3 src/test_utils.py
