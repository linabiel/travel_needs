from db.run_sql import run_sql
from models.country import Country

def save(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING id"
    values = [country.name]
    results = run_sql(sql, values)
    country.id = results[0]['id']
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)