def distance(line1, line2):
    epsilon = 10

    wPerpendicular = .5
    wLateral = .5
    wAngle = .7

    if angle(line1, line2) > 90:
        return False
    else:
        pDistance = perpendiculardistance(line1, line2)
        latDistance = lateraldistance(line1, line2)
        angDistance = angle(line1, line2)

        distance = wPerpendicular * pDistance + wLateral * latDistance + wAngle * angDistance
        if distance <= epsilon:
            return True
        else:
            return False


def angle(line1, line2):
    return 90


def perpendiculardistance(line1, line2):
    return 10


def lateraldistance(line1, line2):
    return 10