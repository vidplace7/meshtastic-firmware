FROM archlinux:base

RUN pacman -Sy --needed --noconfirm \
    sudo \
    debugedit fakeroot binutils pacman-contrib \
    platformio-core python-pip python-grpcio-tools gcc cmake pkgconf protobuf pcre2 git \
    i2c-tools libgpiod yaml-cpp ulfius libuv orcania yder bluez-libs libxkbcommon libinput libx11
RUN useradd -m builduser && \
    passwd -d builduser && \
    echo "builduser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER builduser
# WORKDIR /home/builduser/meshtasticd

# COPY meshtasticd/PKGBUILD PKGBUILD
# COPY meshtasticd/meshtasticd.sysusers meshtasticd.sysusers
# COPY meshtasticd/meshtasticd.install meshtasticd.install
# RUN makepkg --noconfirm
