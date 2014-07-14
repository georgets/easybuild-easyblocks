##
# Copyright 2009-2014 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
EasyBuild support for building and installing PGI, implemented as an easyblock
"""
import os

import easybuild.tools.environment as env
import easybuild.tools.toolchain as toolchain
from easybuild.framework.easyblock import EasyBlock
from easybuild.framework.easyconfig import CUSTOM, MANDATORY
from easybuild.tools.filetools import run_cmd


class EB_PGI(EasyBlock):
    """Support for building/installing PGI."""

    def __init__(self, *args, **kwargs):
        """Initialisation of custom class variables for PGI."""
        super(EB_PGI, self).__init__(*args, **kwargs)

        self.example = None

    def configure_step(self):
        """Custom configuration procedure for PGI."""

    def build_step(self):
        """Custom build procedure for PGI."""

    def test_step(self):
        """Custom built-in test procedure for PGI."""

    def install_step(self):
        """Custom install procedure for PGI."""
       
        cmd = "./install %s" % self.installdir 
        run_cmd(cmd, log_all=True, simple=True, log_ok=True)


    def make_module_extra(self):
        """Custom extra module file entries for PGI."""

        txt = super(EB_PGI, self).make_module_extra()

        return txt
