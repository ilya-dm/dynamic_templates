from django.core.paginator import Paginator
from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    data = list()
    with open('inflation_russia.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for line in reader:
            data.append(line)

    # чтение csv-файла и заполнение контекста
    year = data[0]
    for i in data:
        for d in i:
            if d != 'Год' and i[d] != '':
                i[d] = float(i[d])
    print(data)
    context = {'year':year,
               'table': data}
    return render(request, template_name, context)
