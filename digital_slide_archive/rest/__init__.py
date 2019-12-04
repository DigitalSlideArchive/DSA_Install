#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################################
#  Copyright Kitware Inc.
#
#  Licensed under the Apache License, Version 2.0 ( the "License" );
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
############################################################################

from . import dsa
from . import tcga
from . import aperio
from . import system


def addEndpoints(apiRoot):
    """
    This adds endpoints from each module.

    :param apiRoot: Girder api root class.
    """
    system.addSystemEndpoints(apiRoot)
    apiRoot.tcga = tcga.TCGAResource()
    aperio.addItemEndpoints(apiRoot.item)
    aperio.addTcgaEndpoints(apiRoot.tcga)

    # Attach endpoints defined in `dsa.py` to the api.  This should be
    # an instance derived from Resource:  https://goo.gl/QwJgP2
    apiRoot.dsa_endpoints = dsa.DSAEndpointsResource()
