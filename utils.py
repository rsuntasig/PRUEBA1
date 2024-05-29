def get_presupuesto(country_dict):
  presupuesto_dict = {
    '2024': int(country_dict['2024 Presupuesto'])
  }
  labels = presupuesto_dict.keys()
  values = presupuesto_dict.values()
  return labels, values


def presupuesto_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result
