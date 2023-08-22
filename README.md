# PIS

# Evidencija plinomjera

Ova aplikacija je namijenjena zaposlenicima u plinari kako bi mogli bilježiti potrošnju plina za pojedinog građana.


## Funkcionalnosti
* Dodavanje novih mjerenja plinomjera
* Brisanje postojećih plinomjera
* Mijenjanje vrijednosti podataka mjerenja plinomjera 
* Filtriranje plinomjera po datumu mjerenja ili gradu


## Pokretanje backenda
### Stvaranje docker slike (image)
```python
cd Backend
docker build -t gas_meter_app .
```
### Pokretanje docker slike
```python
docker run -p 5000:5000 gas_meter_app
```
