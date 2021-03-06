
DATE:=$(shell date +%Y%m%d)
DATE2:=$(shell date -Is)

.PHONY: all

centos7-base:
	OS=centos7 ansible-bender build -l org.label-schema.build-date=$(DATE) org.opencontainers.image.created=$(DATE2) --squash playbooks/base-with-updates.yml $(if $(BASE_IMAGE), $(BASE_IMAGE), quay.io/centos/centos:centos7) $(if $(TARGET_IMAGE), $(TARGET_IMAGE), localhost/mafalb/centos7-base)

centos7-systemd:
	ANSIBLE_COLLECTIONS_PATHS=../../..:playbooks/collections OS=centos7 ansible-bender build -l org.label-schema.build-date=$(DATE) org.opencontainers.image.created=$(DATE2) --squash playbooks/systemd.yml $(if $(BASE_IMAGE), $(BASE_IMAGE), localhost/mafalb/centos7-base) $(if $(TARGET_IMAGE), $(TARGET_IMAGE), localhost/mafalb/centos7-systemd)
	
fedora36-base:
	OS=fedora36 ansible-bender build -l org.opencontainers.image.created=$(DATE2) --squash playbooks/base-with-updates.yml $(if $(BASE_IMAGE), $(BASE_IMAGE), registry.fedoraproject.org/fedora:36) $(if $(TARGET_IMAGE), $(TARGET_IMAGE), localhost/mafalb/fedora36-base)

fedora36-systemd:
	ANSIBLE_COLLECTIONS_PATHS=../../.. OS=fedora36 ansible-bender build -l org.opencontainers.image.created=$(DATE2) --squash playbooks/systemd.yml $(if $(BASE_IMAGE), $(BASE_IMAGE), localhost/mafalb/fedora36-base) $(if $(TARGET_IMAGE), $(TARGET_IMAGE), localhost/mafalb/fedora36-systemd)

tools:
	mkdir -p ~/.virtualenvs/ci-tools
	python3 -m venv ~/.virtualenvs/ci-tools
	. ~/.virtualenvs/ci-tools/bin/activate
	pip install ansible-bender molecule molecule-podman ansible-core
