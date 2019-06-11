from typing import Dict, Any

import requests
from django.shortcuts import render
from SPARQLWrapper import SPARQLWrapper, JSON

# Create your views here.
def index(request):
    if request.method =='POST':
        stringbusca = request.POST.get('palavrachave')

        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        busca = stringbusca
        sparql.setQuery("""
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
            PREFIX dbpprop: <http://dbpedia.org/property/>

            SELECT DISTINCT 
                ?name 
                ?release
                ?country 
                ?numberOfEpisodes
                ?numberOfSeasons
                ?abstract 

            WHERE {
            ?instance a <http://dbpedia.org/ontology/TelevisionShow>.
            ?instance foaf:name ?name .
            FILTER REGEX (?name, '^""" + busca + """$', 'i').

            OPTIONAL {
                ?instance dbpprop:country ?country
            }
            OPTIONAL {
                ?instance dbpedia-owl:numberOfEpisodes ?numberOfEpisodes
            }
             OPTIONAL {
                ?instance dbpedia-owl:numberOfSeasons ?numberOfSeasons
            }
            OPTIONAL {
                ?instance dbpedia-owl:releaseDate ?release
            }
            OPTIONAL {

                ?instance dbpedia-owl:abstract ?abstract .
                FILTER (LANG(?abstract) = 'pt').
            }
        }
        """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        print(results)



        context = {'consult': results['results']['bindings'][0]['name']['value'],
                   'abs': results['results']['bindings'][0]['abstract']['value'],
                   'lanc': results['results']['bindings'][0]['release']['value'],
                   'pais': results['results']['bindings'][0]['country']['value'],
                   'eps': results['results']['bindings'][0]['numberOfEpisodes']['value'],
                   'temporadas': results['results']['bindings'][0]['numberOfSeasons']['value']}

        return render(request, 'interface/templates/index.html', context)
    else:
        stringbusca = request.POST.get('palavrachave')

        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        busca = stringbusca
        sparql.setQuery("""
                    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                    PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
                    PREFIX dbpprop: <http://dbpedia.org/property/>

                    SELECT DISTINCT 
                        ?name 
                        ?release
                        ?country 
                        ?numberOfEpisodes
                        ?numberOfSeasons
                        ?abstract 

                    WHERE {
                    ?instance a <http://dbpedia.org/ontology/TelevisionShow>.
                    ?instance foaf:name ?name .
                    FILTER REGEX (?name, '^""" + busca + """$', 'i').

                    OPTIONAL {
                        ?instance dbpprop:country ?country
                    }
                    OPTIONAL {
                        ?instance dbpedia-owl:numberOfEpisodes ?numberOfEpisodes
                    }
                     OPTIONAL {
                        ?instance dbpedia-owl:numberOfSeasons ?numberOfSeasons
                    }
                    OPTIONAL {
                        ?instance dbpedia-owl:released ?release
                    }
                    OPTIONAL {

                        ?instance dbpedia-owl:abstract ?abstract .
                        FILTER (LANG(?abstract) = 'pt').
                    }
                }
                """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        print(results)

        context = {'consult': results['results']['bindings'][0]['name']['value'],
                   'abs': results['results']['bindings'][0]['abstract']['value'],
                   'lanc': results['results']['bindings'][0]['release']['value'],
                   'pais': results['results']['bindings'][0]['country']['value'],
                   'eps': results['results']['bindings'][0]['numberOfEpisodes']['value'],
                   'temporadas': results['results']['bindings'][0]['numberOfSeasons']['value']}

    return render(request, 'interface/templates/index.html', context)







