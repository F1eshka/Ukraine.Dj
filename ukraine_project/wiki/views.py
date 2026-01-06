from django.shortcuts import render

from django.shortcuts import redirect
from django.http import HttpResponse

UKRAINE_INFO = {
    "history": "Україна здобула незалежність у 1991 році. Це найбільша країна, що повністю знаходиться в Європі.",
    "facts": "1. Столиця - Київ. 2. Грошова одиниця - гривня. 3. Найглибша станція метро у світі - Арсенальна."
}

CITIES_DB = {
    "kyiv": "Київ — столиця та найбільше місто України. Місто-герой.",
    "lviv": "Львів — культурна столиця України, відома своєю кавою та архітектурою.",
    "odesa": "Одеса — перлина біля моря, головний порт країни.",
    "kharkiv": "Харків — перша столиця, великий науковий центр."
}

HISTORY_DB = {
    1991: "1991 рік: Проголошення Незалежності України.",
    1996: "1996 рік: Прийняття Конституції України.",
    2004: "2004 рік: Помаранчева революція.",
    2014: "2014 рік: Революція Гідності."
}

CITY_YEAR_DB = {
    ("kyiv", 1991): "У 1991 році в Києві підняли синьо-жовтий прапор над Верховною Радою.",
    ("lviv", 1256): "1256 рік: Перша писемна згадка про Львів.",
    ("odesa", 1794): "1794 рік: Офіційна дата заснування Одеси."
}

MENU = """
<hr>
<a href="/">Головна</a> | 
<a href="/history/">Історія</a> | 
<a href="/cities/">Міста</a> | 
<a href="/facts/">Факти</a>
<hr>
"""

def index(request):
    return HttpResponse(f"<h1>Україна 🇺🇦</h1><p>Ласкаво просимо на портал про Україну.</p>{MENU}")

def facts(request):
    return HttpResponse(f"<h1>Факти про країну</h1><p>{UKRAINE_INFO['facts']}</p>{MENU}")

def history_list(request):
    return HttpResponse(f"<h1>Історія України</h1><p>{UKRAINE_INFO['history']}</p>{MENU}")

def cities_list(request):
    city_param = request.GET.get('city')
    year_param = request.GET.get('year')
    
    if city_param and year_param:
        return city_year_detail(request, city_param, int(year_param))

    links = "".join([f"<li><a href='/cities/{c}'>{c.title()}</a></li>" for c in CITIES_DB])
    return HttpResponse(f"<h1>Міста України</h1><ul>{links}</ul>{MENU}")


def city_detail(request, city_name):
    city_key = city_name.lower() 
    if city_key in CITIES_DB:
        return HttpResponse(f"<h1>{city_name.title()}</h1><p>{CITIES_DB[city_key]}</p>{MENU}")
    else:
        return redirect('/cities/')

def history_year(request, year):
    if year in HISTORY_DB:
        return HttpResponse(f"<h1>Події {year} року</h1><p>{HISTORY_DB[year]}</p>{MENU}")
    else:
        return redirect('/history/')

def city_year_detail(request, city_name, year):
    key = (city_name.lower(), year)
    
    if key in CITY_YEAR_DB:
        return HttpResponse(f"<h1>{city_name.title()} у {year} році</h1><p>{CITY_YEAR_DB[key]}</p>{MENU}")
    else:
        return redirect('/cities/')
