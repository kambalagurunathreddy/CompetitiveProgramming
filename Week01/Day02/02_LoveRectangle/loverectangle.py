def loverectangle(rect1, rect2):
    Rightxa=rect1['left_x']+rect1['width']
    Bottomya=rect1['bottom_y']+rect1['height']
    Rightxb=rect2['left_x']+rect2['width']    
    Bottomyb=rect2['bottom_y']+rect2['height']
    xr=max(rect1['left_x'],rect2['left_x'])
    width=min(Rightxa,Rightxb)-xr
    yr=max(rect1['bottom_y'],rect2['bottom_y'])   
    height=min(Bottomya,Bottomyb)-yr
    if((Rightxa<=rect2['left_x'] and Bottomya<=rect2['bottom_y']) 
        or ((Bottomya or rect1['bottom_y'])==rect2['bottom_y'])
        or (Rightxa or rect1['left_x'] )==rect2['left_x']):
        return{
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }

    return {
            'left_x': xr,
            'bottom_y': yr,
            'width': width,
            'height': height,
        }
rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 3,
        }
rect2 = {
    'left_x': 5,
    'bottom_y': 2,
    'width': 3,
    'height': 6,
}
print(loverectangle(rect1,rect2))