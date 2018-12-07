""" day6_2.py -> This module solves the second problem of the sixth day
    for the advent of code 2018 """
from math import ceil

class Coordinate:
    """ A coordinate class for getting part or all of a coordinate.
        also contains helper functions for working with coordinates """
    def __init__(self, raw_coord):
        self.x_coord = None
        self.y_coord = None
        self.coord = (None, None)
        self.parse_raw(raw_coord)

    def __str__(self):
        return '(%s, %s)' % (self.x_coord, self.y_coord)

    def __repr__(self):
        return '(%s, %s)' % (self.x_coord, self.y_coord)

    def __eq__(self, other):
        return self.x_coord == other.x_coord and self.y_coord == other.y_coord

    def parse_raw(self, raw_coord):
        """ Given a raw (string) of a coordinate, parses it and returns
            the x_dim, y_dim, and (x_dim,y_dim) parts in a tuple """
        raw_coord = raw_coord.strip()
        raw_coord = raw_coord.replace(' ', '')
        raw_coords = raw_coord.split(',')
        self.x_coord = int(raw_coords[0])
        self.y_coord = int(raw_coords[1])
        self.coord = ()

    def manhattan_distance(self, other):
        """ Calculates the manhattan distance between this coordinate
            and another coordinate """
        x_diff = abs(self.x_coord - other.x_coord)
        y_diff = abs(self.y_coord - other.y_coord)
        return x_diff + y_diff

    @staticmethod
    def closest_manhattan(to_coord, coordinates):
        """ Calculates which coordinate in a given list of coordinates is closest
            to the coordinate passed in """
        # Set the initial values to compare against using the first value in coordinates
        closest_coordinate = coordinates[0]
        closest_coordinate_dist = closest_coordinate.manhattan_distance(to_coord)
        tied = False
        # Search for the closest coordinate
        for coord in coordinates[1:]:
            # Get the manhattan distance between these coordinates
            dist_between = coord.manhattan_distance(to_coord)
            # Update the newest closest coordinate if current coord is closer
            if dist_between < closest_coordinate_dist:
                tied = False
                closest_coordinate = coord
                closest_coordinate_dist = dist_between
            elif dist_between == closest_coordinate_dist:
                tied = True
        return Coordinate('-1,-1') if tied else closest_coordinate

    @staticmethod
    def total_manhattan_distance(from_coord, to_coords):
        """ Calculates the total manhattan distance from a given coordinate
            to all other coordinates """
        return sum([coord.manhattan_distance(from_coord) for coord in to_coords])


