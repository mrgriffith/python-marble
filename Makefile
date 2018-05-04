# Makefile for the DMA project
DMA_REPO=.
EXTERN_REPO=$(DMA_REPO)/extern/
EXTERN_COMMON_REPO=$(EXTERN_REPO)/common
# PROTO where the source .proto files live
PROTO_SOURCE=$(EXTERN_COMMON_REPO)/messaging/proto
# generated protobuf files
PROTOBUF_DMA=$(DMA_REPO)/dma/protobuf

# Documentation Directory
DOCROOT=$(DMA_REPO)/html

CONNECTION=$(EXTERN_COMMON_REPO)/messaging/python/Connection.py

REQS=$(PROTOBUF_DMA)/Connection.py \
	$(PROTOBUF_DMA)/CMN_MAPI_pb2.py \
	$(PROTOBUF_DMA)/DMA_MAPI_pb2.py \
	$(PROTOBUF_DMA)/__init__.py

all: PRE $(REQS)

PRE: 
	@# cannot store empty directories in git, so we need to create 
	@# $(PROTOBUF_DMA) if it does not exist
	@test -d $(PROTOBUF_DMA) || mkdir $(PROTOBUF_DMA)

$(PROTOBUF_DMA)/Connection.py: $(CONNECTION)
	cp $< $@

# -------------------- protocol buffer messages  ----------------------
# Common messages
$(PROTOBUF_DMA)/CMN_MAPI_pb2.py: $(PROTO_SOURCE)/CMN_MAPI.proto
	protoc -I=$(PROTO_SOURCE) --python_out=$(PROTOBUF_DMA) $(PROTO_SOURCE)/CMN_MAPI.proto

# DMA messages
$(PROTOBUF_DMA)/DMA_MAPI_pb2.py: $(PROTO_SOURCE)/DMA_MAPI.proto
	protoc -I=$(PROTO_SOURCE) --python_out=$(PROTOBUF_DMA) $(PROTO_SOURCE)/DMA_MAPI.proto

$(PROTOBUF_DMA)/__init__.py:
	touch $(PROTOBUF_DMA)/__init__.py
# -------------------- protocol buffer messages  ----------------------

.PHONY: test
test:
	py.test

coverage:
	py.test --cov --cov-report term-missing

clean: pyclean
	@rm -f $(REQS) $(DMA)/*{.pyc,~}


pyclean:
	@rm $(REQS)
	@find . -name "*.pyc" | xargs rm
	@rm -rf test/__pycache__

check:
	@flake8 --exclude=dma/protobuf/*.py,extern/common

.PHONY: doc
doc:
	@test -d $(DOCROOT) || mkdir $(DOCROOT)
	@echo "Generating Design Document in $(DOCROOT)"
	@asciidoc --backend=html5 -a icons -a iconsdir=http://asciidoc.org/images/icons -o $(DOCROOT)/design.html doc/design.asciidoc

help:
	@echo "The following key make targets are available:"
	@echo " "
	@echo "all (default)  Compiles all protobuf targets"
	@echo "doc            Generates documentation"
	@echo "clean          Removes generated files from the build directory"
	@echo "docclean       Removes generated html files from the build directory"
	@echo "pyclean        Removes generated python files from the build directory"
	@echo "check          Checks source for style guide compliance"
	@echo "test           Runs tests for the DMA"
