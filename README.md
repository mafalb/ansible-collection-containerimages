# Ansible Collection - mafalb.containerimages

|||
|---|---|
|prod|![prod branch](https://github.com/mafalb/ansible-collection-containerimages/workflows/CI/badge.svg?branch=prod)|
|dev|![dev branch](https://github.com/mafalb/ansible-collection-containerimages/workflows/CI/badge.svg?branch=dev)|


We build some containers.

## Workflows

### CI

**CI and Build** (but do not publish). Triggered by commit.

### Build

**Build and publish** a container. Used to bootstrap. Triggered by hand.

### Update

Pull the latest container and check for updates. If any, **build and publish**. Triggered Periodically.


## Roles

### [mafalb.containerimages.systemd](roles/systemd/README.md)

### [mafalb.containerimages.cleanup](roles/cleanup/README.md)

### [mafalb.containerimages.build](roles/build/README.md)



## License

Copyright (c) 2021 Markus Falb <markus.falb@mafalb.at>

GPL-3.0-or-later
