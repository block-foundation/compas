from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import Rhino
import compas_rhino

from compas.utilities import abstractclassmethod


class RhinoGeometry(object):
    """Base class for Rhino Geometry and DocObject wrappers.

    Attributes
    ----------
    name: str
        The name of the object.
    type: str
        The type of the object.
    guid: str
        The GUID of the object.
    object: :class:`Rhino.DocObjects.RhinoObject`
        A reference to the Rhino DocObject, if it exists.
    geometry: :class:`Rhino.Geometry.GeometryBase`
        A reference to the Rhino Geometry Object.

    """

    def __init__(self):
        super(RhinoGeometry, self).__init__()
        self.guid = None
        self.object = None
        self.geometry = None
        self._type = None
        self._name = None

    @property
    def type(self):
        if self.object:
            return self.object.ObjectType
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def name(self):
        if self.object:
            return self.object.Attributes.Name
        return self._name

    @name.setter
    def name(self, value):
        if self.object:
            self.object.Attributes.Name = value
            self.object.CommitChanges()
        else:
            self._name = value

    @classmethod
    def from_guid(cls, guid):
        """Construct a Rhino object wrapper from the GUID of an existing Rhino object.

        Parameters
        ----------
        guid : str
            The GUID of the Rhino object.

        Returns
        -------
        :class:`compas_rhino.geometry.RhinoGeometry`
            The Rhino object wrapper.
        """
        obj = compas_rhino.find_object(guid)
        return cls.from_object(obj)

    @classmethod
    def from_object(cls, obj):
        """Construct a Rhino object wrapper from an existing Rhino object.

        Parameters
        ----------
        obj : Rhino.DocObjects.RhinoObject
            The Rhino object.

        Returns
        -------
        :class:`compas_rhino.geometry.RhinoGeometry`
            The Rhino object wrapper.
        """
        wrapper = cls()
        wrapper.guid = obj.Id
        wrapper.object = obj
        wrapper.geometry = obj.Geometry
        return wrapper

    @abstractclassmethod
    def from_geometry(cls, geometry):
        pass

    @abstractclassmethod
    def from_selection(cls):
        pass

    def to_compas(self):
        raise NotImplementedError

    def transform(self, T):
        """Transform the Rhino object.

        Parameters
        ----------
        T : :class:`compas.geometry.Transformation` or Rhino.Geomtry.Transform
            The transformation matrix.

        Returns
        -------
        None
            The Rhino object is transformed in place.
        """
        if not isinstance(T, Rhino.Geometry.Transform):
            M = Rhino.Geometry.Transform(0.0)
            for i in range(4):
                for j in range(4):
                    M[i, j] = T[i, j]
        else:
            M = T
        self.geometry.Transform(M)
