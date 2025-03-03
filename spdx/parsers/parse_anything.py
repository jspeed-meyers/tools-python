# Copyright (c) spdx contributors
# SPDX-License-Identifier: Apache-2.0
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import spdx.file as spdxfile
from spdx.parsers import jsonparser
from spdx.parsers import yamlparser
from spdx.parsers import rdf
from spdx.parsers import xmlparser
from spdx.parsers import tagvalue
from spdx.parsers.loggers import StandardLogger
from spdx.parsers import jsonyamlxmlbuilders, tagvaluebuilders, rdfbuilders
from spdx.parsers.builderexceptions import FileTypeError


def parse_file(fn, encoding="utf-8"):
    builder_module = jsonyamlxmlbuilders
    read_data = False
    if fn.endswith(".rdf") or fn.endswith(".rdf.xml"):
        encoding = None
        parsing_module = rdf
        builder_module = rdfbuilders
    elif fn.endswith(".tag") or fn.endswith(".spdx"):
        parsing_module = tagvalue
        builder_module = tagvaluebuilders
        read_data = True
    elif fn.endswith(".json"):
        parsing_module = jsonparser
    elif fn.endswith(".xml"):
        parsing_module = xmlparser
    elif fn.endswith(".yaml") or fn.endswith(".yml"):
        parsing_module = yamlparser
    else:
        raise FileTypeError("FileType Not Supported" + str(fn))

    p = parsing_module.Parser(builder_module.Builder(), StandardLogger())
    if hasattr(p, "build"):
        p.build()
    with open(fn, "r", encoding=encoding) as f:
        if read_data:
            data = f.read()
            return p.parse(data)
        else:
            return p.parse(f)
