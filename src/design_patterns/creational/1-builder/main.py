import builder

if __name__ == '__main__':
    director = builder.Director()

    director.builder = builder.BuilderHouse()
    director.construct_building()
    building = director.get_building()
    print(building)

    director.builder = builder.BuilderFlat()
    director.construct_building()
    building = director.get_building()
    print(building)

