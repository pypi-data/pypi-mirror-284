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

class CompositeSequenceValueObject(object):
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
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'array_design': 'ArrayDesignValueObject'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'array_design': 'arrayDesign'
    }

    def __init__(self, id=None, name=None, description=None, array_design=None):  # noqa: E501
        """CompositeSequenceValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._array_design = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if array_design is not None:
            self.array_design = array_design

    @property
    def id(self):
        """Gets the id of this CompositeSequenceValueObject.  # noqa: E501


        :return: The id of this CompositeSequenceValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompositeSequenceValueObject.


        :param id: The id of this CompositeSequenceValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CompositeSequenceValueObject.  # noqa: E501


        :return: The name of this CompositeSequenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CompositeSequenceValueObject.


        :param name: The name of this CompositeSequenceValueObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CompositeSequenceValueObject.  # noqa: E501


        :return: The description of this CompositeSequenceValueObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CompositeSequenceValueObject.


        :param description: The description of this CompositeSequenceValueObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def array_design(self):
        """Gets the array_design of this CompositeSequenceValueObject.  # noqa: E501


        :return: The array_design of this CompositeSequenceValueObject.  # noqa: E501
        :rtype: ArrayDesignValueObject
        """
        return self._array_design

    @array_design.setter
    def array_design(self, array_design):
        """Sets the array_design of this CompositeSequenceValueObject.


        :param array_design: The array_design of this CompositeSequenceValueObject.  # noqa: E501
        :type: ArrayDesignValueObject
        """

        self._array_design = array_design

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
        if issubclass(CompositeSequenceValueObject, dict):
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
        if not isinstance(other, CompositeSequenceValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
