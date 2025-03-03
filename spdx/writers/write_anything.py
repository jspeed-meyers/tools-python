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


from spdx.writers import json
from spdx.writers import yaml
from spdx.writers import rdf
from spdx.writers import xml
from spdx.writers import tagvalue
from spdx.parsers.builderexceptions import FileTypeError


def write_file(doc, fn, validate=True, encoding="utf-8"):
    out_mode = "w"
    if fn.endswith(".rdf") or fn.endswith(".rdf.xml"):
        writer_module = rdf
        out_mode = "wb"
        encoding = None
    elif fn.endswith(".tag") or fn.endswith(".spdx"):
        writer_module = tagvalue
    elif fn.endswith(".json"):
        writer_module = json
    elif fn.endswith(".xml"):
        writer_module = xml
    elif fn.endswith(".yaml"):
        writer_module = yaml
    else:
        raise FileTypeError("FileType Not Supported")

    with open(fn, out_mode, encoding=encoding) as out:
        p = writer_module.write_document(doc, out, validate)
