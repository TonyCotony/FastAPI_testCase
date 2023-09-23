import random

import requests
import json

from core.database.database_session import get_db

# url11 = "http://google.com"
# response = requests.get(url11)
# print(response)

data = {
    "description": "string",
    "headers": {
        "additionalProp1": {
            "description": "string",
            "required": True,
            "deprecated": True,
            "style": "string",
            "explode": True,
            "allowReserved": True,
            "schema": {
                "$schema": "string",
                "$vocabulary": "string",
                "$id": "string",
                "$anchor": "string",
                "$dynamicAnchor": "string",
                "$ref": "string",
                "$dynamicRef": "string",
                "$defs": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "$comment": "string",
                "allOf": [
                    "string",
                    True
                ],
                "anyOf": [
                    "string",
                    True
                ],
                "oneOf": [
                    "string",
                    True
                ],
                "not": "string",
                "if": "string",
                "then": "string",
                "else": "string",
                "dependentSchemas": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "prefixItems": [
                    "string",
                    True
                ],
                "items": [],
                "contains": "string",
                "properties": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "patternProperties": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "additionalProperties": "string",
                "propertyNames": "string",
                "unevaluatedItems": "string",
                "unevaluatedProperties": "string",
                "type": "string",
                "enum": [
                    "string"
                ],
                "const": "string",
                "multipleOf": 1,
                "maximum": 0,
                "exclusiveMaximum": 0,
                "minimum": 0,
                "exclusiveMinimum": 0,
                "maxLength": 0,
                "minLength": 0,
                "pattern": "string",
                "maxItems": 0,
                "minItems": 0,
                "uniqueItems": True,
                "maxContains": 0,
                "minContains": 0,
                "maxProperties": 0,
                "minProperties": 0,
                "required": [
                    "string"
                ],
                "dependentRequired": {
                    "additionalProp1": [
                        "string"
                    ],
                    "additionalProp2": [
                        "string"
                    ],
                    "additionalProp3": [
                        "string"
                    ]
                },
                "format": "string",
                "contentEncoding": "string",
                "contentMediaType": "string",
                "contentSchema": "string",
                "title": "string",
                "description": "string",
                "default": "string",
                "deprecated": True,
                "readOnly": True,
                "writeOnly": True,
                "examples": [
                    "string"
                ],
                "discriminator": {
                    "propertyName": "string",
                    "mapping": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    }
                },
                "xml": {
                    "name": "string",
                    "namespace": "string",
                    "prefix": "string",
                    "attribute": True,
                    "wrapped": True,
                    "additionalProp1": {}
                },
                "externalDocs": {
                    "description": "string",
                    "url": "https://example.com/",
                    "additionalProp1": {}
                },
                "example": "string",
                "additionalProp1": {}
            },
            "example": "string",
            "examples": {
                "additionalProp1": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                },
                "additionalProp2": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                },
                "additionalProp3": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                }
            },
            "content": {
                "additionalProp1": {
                    "schema": {
                        "$schema": "string",
                        "$vocabulary": "string",
                        "$id": "string",
                        "$anchor": "string",
                        "$dynamicAnchor": "string",
                        "$ref": "string",
                        "$dynamicRef": "string",
                        "$defs": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "$comment": "string",
                        "allOf": [
                            "string",
                            True
                        ],
                        "anyOf": [
                            "string",
                            True
                        ],
                        "oneOf": [
                            "string",
                            True
                        ],
                        "not": "string",
                        "if": "string",
                        "then": "string",
                        "else": "string",
                        "dependentSchemas": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "prefixItems": [
                            "string",
                            True
                        ],
                        "items": [],
                        "contains": "string",
                        "properties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "patternProperties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "additionalProperties": "string",
                        "propertyNames": "string",
                        "unevaluatedItems": "string",
                        "unevaluatedProperties": "string",
                        "type": "string",
                        "enum": [
                            "string"
                        ],
                        "const": "string",
                        "multipleOf": 1,
                        "maximum": 0,
                        "exclusiveMaximum": 0,
                        "minimum": 0,
                        "exclusiveMinimum": 0,
                        "maxLength": 0,
                        "minLength": 0,
                        "pattern": "string",
                        "maxItems": 0,
                        "minItems": 0,
                        "uniqueItems": True,
                        "maxContains": 0,
                        "minContains": 0,
                        "maxProperties": 0,
                        "minProperties": 0,
                        "required": [
                            "string"
                        ],
                        "dependentRequired": {
                            "additionalProp1": [
                                "string"
                            ],
                            "additionalProp2": [
                                "string"
                            ],
                            "additionalProp3": [
                                "string"
                            ]
                        },
                        "format": "string",
                        "contentEncoding": "string",
                        "contentMediaType": "string",
                        "contentSchema": "string",
                        "title": "string",
                        "description": "string",
                        "default": "string",
                        "deprecated": True,
                        "readOnly": True,
                        "writeOnly": True,
                        "examples": [
                            "string"
                        ],
                        "discriminator": {
                            "propertyName": "string",
                            "mapping": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            }
                        },
                        "xml": {
                            "name": "string",
                            "namespace": "string",
                            "prefix": "string",
                            "attribute": True,
                            "wrapped": True,
                            "additionalProp1": {}
                        },
                        "externalDocs": {
                            "description": "string",
                            "url": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "example": "string",
                        "additionalProp1": {}
                    },
                    "example": "string",
                    "examples": {
                        "additionalProp1": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        }
                    },
                    "encoding": {
                        "additionalProp1": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        }
                    },
                    "additionalProp1": {}
                },
                "additionalProp2": {
                    "schema": {
                        "$schema": "string",
                        "$vocabulary": "string",
                        "$id": "string",
                        "$anchor": "string",
                        "$dynamicAnchor": "string",
                        "$ref": "string",
                        "$dynamicRef": "string",
                        "$defs": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "$comment": "string",
                        "allOf": [
                            "string",
                            True
                        ],
                        "anyOf": [
                            "string",
                            True
                        ],
                        "oneOf": [
                            "string",
                            True
                        ],
                        "not": "string",
                        "if": "string",
                        "then": "string",
                        "else": "string",
                        "dependentSchemas": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "prefixItems": [
                            "string",
                            True
                        ],
                        "items": [],
                        "contains": "string",
                        "properties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "patternProperties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "additionalProperties": "string",
                        "propertyNames": "string",
                        "unevaluatedItems": "string",
                        "unevaluatedProperties": "string",
                        "type": "string",
                        "enum": [
                            "string"
                        ],
                        "const": "string",
                        "multipleOf": 1,
                        "maximum": 0,
                        "exclusiveMaximum": 0,
                        "minimum": 0,
                        "exclusiveMinimum": 0,
                        "maxLength": 0,
                        "minLength": 0,
                        "pattern": "string",
                        "maxItems": 0,
                        "minItems": 0,
                        "uniqueItems": True,
                        "maxContains": 0,
                        "minContains": 0,
                        "maxProperties": 0,
                        "minProperties": 0,
                        "required": [
                            "string"
                        ],
                        "dependentRequired": {
                            "additionalProp1": [
                                "string"
                            ],
                            "additionalProp2": [
                                "string"
                            ],
                            "additionalProp3": [
                                "string"
                            ]
                        },
                        "format": "string",
                        "contentEncoding": "string",
                        "contentMediaType": "string",
                        "contentSchema": "string",
                        "title": "string",
                        "description": "string",
                        "default": "string",
                        "deprecated": True,
                        "readOnly": True,
                        "writeOnly": True,
                        "examples": [
                            "string"
                        ],
                        "discriminator": {
                            "propertyName": "string",
                            "mapping": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            }
                        },
                        "xml": {
                            "name": "string",
                            "namespace": "string",
                            "prefix": "string",
                            "attribute": True,
                            "wrapped": True,
                            "additionalProp1": {}
                        },
                        "externalDocs": {
                            "description": "string",
                            "url": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "example": "string",
                        "additionalProp1": {}
                    },
                    "example": "string",
                    "examples": {
                        "additionalProp1": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        }
                    },
                    "encoding": {
                        "additionalProp1": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        }
                    },
                    "additionalProp1": {}
                },
                "additionalProp3": {
                    "schema": {
                        "$schema": "string",
                        "$vocabulary": "string",
                        "$id": "string",
                        "$anchor": "string",
                        "$dynamicAnchor": "string",
                        "$ref": "string",
                        "$dynamicRef": "string",
                        "$defs": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "$comment": "string",
                        "allOf": [
                            "string",
                            True
                        ],
                        "anyOf": [
                            "string",
                            True
                        ],
                        "oneOf": [
                            "string",
                            True
                        ],
                        "not": "string",
                        "if": "string",
                        "then": "string",
                        "else": "string",
                        "dependentSchemas": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "prefixItems": [
                            "string",
                            True
                        ],
                        "items": [],
                        "contains": "string",
                        "properties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "patternProperties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "additionalProperties": "string",
                        "propertyNames": "string",
                        "unevaluatedItems": "string",
                        "unevaluatedProperties": "string",
                        "type": "string",
                        "enum": [
                            "string"
                        ],
                        "const": "string",
                        "multipleOf": 1,
                        "maximum": 0,
                        "exclusiveMaximum": 0,
                        "minimum": 0,
                        "exclusiveMinimum": 0,
                        "maxLength": 0,
                        "minLength": 0,
                        "pattern": "string",
                        "maxItems": 0,
                        "minItems": 0,
                        "uniqueItems": True,
                        "maxContains": 0,
                        "minContains": 0,
                        "maxProperties": 0,
                        "minProperties": 0,
                        "required": [
                            "string"
                        ],
                        "dependentRequired": {
                            "additionalProp1": [
                                "string"
                            ],
                            "additionalProp2": [
                                "string"
                            ],
                            "additionalProp3": [
                                "string"
                            ]
                        },
                        "format": "string",
                        "contentEncoding": "string",
                        "contentMediaType": "string",
                        "contentSchema": "string",
                        "title": "string",
                        "description": "string",
                        "default": "string",
                        "deprecated": True,
                        "readOnly": True,
                        "writeOnly": True,
                        "examples": [
                            "string"
                        ],
                        "discriminator": {
                            "propertyName": "string",
                            "mapping": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            }
                        },
                        "xml": {
                            "name": "string",
                            "namespace": "string",
                            "prefix": "string",
                            "attribute": True,
                            "wrapped": True,
                            "additionalProp1": {}
                        },
                        "externalDocs": {
                            "description": "string",
                            "url": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "example": "string",
                        "additionalProp1": {}
                    },
                    "example": "string",
                    "examples": {
                        "additionalProp1": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        }
                    },
                    "encoding": {
                        "additionalProp1": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        }
                    },
                    "additionalProp1": {}
                }
            },
            "additionalProp1": {}
        },
        "additionalProp2": {
            "description": "string",
            "required": True,
            "deprecated": True,
            "style": "string",
            "explode": True,
            "allowReserved": True,
            "schema": {
                "$schema": "string",
                "$vocabulary": "string",
                "$id": "string",
                "$anchor": "string",
                "$dynamicAnchor": "string",
                "$ref": "string",
                "$dynamicRef": "string",
                "$defs": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "$comment": "string",
                "allOf": [
                    "string",
                    True
                ],
                "anyOf": [
                    "string",
                    True
                ],
                "oneOf": [
                    "string",
                    True
                ],
                "not": "string",
                "if": "string",
                "then": "string",
                "else": "string",
                "dependentSchemas": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "prefixItems": [
                    "string",
                    True
                ],
                "items": [],
                "contains": "string",
                "properties": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "patternProperties": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "additionalProperties": "string",
                "propertyNames": "string",
                "unevaluatedItems": "string",
                "unevaluatedProperties": "string",
                "type": "string",
                "enum": [
                    "string"
                ],
                "const": "string",
                "multipleOf": 1,
                "maximum": 0,
                "exclusiveMaximum": 0,
                "minimum": 0,
                "exclusiveMinimum": 0,
                "maxLength": 0,
                "minLength": 0,
                "pattern": "string",
                "maxItems": 0,
                "minItems": 0,
                "uniqueItems": True,
                "maxContains": 0,
                "minContains": 0,
                "maxProperties": 0,
                "minProperties": 0,
                "required": [
                    "string"
                ],
                "dependentRequired": {
                    "additionalProp1": [
                        "string"
                    ],
                    "additionalProp2": [
                        "string"
                    ],
                    "additionalProp3": [
                        "string"
                    ]
                },
                "format": "string",
                "contentEncoding": "string",
                "contentMediaType": "string",
                "contentSchema": "string",
                "title": "string",
                "description": "string",
                "default": "string",
                "deprecated": True,
                "readOnly": True,
                "writeOnly": True,
                "examples": [
                    "string"
                ],
                "discriminator": {
                    "propertyName": "string",
                    "mapping": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    }
                },
                "xml": {
                    "name": "string",
                    "namespace": "string",
                    "prefix": "string",
                    "attribute": True,
                    "wrapped": True,
                    "additionalProp1": {}
                },
                "externalDocs": {
                    "description": "string",
                    "url": "https://example.com/",
                    "additionalProp1": {}
                },
                "example": "string",
                "additionalProp1": {}
            },
            "example": "string",
            "examples": {
                "additionalProp1": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                },
                "additionalProp2": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                },
                "additionalProp3": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                }
            },
            "content": {
                "additionalProp1": {
                    "schema": {
                        "$schema": "string",
                        "$vocabulary": "string",
                        "$id": "string",
                        "$anchor": "string",
                        "$dynamicAnchor": "string",
                        "$ref": "string",
                        "$dynamicRef": "string",
                        "$defs": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "$comment": "string",
                        "allOf": [
                            "string",
                            True
                        ],
                        "anyOf": [
                            "string",
                            True
                        ],
                        "oneOf": [
                            "string",
                            True
                        ],
                        "not": "string",
                        "if": "string",
                        "then": "string",
                        "else": "string",
                        "dependentSchemas": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "prefixItems": [
                            "string",
                            True
                        ],
                        "items": [],
                        "contains": "string",
                        "properties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "patternProperties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "additionalProperties": "string",
                        "propertyNames": "string",
                        "unevaluatedItems": "string",
                        "unevaluatedProperties": "string",
                        "type": "string",
                        "enum": [
                            "string"
                        ],
                        "const": "string",
                        "multipleOf": 1,
                        "maximum": 0,
                        "exclusiveMaximum": 0,
                        "minimum": 0,
                        "exclusiveMinimum": 0,
                        "maxLength": 0,
                        "minLength": 0,
                        "pattern": "string",
                        "maxItems": 0,
                        "minItems": 0,
                        "uniqueItems": True,
                        "maxContains": 0,
                        "minContains": 0,
                        "maxProperties": 0,
                        "minProperties": 0,
                        "required": [
                            "string"
                        ],
                        "dependentRequired": {
                            "additionalProp1": [
                                "string"
                            ],
                            "additionalProp2": [
                                "string"
                            ],
                            "additionalProp3": [
                                "string"
                            ]
                        },
                        "format": "string",
                        "contentEncoding": "string",
                        "contentMediaType": "string",
                        "contentSchema": "string",
                        "title": "string",
                        "description": "string",
                        "default": "string",
                        "deprecated": True,
                        "readOnly": True,
                        "writeOnly": True,
                        "examples": [
                            "string"
                        ],
                        "discriminator": {
                            "propertyName": "string",
                            "mapping": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            }
                        },
                        "xml": {
                            "name": "string",
                            "namespace": "string",
                            "prefix": "string",
                            "attribute": True,
                            "wrapped": True,
                            "additionalProp1": {}
                        },
                        "externalDocs": {
                            "description": "string",
                            "url": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "example": "string",
                        "additionalProp1": {}
                    },
                    "example": "string",
                    "examples": {
                        "additionalProp1": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        }
                    },
                    "encoding": {
                        "additionalProp1": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        }
                    },
                    "additionalProp1": {}
                },
                "additionalProp2": {
                    "schema": {
                        "$schema": "string",
                        "$vocabulary": "string",
                        "$id": "string",
                        "$anchor": "string",
                        "$dynamicAnchor": "string",
                        "$ref": "string",
                        "$dynamicRef": "string",
                        "$defs": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "$comment": "string",
                        "allOf": [
                            "string",
                            True
                        ],
                        "anyOf": [
                            "string",
                            True
                        ],
                        "oneOf": [
                            "string",
                            True
                        ],
                        "not": "string",
                        "if": "string",
                        "then": "string",
                        "else": "string",
                        "dependentSchemas": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "prefixItems": [
                            "string",
                            True
                        ],
                        "items": [],
                        "contains": "string",
                        "properties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "patternProperties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "additionalProperties": "string",
                        "propertyNames": "string",
                        "unevaluatedItems": "string",
                        "unevaluatedProperties": "string",
                        "type": "string",
                        "enum": [
                            "string"
                        ],
                        "const": "string",
                        "multipleOf": 1,
                        "maximum": 0,
                        "exclusiveMaximum": 0,
                        "minimum": 0,
                        "exclusiveMinimum": 0,
                        "maxLength": 0,
                        "minLength": 0,
                        "pattern": "string",
                        "maxItems": 0,
                        "minItems": 0,
                        "uniqueItems": True,
                        "maxContains": 0,
                        "minContains": 0,
                        "maxProperties": 0,
                        "minProperties": 0,
                        "required": [
                            "string"
                        ],
                        "dependentRequired": {
                            "additionalProp1": [
                                "string"
                            ],
                            "additionalProp2": [
                                "string"
                            ],
                            "additionalProp3": [
                                "string"
                            ]
                        },
                        "format": "string",
                        "contentEncoding": "string",
                        "contentMediaType": "string",
                        "contentSchema": "string",
                        "title": "string",
                        "description": "string",
                        "default": "string",
                        "deprecated": True,
                        "readOnly": True,
                        "writeOnly": True,
                        "examples": [
                            "string"
                        ],
                        "discriminator": {
                            "propertyName": "string",
                            "mapping": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            }
                        },
                        "xml": {
                            "name": "string",
                            "namespace": "string",
                            "prefix": "string",
                            "attribute": True,
                            "wrapped": True,
                            "additionalProp1": {}
                        },
                        "externalDocs": {
                            "description": "string",
                            "url": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "example": "string",
                        "additionalProp1": {}
                    },
                    "example": "string",
                    "examples": {
                        "additionalProp1": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        }
                    },
                    "encoding": {
                        "additionalProp1": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        }
                    },
                    "additionalProp1": {}
                },
                "additionalProp3": {
                    "schema": {
                        "$schema": "string",
                        "$vocabulary": "string",
                        "$id": "string",
                        "$anchor": "string",
                        "$dynamicAnchor": "string",
                        "$ref": "string",
                        "$dynamicRef": "string",
                        "$defs": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "$comment": "string",
                        "allOf": [
                            "string",
                            True
                        ],
                        "anyOf": [
                            "string",
                            True
                        ],
                        "oneOf": [
                            "string",
                            True
                        ],
                        "not": "string",
                        "if": "string",
                        "then": "string",
                        "else": "string",
                        "dependentSchemas": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "prefixItems": [
                            "string",
                            True
                        ],
                        "items": [],
                        "contains": "string",
                        "properties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "patternProperties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "additionalProperties": "string",
                        "propertyNames": "string",
                        "unevaluatedItems": "string",
                        "unevaluatedProperties": "string",
                        "type": "string",
                        "enum": [
                            "string"
                        ],
                        "const": "string",
                        "multipleOf": 1,
                        "maximum": 0,
                        "exclusiveMaximum": 0,
                        "minimum": 0,
                        "exclusiveMinimum": 0,
                        "maxLength": 0,
                        "minLength": 0,
                        "pattern": "string",
                        "maxItems": 0,
                        "minItems": 0,
                        "uniqueItems": True,
                        "maxContains": 0,
                        "minContains": 0,
                        "maxProperties": 0,
                        "minProperties": 0,
                        "required": [
                            "string"
                        ],
                        "dependentRequired": {
                            "additionalProp1": [
                                "string"
                            ],
                            "additionalProp2": [
                                "string"
                            ],
                            "additionalProp3": [
                                "string"
                            ]
                        },
                        "format": "string",
                        "contentEncoding": "string",
                        "contentMediaType": "string",
                        "contentSchema": "string",
                        "title": "string",
                        "description": "string",
                        "default": "string",
                        "deprecated": True,
                        "readOnly": True,
                        "writeOnly": True,
                        "examples": [
                            "string"
                        ],
                        "discriminator": {
                            "propertyName": "string",
                            "mapping": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            }
                        },
                        "xml": {
                            "name": "string",
                            "namespace": "string",
                            "prefix": "string",
                            "attribute": True,
                            "wrapped": True,
                            "additionalProp1": {}
                        },
                        "externalDocs": {
                            "description": "string",
                            "url": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "example": "string",
                        "additionalProp1": {}
                    },
                    "example": "string",
                    "examples": {
                        "additionalProp1": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        }
                    },
                    "encoding": {
                        "additionalProp1": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        }
                    },
                    "additionalProp1": {}
                }
            },
            "additionalProp1": {}
        },
        "additionalProp3": {
            "description": "string",
            "required": True,
            "deprecated": True,
            "style": "string",
            "explode": True,
            "allowReserved": True,
            "schema": {
                "$schema": "string",
                "$vocabulary": "string",
                "$id": "string",
                "$anchor": "string",
                "$dynamicAnchor": "string",
                "$ref": "string",
                "$dynamicRef": "string",
                "$defs": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "$comment": "string",
                "allOf": [
                    "string",
                    True
                ],
                "anyOf": [
                    "string",
                    True
                ],
                "oneOf": [
                    "string",
                    True
                ],
                "not": "string",
                "if": "string",
                "then": "string",
                "else": "string",
                "dependentSchemas": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "prefixItems": [
                    "string",
                    True
                ],
                "items": [],
                "contains": "string",
                "properties": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "patternProperties": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "additionalProperties": "string",
                "propertyNames": "string",
                "unevaluatedItems": "string",
                "unevaluatedProperties": "string",
                "type": "string",
                "enum": [
                    "string"
                ],
                "const": "string",
                "multipleOf": 1,
                "maximum": 0,
                "exclusiveMaximum": 0,
                "minimum": 0,
                "exclusiveMinimum": 0,
                "maxLength": 0,
                "minLength": 0,
                "pattern": "string",
                "maxItems": 0,
                "minItems": 0,
                "uniqueItems": True,
                "maxContains": 0,
                "minContains": 0,
                "maxProperties": 0,
                "minProperties": 0,
                "required": [
                    "string"
                ],
                "dependentRequired": {
                    "additionalProp1": [
                        "string"
                    ],
                    "additionalProp2": [
                        "string"
                    ],
                    "additionalProp3": [
                        "string"
                    ]
                },
                "format": "string",
                "contentEncoding": "string",
                "contentMediaType": "string",
                "contentSchema": "string",
                "title": "string",
                "description": "string",
                "default": "string",
                "deprecated": True,
                "readOnly": True,
                "writeOnly": True,
                "examples": [
                    "string"
                ],
                "discriminator": {
                    "propertyName": "string",
                    "mapping": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    }
                },
                "xml": {
                    "name": "string",
                    "namespace": "string",
                    "prefix": "string",
                    "attribute": True,
                    "wrapped": True,
                    "additionalProp1": {}
                },
                "externalDocs": {
                    "description": "string",
                    "url": "https://example.com/",
                    "additionalProp1": {}
                },
                "example": "string",
                "additionalProp1": {}
            },
            "example": "string",
            "examples": {
                "additionalProp1": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                },
                "additionalProp2": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                },
                "additionalProp3": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                }
            },
            "content": {
                "additionalProp1": {
                    "schema": {
                        "$schema": "string",
                        "$vocabulary": "string",
                        "$id": "string",
                        "$anchor": "string",
                        "$dynamicAnchor": "string",
                        "$ref": "string",
                        "$dynamicRef": "string",
                        "$defs": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "$comment": "string",
                        "allOf": [
                            "string",
                            True
                        ],
                        "anyOf": [
                            "string",
                            True
                        ],
                        "oneOf": [
                            "string",
                            True
                        ],
                        "not": "string",
                        "if": "string",
                        "then": "string",
                        "else": "string",
                        "dependentSchemas": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "prefixItems": [
                            "string",
                            True
                        ],
                        "items": [],
                        "contains": "string",
                        "properties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "patternProperties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "additionalProperties": "string",
                        "propertyNames": "string",
                        "unevaluatedItems": "string",
                        "unevaluatedProperties": "string",
                        "type": "string",
                        "enum": [
                            "string"
                        ],
                        "const": "string",
                        "multipleOf": 1,
                        "maximum": 0,
                        "exclusiveMaximum": 0,
                        "minimum": 0,
                        "exclusiveMinimum": 0,
                        "maxLength": 0,
                        "minLength": 0,
                        "pattern": "string",
                        "maxItems": 0,
                        "minItems": 0,
                        "uniqueItems": True,
                        "maxContains": 0,
                        "minContains": 0,
                        "maxProperties": 0,
                        "minProperties": 0,
                        "required": [
                            "string"
                        ],
                        "dependentRequired": {
                            "additionalProp1": [
                                "string"
                            ],
                            "additionalProp2": [
                                "string"
                            ],
                            "additionalProp3": [
                                "string"
                            ]
                        },
                        "format": "string",
                        "contentEncoding": "string",
                        "contentMediaType": "string",
                        "contentSchema": "string",
                        "title": "string",
                        "description": "string",
                        "default": "string",
                        "deprecated": True,
                        "readOnly": True,
                        "writeOnly": True,
                        "examples": [
                            "string"
                        ],
                        "discriminator": {
                            "propertyName": "string",
                            "mapping": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            }
                        },
                        "xml": {
                            "name": "string",
                            "namespace": "string",
                            "prefix": "string",
                            "attribute": True,
                            "wrapped": True,
                            "additionalProp1": {}
                        },
                        "externalDocs": {
                            "description": "string",
                            "url": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "example": "string",
                        "additionalProp1": {}
                    },
                    "example": "string",
                    "examples": {
                        "additionalProp1": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        }
                    },
                    "encoding": {
                        "additionalProp1": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        }
                    },
                    "additionalProp1": {}
                },
                "additionalProp2": {
                    "schema": {
                        "$schema": "string",
                        "$vocabulary": "string",
                        "$id": "string",
                        "$anchor": "string",
                        "$dynamicAnchor": "string",
                        "$ref": "string",
                        "$dynamicRef": "string",
                        "$defs": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "$comment": "string",
                        "allOf": [
                            "string",
                            True
                        ],
                        "anyOf": [
                            "string",
                            True
                        ],
                        "oneOf": [
                            "string",
                            True
                        ],
                        "not": "string",
                        "if": "string",
                        "then": "string",
                        "else": "string",
                        "dependentSchemas": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "prefixItems": [
                            "string",
                            True
                        ],
                        "items": [],
                        "contains": "string",
                        "properties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "patternProperties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "additionalProperties": "string",
                        "propertyNames": "string",
                        "unevaluatedItems": "string",
                        "unevaluatedProperties": "string",
                        "type": "string",
                        "enum": [
                            "string"
                        ],
                        "const": "string",
                        "multipleOf": 1,
                        "maximum": 0,
                        "exclusiveMaximum": 0,
                        "minimum": 0,
                        "exclusiveMinimum": 0,
                        "maxLength": 0,
                        "minLength": 0,
                        "pattern": "string",
                        "maxItems": 0,
                        "minItems": 0,
                        "uniqueItems": True,
                        "maxContains": 0,
                        "minContains": 0,
                        "maxProperties": 0,
                        "minProperties": 0,
                        "required": [
                            "string"
                        ],
                        "dependentRequired": {
                            "additionalProp1": [
                                "string"
                            ],
                            "additionalProp2": [
                                "string"
                            ],
                            "additionalProp3": [
                                "string"
                            ]
                        },
                        "format": "string",
                        "contentEncoding": "string",
                        "contentMediaType": "string",
                        "contentSchema": "string",
                        "title": "string",
                        "description": "string",
                        "default": "string",
                        "deprecated": True,
                        "readOnly": True,
                        "writeOnly": True,
                        "examples": [
                            "string"
                        ],
                        "discriminator": {
                            "propertyName": "string",
                            "mapping": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            }
                        },
                        "xml": {
                            "name": "string",
                            "namespace": "string",
                            "prefix": "string",
                            "attribute": True,
                            "wrapped": True,
                            "additionalProp1": {}
                        },
                        "externalDocs": {
                            "description": "string",
                            "url": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "example": "string",
                        "additionalProp1": {}
                    },
                    "example": "string",
                    "examples": {
                        "additionalProp1": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        }
                    },
                    "encoding": {
                        "additionalProp1": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        }
                    },
                    "additionalProp1": {}
                },
                "additionalProp3": {
                    "schema": {
                        "$schema": "string",
                        "$vocabulary": "string",
                        "$id": "string",
                        "$anchor": "string",
                        "$dynamicAnchor": "string",
                        "$ref": "string",
                        "$dynamicRef": "string",
                        "$defs": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "$comment": "string",
                        "allOf": [
                            "string",
                            True
                        ],
                        "anyOf": [
                            "string",
                            True
                        ],
                        "oneOf": [
                            "string",
                            True
                        ],
                        "not": "string",
                        "if": "string",
                        "then": "string",
                        "else": "string",
                        "dependentSchemas": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "prefixItems": [
                            "string",
                            True
                        ],
                        "items": [],
                        "contains": "string",
                        "properties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "patternProperties": {
                            "additionalProp1": "string",
                            "additionalProp2": "string",
                            "additionalProp3": "string"
                        },
                        "additionalProperties": "string",
                        "propertyNames": "string",
                        "unevaluatedItems": "string",
                        "unevaluatedProperties": "string",
                        "type": "string",
                        "enum": [
                            "string"
                        ],
                        "const": "string",
                        "multipleOf": 1,
                        "maximum": 0,
                        "exclusiveMaximum": 0,
                        "minimum": 0,
                        "exclusiveMinimum": 0,
                        "maxLength": 0,
                        "minLength": 0,
                        "pattern": "string",
                        "maxItems": 0,
                        "minItems": 0,
                        "uniqueItems": True,
                        "maxContains": 0,
                        "minContains": 0,
                        "maxProperties": 0,
                        "minProperties": 0,
                        "required": [
                            "string"
                        ],
                        "dependentRequired": {
                            "additionalProp1": [
                                "string"
                            ],
                            "additionalProp2": [
                                "string"
                            ],
                            "additionalProp3": [
                                "string"
                            ]
                        },
                        "format": "string",
                        "contentEncoding": "string",
                        "contentMediaType": "string",
                        "contentSchema": "string",
                        "title": "string",
                        "description": "string",
                        "default": "string",
                        "deprecated": True,
                        "readOnly": True,
                        "writeOnly": True,
                        "examples": [
                            "string"
                        ],
                        "discriminator": {
                            "propertyName": "string",
                            "mapping": {
                                "additionalProp1": "string",
                                "additionalProp2": "string",
                                "additionalProp3": "string"
                            }
                        },
                        "xml": {
                            "name": "string",
                            "namespace": "string",
                            "prefix": "string",
                            "attribute": True,
                            "wrapped": True,
                            "additionalProp1": {}
                        },
                        "externalDocs": {
                            "description": "string",
                            "url": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "example": "string",
                        "additionalProp1": {}
                    },
                    "example": "string",
                    "examples": {
                        "additionalProp1": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "summary": "string",
                            "description": "string",
                            "value": "string",
                            "externalValue": "https://example.com/",
                            "additionalProp1": {}
                        }
                    },
                    "encoding": {
                        "additionalProp1": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp2": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        },
                        "additionalProp3": {
                            "contentType": "string",
                            "headers": {
                                "additionalProp1": {},
                                "additionalProp2": {},
                                "additionalProp3": {}
                            },
                            "style": "string",
                            "explode": True,
                            "allowReserved": True,
                            "additionalProp1": {}
                        }
                    },
                    "additionalProp1": {}
                }
            },
            "additionalProp1": {}
        }
    },
    "content": {
        "additionalProp1": {
            "schema": {
                "$schema": "string",
                "$vocabulary": "string",
                "$id": "string",
                "$anchor": "string",
                "$dynamicAnchor": "string",
                "$ref": "string",
                "$dynamicRef": "string",
                "$defs": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "$comment": "string",
                "allOf": [
                    "string",
                    True
                ],
                "anyOf": [
                    "string",
                    True
                ],
                "oneOf": [
                    "string",
                    True
                ],
                "not": "string",
                "if": "string",
                "then": "string",
                "else": "string",
                "dependentSchemas": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "prefixItems": [
                    "string",
                    True
                ],
                "items": [],
                "contains": "string",
                "properties": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "patternProperties": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "additionalProperties": "string",
                "propertyNames": "string",
                "unevaluatedItems": "string",
                "unevaluatedProperties": "string",
                "type": "string",
                "enum": [
                    "string"
                ],
                "const": "string",
                "multipleOf": 1,
                "maximum": 0,
                "exclusiveMaximum": 0,
                "minimum": 0,
                "exclusiveMinimum": 0,
                "maxLength": 0,
                "minLength": 0,
                "pattern": "string",
                "maxItems": 0,
                "minItems": 0,
                "uniqueItems": True,
                "maxContains": 0,
                "minContains": 0,
                "maxProperties": 0,
                "minProperties": 0,
                "required": [
                    "string"
                ],
                "dependentRequired": {
                    "additionalProp1": [
                        "string"
                    ],
                    "additionalProp2": [
                        "string"
                    ],
                    "additionalProp3": [
                        "string"
                    ]
                },
                "format": "string",
                "contentEncoding": "string",
                "contentMediaType": "string",
                "contentSchema": "string",
                "title": "string",
                "description": "string",
                "default": "string",
                "deprecated": True,
                "readOnly": True,
                "writeOnly": True,
                "examples": [
                    "string"
                ],
                "discriminator": {
                    "propertyName": "string",
                    "mapping": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    }
                },
                "xml": {
                    "name": "string",
                    "namespace": "string",
                    "prefix": "string",
                    "attribute": True,
                    "wrapped": True,
                    "additionalProp1": {}
                },
                "externalDocs": {
                    "description": "string",
                    "url": "https://example.com/",
                    "additionalProp1": {}
                },
                "example": "string",
                "additionalProp1": {}
            },
            "example": "string",
            "examples": {
                "additionalProp1": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                },
                "additionalProp2": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                },
                "additionalProp3": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                }
            },
            "encoding": {
                "additionalProp1": {
                    "contentType": "string",
                    "headers": {
                        "additionalProp1": {},
                        "additionalProp2": {},
                        "additionalProp3": {}
                    },
                    "style": "string",
                    "explode": True,
                    "allowReserved": True,
                    "additionalProp1": {}
                },
                "additionalProp2": {
                    "contentType": "string",
                    "headers": {
                        "additionalProp1": {},
                        "additionalProp2": {},
                        "additionalProp3": {}
                    },
                    "style": "string",
                    "explode": True,
                    "allowReserved": True,
                    "additionalProp1": {}
                },
                "additionalProp3": {
                    "contentType": "string",
                    "headers": {
                        "additionalProp1": {},
                        "additionalProp2": {},
                        "additionalProp3": {}
                    },
                    "style": "string",
                    "explode": True,
                    "allowReserved": True,
                    "additionalProp1": {}
                }
            },
            "additionalProp1": {}
        },
        "additionalProp2": {
            "schema": {
                "$schema": "string",
                "$vocabulary": "string",
                "$id": "string",
                "$anchor": "string",
                "$dynamicAnchor": "string",
                "$ref": "string",
                "$dynamicRef": "string",
                "$defs": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "$comment": "string",
                "allOf": [
                    "string",
                    True
                ],
                "anyOf": [
                    "string",
                    True
                ],
                "oneOf": [
                    "string",
                    True
                ],
                "not": "string",
                "if": "string",
                "then": "string",
                "else": "string",
                "dependentSchemas": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "prefixItems": [
                    "string",
                    True
                ],
                "items": [],
                "contains": "string",
                "properties": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "patternProperties": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "additionalProperties": "string",
                "propertyNames": "string",
                "unevaluatedItems": "string",
                "unevaluatedProperties": "string",
                "type": "string",
                "enum": [
                    "string"
                ],
                "const": "string",
                "multipleOf": 1,
                "maximum": 0,
                "exclusiveMaximum": 0,
                "minimum": 0,
                "exclusiveMinimum": 0,
                "maxLength": 0,
                "minLength": 0,
                "pattern": "string",
                "maxItems": 0,
                "minItems": 0,
                "uniqueItems": True,
                "maxContains": 0,
                "minContains": 0,
                "maxProperties": 0,
                "minProperties": 0,
                "required": [
                    "string"
                ],
                "dependentRequired": {
                    "additionalProp1": [
                        "string"
                    ],
                    "additionalProp2": [
                        "string"
                    ],
                    "additionalProp3": [
                        "string"
                    ]
                },
                "format": "string",
                "contentEncoding": "string",
                "contentMediaType": "string",
                "contentSchema": "string",
                "title": "string",
                "description": "string",
                "default": "string",
                "deprecated": True,
                "readOnly": True,
                "writeOnly": True,
                "examples": [
                    "string"
                ],
                "discriminator": {
                    "propertyName": "string",
                    "mapping": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    }
                },
                "xml": {
                    "name": "string",
                    "namespace": "string",
                    "prefix": "string",
                    "attribute": True,
                    "wrapped": True,
                    "additionalProp1": {}
                },
                "externalDocs": {
                    "description": "string",
                    "url": "https://example.com/",
                    "additionalProp1": {}
                },
                "example": "string",
                "additionalProp1": {}
            },
            "example": "string",
            "examples": {
                "additionalProp1": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                },
                "additionalProp2": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                },
                "additionalProp3": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                }
            },
            "encoding": {
                "additionalProp1": {
                    "contentType": "string",
                    "headers": {
                        "additionalProp1": {},
                        "additionalProp2": {},
                        "additionalProp3": {}
                    },
                    "style": "string",
                    "explode": True,
                    "allowReserved": True,
                    "additionalProp1": {}
                },
                "additionalProp2": {
                    "contentType": "string",
                    "headers": {
                        "additionalProp1": {},
                        "additionalProp2": {},
                        "additionalProp3": {}
                    },
                    "style": "string",
                    "explode": True,
                    "allowReserved": True,
                    "additionalProp1": {}
                },
                "additionalProp3": {
                    "contentType": "string",
                    "headers": {
                        "additionalProp1": {},
                        "additionalProp2": {},
                        "additionalProp3": {}
                    },
                    "style": "string",
                    "explode": True,
                    "allowReserved": True,
                    "additionalProp1": {}
                }
            },
            "additionalProp1": {}
        },
        "additionalProp3": {
            "schema": {
                "$schema": "string",
                "$vocabulary": "string",
                "$id": "string",
                "$anchor": "string",
                "$dynamicAnchor": "string",
                "$ref": "string",
                "$dynamicRef": "string",
                "$defs": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "$comment": "string",
                "allOf": [
                    "string",
                    True
                ],
                "anyOf": [
                    "string",
                    True
                ],
                "oneOf": [
                    "string",
                    True
                ],
                "not": "string",
                "if": "string",
                "then": "string",
                "else": "string",
                "dependentSchemas": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "prefixItems": [
                    "string",
                    True
                ],
                "items": [],
                "contains": "string",
                "properties": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "patternProperties": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                },
                "additionalProperties": "string",
                "propertyNames": "string",
                "unevaluatedItems": "string",
                "unevaluatedProperties": "string",
                "type": "string",
                "enum": [
                    "string"
                ],
                "const": "string",
                "multipleOf": 1,
                "maximum": 0,
                "exclusiveMaximum": 0,
                "minimum": 0,
                "exclusiveMinimum": 0,
                "maxLength": 0,
                "minLength": 0,
                "pattern": "string",
                "maxItems": 0,
                "minItems": 0,
                "uniqueItems": True,
                "maxContains": 0,
                "minContains": 0,
                "maxProperties": 0,
                "minProperties": 0,
                "required": [
                    "string"
                ],
                "dependentRequired": {
                    "additionalProp1": [
                        "string"
                    ],
                    "additionalProp2": [
                        "string"
                    ],
                    "additionalProp3": [
                        "string"
                    ]
                },
                "format": "string",
                "contentEncoding": "string",
                "contentMediaType": "string",
                "contentSchema": "string",
                "title": "string",
                "description": "string",
                "default": "string",
                "deprecated": True,
                "readOnly": True,
                "writeOnly": True,
                "examples": [
                    "string"
                ],
                "discriminator": {
                    "propertyName": "string",
                    "mapping": {
                        "additionalProp1": "string",
                        "additionalProp2": "string",
                        "additionalProp3": "string"
                    }
                },
                "xml": {
                    "name": "string",
                    "namespace": "string",
                    "prefix": "string",
                    "attribute": True,
                    "wrapped": True,
                    "additionalProp1": {}
                },
                "externalDocs": {
                    "description": "string",
                    "url": "https://example.com/",
                    "additionalProp1": {}
                },
                "example": "string",
                "additionalProp1": {}
            },
            "example": "string",
            "examples": {
                "additionalProp1": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                },
                "additionalProp2": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                },
                "additionalProp3": {
                    "summary": "string",
                    "description": "string",
                    "value": "string",
                    "externalValue": "https://example.com/",
                    "additionalProp1": {}
                }
            },
            "encoding": {
                "additionalProp1": {
                    "contentType": "string",
                    "headers": {
                        "additionalProp1": {},
                        "additionalProp2": {},
                        "additionalProp3": {}
                    },
                    "style": "string",
                    "explode": True,
                    "allowReserved": True,
                    "additionalProp1": {}
                },
                "additionalProp2": {
                    "contentType": "string",
                    "headers": {
                        "additionalProp1": {},
                        "additionalProp2": {},
                        "additionalProp3": {}
                    },
                    "style": "string",
                    "explode": True,
                    "allowReserved": True,
                    "additionalProp1": {}
                },
                "additionalProp3": {
                    "contentType": "string",
                    "headers": {
                        "additionalProp1": {},
                        "additionalProp2": {},
                        "additionalProp3": {}
                    },
                    "style": "string",
                    "explode": True,
                    "allowReserved": True,
                    "additionalProp1": {}
                }
            },
            "additionalProp1": {}
        }
    },
    "links": {
        "additionalProp1": {
            "operationRef": "string",
            "operationId": "string",
            "parameters": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
            },
            "requestBody": "string",
            "description": "string",
            "server": {
                "url": "https://example.com/",
                "description": "string",
                "variables": {
                    "additionalProp1": {
                        "enum": [
                            "string"
                        ],
                        "default": "string",
                        "description": "string",
                        "additionalProp1": {}
                    },
                    "additionalProp2": {
                        "enum": [
                            "string"
                        ],
                        "default": "string",
                        "description": "string",
                        "additionalProp1": {}
                    },
                    "additionalProp3": {
                        "enum": [
                            "string"
                        ],
                        "default": "string",
                        "description": "string",
                        "additionalProp1": {}
                    }
                },
                "additionalProp1": {}
            },
            "additionalProp1": {}
        },
        "additionalProp2": {
            "operationRef": "string",
            "operationId": "string",
            "parameters": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
            },
            "requestBody": "string",
            "description": "string",
            "server": {
                "url": "https://example.com/",
                "description": "string",
                "variables": {
                    "additionalProp1": {
                        "enum": [
                            "string"
                        ],
                        "default": "string",
                        "description": "string",
                        "additionalProp1": {}
                    },
                    "additionalProp2": {
                        "enum": [
                            "string"
                        ],
                        "default": "string",
                        "description": "string",
                        "additionalProp1": {}
                    },
                    "additionalProp3": {
                        "enum": [
                            "string"
                        ],
                        "default": "string",
                        "description": "string",
                        "additionalProp1": {}
                    }
                },
                "additionalProp1": {}
            },
            "additionalProp1": {}
        },
        "additionalProp3": {
            "operationRef": "string",
            "operationId": "string",
            "parameters": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
            },
            "requestBody": "string",
            "description": "string",
            "server": {
                "url": "https://example.com/",
                "description": "string",
                "variables": {
                    "additionalProp1": {
                        "enum": [
                            "string"
                        ],
                        "default": "string",
                        "description": "string",
                        "additionalProp1": {}
                    },
                    "additionalProp2": {
                        "enum": [
                            "string"
                        ],
                        "default": "string",
                        "description": "string",
                        "additionalProp1": {}
                    },
                    "additionalProp3": {
                        "enum": [
                            "string"
                        ],
                        "default": "string",
                        "description": "string",
                        "additionalProp1": {}
                    }
                },
                "additionalProp1": {}
            },
            "additionalProp1": {}
        }
    },
    "additionalProp1": {}
}

