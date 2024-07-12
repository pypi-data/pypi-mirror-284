RYE_EXEC ?= rye run
PYTHON_VERSION ?= 3.8
PATH := $(HOME)/.rye/shims:$(PATH)

SHELL := /bin/bash
PYTHON_FILES := $(shell find src/ -type f -name '*.py' -o -name '*.pyi')

USE_UV ?= true
REQUIRED_UV_VERSION ?= 0.2.24
REQUIRED_RYE_VERSION ?= 0.36.0
bootstrap-uv:
	@INSTALLED_UV_VERSION=$$(uv --version 2>/dev/null | awk '{print $$2}' || echo "0.0.0"); \
    UV_VERSION=$$(printf '%s\n' "$(REQUIRED_UV_VERSION)" "$$INSTALLED_UV_VERSION" | sort -V | head -n1); \
	if [ "$$UV_VERSION" != "$(REQUIRED_UV_VERSION)" ]; then \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	fi

bootstrap: bootstrap-uv
	@INSTALLED_RYE_VERSION=$$(rye --version 2>/dev/null | head -n1 | awk '{print $$2}' || echo "0.0.0"); \
	DETECTED_RYE_VERSION=$$(printf '%s\n' "$(REQUIRED_RYE_VERSION)" "$$INSTALLED_RYE_VERSION" | sort -V | head -n1); \
	if [ "$$DETECTED_RYE_VERSION" != "$(REQUIRED_RYE_VERSION)" ]; then \
		rye self update || curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" RYE_VERSION="$(REQUIRED_RY_VERSION)" bash; \
	fi
	@rye config --set-bool behavior.use-uv=$(USE_UV)
	@rye pin --relaxed $(PYTHON_VERSION)


bootstrap-latest:
	@$(MAKE) bootstrap REQUIRED_RYE_VERSION=latest REQUIRED_UV_VERSION=latest
	@rye --version
	@uv --version
.PHONY: bootstrap-latest


install: bootstrap
	@rye sync -f
	@cp requirements-dev.lock requirements-dev-py$$(echo $(PYTHON_VERSION) | sed "s/\.//").lock
.PHONY: install


sync: bootstrap
	@rye sync --no-lock
.PHONY: sync

lock: bootstrap
ifdef update_all
	@rye sync --update-all
else
	@rye sync
endif
	@cp requirements-dev.lock requirements-dev-py$$(echo $(PYTHON_VERSION) | sed "s/\.//").lock
.PHONY: lock


update: bootstrap
	@$(MAKE) lock update_all=1
.PHONY: update

format:
	@$(RYE_EXEC) ruff check --fix src/
	@$(RYE_EXEC) isort src/
	@$(RYE_EXEC) ruff format src/
.PHONY: format

lint:
	@$(RYE_EXEC) ruff check src/
	@$(RYE_EXEC) ruff format --check src/
	@$(RYE_EXEC) isort --check src/
.PHONY: lint

test:
	@$(RYE_EXEC) tox -e system-unit,system-immutables
.PHONY: test

doctest:
	@$(RYE_EXEC) tox -e system-doctest
.PHONY: test

mypy:
	@$(RYE_EXEC) tox -e system-staticcheck
.PHONY: mypy

pyright:
	@$(RYE_EXEC) pyright src/xotless
.PHONY: pyright


SPHINXOPTS ?= -W
docs/build:
	make SPHINXOPTS=$(SPHINXOPTS) SPHINXBUILD="$(RYE_EXEC) sphinx-build" -C docs html
.PHONY: docs/build


CADDY_IMAGE ?= caddy:2.7-alpine
CADDY_SERVER_PORT ?= 6942
docs/browse: docs/build
	@docker run --rm --network host \
        -v $(PWD)/docs/build/html/:/var/www \
        -it $(CADDY_IMAGE) \
	    caddy file-server --browse --listen :$(CADDY_SERVER_PORT) --root /var/www
.PHONY: docs/browse
