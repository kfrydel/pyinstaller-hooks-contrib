# ------------------------------------------------------------------
# Copyright (c) 2024 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

# hook for https://github.com/sissaschool/xmlschema
from PyInstaller.utils.hooks import collect_data_files

# the library contains a bunch of XSD schemas which are loaded in run time
datas = collect_data_files("xmlschema")