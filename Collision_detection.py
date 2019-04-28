# Collision Detection class

class Collision_Detection:
    def takra(self, rect1, rect2):
        if rect1.x > rect2.x:
            rect1,rect2 = rect2,rect1
        if rect1.x + rect1.w >= rect2.x:
            if rect1.y + rect1.h < rect2.y:
                return False
            elif rect1.y > rect2.y + rect2.h:
                return False
            return True
        return False

