import unittest
import os.path
from yacg.builder.jsonBuilder import getModelFromJson
from yacg.model.model import IntegerType, NumberType
from yacg.model.model import StringType, UuidType
from yacg.model.model import DateType, DateTimeType
from yacg.model.model import EnumType, ComplexType


class TestJsonBuilder (unittest.TestCase):
    def testSingleTypeSchema(self):
        modelFile = 'resources/models/json/examples/single_type_schema.json'
        modelFileExists = os.path.isfile(modelFile)
        self.assertTrue ('model file exists: '+ modelFile,modelFileExists)
        modelTypes = getModelFromJson (modelFile)
        self.assertIsNotNone (modelTypes)
        self.assertEqual(3,len(modelTypes))

        mainType = None
        anotherType = None
        innerComplexType = None
        for type in modelTypes:
            if type.name == 'SingleTypeSchema':
                mainType = type
            elif type.name == 'AnotherType':
                anotherType = type
            else:
                innerComplexType = type
        self.assertIsNotNone (mainType)
        self.assertEqual(4,len(mainType.properties))
        self.assertTrue (isinstance (mainType.properties[0].type, StringType)) 
        self.assertTrue (isinstance (mainType.properties[1].type, NumberType)) 
        self.assertTrue (isinstance (mainType.properties[2].type, EnumType)) 
        self.assertTrue (isinstance (mainType.properties[3].type, ComplexType)) 

        self.assertIsNotNone (anotherType)
        self.assertEqual(2,len(anotherType.properties))
        self.assertTrue (isinstance (anotherType.properties[0].type, DateTimeType)) 
        self.assertTrue (isinstance (anotherType.properties[1].type, NumberType)) 

        self.assertIsNotNone (innerComplexType)
        self.assertEqual(3,len(innerComplexType.properties))
        self.assertTrue (isinstance (innerComplexType.properties[0].type, StringType)) 
        self.assertTrue (isinstance (innerComplexType.properties[1].type, IntegerType)) 
        self.assertTrue (isinstance (innerComplexType.properties[2].type, ComplexType)) 
        self.assertEqual(anotherType, innerComplexType.properties[2].type)

if __name__ == '__main__':
    unittest.main()