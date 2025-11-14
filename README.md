# projet_web_semantique
L’objectif du projet est de transformer les données ouvertes sur la pollution en données sémantiques et de  lier ses données sémantiques au cloud 


## Structure

- `data/` : fichiers RDF/TTL
- `queries/` : requêtes SPARQL
- `scripts/` : scripts d'import/export ou automation
- `images/` : images de la construction de squelette sous OPENREFINE

## Usage

1. Lancer Fuseki :
```bash
fuseki-server --file=data/dataset.ttl /dataset

