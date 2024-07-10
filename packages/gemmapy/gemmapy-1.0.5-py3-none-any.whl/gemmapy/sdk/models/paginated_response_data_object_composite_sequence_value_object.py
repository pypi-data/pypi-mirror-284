# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma RESTful API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  Use of this webpage and the Gemma Web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.  You can [consult the CHANGELOG.md file](https://gemma.msl.ubc.ca/resources/restapidocs/CHANGELOG.md) to view  release notes and recent changes to the Gemma RESTful API.   # noqa: E501

    OpenAPI spec version: 2.8.0
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaginatedResponseDataObjectCompositeSequenceValueObject(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data': 'list[CompositeSequenceValueObject]',
        'group_by': 'list[str]',
        'sort': 'SortValueObject',
        'offset': 'int',
        'limit': 'int',
        'total_elements': 'int'
    }

    attribute_map = {
        'data': 'data',
        'group_by': 'groupBy',
        'sort': 'sort',
        'offset': 'offset',
        'limit': 'limit',
        'total_elements': 'totalElements'
    }

    def __init__(self, data=None, group_by=None, sort=None, offset=None, limit=None, total_elements=None):  # noqa: E501
        """PaginatedResponseDataObjectCompositeSequenceValueObject - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._group_by = None
        self._sort = None
        self._offset = None
        self._limit = None
        self._total_elements = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if group_by is not None:
            self.group_by = group_by
        if sort is not None:
            self.sort = sort
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total_elements is not None:
            self.total_elements = total_elements

    @property
    def data(self):
        """Gets the data of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501


        :return: The data of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501
        :rtype: list[CompositeSequenceValueObject]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PaginatedResponseDataObjectCompositeSequenceValueObject.


        :param data: The data of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501
        :type: list[CompositeSequenceValueObject]
        """

        self._data = data

    @property
    def group_by(self):
        """Gets the group_by of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501


        :return: The group_by of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this PaginatedResponseDataObjectCompositeSequenceValueObject.


        :param group_by: The group_by of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501
        :type: list[str]
        """

        self._group_by = group_by

    @property
    def sort(self):
        """Gets the sort of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501


        :return: The sort of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501
        :rtype: SortValueObject
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this PaginatedResponseDataObjectCompositeSequenceValueObject.


        :param sort: The sort of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501
        :type: SortValueObject
        """

        self._sort = sort

    @property
    def offset(self):
        """Gets the offset of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501


        :return: The offset of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PaginatedResponseDataObjectCompositeSequenceValueObject.


        :param offset: The offset of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501


        :return: The limit of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PaginatedResponseDataObjectCompositeSequenceValueObject.


        :param limit: The limit of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def total_elements(self):
        """Gets the total_elements of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501


        :return: The total_elements of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """Sets the total_elements of this PaginatedResponseDataObjectCompositeSequenceValueObject.


        :param total_elements: The total_elements of this PaginatedResponseDataObjectCompositeSequenceValueObject.  # noqa: E501
        :type: int
        """

        self._total_elements = total_elements

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PaginatedResponseDataObjectCompositeSequenceValueObject, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaginatedResponseDataObjectCompositeSequenceValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
