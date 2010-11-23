#
# treeinfo.py
#
# Copyright (C) 2010  Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Red Hat Author(s):  Martin Gracik <mgracik@redhat.com>
#

import logging
logger = logging.getLogger("pylorax.treeinfo")

import ConfigParser
import time
from sysutils import *


class TreeInfo(object):

    def __init__(self, workdir, product, version, variant, basearch,
                 discnum=1, totaldiscs=1, packagedir=""):

        self.path = joinpaths(workdir, ".treeinfo")
        self.c = ConfigParser.ConfigParser()

        section = "general"
        data = {"timestamp": time.time(),
                "family": product,
                "version": version,
                "variant": variant or "",
                "arch": basearch,
                "discnum": discnum,
                "totaldiscs": totaldiscs,
                "packagedir": packagedir}

        self.c.add_section(section)
        map(lambda (key, value): self.c.set(section, key, value), data.items())

    def add_section(self, section, data):
        if not self.c.has_section(section):
            self.c.add_section(section)

        map(lambda (key, value): self.c.set(section, key, value), data.items())

    def write(self):
        logger.info("writing .treeinfo file")
        with open(self.path, "w") as fobj:
            self.c.write(fobj)