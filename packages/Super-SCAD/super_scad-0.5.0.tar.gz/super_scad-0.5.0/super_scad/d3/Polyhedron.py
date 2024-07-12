import itertools
from typing import Iterable, List, Tuple

from super_scad.boolean.Union import Union
from super_scad.d3.Cylinder import Cylinder
from super_scad.d3.private.PrivatePolyhedron import PrivatePolyhedron
from super_scad.d3.Sphere import Sphere
from super_scad.other.Modify import Modify
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.transformation.Paint import Paint
from super_scad.transformation.Translate3D import Translate3D
from super_scad.type.Color import Color
from super_scad.type.Point3 import Point3


class Polyhedron(ScadWidget):
    """
    Widget for creating polyhedrons. See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Primitive_Solids#polyhedron.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 faces: List[List[Point3] | Tuple[Point3, ...]],
                 highlight_face: int | None = None,
                 highlight_diameter: float | None = None,
                 convexity: int | None = None):
        """
        Object constructor.

        :param faces:  The faces that collectively enclose the solid.
        :param highlight_face: The index of the face to highlight. Each point of the face is marked, the first point is
                           colored red, the second orange, the third green, and all other points are color black.
        :param highlight_diameter: The diameter of the spheres that highlight the nodes of the faces.
        :param convexity: Number of "inward" curves, i.e. expected number of path crossings of an arbitrary line through
                          the polyhedron.

        Each face consists of 3 or more points. Faces may be defined in any order, but the points of each face must be
        ordered correctly, must be ordered in clockwise direction when looking at each face from outside inward. Define
        enough faces to fully enclose the solid, with no overlap. If points that describe a single face are not on the
        same plane, the face is by OpenSCAD automatically split into triangles as needed.
        """
        ScadWidget.__init__(self, args=locals())

        for key, face in enumerate(faces):
            assert len(face) >= 3, f'Each face must have 3 or more points. Face {key} as only {len(face)} points'

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def highlight_face(self) -> int | None:
        """
        Returns the index of the face to highlight
        """
        return self._args.get('highlight_face')

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def highlight_diameter(self) -> float | None:
        """
        Returns the diameter of the spheres that highlight the nodes of the faces.
        """
        return self._args.get('highlight_diameter')

    # ------------------------------------------------------------------------------------------------------------------
    def real_highlight_diameter(self, context: Context) -> float:
        """
        Returns the real diameter of the spheres that highlight the nodes of the faces.
        """
        diameter = self.highlight_diameter
        if diameter is not None:
            return max(diameter, 5.0 * context.resolution)

        face = self._args['faces'][self.highlight_face]

        total_distance = 0.0
        prev_point = None
        for point in face:
            if prev_point is not None:
                total_distance += (point - prev_point).length
            prev_point = point

        if prev_point is not None:
            total_distance += (face[0] - prev_point).length

        average_distance = total_distance / (len(face) + 1)
        diameter = 0.1 * average_distance

        return max(diameter, 5.0 * context.resolution)

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def convexity(self) -> int | None:
        """
        Returns the number of "inward" curves, i.e. expected number of path crossings of an arbitrary line through the
        child widget.
        """
        return self._args.get('convexity')

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __clean_face(face: List[int]) -> List[int] | None:
        """
        Removes fused point from a face. If face has only two or fewer points, returns None.

        @param face: The face.
        """
        new_face = [key for key, _g in itertools.groupby(face)]
        if new_face[0] == new_face[-1]:
            new_face.pop()

        if len(new_face) >= 3:
            return new_face

        return None

    # ------------------------------------------------------------------------------------------------------------------
    def __pass1(self, context: Context) -> Tuple[List[Point3], List[List[int]]]:
        """
        Pass 1: Remove fused points and enumerate points in faces.

        @param context: The build context.
        """
        digits = context.length_digits
        faces = self._args['faces']
        distinct_points = []
        real_faces = []
        for face in faces:
            new_face = []
            for point in face:
                point_rounded = Point3(round(float(point.x), digits),
                                       round(float(point.y), digits),
                                       round(float(point.z), digits))
                try:
                    index = distinct_points.index(point_rounded)
                except ValueError:
                    index = len(distinct_points)
                    distinct_points.append(point_rounded)
                new_face.append(index)

            if self.__clean_face(new_face) is not None:
                real_faces.append(new_face)

        return distinct_points, real_faces

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __pass2(points: List[Point3],
                faces: List[List[int]]) -> Tuple[List[Point3], List[List[int]]]:
        """
        Pass 2: Remove unused points and renumber points.

        @param points: The list of distinct (non-fused) points.
        @param faces: The faces.
        """
        point_keys = set()
        for face in faces:
            point_keys.update(face)

        if len(point_keys) == len(points):
            return points, faces

        new_points = []
        key_map = {}
        for key, point in enumerate(points):
            if key in point_keys:
                new_points.append(point)
                key_map[key] = len(new_points) - 1

        new_faces = []
        for face in faces:
            new_face = []
            for key in face:
                new_face.append(key_map[key])
            new_faces.append(new_face)

        return new_points, new_faces

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __crate_markers_nodes(face: Iterable[Point3], diameter: float) -> List[ScadWidget]:
        """
        Create markers of the nodes of a face.

        :param face: The face.
        :param diameter: The diameter of the markers.
        """
        nodes = []
        for key, point in enumerate(face):
            if key == 0:
                color = Color(color='red')
            elif key == 1:
                color = Color(color='orange')
            elif key == 2:
                color = Color(color='green')
            else:
                color = Color(color='black')

            node = Paint(color=color,
                         child=Translate3D(vector=point,
                                           child=Sphere(diameter=diameter, fn=16)))
            nodes.append(node)

        return nodes

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __crate_markers_edges(face: Iterable[Point3],
                              diameter: float,
                              context: Context) -> List[ScadWidget]:
        """
        Create markers of the edges of a face.

        :param face: The face.
        :param diameter: The diameter of cylinders on the edges.
        :param context: The build context.
        """

        edges = []
        prev_point = None
        first_point = None
        for key, point in enumerate(face):
            if prev_point is None:
                first_point = point
            else:
                if (point - prev_point).length >= context.resolution:
                    edge = Paint(color=Color(color='black'),
                                 child=Cylinder(start_point=prev_point,
                                                end_point=point,
                                                diameter=diameter,
                                                fn=16))
                    edges.append(edge)

            prev_point = point

        if prev_point is not None and first_point is not None:
            if (first_point - prev_point).length >= context.resolution:
                edge = Paint(color=Color(color='black'),
                             child=Cylinder(start_point=prev_point,
                                            end_point=first_point,
                                            diameter=diameter))
                edges.append(edge)

        return edges

    # ------------------------------------------------------------------------------------------------------------------
    def __crate_markers(self, context: Context) -> Tuple[List[ScadWidget], List[ScadWidget]]:
        """
        Create markers to highlight a face.

        :param context: The build context.
        """
        diameter_node = self.real_highlight_diameter(context)
        diameter_edge = 0.2 * diameter_node

        face = self._args['faces'][self.highlight_face]
        nodes = self.__crate_markers_nodes(face, diameter_node)
        edges = self.__crate_markers_edges(face, diameter_edge, context)

        return nodes, edges

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        distinct_points, real_faces = self.__pass1(context)
        distinct_points, real_faces = self.__pass2(distinct_points, real_faces)

        polyhedron = PrivatePolyhedron(points=distinct_points, faces=real_faces, convexity=self.convexity)

        if self.highlight_face is None:
            return polyhedron

        markers = self.__crate_markers(context)

        return Union(children=[polyhedron] + markers[0] + markers[1])

# ----------------------------------------------------------------------------------------------------------------------
