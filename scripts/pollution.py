from rdflib import Graph

g = Graph()
g.parse("data/pollution.ttl", format="turtle")

# 1Liste des pays
q1 = """
PREFIX ex: <http://example.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?country ?label ?code
WHERE {
  ?country a ex:Country ;
           rdfs:label ?label ;
           ex:countryCode ?code .
}
"""
print("=== Liste des pays ===")
for row in g.query(q1):
    print(f"{row.label} ({row.code})")

# 2️⃣ Observations pour Afghanistan
q2 = """
PREFIX ex: <http://example.com/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?year (ROUND(?air) as ?air) (ROUND(?house) as ?house) (ROUND(?particulate) as ?particulate) (ROUND(?ozone) as ?ozone)
WHERE {
  ?obs a ex:Observation ;
       ex:hasCountry ex:Afghanistan ;
       ex:hasYear ?y ;
       ex:deathAirPollution ?air ;
       ex:deathHouseholdPollution ?house ;
       ex:deathAmbientParticulatePollution ?particulate ;
       ex:deathAmbientOzonePollution ?ozone .
  ?y ex:value ?year .
}
ORDER BY ?year
"""
print("\n=== Observations Afghanistan ===")
for row in g.query(q2):
    print(f"{row.year}: air={row.air}, household={row.house}, ozone={row.ozone}, particulate={row.particulate}")
# 3Moyenne globale
q3 = """
PREFIX ex: <http://example.com/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT
  (AVG(xsd:decimal(?air)) AS ?avgAir)
  (AVG(xsd:decimal(?house)) AS ?avgHouse)
  (AVG(xsd:decimal(?particulate)) AS ?avgParticulate)
  (AVG(xsd:decimal(?ozone)) AS ?avgOzone)
WHERE {
  ?obs a ex:Observation ;
       ex:deathAirPollution ?air ;
       ex:deathHouseholdPollution ?house ;
       ex:deathAmbientParticulatePollution ?particulate ;
       ex:deathAmbientOzonePollution ?ozone .
}
"""
print("\n=== Moyennes globales ===")
for row in g.query(q3):
    print(f"Air={row.avgAir}, Household={row.avgHouse}, Particulate={row.avgParticulate}, Ozone={row.avgOzone}")

# Dernière année
q4 = """
PREFIX ex: <http://example.com/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT (MAX(xsd:integer(?year)) AS ?latestYear)
WHERE {
  ?y a ex:Year ;
     ex:value ?year .
}
"""
print("\n=== Année la plus récente ===")
for row in g.query(q4):
    print(f"Dernière année disponible: {row.latestYear}")
