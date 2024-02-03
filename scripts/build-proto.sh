#!/bin/bash
echo "building service proto definition $0"

TARGET="SERVER"
if [ $# -eq 0 ]
  then
    TARGET="SERVER"
  else
    TARGET="$1"
fi

if [ "$TARGET" = "SERVER" ]
    then
        echo "target server"
        python3 -m grpc_tools.protoc --python_out=./src --grpc_python_out=./src --pyi_out=./src --proto_path=. proto/route_guide.proto
    else
        echo "target $TARGET"
        python3 -m grpc_tools.protoc --python_out=./client --grpc_python_out=./client --proto_path=. proto/route_guide.proto
fi

# python3 -m grpc_tools.protoc --python_out=./src --grpc_python_out=./src --pyi_out=./src --proto_path=. proto/route_guide.proto