class Grid:
    """ A grid class for containing the grid structure and metadata and
        methods for working with it """
    def __init__(self, boundaries_tup, grid):
        self.smallest_x = boundaries_tup[0]
        self.smallest_y = boundaries_tup[1]
        self.largest_x = boundaries_tup[2]
        self.largest_y = boundaries_tup[3]
        self.grid = grid

    @classmethod
    def manhattan_grid(cls, coordinates):
        """ Generates a grid showing the coordinate at the closest manhattan
        distance at each point """
        # Get the shape of the grid
        sm_x, lg_x, sm_y, lg_y = Grid.grid_shape(coordinates)
        # Construct the grid
        grid = {}
        for x_dim in range(sm_x, lg_x+1):
            grid[x_dim] = {}
            for y_dim in range(sm_y, lg_y+1):
                # Set each value to be the closest coordinate
                closest = Coordinate('%s,%s' % (x_dim, y_dim))
                grid[x_dim][y_dim] = Coordinate.closest_manhattan(closest, coordinates)
        return cls((sm_x, sm_y, lg_x, lg_y), grid)

    @staticmethod
    def manhattan_region_all_coords(coordinates):
        """ Calculates the size of the region containing all locations with a total
            manhattan distance of less than 10k """
        # Get the shape of the grid
        sm_x, lg_x, sm_y, lg_y = Grid.grid_shape2(coordinates)
        # Calculate the area within a total manhattan distance of 10k
        area = 0
        # Check each spot
        for x_dim in range(sm_x, lg_x+1):
            for y_dim in range(sm_y, lg_y+1):
                # Calculate total distance at current spot
                current = Coordinate('%s,%s' % (x_dim, y_dim))
                total_dist = Coordinate.total_manhattan_distance(current, coordinates)
                # Increment area if within the alotted total distance
                if total_dist < 10000:
                    area += 1
        return area

    @staticmethod
    def grid_shape(coordinates):
        """ Gets the smallest and largest values for X and Y in a list of
            coordinates and returns them in a tuple """
        # Define initial values based on the first coordinate
        smallest_x, largest_x = (coordinates[0].x_coord, coordinates[0].x_coord)
        smallest_y, largest_y = (coordinates[0].y_coord, coordinates[0].y_coord)
        # Search for the true values
        for coordinate in coordinates:
            smallest_x = coordinate.x_coord if coordinate.x_coord < smallest_x else smallest_x
            largest_x = coordinate.x_coord if coordinate.x_coord > largest_x else largest_x
            smallest_y = coordinate.y_coord if coordinate.y_coord < smallest_y else smallest_y
            largest_y = coordinate.y_coord if coordinate.y_coord > largest_y else largest_y
        # Return the results
        return (smallest_x, largest_x, smallest_y, largest_y)

    @staticmethod
    def grid_shape2(coordinates):
        """ Gets the smallest and largest values for X and Y in a list coordinates
            and uses them to calculate the size of the grid """
        # Define initial values based on the first coordinate
        smallest_x, largest_x = (coordinates[0].x_coord, coordinates[0].x_coord)
        smallest_y, largest_y = (coordinates[0].y_coord, coordinates[0].y_coord)
        # Search for the true values
        for coordinate in coordinates:
            smallest_x = coordinate.x_coord if coordinate.x_coord < smallest_x else smallest_x
            largest_x = coordinate.x_coord if coordinate.x_coord > largest_x else largest_x
            smallest_y = coordinate.y_coord if coordinate.y_coord < smallest_y else smallest_y
            largest_y = coordinate.y_coord if coordinate.y_coord > largest_y else largest_y
        # Return the results
        radius = int(ceil(10000/len(coordinates)))
        return (smallest_x-radius, largest_x+radius, smallest_y-radius, largest_y+radius)

    def get_finite_coordinates(self, coordinates):
        """ Creates a list of coordinates which are contained in a finite area
            within the grid """
            # Calculate all coordinates which are infinite (not on an edge)
        bound_coordinates = [coordinate for coordinate in coordinates if\
            coordinate.x_coord != self.smallest_x and\
            coordinate.x_coord != self.largest_x and\
            coordinate.y_coord != self.smallest_y and\
            coordinate.y_coord != self.largest_y]
        return bound_coordinates

    def coordinate_area(self, coordinate):
        """ Calculates the area a given coordinate holds in a given grid """
        area = 0
        # Count each space in the grid which this coordinate holds
        for x_dim in range(self.smallest_x, self.largest_x+1):
            for y_dim in range(self.smallest_y, self.largest_y+1):
                if self.grid[x_dim][y_dim] == coordinate:
                    area += 1
        return area

    def largest_bound_area(self, coordinates):
        """ Determines which coordinate in a given list encapsulates the
            largest area of a given grid and returns that area """
        largest_area = 0
        # Check the area of each coordinate given
        for coordinate in coordinates:
            coord_area = self.coordinate_area(coordinate)
            # Update the largest area if a bigger one is found
            if coord_area > largest_area:
                largest_area = coord_area
        return largest_area


if __name__ == '__main__':
    # Read in the coordinates
    with open('day6.txt') as coordinates_file:
        COORDINATES = [Coordinate(coord_string) for coord_string in coordinates_file]
    # Calculate the area where the total manhattan distance at each spot < 10k
    print(Grid.manhattan_region_all_coords(COORDINATES))
