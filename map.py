import folium

year = int(input("Please, enter a year: "))
large = int(input("Please, enter a limit: "))

map = folium.Map()


def get_data():
    """
    None -> list(list, list, ... )
    Read a file and return a list of lists with movies of the year.
    [[movie, place...]
    """
    counter = 0
    new_file = []
    with open("locations.csv", encoding='utf-8', errors='ignore') as file:
        for line in file:
            if counter < large:
                try:
                    line = line.strip().split(",")
                    if line[1] == str(year) and line[3] != 'NO DATA':
                        if line[0].startswith('"'):
                            line[0] = line[0][1:-2]
                        line.pop(2)
                        line.pop(1)
                        new_file.append(line)
                        counter += 1
                except IndexError:
                    continue
    return new_file


def dict_of_movies():
    """
    list(list, list ...) -> dict
    Return a dict with movies and locations.
    {movie : [place, place, ...]}
    """
    new_file = get_data()
    dict_a = {}
    for line in new_file:
        if line[0] not in dict_a:
            dict_a[line[0]] = []
        dict_a.get(line[0]).append(line[1])
    return dict_a


def check_if_films():
    '''
    dict -> list
    Return a list of films.
    '''
    dict_films = dict_of_movies()
    tuple_films = list(dict_films.items())
    list_films = []
    for tupl in tuple_films:
        if len(tupl[1]) == 1:
            list_films.append(tupl)
    return list_films


def check_if_serials():
    '''
    dict -> list
    Return a list of serials.
    '''
    dict_serials = dict_of_movies()
    tuple_serials = list(dict_serials.items())
    list_serials = []
    for tupl in tuple_serials:
        if len(tupl[1]) > 1:
            list_serials.append(tupl)
    return list_serials


def get_place_lst():
    """
    list(list, list, ... ) -> list
    Return a location of movies.
    """
    data = get_data()
    lst = []
    for ls in data:
        if ls[1] not in lst:
            lst.append(ls[1])
    lst_loc = list(set(lst))
    return lst_loc


from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="specify_your_app_name_here", timeout=100)
from geopy.extra.rate_limiter import RateLimiter

geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)


def coordinates_func():
    '''
    list -> list(list,....... ]
    Return a list of lists, every of them consists of a location, a latitude and a longitude.
    '''
    lst_location = get_place_lst()
    all_geo_list = []
    for city in lst_location:
        try:
            location = geolocator.geocode(city)
            small_list = []
            small_list.append(city)
            small_list.append(location.latitude)
            small_list.append(location.longitude)
            all_geo_list.append(small_list)
        except TypeError:
            continue
        except AttributeError:
            continue
    return all_geo_list


def finaly_film_list():
    '''
    list(tuple(str, list)), list -> list
    Return a list of lists:
    [[film, location, latitude, longitude]...]
    '''
    list_film = check_if_films()
    list_coo = coordinates_func()

    all_list = []
    for tupl in list_film:
        for lst in list_coo:
            if tupl[1][0] == lst[0]:
                new_lst = []
                new_lst.append(tupl[0])
                new_lst.append(tupl[1][0])
                new_lst.append(lst[1])
                new_lst.append(lst[2])
                all_list.append(new_lst)
    return all_list


def finaly_serial_list():
    """
    list(tuple(str, list)), list -> list
    Return a list of lists: [[serial, location, latitude, longitude]...]
    """
    list_serials = check_if_serials()
    list_coo = coordinates_func()
    all_list = []
    for lst in list_coo:
        for tupl in list_serials:
            for place in tupl[1]:
                if place == lst[0]:
                    new_lst = []
                    new_lst.append(tupl[0])
                    new_lst.append(place)
                    new_lst.append(lst[1])
                    new_lst.append(lst[2])
                    if new_lst not in all_list:
                        all_list.append(new_lst)
    return all_list


fg_year_film = folium.FeatureGroup(name="Film pointers")


def layer_first_films():
    '''
    [[film, location, latitude, longitude]...........] -> map
    '''
    all_geo_list = finaly_film_list()
    for ls in all_geo_list:
        fg_year_film.add_child(folium.Marker(location=[ls[2], ls[3]], popup=ls[0], icon=folium.Icon(color='green')))
    return map.add_child(fg_year_film)


layer_first_films()

fg_year_serial = folium.FeatureGroup(name="Serial pointers")


def layer_second_serial():
    '''
    [[film, location, latitude, longitude]...........] -> map
    '''
    all_geo_list = finaly_serial_list()
    for ls in all_geo_list:
        fg_year_serial.add_child(folium.Marker(location=[ls[2], ls[3]], popup=ls[0], icon=folium.Icon(color='red')))
    return map.add_child(fg_year_serial)


layer_second_serial()

fg_population = folium.FeatureGroup(name="Population")


def layer_third_population():
    """
    Return a map painting according to the population level of the countries.
    """
    fg_population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                                           style_function=lambda x: {'fillColor': 'green'
                                           if x['properties']['POP2005'] < 10000000
                                           else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                           else 'red'}))
    return map.add_child(fg_population)


layer_third_population()

map.add_child(folium.LayerControl())
map.save('Main_map.html')

