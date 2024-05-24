# 2023_wa_sz_prochazka_gaflix
**epicky high budget netflix**
1. `git clone https://github.com/gyarab/2023_wa_sz_prochazka_gaflix.git`
2. `py -3 -m venv venv`
3. `source ./venv/Scripts/activate`
4. `pip install -r requirements.txt`
## Zapnuti serveru
1. `python manage.py runserver`
## Vytvoremi admina
1. `./manage.py createsuperuser`
## Database
1. `python manage.py makemigrations`
2. `python manage.py migrate`
- když to troli smazat slozku `migrations`
## Fixtures
- dump test data`./manage.py dumpdata --indent 2 filmy.MODELNAME > fixtures/FILENAMEOFMODEL.json`  
  UTF-8 Chars: sh - `export PYTHONIOENCODING=utf-8 && python manage.py dumpdata --indent 2 MODELNAME > fixtures/FILENAMEOFMODEL.json`
- load fixtures - `python manage.py loaddata fixtures/FILENAMEOFMODEL.json`
