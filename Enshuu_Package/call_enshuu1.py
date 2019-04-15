import Enshuu1.circle as circle
import Enshuu1.rectangle as rectangle
import Enshuu1.sector as sector

circle_area=circle.calc_area(r=10)
print("\t area={}".format(circle_area))

rectangle_area=rectangle.calc_area(a=3,b=5)
print("\t area={}".format(circle_area))

sector1_area=sector.calc_area(r=10,radius=180)
sector2_area=sector.calc_area(r=10,radius=0)

for sector_area in [sector1_area,sector2_area]:
    if sector_area is not None:
        print("\t area={}".format(sector_area))
    else:
        print("Radius is Invalid Value!")