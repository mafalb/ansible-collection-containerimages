
centos7.updates:
	OS=centos7 ansible-bender build playbooks/base-with-updates.yml --squash

centos7.systemd:
	OS=centos7 ansible-bender build playbooks/systemd.yml --squash
	
fedora36.updates:
	OS=fedora36 ansible-bender build playbooks/base-with-updates.yml --squash

tools:
	mkdir -p ~/.virtualenvs/ci-tools
	python3 -m venv ~/.virtualenvs/ci-tools
	. ~/.virtualenvs/ci-tools/bin/activate
	pip install ansible-bender molecule molecule-podman
