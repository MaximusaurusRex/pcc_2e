def car_descriptor(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


print(car_descriptor('honda', 'civic', year=1986, color='silver'))
