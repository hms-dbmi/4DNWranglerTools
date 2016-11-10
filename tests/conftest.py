# flake8: noqa
import pytest
import wranglertools.fdnDCIC as fdnDCIC


class MockedResponse(object):
    def __init__(self, json, status):
        self._json = json
        self.status_code = status

    def json(self):
        return self._json


@pytest.fixture
def connection():
    keypairs = {
                "default":
                {"server": "https://data.4dnucleome.org/",
                 "key": "testkey",
                 "secret": "testsecret"
                 }
                }
    key = fdnDCIC.FDN_Key(keypairs, "default")
    connection = fdnDCIC.FDN_Connection(key)
    return connection


@pytest.fixture
def connection_public():
    keypairs = {
                "default":
                {"server": "https://data.4dnucleome.org/",
                 "key": "",
                 "secret": ""
                 }
                }
    key2 = fdnDCIC.FDN_Key(keypairs, "default")
    connection = fdnDCIC.FDN_Connection(key2)
    return connection


@pytest.fixture
def connection_koray():
    keypairs = {
                "default": {
                  "key": "E2IG34B5",
                  "secret": "x24acskzaavaqgva",
                  "server": "http://4dn-web-dev.us-east-1.elasticbeanstalk.com/"
                }
                }
    key = fdnDCIC.FDN_Key(keypairs, "default")
    connection = fdnDCIC.FDN_Connection(key)
    return connection


@pytest.fixture(scope="module")
def item_properties():
    return {'@id': {'calculatedProperty': True, 'title': 'ID', 'type': 'string'},
            '@type': {'calculatedProperty': True,
                      'items': {'type': 'string'},
                      'title': 'Type',
                      'type': 'array'},
            'description': {'rdfs:subPropertyOf': 'dc:description',
                            'title': 'Description',
                            'type': 'string'},
            "experiment_sets": {"type": "array",
                                "description": "Experiment Sets that are associated with this experiment.",
                                "title": "Experiment Sets",
                                "items": {
                                    "type": "string",
                                    "description": "An experiment set that is associated wtih this experiment.",
                                    "linkTo": "ExperimentSet",
                                    "title": "Experiment Set"},
                                "uniqueItems": True},
            'end_date': {'anyOf': [{'format': 'date-time'}, {'format': 'date'}],
                         'comment': 'Date can be submitted as YYYY-MM-DD or '
                         'YYYY-MM-DDTHH:MM:SSTZD (TZD is the time zone '
                         'designator; use Z to express time in UTC or for time '
                         'expressed in local time add a time zone offset from '
                         'UTC +HH:MM or -HH:MM).',
                         'title': 'End date',
                         'type': 'string'},
            'name': {'description': 'The official grant number from the NIH database, if '
                     'applicable',
                     'pattern': '^[A-Za-z0-9\\-]+$',
                     'title': 'Number',
                     'type': 'string',
                     'uniqueKey': True},
            'pi': {'comment': 'See user.json for available identifiers.',
                   'description': 'Principle Investigator of the grant.',
                   'linkTo': 'User',
                   'title': 'P.I.',
                   'type': 'string'},
            'project': {'description': 'The name of the consortium project',
                        'enum': ['4DN', 'External'],
                        'title': 'Project',
                        'type': 'string'},
            'schema_version': {'comment': 'Do not submit, value is assigned by the '
                               'server. The version of the JSON schema that '
                               'the server uses to validate the object. Schema '
                               'version indicates generation of schema used to '
                               'save version to to enable upgrade steps to '
                               'work. Individual schemas should set the '
                               'default.',
                               'default': '1',
                               'pattern': '^\\d+(\\.\\d+)*$',
                               'requestMethod': [],
                               'title': 'Schema Version',
                               'type': 'string'},
            'start_date': {'anyOf': [{'format': 'date-time'}, {'format': 'date'}],
                           'comment': 'Date can be submitted as YYYY-MM-DD or '
                           'YYYY-MM-DDTHH:MM:SSTZD (TZD is the time zone '
                           'designator; use Z to express time in UTC or for '
                           'time expressed in local time add a time zone '
                           'offset from UTC +HH:MM or -HH:MM).',
                           'title': 'Start date',
                           'type': 'string'},
            'status': {'default': 'current',
                       'enum': ['current',
                                'in progress',
                                'deleted',
                                'replaced',
                                'released',
                                'revoked'],
                       'title': 'Status',
                       'type': 'string'},
            'title': {'description': 'The grant name from the NIH database, if '
                      'applicable.',
                      'rdfs:subPropertyOf': 'dc:title',
                      'title': 'Name',
                      'type': 'string'},
            'url': {'@type': '@id',
                    'description': 'An external resource with additional information '
                    'about the grant.',
                    'format': 'uri',
                    'rdfs:subPropertyOf': 'rdfs:seeAlso',
                    'title': 'URL',
                    'type': 'string'},
            'uuid': {'format': 'uuid',
                     'requestMethod': 'POST',
                     'serverDefault': 'uuid4',
                     'title': 'UUID',
                     'type': 'string'},
            'viewing_group': {'description': 'The group that determines which set of data '
                              'the user has permission to view.',
                              'enum': ['4DN', 'Not 4DN'],
                              'title': 'View access group',
                              'type': 'string'}}


