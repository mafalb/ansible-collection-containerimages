
DATE:=$(shell date +%Y%m%d)
DATE2:=$(shell date -Is)

playbooks/collections:
	ansible-galaxy collection install -r requirements.yml -p playbooks/collections

.PHONY: all

centos7-base: playbooks/collections
	OS=centos7 ansible-bender build -l org.label-schema.build-date=$(DATE) org.opencontainers.image.created=$(DATE2) --squash playbooks/base.yml $(if $(BASE_IMAGE), $(BASE_IMAGE), quay.io/centos/centos:centos7) $(if $(TARGET_IMAGE), $(TARGET_IMAGE), localhost/mafalb/centos7-base)

centos7-systemd: playbooks/collections
	ANSIBLE_COLLECTIONS_PATHS=../../..:playbooks/collections OS=centos7 ansible-bender build -l org.label-schema.build-date=$(DATE) org.opencontainers.image.created=$(DATE2) --squash playbooks/systemd.yml $(if $(BASE_IMAGE), $(BASE_IMAGE), localhost/mafalb/centos7-base) $(if $(TARGET_IMAGE), $(TARGET_IMAGE), localhost/mafalb/centos7-systemd)
	
fedora36-base: playbooks/collections
	OS=fedora36 ansible-bender build -l org.opencontainers.image.created=$(DATE2) --squash playbooks/base.yml $(if $(BASE_IMAGE), $(BASE_IMAGE), registry.fedoraproject.org/fedora:36) $(if $(TARGET_IMAGE), $(TARGET_IMAGE), localhost/mafalb/fedora36-base)

fedora36-systemd: playbooks/collections
	ANSIBLE_COLLECTIONS_PATHS=../../..:playbooks/collections OS=fedora36 ansible-bender build -l org.opencontainers.image.created=$(DATE2) --squash playbooks/systemd.yml $(if $(BASE_IMAGE), $(BASE_IMAGE), localhost/mafalb/fedora36-base) $(if $(TARGET_IMAGE), $(TARGET_IMAGE), localhost/mafalb/fedora36-systemd)

tools:
	mkdir -p ~/.virtualenvs/ci-tools
	python3 -m venv ~/.virtualenvs/ci-tools
	. ~/.virtualenvs/ci-tools/bin/activate
	pip install ansible-bender molecule molecule-podman ansible-core 'ansible-lint<6' flake8
