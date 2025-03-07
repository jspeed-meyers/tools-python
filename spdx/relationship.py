# Copyright (c) 2020 Yash Varshney
# SPDX-License-Identifier: Apache-2.0
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#    http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import auto, Enum

from spdx.parsers.loggers import ErrorMessages


class RelationshipType(Enum):
    AMENDS = auto()
    OTHER = auto()
    COPY_OF = auto()
    TEST_OF = auto()
    ANCESTOR_OF = auto()
    BUILD_DEPENDENCY_OF = auto()
    BUILD_TOOL_OF = auto()
    CONTAINED_BY = auto()
    CONTAINS = auto()
    DATA_FILE_OF = auto()
    DEPENDENCY_MANIFEST_OF = auto()
    DEPENDENCY_OF = auto()
    DEPENDS_ON = auto()
    DESCENDANT_OF = auto()
    DESCRIBED_BY = auto()
    DESCRIBES = auto()
    DEV_DEPENDENCY_OF = auto()
    DEV_TOOL_OF = auto()
    DISTRIBUTION_ARTIFACT = auto()
    DOCUMENTATION_OF = auto()
    DYNAMIC_LINK = auto()
    EXAMPLE_OF = auto()
    EXPANDED_FROM_ARCHIVE = auto()
    FILE_ADDED = auto()
    FILE_DELETED = auto()
    FILE_MODIFIED = auto()
    GENERATED_FROM = auto()
    GENERATES = auto()
    HAS_PREREQUISITE = auto()
    METAFILE_OF = auto()
    OPTIONAL_COMPONENT_OF = auto()
    OPTIONAL_DEPENDENCY_OF = auto()
    PACKAGE_OF = auto()
    PATCH_APPLIED = auto()
    PATCH_FOR = auto()
    PREREQUISITE_FOR = auto()
    PROVIDED_DEPENDENCY_OF = auto()
    RUNTIME_DEPENDENCY_OF = auto()
    STATIC_LINK = auto()
    TEST_CASE_OF = auto()
    TEST_DEPENDENCY_OF = auto()
    TEST_TOOL_OF = auto()
    VARIANT_OF = auto()
    REQUIREMENT_DESCRIPTION_FOR = auto()
    SPECIFICATION_FOR = auto()


class Relationship(object):
    """
    Document relationship information
    Fields:
    - relationship:  provides information about the relationship between two SPDX elements.
    - relationship_comment:  place for the SPDX file creator to record any general comments. Optional, One
    """

    def __init__(self, relationship=None, relationship_comment=None):
        self.relationship = relationship
        self.relationship_comment = relationship_comment

    def __eq__(self, other):
        return (
            isinstance(other, Relationship)
            and self.relationship == other.relationship
        )

    @property
    def has_comment(self):
        return self.relationship_comment is not None

    @property
    def spdx_element_id(self):
        return self.relationship.split(" ")[0]

    @property
    def relationship_type(self):
        return self.relationship.split(" ")[1]

    @property
    def related_spdx_element(self):
        return self.relationship.split(" ")[2]

    def validate(self, messages: ErrorMessages) -> ErrorMessages:
        """
        Check that all the fields are valid.
        Appends any error messages to messages parameter shall be a ErrorMessages.
        """
        r_type = self.relationship_type
        if r_type not in [name for name, _ in RelationshipType.__members__.items()]:
            messages.append(
                "Relationship type must be one of the constants defined in "
                "class spdx.relationship.Relationship"
            )
        return messages
