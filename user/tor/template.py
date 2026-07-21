pkgname = "tor"
pkgver = "0.4.9.11"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "asciidoc",
    "automake",
    "pkgconf",
]
makedepends = [
    "dinit-chimera",
    "libevent-devel",
    "openssl3-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Anonymizing overlay network"
license = "BSD-3-Clause"
url = "https://gitlab.com/torproject/tor"
source = f"{url}/-/archive/tor-{pkgver}/tor-tor-{pkgver}.tar.gz"
sha256 = "5dcc2e0808674c9fdb8ff6032a8c8d5467211bc5ac225ddaf6a4e2484139baec"
# requires shellcheck
options = ["etcfiles", "!check"]


def post_install(self):
    self.install_file("src/config/torrc.sample.in", "usr/share/tor")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "tor")
    self.install_license("LICENSE")
