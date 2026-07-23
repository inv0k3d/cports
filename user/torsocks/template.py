pkgname = "torsocks"
pkgver = "2.5.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "openssl3-devel",
]

pkgdesc = "Wrapper to torify applications"
license = "GPL-2.0-only"
url = "https://gitlab.torproject.org/tpo/core/torsocks"
source = f"{url}/-/archive/v{pkgver}/torsocks-v{pkgver}.tar.gz"
sha256 = "0fc8e18f2dc2e12f1129054f6d5acc7ecc3f0345bb57ed653fc8c6674e6ecc7e"
options = ["etcfiles"]


def post_install(self):
    self.install_file("ChangeLog", "usr/share/torsocks")
    self.install_file("doc/notes/DEBUG", "usr/share/torsocks")
    self.install_file("doc/socks/SOCKS5", "usr/share/torsocks")
    self.install_file("doc/socks/socks-extensions.txt", "usr/share/torsocks")
    self.install_license("GPL-2.0.txt")

