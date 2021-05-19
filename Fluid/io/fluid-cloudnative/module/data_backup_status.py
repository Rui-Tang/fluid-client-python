# coding: utf-8

"""
    fluid

    client for fluid  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from Fluid.io.fluid-cloudnative.module.backup_location import BackupLocation  # noqa: F401,E501
from Fluid.io.fluid-cloudnative.module.condition import Condition  # noqa: F401,E501


class DataBackupStatus(object):
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
        'backup_location': 'BackupLocation',
        'conditions': 'list[Condition]',
        'duration': 'str',
        'phase': 'str'
    }

    attribute_map = {
        'backup_location': 'backupLocation',
        'conditions': 'conditions',
        'duration': 'duration',
        'phase': 'phase'
    }

    def __init__(self, backup_location=None, conditions=None, duration=None, phase=None):  # noqa: E501
        """DataBackupStatus - a model defined in Swagger"""  # noqa: E501

        self._backup_location = None
        self._conditions = None
        self._duration = None
        self._phase = None
        self.discriminator = None

        if backup_location is not None:
            self.backup_location = backup_location
        self.conditions = conditions
        self.duration = duration
        self.phase = phase

    @property
    def backup_location(self):
        """Gets the backup_location of this DataBackupStatus.  # noqa: E501

        BackupLocation tell user the location to save data of the DataBackup  # noqa: E501

        :return: The backup_location of this DataBackupStatus.  # noqa: E501
        :rtype: BackupLocation
        """
        return self._backup_location

    @backup_location.setter
    def backup_location(self, backup_location):
        """Sets the backup_location of this DataBackupStatus.

        BackupLocation tell user the location to save data of the DataBackup  # noqa: E501

        :param backup_location: The backup_location of this DataBackupStatus.  # noqa: E501
        :type: BackupLocation
        """

        self._backup_location = backup_location

    @property
    def conditions(self):
        """Gets the conditions of this DataBackupStatus.  # noqa: E501

        Conditions consists of transition information on DataBackup's Phase  # noqa: E501

        :return: The conditions of this DataBackupStatus.  # noqa: E501
        :rtype: list[Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this DataBackupStatus.

        Conditions consists of transition information on DataBackup's Phase  # noqa: E501

        :param conditions: The conditions of this DataBackupStatus.  # noqa: E501
        :type: list[Condition]
        """
        if conditions is None:
            raise ValueError("Invalid value for `conditions`, must not be `None`")  # noqa: E501

        self._conditions = conditions

    @property
    def duration(self):
        """Gets the duration of this DataBackupStatus.  # noqa: E501

        Duration tell user how much time was spent to backup  # noqa: E501

        :return: The duration of this DataBackupStatus.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DataBackupStatus.

        Duration tell user how much time was spent to backup  # noqa: E501

        :param duration: The duration of this DataBackupStatus.  # noqa: E501
        :type: str
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def phase(self):
        """Gets the phase of this DataBackupStatus.  # noqa: E501

        Phase describes current phase of DataBackup  # noqa: E501

        :return: The phase of this DataBackupStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this DataBackupStatus.

        Phase describes current phase of DataBackup  # noqa: E501

        :param phase: The phase of this DataBackupStatus.  # noqa: E501
        :type: str
        """
        if phase is None:
            raise ValueError("Invalid value for `phase`, must not be `None`")  # noqa: E501

        self._phase = phase

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
        if issubclass(DataBackupStatus, dict):
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
        if not isinstance(other, DataBackupStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other