data2 = {
    'name': 'SoCowBeast',
    'weight': random.randint(10, 15000),
    'type': random.randint(1, 3),
    'cargo_cost': random.randint(57, 120000),
    # 'delivery_cost': 1003.1
}

url = "http://127.0.0.1:8080/create_session/pepega/"

url_new = "http://127.0.0.1:8080/create_session/pepega2/"
url2 = 'http://127.0.0.1:8080/whoami'
url3 = 'http://127.0.0.1:8080/register_cargo'

# response = requests.post(url, data=json.dumps(data)).json()
response = requests.post(url, data=json.dumps(data))
# answer = response.get("replies")
print(f'register user - {response.json()}')
print(response)
new_cargo_response = requests.post(url3, data=json.dumps(data2), cookies=response.cookies)
print(f'new cargo register - {new_cargo_response}')
print(new_cargo_response.json())
data = {'id': 4}
url4 = 'http://127.0.0.1:8080/get_cargo'
get_cargo_response = requests.get(url4, cookies=response.cookies, data=json.dumps(data))
print(f"get cargo - {get_cargo_response}")
print(get_cargo_response.json())

data3 = {
    'page': 1,
    'per_page': 10,
    'cargo_type': 3,
    # 'delivery_cost_calculated': False
}
url6 = 'http://127.0.0.1:8080/get_owned_cargos'
get_owned_cargos_response = requests.get(url6, data=json.dumps(data3), cookies=response.cookies)
print(f"get all owned session cargo - {get_owned_cargos_response}")
print(get_owned_cargos_response.json())

url5 = 'http://127.0.0.1:8080/get_cargo_types'
post_cargo_response = requests.get(url5, cookies=response.cookies)
print(f"\n\nget cargo types - {post_cargo_response}")
print(post_cargo_response.json())

url12 = "http://127.0.0.1:8080/get_cargo"
data = {
    'id': 16
}
get_filtered_cargo_response = requests.get(url12, data=json.dumps(data))
print(get_filtered_cargo_response)
print(get_filtered_cargo_response.json())

url = "http://127.0.0.1:8080/register_delivery"
data = {
    'id': 1,
    "company_id": random.randint(1, 3)
}
assign_company_to_deliver_cargo = requests.post(url, data=json.dumps(data))
print(assign_company_to_deliver_cargo)
print(assign_company_to_deliver_cargo.json())

# response = requests.post(url_new, data=json.dumps(data))
# # answer = response.get("replies")
# print(f'register user - {response.json()}')
# print(response)
#
# url4 = 'http://127.0.0.1:8080/get_cargo?id=1'
# get_cargo_response = requests.get(url4, cookies=response.cookies)
# print(f"get new session cargo - {get_cargo_response}")
# print(get_cargo_response.json())
