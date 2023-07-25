import  math
class Controller:
    def rotate_point(self, x, y, angle):
        angle_rad = math.radians(angle)
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)
        x_rot = (x * cos_theta) - (y * sin_theta)
        y_rot = (x * sin_theta) + (y * cos_theta)
        return x_rot, y_rot

    def calculate_vertices(self, center_x, center_y, length, width, angle):
        half_length = length / 2
        half_width = width / 2

        # Calculate the four corners of the rectangle
        top_left = self.rotate_point(-half_length, half_width, angle)
        top_right = self.rotate_point(half_length, half_width, angle)
        bottom_left = self.rotate_point(-half_length, -half_width, angle)
        bottom_right = self.rotate_point(half_length, -half_width, angle)

        # Translate the rotated points to the center coordinates
        top_left = (top_left[0] + center_x, top_left[1] + center_y)
        top_right = (top_right[0] + center_x, top_right[1] + center_y)
        bottom_left = (bottom_left[0] + center_x, bottom_left[1] + center_y)
        bottom_right = (bottom_right[0] + center_x, bottom_right[1] + center_y)

        return top_left, top_right, bottom_left, bottom_right

    def is_inside_rectangle(point, vertices):
        # Find the minimum and maximum x and y coordinates of the rectangle
        min_x = min(vertex[0] for vertex in vertices)
        max_x = max(vertex[0] for vertex in vertices)
        min_y = min(vertex[1] for vertex in vertices)
        max_y = max(vertex[1] for vertex in vertices)

        # Check if the given point is inside the rectangle
        if min_x <= point[0] <= max_x and min_y <= point[1] <= max_y:
            return True
        else:
            return False

    def check_rectangle_crossing(self, center1_x, center1_y, length1, width1, angle1,
                                 center2_x, center2_y, length2, width2, angle2):
        # Calculate the four vertices for each rectangle
        vertices1 = self.calculate_vertices(center1_x, center1_y, length1, width1, angle1)
        vertices2 = self.calculate_vertices(center2_x, center2_y, length2, width2, angle2)

        # Check for intersection
        for vertex in vertices1:
            if self.is_inside_rectangle(vertex, vertices2):
                return True

        for vertex in vertices2:
            if self.is_inside_rectangle(vertex, vertices1):
                return True

        return False



    # Same as the previous code block



    # # Example usage:
    # center1_x, center1_y = 0, 0
    # length1, width1 = 4, 2
    # angle1 = 0
    #
    # center2_x, center2_y = 3, 0
    # length2, width2 = 4, 2
    # angle2 = 30
    #
    # crossing = check_rectangle_crossing(center1_x, center1_y, length1, width1, angle1,
    #                                     center2_x, center2_y, length2, width2, angle2)
    #
    # if crossing:
    #     print("Rectangles are crossing.")
    # else:
    #     print("Rectangles are not crossing.")