@pytest.fixture
def calc_properties():
    return {'@id': {'calculatedProperty': True, 'title': 'ID', 'type':
                    'string'},
            '@type': {'calculatedProperty': True,
                      'items': {'type': 'string'},
                      'title': 'Type',
                      'type': 'array'},
            'description': {'rdfs:subPropertyOf': 'dc:description',
                            'title': 'Description',
                            'type': 'string'},
            }


@pytest.fixture
def embed_properties():
    return {'experiment_relation': {'description': 'All related experiments',
                                    'items': {'additionalProperties': False,
                                              'properties':
                                              {'experiment': {'description': 'The '
                                                                             'related '
                                                                             'experiment',
                                                              'linkTo': 'Experiment',
                                                              'type': 'string'},
                                               'relationship_type': {'description': 'A '
                                                                     'controlled '
                                                                     'term '
                                                                     'specifying '
                                                                     'the '
                                                                     'relationship '
                                                                     'between '
                                                                     'experiments.',
                                                                     'enum': ['controlled '
                                                                              'by',
                                                                              'control '
                                                                              'for',
                                                                              'derived '
                                                                              'from',
                                                                              'source '
                                                                              'for'],
                                                                     'title': 'Relationship '
                                                                              'Type',
                                                                              'type': 'string'}},
                                              'title': 'Experiment relation',
                                              'type': 'object'},
                                    'title': 'Experiment relations',
                                    'type': 'array'},
            }


@pytest.fixture
def file_metadata():
    from collections import OrderedDict
    return OrderedDict([('aliases', 'dcic:HIC00test2'),
                        ('award', '/awards/OD008540-01/'),
                        ('file_classification', 'raw file'),
                        ('file_format', 'fastq'),
                        ('filesets', ''),
                        ('instrument', 'Illumina HiSeq 2000'),
                        ('lab', '/labs/erez-liebermanaiden-lab/'),
                        ('paired_end', ''),
                        ('related_files.file', 'testfile.fastq'),
                        ('related_files.relationship_type', 'related_to'),
                        ('experiment_relation.experiment', 'test:exp002'),
                        ('experiment_relation.relationship_type', 'controlled by'),
                        ('experiment_relation.experiment-1', 'test:exp003'),
                        ('experiment_relation.relationship_type-1', 'source for'),
                        ('experiment_relation.experiment-2', 'test:exp004'),
                        ('experiment_relation.relationship_type-2', 'source for'),
                        ('status', 'uploaded')])


@pytest.fixture
def file_metadata_type():
    return {'aliases': 'array',
            'award': 'string',
            'file_classification': 'string',
            'file_format': 'string',
            'filesets': 'array',
            'instrument': 'string',
            'lab': 'string',
            'paired_end': 'string',
            'related_files.file': 'array',
            'related_files.relationship_type': 'array',
            'experiment_relation.experiment': 'array',
            'experiment_relation.relationship_type': 'array',
            'experiment_relation.experiment-1': 'array',
            'experiment_relation.relationship_type-1': 'array',
            'experiment_relation.experiment-2': 'array',
            'experiment_relation.relationship_type-2': 'array',
            'status': 'string'}


