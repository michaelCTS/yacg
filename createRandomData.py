import argparse
import sys
import logging
import yaml
import json
from yacg.util.fileUtils import doesFileExist
from yacg.util.outputUtils import printError, printInfo
import yacg.builder.impl.dictionaryBuilder as builder
import yacg.model.randomFuncs as randomFuncs
import yacg.model.random_config as randomConfig
from yacg.util.fileUtils import getFileExt


description = """Reads a JSON schema model in JSON our YAML generates random data
for specific annotated types
"""

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(prog='createRandomData', description=description)
parser.add_argument('--model', help='with random generation information annotated model schema')
parser.add_argument('--outputDir', help='name of the directory to store the data with random data')
parser.add_argument('--type', nargs='+', help='type name to generate data for, alternative to specific annotation')
parser.add_argument('--yaml', help='the default output is JSON, set this if YAML output desired', action='store_true')
parser.add_argument('--noIndent', help='set this if the output should not be beautified', action='store_true')
parser.add_argument('--defaultElemCount', help='default number of elements to generate for a type')
parser.add_argument('--defaultTypeDepth', help='default depth to generate complex types')
parser.add_argument('--defaultMinArrayElemCount', help='default minimal array element count')
parser.add_argument('--defaultMaxArrayElemCount', help='default maximal array element count')
parser.add_argument('--defaultMinDate', help='default minimal date for date and timestamp fields')
parser.add_argument('--defaultMaxDate', help='default maximal date for date and timestamp fields')


class Args:
    def __init__(self) -> None:
        self.model = None
        self.outputDir = None
        self.type = []
        self.yaml = False
        self.noIndent = False
        self.defaultElemCount = None
        self.defaultTypeDepth = None
        self.defaultMinArrayElemCount = None
        self.defaultMaxArrayElemCount = None
        self.defaultMinDate = None
        self.defaultMaxDate = None


def createDefaultConfig(args):
    defaultConfig = randomConfig.RamdonDefaultConfig()
    defaultConfig.defaultElemCount = int(args.defaultElemCount) if args.defaultElemCount is not None else None
    defaultConfig.defaultTypeDepth = int(args.defaultTypeDepth) if args.defaultTypeDepth is not None else None
    defaultConfig.defaultMinArrayElemCount = int(args.defaultMinArrayElemCount) if args.defaultMinArrayElemCount is not None else None
    defaultConfig.defaultMaxArrayElemCount = int(args.defaultMaxArrayElemCount) if args.defaultMaxArrayElemCount is not None else None
    defaultConfig.defaultMinDate = args.defaultMinDate if args.defaultMinDate is not None else None
    defaultConfig.defaultMaxDate = args.defaultMaxDate if args.defaultMaxDate is not None else None
    return defaultConfig


def _printJson(randomDataDict, typeName, destDir, noIndent):
    outputFile = "{}/{}.json".format(destDir, typeName)
    printInfo('\nWrite JSON: {}'.format(outputFile))
    with open(outputFile, 'w') as outfile:
        if noIndent:
            json.dump(randomDataDict, outfile)
        else:
            json.dump(randomDataDict, outfile, indent=4)


def _printYaml(randomDataDict, typeName, destDir, noIndent):
    outputFile = "{}/{}.yaml".format(destDir, typeName)
    printInfo('\nWrite yaml: {}'.format(outputFile))
    with open(outputFile, 'w') as outfile:
        if noIndent:
            yaml.dump(randomDataDict, outfile, sort_keys=False)
        else:
            yaml.dump(randomDataDict, outfile, indent=4, sort_keys=False)


def _searchForTypesToGenerateAndProcessThem(args, loadedTypes):
    """takes the prepared meta model ..."""
    defaultConfig = createDefaultConfig(args)
    for t in loadedTypes:
        if (t.name in args.type) or ((t.processing is not None) and (t.procession.randElemCount > 0)):
            randomData = randomFuncs.generateRandomData(t, defaultConfig)
            if args.yaml:
                _printYaml(randomData, t.name, args.outputDir, args.noIndent)
            else:
                _printJson(randomData, t.name, args.outputDir, args.noIndent)


def main(args):
    yamlExtensions = set(['.yaml', '.yml'])
    fileExt = getFileExt(args.model)
    loadedTypes = []
    if fileExt.lower() in yamlExtensions:
        dict = builder.getParsedSchemaFromYaml(args.model)
    else:
        dict = builder.getParsedSchemaFromJson(args.model)
    loadedTypes = builder.extractTypes(dict, args.model, [], False)

    randomFuncs.extendMetaModelWithRandomConfigTypes(loadedTypes)
    _searchForTypesToGenerateAndProcessThem(args, loadedTypes)


if __name__ == '__main__':
    args = parser.parse_args()
    if args.model is None:
        printError('\nModel file not given. It can be passed as parameter or over stdin ... cancel')
        sys.exit(1)
    if not doesFileExist(args.model):
        printError('\nModel file not found ... cancel: {}'.format(args.model))
        sys.exit(1)
    main(args)
