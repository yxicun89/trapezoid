
def trapezoid_area(top, bottom, height):
    try:

        top, bottom, height = float(top), float(bottom), float(height)

        if top > 0 and bottom > 0 and height > 0: 
            area = (top + bottom) * height * 0.5
            return area

        else:
            raise Exception 
    except:
        return False