@pytest.fixture
def returned_award_schema():
    data = {"title":"Grant","id":"/profiles/award.json","$schema":"http://json-schema.org/draft-04/schema#","required":["name"],"identifyingProperties":["uuid","name","title"],"additionalProperties":False,"mixinProperties":[{"$ref":"mixins.json#/schema_version"},{"$ref":"mixins.json#/uuid"},{"$ref":"mixins.json#/submitted"},{"$ref":"mixins.json#/status"}],"type":"object","properties":{"status":{"readonly":True,"type":"string","default":"released","enum":["released","current","revoked","deleted","replaced","in review by lab","in review by project","released to project"],"title":"Status","permission":"import_items"},"submitted_by":{"readonly":True,"type":"string","serverDefault":"userid","linkTo":"User","comment":"Do not submit, value is assigned by the server. The user that created the object.","title":"Submitted by","rdfs:subPropertyOf":"dc:creator","permission":"import_items"},"date_created":{"readonly":True,"type":"string","serverDefault":"now","anyOf":[{"format":"date-time"},{"format":"date"}],"comment":"Do not submit, value is assigned by the server. The date the object is created.","title":"Date created","rdfs:subPropertyOf":"dc:created","permission":"import_items"},"uuid":{"requestMethod":"POST","readonly":True,"type":"string","serverDefault":"uuid4","format":"uuid","title":"UUID","permission":"import_items"},"schema_version":{"requestMethod":[],"type":"string","default":"1","pattern":"^\\d+(\\.\\d+)*$","comment":"Do not submit, value is assigned by the server. The version of the JSON schema that the server uses to validate the object. Schema version indicates generation of schema used to save version to to enable upgrade steps to work. Individual schemas should set the default.","title":"Schema Version"},"title":{"description":"The grant name from the NIH database, if applicable.","type":"string","title":"Name","rdfs:subPropertyOf":"dc:title"},"name":{"description":"The official grant number from the NIH database, if applicable","uniqueKey":True,"type":"string","title":"Number","pattern":"^[A-Za-z0-9\\-]+$"},"description":{"type":"string","title":"Description","rdfs:subPropertyOf":"dc:description"},"start_date":{"anyOf":[{"format":"date-time"},{"format":"date"}],"comment":"Date can be submitted as YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSTZD (TZD is the time zone designator; use Z to express time in UTC or for time expressed in local time add a time zone offset from UTC +HH:MM or -HH:MM).","type":"string","title":"Start date"},"end_date":{"anyOf":[{"format":"date-time"},{"format":"date"}],"comment":"Date can be submitted as YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSTZD (TZD is the time zone designator; use Z to express time in UTC or for time expressed in local time add a time zone offset from UTC +HH:MM or -HH:MM).","type":"string","title":"End date"},"url":{"format":"uri","type":"string","@type":"@id","description":"An external resource with additional information about the grant.","title":"URL","rdfs:subPropertyOf":"rdfs:seeAlso"},"pi":{"description":"Principle Investigator of the grant.","comment":"See user.json for available identifiers.","type":"string","title":"P.I.","linkTo":"User"},"project":{"description":"The name of the consortium project","type":"string","title":"Project","enum":["4DN","External"]},"viewing_group":{"description":"The group that determines which set of data the user has permission to view.","type":"string","title":"View access group","enum":["4DN","Not 4DN"]},"@id":{"calculatedProperty":True,"type":"string","title":"ID"},"@type":{"calculatedProperty":True,"title":"Type","type":"array","items":{"type":"string"}}},"boost_values":{"name":1,"title":1,"pi.title":1},"@type":["JSONSchema"]}
    return MockedResponse(data, 200)


