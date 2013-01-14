from math import degrees, atan2, sqrt

def shader(position, source, radius=300, angle=0, spread=90):
    
    """ Returns a 0.0 - 1.0 brightness adjusted to a light source.
    
    The light source is positioned at dx, dy.
    The returned float is calculated for x, y position
    (e.g. an oval at x, y should have this brightness).
    
    The radius influences the strength of the light,
    angle and spread control the direction of the light.
    
    """
    
    if angle != None:
        radius *= 2
    
    x = position.x
    y = position.y
    
    dx = source.x
    dy = source.y
    
    # Get the distance and angle between point and light source.
    d = sqrt((dx-x)**2 + (dy-y)**2)
    a = degrees(atan2(dy-y, dx-x)) + 180
    
    # If no angle is defined, 
    # light is emitted evenly in all directions
    # and carries as far as the defined radius
    # (e.g. like a radial gradient).
    if d <= radius:
        d1 = 1.0 * d / radius
    else:
        d1 = 1.0
    if angle == None:
        return 1-d1  

    # Normalize the light's direction and spread
    # between 0 and 360.
    angle = 360-angle%360
    spread = max(0, min(spread, 360))
    if spread == 0:
        return 0.0    
    
    # Objects that fall within the spreaded direction
    # of the light are illuminated.
    d = abs(a-angle)
    if d <= spread/2:
        d2 = d / spread + d1
    else:
        d2 = 1.0
    
    # Wrapping from 0 to 360:
    # a light source with a direction of 10 degrees
    # and a spread of 45 degrees illuminates
    # objects between 0 and 35 degrees and 350 and 360 degrees.
    if 360-angle <= spread/2:
        d = abs(360-angle+a)
        if d <= spread/2:
            d2 = d / spread + d1
    # Wrapping from 360 to 0.
    if angle < spread/2:
        d = abs(360+angle-a)
        if d <= spread/2:
            d2 = d / spread + d1
    
    return 1 - max(0, min(d2, 1))