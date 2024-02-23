#!/bin/bash -eu
# shellcheck disable=SC2002

set -o pipefail
set -e
set -x

cat tests/imagetree.yml|python3 bin/containerimages.py children --os centos7 --flavor base|grep bla1
cat tests/imagetree.yml|python3 bin/containerimages.py children --os centos7 --flavor base|grep bla2
cat tests/imagetree.yml|python3 bin/containerimages.py children --os centos7 --flavor base|grep systemd
count=$(cat tests/imagetree.yml|python3 bin/containerimages.py children --os centos7 --flavor base|wc -l)
test "$count" = 3

cat tests/imagetree.yml|python3 bin/containerimages.py parentimage --os centos7 --flavor base
cat tests/imagetree.yml|python3 bin/containerimages.py parentimage --os centos7 --flavor systemd
cat tests/imagetree.yml|python3 bin/containerimages.py parentimage --os centos7 --flavor bla1
cat tests/imagetree.yml|python3 bin/containerimages.py parentimage --os centos7 --flavor bla2

image1=$(cat tests/imagetree.yml|python3 bin/containerimages.py parentimage --os centos7 --flavor systemd)
test "$image1" = "quay.io/centos/centos:centos7"
image2=$(cat tests/imagetree.yml|python3 bin/containerimages.py parentimage --os centos7 --flavor bla1)
test "$image2" = 'None'

cat tests/imagetree.yml|python3 bin/containerimages.py parent --os centos7 --flavor base|grep None
cat tests/imagetree.yml|python3 bin/containerimages.py parent --os centos7 --flavor systemd|grep base

cat tests/imagetree.yml|python3 bin/containerimages.py listos|grep centos7
cat tests/imagetree.yml|python3 bin/containerimages.py listos|grep fedora36


cat tests/imagetree.yml|python3 bin/containerimages.py attribute --os centos7 --flavor systemd --attribute flavor|grep systemd
cat tests/imagetree.yml|python3 bin/containerimages.py attribute --os centos7 --flavor systemd --attribute os|grep centos7
cat tests/imagetree.yml|python3 bin/containerimages.py attribute --os centos7 --flavor base --attribute base_image|grep quay