@pytest.fixture
def returned_vendor_schema():
    data = {"title":"Vendor","description":"Schema for submitting an originating lab or vendor.","id":"/profiles/vendor.json","$schema":"http://json-schema.org/draft-04/schema#","type":"object","required":["title"],"identifyingProperties":["uuid","name"],"additionalProperties":False,"mixinProperties":[{"$ref":"mixins.json#/schema_version"},{"$ref":"mixins.json#/uuid"},{"$ref":"mixins.json#/status"},{"$ref":"mixins.json#/notes"},{"$ref":"mixins.json#/submitted"},{"$ref":"mixins.json#/attribution"},{"$ref":"mixins.json#/aliases"}],"properties":{"aliases":{"type":"array","default":[],"uniqueItems":True,"title":"Lab aliases","description":"Lab specific identifiers to reference an object.","items":{"comment":"Current convention is colon separated lab name and lab identifier. (e.g. john-doe:42).","pattern":"^\\S+:\\S+","uniqueKey":"alias","title":"Lab alias","description":"A lab specific identifier to reference an object.","type":"string"}},"award":{"comment":"See award.json for list of available identifiers.","title":"Grant","description":"Grant associated with the submission.","linkTo":"Award","type":"string"},"lab":{"description":"Lab associated with the submission.","linkSubmitsFor":True,"title":"Lab","comment":"See lab.json for list of available identifiers.","linkTo":"Lab","type":"string"},"date_created":{"anyOf":[{"format":"date-time"},{"format":"date"}],"serverDefault":"now","readonly":True,"type":"string","comment":"Do not submit, value is assigned by the server. The date the object is created.","title":"Date created","rdfs:subPropertyOf":"dc:created","permission":"import_items"},"submitted_by":{"serverDefault":"userid","readonly":True,"type":"string","comment":"Do not submit, value is assigned by the server. The user that created the object.","linkTo":"User","title":"Submitted by","rdfs:subPropertyOf":"dc:creator","permission":"import_items"},"notes":{"elasticsearch_mapping_index_type":{"title":"Field mapping index type","description":"Defines one of three types of indexing available","type":"string","enum":["analyzed","not_analyzed","no"],"default":"analyzed"},"description":"DCIC internal notes.","type":"string","title":"Notes"},"status":{"readonly":True,"default":"in review by lab","title":"Status","type":"string","enum":["released","current","revoked","deleted","replaced","in review by lab","in review by project","released to project"],"permission":"import_items"},"uuid":{"serverDefault":"uuid4","readonly":True,"requestMethod":"POST","type":"string","title":"UUID","format":"uuid","permission":"import_items"},"schema_version":{"default":"1","pattern":"^\\d+(\\.\\d+)*$","requestMethod":[],"title":"Schema Version","comment":"Do not submit, value is assigned by the server. The version of the JSON schema that the server uses to validate the object. Schema version indicates generation of schema used to save version to to enable upgrade steps to work. Individual schemas should set the default.","type":"string"},"description":{"title":"Description","description":"A plain text description of the source.","type":"string","default":""},"title":{"title":"Name","description":"The complete name of the originating lab or vendor. ","type":"string"},"name":{"uniqueKey":True,"type":"string","description":"DON'T SUBMIT, auto-generated, use for referencing vendors in other sheets.","pattern":"^[a-z0-9\\-]+$"},"url":{"title":"URL","description":"An external resource with additional information about the source.","type":"string","format":"uri"},"@type":{"calculatedProperty":True,"title":"Type","type":"array","items":{"type":"string"}},"@id":{"calculatedProperty":True,"title":"ID","type":"string"}},"boost_values":{"name":1,"title":1},"@type":["JSONSchema"]}
    return MockedResponse(data, 200)


