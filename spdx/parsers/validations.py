# Copyright (c) 2014 Ahmed H. Ismail
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

import re

import rdflib
import uritools

from spdx import creationinfo
from spdx import license
from spdx import utils


def validate_is_free_form_text_or_str(value, optional=False) -> bool:
    if value is None:
        return optional
    if not isinstance(value, str):
        return False
    if "\n" in value:
        TEXT_RE = re.compile(r"<text>(.|\n)*</text>", re.UNICODE)
        match = TEXT_RE.match(value)
        return match is not None
    return True


def validate_tool_name(value, optional=False):
    striped_value = value.strip()
    if optional:
        return len(striped_value) == 0
    else:
        return not (len(striped_value) == 0)


def validate_person_name(value, optional=False):
    return validate_tool_name(value, optional)


def validate_org_name(value, optional=False):
    return validate_tool_name(value, optional)


def validate_data_lics(value):
    return value == "CC0-1.0"


def validate_doc_name(value, optional=False):
    return validate_tool_name(value, optional)


def validate_pkg_supplier(value, optional=False):
    if optional and value is None:
        return True
    return isinstance(
        value, (utils.NoAssert, creationinfo.Person, creationinfo.Organization)
    )


def validate_pkg_originator(value, optional=False):
    return validate_pkg_supplier(value, optional)


def validate_pkg_homepage(value, optional=False):
    if value is None:
        return optional

    return isinstance(value, (str, utils.NoAssert, utils.SPDXNone))


def validate_pkg_cr_text(value, optional=False):
    if isinstance(value, (utils.NoAssert, utils.SPDXNone)):
        return True
    elif validate_is_free_form_text_or_str(value, optional):
        return True
    elif value is None:
        return optional
    else:
        return False


def validate_pkg_summary(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_pkg_desc(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_pkg_comment(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_pkg_attribution_text(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_file_attribution_text(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_snippet_attribution_text(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_pkg_ext_ref_category(value, optional=False):
    # PACKAGE_MANAGER is used in the json schema for 2.2. For now, we simply allow both versions
    return value.upper() in ["SECURITY", "OTHER", "PACKAGE-MANAGER", "PACKAGE_MANAGER"]


def validate_pkg_ext_ref_type(value, optional=False):
    return re.match(r"^\S+$", value) is not None


def validate_pkg_ext_ref_comment(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_doc_comment(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_doc_spdx_id(value, optional=False):
    if value is None:
        return optional

    return value.endswith("#SPDXRef-DOCUMENT")


def validate_doc_namespace(value, optional=False):
    if value is None:
        return optional

    return uritools.isabsuri(value) and ("#" not in value)


def validate_creator(value, optional=False):
    if value is None:
        return optional
    else:
        return isinstance(value, creationinfo.Creator)


def validate_creation_comment(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_reviewer(value, optional=False):
    return validate_creator(value, optional)


def validate_review_comment(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_annotator(value, optional=False):
    return validate_creator(value, optional)


def validate_annotation_comment(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_annotation_type(value, optional=False):
    value = value.strip()
    return value == "REVIEW" or value == "OTHER"


def validate_relationship_comment(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_pkg_spdx_id(value, optional=False):
    value = value.split("#")[-1]
    TEXT_RE = re.compile(r"SPDXRef-([A-Za-z0-9\.\-]+)", re.UNICODE)
    if value is None:
        return optional
    else:
        return TEXT_RE.match(value) is not None


def validate_pkg_files_analyzed(value, optional=False):
    if value in ["True", "true", "False", "false", True, False]:
        return True
    else:
        return optional


def validate_pkg_src_info(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_pkg_lics_comment(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_file_spdx_id(value, optional=False):
    value = value.split("#")[-1]
    TEXT_RE = re.compile(r"SPDXRef-([A-Za-z0-9.\-]+)", re.UNICODE)
    if value is None:
        return optional
    else:
        return TEXT_RE.match(value) is not None


def validate_file_comment(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_file_lics_comment(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_file_cpyright(value, optional=False):
    if isinstance(value, (utils.NoAssert, utils.SPDXNone)):
        return True
    return validate_is_free_form_text_or_str(value, optional)


def validate_lics_from_file(value, optional=False):
    if value is None:
        return optional
    return isinstance(value, (license.License, utils.SPDXNone, utils.NoAssert))


def validate_file_notice(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_lics_conc(value, optional=False):
    if value is None:
        return optional
    return isinstance(value, (utils.NoAssert, utils.SPDXNone, license.License))


def validate_file_lics_in_file(value, optional=False):
    if value is None:
        return optional
    return isinstance(value, (utils.NoAssert, utils.SPDXNone, license.License))


def validate_extracted_lic_id(value, optional=False):
    if value is None:
        return optional
    else:
        return value.startswith("LicenseRef-")


def validate_extr_lic_name(value, optional=False):
    if value is None:
        return optional
    else:
        return isinstance(value, (str, utils.NoAssert, rdflib.Literal))


def validate_snippet_spdx_id(value, optional=False):
    if value is None:
        return optional
    value = value.split("#")[-1]
    return re.match(r"^SPDXRef[A-Za-z0-9.\-]+$", value) is not None


def validate_snip_comment(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_snippet_copyright(value, optional=False):
    if validate_is_free_form_text_or_str(value, optional):
        return True
    elif isinstance(value, (utils.NoAssert, utils.SPDXNone)):
        return True
    elif value is None:
        return optional
    else:
        return False


def validate_snip_lic_comment(value, optional=False):
    return validate_is_free_form_text_or_str(value, optional)


def validate_snip_file_spdxid(value, optional=False):
    if value is None:
        return optional
    return (
        re.match(r"(DocumentRef[A-Za-z0-9.\-]+:){0,1}SPDXRef[A-Za-z0-9.\-]+", value)
        is not None
    )


def validate_snip_lics_info(value, optional=False):
    if value is None:
        return optional
    return isinstance(value, (utils.NoAssert, utils.SPDXNone, license.License))
