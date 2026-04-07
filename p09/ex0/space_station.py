from pydantic import field
class SpaceStation():
    station_id = field( 3-10 )
    name =String, 1-50 characters
    crew_size =  Integer, 1-20 people
    power_level =  Float, 0.0-100.0 percent
    oxygen_level =  Float, 0.0-100.0 percent
    last_maintenance =  DateTime field
    is_operational =  Boolean, defaults to True
    notes =  Optional string, max 200 characters
def main(): 
    print("Space Station Data Validation")
    print("========================================")