@pytest.fixture
def returned_vendor_items():
    data = {"@id": "/search/?type=Vendor&format=json", "clear_filters": "/search/?type=Vendor", "total": 16, "@context": "/terms/", "filters": [{"field": "type", "term": "Vendor", "remove": "/search/?format=json"}], "facets": [{"field": "type", "title": "Data Type", "terms": [{"doc_count": 16, "key": "Vendor"}, {"doc_count": 0, "key": "AccessKey"}, {"doc_count": 0, "key": "AnalysisStep"}, {"doc_count": 0, "key": "Award"}, {"doc_count": 0, "key": "Biosample"}, {"doc_count": 0, "key": "BiosampleCellCulture"}, {"doc_count": 0, "key": "Biosource"}, {"doc_count": 0, "key": "Construct"}, {"doc_count": 0, "key": "Document"}, {"doc_count": 0, "key": "Enzyme"}, {"doc_count": 0, "key": "Experiment"}, {"doc_count": 0, "key": "ExperimentCaptureC"}, {"doc_count": 0, "key": "ExperimentHiC"}, {"doc_count": 0, "key": "ExperimentSet"}, {"doc_count": 0, "key": "File"}, {"doc_count": 0, "key": "FileFasta"}, {"doc_count": 0, "key": "FileFastq"}, {"doc_count": 0, "key": "FileProcessed"}, {"doc_count": 0, "key": "FileSet"}, {"doc_count": 0, "key": "GenomicRegion"}, {"doc_count": 0, "key": "Individual"}, {"doc_count": 0, "key": "IndividualHuman"}, {"doc_count": 0, "key": "IndividualMouse"}, {"doc_count": 0, "key": "Lab"}, {"doc_count": 0, "key": "Modification"}, {"doc_count": 0, "key": "Organism"}, {"doc_count": 0, "key": "Protocol"}, {"doc_count": 0, "key": "Publication"}, {"doc_count": 0, "key": "PublicationTracking"}, {"doc_count": 0, "key": "Software"}, {"doc_count": 0, "key": "Target"}, {"doc_count": 0, "key": "Treatment"}, {"doc_count": 0, "key": "TreatmentChemical"}, {"doc_count": 0, "key": "TreatmentRnai"}, {"doc_count": 0, "key": "User"}, {"doc_count": 0, "key": "Workflow"}, {"doc_count": 0, "key": "WorkflowMapping"}, {"doc_count": 0, "key": "WorkflowRun"}], "total": 16}, {"field": "audit.INTERNAL_ACTION.category", "title": "Audit category: DCC ACTION", "terms": [{"doc_count": 0, "key": "mismatched status"}, {"doc_count": 0, "key": "validation error"}, {"doc_count": 0, "key": "validation error: published_by"}, {"doc_count": 0, "key": "validation error: run_status"}, {"doc_count": 0, "key": "validation error: status"}, {"doc_count": 0, "key": "validation error: version"}, {"doc_count": 0, "key": "validation error: workflow_steps/0"}], "total": 16}], "columns": {"@id": "ID", "title": "Name", "description": "Description", "name": "name", "aliases": "Lab aliases"}, "views": [{"href": "/report/?type=Vendor&format=json", "icon": "table", "title": "View tabular report"}], "@type": ["Search"], "notification": "Success", "title": "Search", "@graph": [{"@type": ["Vendor", "Item"], "name": "test-vendor3", "title": "Test Vendor3", "description": "test description", "aliases": ["dcic:vendor_test3"], "@id": "/vendors/test-vendor3/"}, {"@type": ["Vendor", "Item"], "name": "test-vendor2", "title": "Test Vendor2", "description": "test description", "aliases": ["dcic:vendor_test2"], "@id": "/vendors/test-vendor2/"}, {"@type": ["Vendor", "Item"], "name": "test-vendor", "title": "Test Vendor", "description": "test description", "aliases": ["dcic:vendor_test"], "@id": "/vendors/test-vendor/"}, {"@type": ["Vendor", "Item"], "name": "atcc", "title": "ATCC", "description": "", "aliases": ["dekker:atcc"], "@id": "/vendors/atcc/"}, {"@type": ["Vendor", "Item"], "name": "coriell", "title": "Coriell", "description": "", "aliases": ["dekker:coriell"], "@id": "/vendors/coriell/"}, {"@type": ["Vendor", "Item"], "name": "wicell", "title": "WiCell", "description": "", "aliases": ["dekker:wicell"], "@id": "/vendors/wicell/"}, {"@type": ["Vendor", "Item"], "name": "-weissman-lab", "title": " Weissman Lab", "description": "", "aliases": ["dcic:weismann"], "@id": "/vendors/-weissman-lab/"}, {"@type": ["Vendor", "Item"], "name": "haplogen-gmbh", "title": "Haplogen GmbH", "description": "", "aliases": ["dcic:haplogen"], "@id": "/vendors/haplogen-gmbh/"}, {"@type": ["Vendor", "Item"], "name": "lonza-walkersville-inc", "title": "Lonza Walkersville Inc", "description": "", "aliases": ["dcic:lonza"], "@id": "/vendors/lonza-walkersville-inc/"}, {"@type": ["Vendor", "Item"], "name": "american-type-culture-collection", "title": "American Type Culture Collection", "description": "", "aliases": ["dcic:atcc"], "@id": "/vendors/american-type-culture-collection/"}, {"@type": ["Vendor", "Item"], "name": "coriell-institute-for-medical-research", "title": "Coriell Institute for Medical Research", "description": "", "aliases": ["dcic:coriell"], "@id": "/vendors/coriell-institute-for-medical-research/"}, {"@type": ["Vendor", "Item"], "name": "aiden-lab", "title": "Aiden Lab", "description": "", "aliases": ["dcic:aidenlab"], "@id": "/vendors/aiden-lab/"}, {"@type": ["Vendor", "Item"], "name": "horizon-genomics", "title": "Horizon Genomics", "description": "", "aliases": ["dcic:horizon"], "@id": "/vendors/horizon-genomics/"}, {"@type": ["Vendor", "Item"], "name": "thermofisher-scientific", "title": "ThermoFisher Scientific", "description": "previously also Fermentas", "aliases": [], "@id": "/vendors/thermofisher-scientific/"}, {"@type": ["Vendor", "Item"], "name": "new-england-biolabs", "title": "New England Biolabs", "description": "", "aliases": [], "@id": "/vendors/new-england-biolabs/"}, {"@type": ["Vendor", "Item"], "name": "worthington-biochemical", "title": "Worthington Biochemical", "description": "", "aliases": [], "@id": "/vendors/worthington-biochemical/"}], "sort": {"date_created": {"order": "desc", "ignore_unmapped": True}, "label": {"order": "asc", "ignore_unmapped": True, "missing": "_last"}}}
    return MockedResponse(data, 200)


