import unittest
import os.path
import yacg.builder.jsonBuilder
import yacg.builder.yamlBuilder

class TestJsonBuilder (unittest.TestCase):
    def testYamlAndJsonEquality(self):
        jsonModelFile = 'resources/models/json/config_schema.json'
        jsonModelFileExists = os.path.isfile(jsonModelFile)
        self.assertTrue ('json model file exists: '+ jsonModelFile,jsonModelFileExists)

        yamlModelFile = 'resources/models/yaml/config_schema.yaml'
        yamlModelFileExists = os.path.isfile(yamlModelFile)
        self.assertTrue ('yaml model file exists: '+ yamlModelFile,yamlModelFileExists)

        parsedJsonSchema = yacg.builder.jsonBuilder.getParsedSchema(jsonModelFile)
        self.assertIsNotNone (parsedJsonSchema)
        parsedYamlSchema = yacg.builder.yamlBuilder.getParsedSchema(yamlModelFile)        
        self.assertIsNotNone (parsedYamlSchema)

        self.assertEqual(parsedYamlSchema,parsedYamlSchema)