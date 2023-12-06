import pytest
import main

@pytest.mark.integration
def test_main(client, init_database):
    path = "http://192.168.3.27:8080/input"
    response = client.post(
        path,
         json =
             {
                 "criteria": [
                     {
                         "criterionName": "Risco",
                         "weight": 4.0,
                         "alternatives": [
                             {
                                 "name": "A",
                                 "note": [
                                     8,
                                     10,
                                     10
                                 ]
                             },
                             {
                                 "name": "B",
                                 "note": [
                                     7,
                                     8,
                                     9
                                 ]
                             },
                             {
                                 "name": "C",
                                 "note": [
                                     1,
                                     2,
                                     4
                                 ]
                             },
                             {
                                 "name": "D",
                                 "note": [
                                     1,
                                     1,
                                     2
                                 ]
                             },
                             {
                                 "name": "E",
                                 "note": [
                                     3,
                                     5,
                                     6
                                 ]
                             },
                             {
                                 "name": "F",
                                 "note": [
                                     5,
                                     6,
                                     7
                                 ]
                             }
                         ]
                     },
                     {
                         "criterionName": "Competitivo",
                         "weight": 3.0,
                         "alternatives": [
                             {
                                 "name": "A",
                                 "note": [
                                     2,
                                     3,
                                     4
                                 ]
                             },
                             {
                                 "name": "B",
                                 "note": [
                                     4,
                                     5,
                                     6
                                 ]
                             },
                             {
                                 "name": "C",
                                 "note": [
                                     4,
                                     6,
                                     7
                                 ]
                             },
                             {
                                 "name": "D",
                                 "note": [
                                     1,
                                     2,
                                     3
                                 ]
                             },
                             {
                                 "name": "E",
                                 "note": [
                                     6,
                                     9,
                                     10
                                 ]
                             },
                             {
                                 "name": "F",
                                 "note": [
                                     6,
                                     9,
                                     10
                                 ]
                             }
                         ]
                     },
                     {
                         "criterionName": "Potencial",
                         "weight": 3.0,
                         "alternatives": [
                             {
                                 "name": "A",
                                 "note": [
                                     1,
                                     2,
                                     4
                                 ]
                             },
                             {
                                 "name": "B",
                                 "note": [
                                     7,
                                     8,
                                     9
                                 ]
                             },
                             {
                                 "name": "C",
                                 "note": [
                                     3,
                                     5,
                                     6
                                 ]
                             },
                             {
                                 "name": "D",
                                 "note": [
                                     7,
                                     9,
                                     10
                                 ]
                             },
                             {
                                 "name": "E",
                                 "note": [
                                     8,
                                     10,
                                     10
                                 ]
                             },
                             {
                                 "name": "F",
                                 "note": [
                                     1,
                                     2,
                                     3
                                 ]
                             }
                         ]
                     }
                 ]
            }
    )
    assert response.status_code == 200
    #assert b'{"ranking": [{"Alternativa": "B", "Nota": 0.25297745436318164}, {"Alternativa": "E", "Nota": 0.33559956729789275}, {"Alternativa": "F", "Nota": 0.48841554361417727}, {"Alternativa": "A", "Nota": 0.49003173076923084}, {"Alternativa": "C", "Nota": 0.6927731930975416}, {"Alternativa": "D", "Nota": 0.7402025108579762}]}\n' in response.data