@pytest.fixture
def returned_post_new_vendor():
    data = {'status': 'success', '@type': ['result'], '@graph': [{'title': 'Test Vendor2', 'date_created': '2016-11-10T16:14:28.097832+00:00', 'submitted_by': '/users/986b362f-4eb6-4a9c-8173-3ab267307e3a/', 'aliases': ['dcic:vendor_test2'], 'name': 'test-vendor', 'status': 'in review by lab', 'uuid': 'ab487748-5904-42c8-9a8b-47f82df9f049', '@type': ['Vendor', 'Item'], 'schema_version': '1', 'url': 'http://www.test_vendor.com', '@id': '/vendors/test-vendor/', 'description': 'test description'}]}
    return MockedResponse(data, 201)


@pytest.fixture
def returned__patch_vendor():
    data = {'@type': ['result'], 'status': 'success', '@graph': [{'name': 'test-vendor', 'aliases': ['dcic:vendor_test'], 'schema_version': '1', 'description': 'test description new', 'status': 'in review by lab', 'title': 'Test Vendor', 'date_created': '2016-11-10T16:12:45.436813+00:00', 'url': 'http://www.test_vendor.com', '@id': '/vendors/test-vendor/', 'uuid': '004e2c5e-9825-43e2-98d2-fa078dd68be2', 'submitted_by': '/users/986b362f-4eb6-4a9c-8173-3ab267307e3a/', '@type': ['Vendor', 'Item']}]}
    return MockedResponse(data, 200)


@pytest.fixture
def award_dict():
    return {'properties': {'project': {'type': 'string', 'title': 'Project', 'description': 'The name of the consortium project', 'enum': ['4DN', 'External']}, 'start_date': {'anyOf': [{'format': 'date-time'}, {'format': 'date'}], 'type': 'string', 'title': 'Start date', 'comment': 'Date can be submitted as YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSTZD (TZD is the time zone designator; use Z to express time in UTC or for time expressed in local time add a time zone offset from UTC +HH:MM or -HH:MM).'}, '@id': {'type': 'string', 'title': 'ID', 'calculatedProperty': True}, 'description': {'type': 'string', 'rdfs:subPropertyOf': 'dc:description', 'title': 'Description'}, 'end_date': {'anyOf': [{'format': 'date-time'}, {'format': 'date'}], 'type': 'string', 'title': 'End date', 'comment': 'Date can be submitted as YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSTZD (TZD is the time zone designator; use Z to express time in UTC or for time expressed in local time add a time zone offset from UTC +HH:MM or -HH:MM).'}, 'name': {'uniqueKey': True, 'type': 'string', 'pattern': '^[A-Za-z0-9\\-]+$', 'title': 'Number', 'description': 'The official grant number from the NIH database, if applicable'}, '@type': {'items': {'type': 'string'}, 'type': 'array', 'title': 'Type', 'calculatedProperty': True}, 'submitted_by': {'serverDefault': 'userid', 'permission': 'import_items', 'type': 'string', 'rdfs:subPropertyOf': 'dc:creator', 'title': 'Submitted by', 'readonly': True, 'linkTo': 'User', 'comment': 'Do not submit, value is assigned by the server. The user that created the object.'}, 'date_created': {'serverDefault': 'now', 'permission': 'import_items', 'type': 'string', 'rdfs:subPropertyOf': 'dc:created', 'title': 'Date created', 'readonly': True, 'comment': 'Do not submit, value is assigned by the server. The date the object is created.', 'anyOf': [{'format': 'date-time'}, {'format': 'date'}]}, 'title': {'type': 'string', 'rdfs:subPropertyOf': 'dc:title', 'title': 'Name', 'description': 'The grant name from the NIH database, if applicable.'}, 'viewing_group': {'type': 'string', 'title': 'View access group', 'description': 'The group that determines which set of data the user has permission to view.', 'enum': ['4DN', 'Not 4DN']}, 'schema_version': {'type': 'string', 'pattern': '^\\d+(\\.\\d+)*$', 'title': 'Schema Version', 'default': '1', 'requestMethod': [], 'comment': 'Do not submit, value is assigned by the server. The version of the JSON schema that the server uses to validate the object. Schema version indicates generation of schema used to save version to to enable upgrade steps to work. Individual schemas should set the default.'}, 'url': {'type': 'string', 'rdfs:subPropertyOf': 'rdfs:seeAlso', 'format': 'uri', 'title': 'URL', 'description': 'An external resource with additional information about the grant.', '@type': '@id'}, 'uuid': {'serverDefault': 'uuid4', 'permission': 'import_items', 'type': 'string', 'format': 'uuid', 'title': 'UUID', 'readonly': True, 'requestMethod': 'POST'}, 'status': {'enum': ['released', 'current', 'revoked', 'deleted', 'replaced', 'in review by lab', 'in review by project', 'released to project'], 'permission': 'import_items', 'type': 'string', 'title': 'Status', 'readonly': True, 'default': 'released'}, 'pi': {'linkTo': 'User', 'type': 'string', 'title': 'P.I.', 'description': 'Principle Investigator of the grant.', 'comment': 'See user.json for available identifiers.'}}, 'type': 'object', 'mixinProperties': [{'$ref': 'mixins.json#/schema_version'}, {'$ref': 'mixins.json#/uuid'}, {'$ref': 'mixins.json#/submitted'}, {'$ref': 'mixins.json#/status'}], 'title': 'Grant', 'required': ['name'], 'boost_values': {'pi.title': 1.0, 'title': 1.0, 'name': 1.0}, 'identifyingProperties': ['uuid', 'name', 'title'], 'additionalProperties': False, '$schema': 'http://json-schema.org/draft-04/schema#', '@type': ['JSONSchema'], 'id': '/profiles/award.json'}
