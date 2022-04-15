#!/bin/bash

scriptPos=${0%/*}

# script takes the yacg models and generate the program code
# based on them

# to see what jobs are executed run:
#  `bin/generateCodeForYacg.sh --skipCodeGenDryRun`

pushd $scriptPos/.. > /dev/null

echo "create meta model classes ..."
if ! pipenv run python3 yacg.py --models \
    resources/models/json/yacg_model_schema.json \
    --singleFileTemplates pythonBeans=${scriptPos}/../yacg/model/model.py \
                pythonBeansTests=${scriptPos}/../tests/model/test_model.py \
                plantUml=${scriptPos}/../docs/puml/yacg_model.puml \
    --protocolFile logs/gen_yacg_model.log \
    --skipCodeGenIfVersionUnchanged $*\
    --templateParameters baseModelDomain=yacg.model.model \
                         title="yacg model"; then
    echo "    ERROR while create meta model classes"
    exit 1
fi

echo "create config model classes ..."
if ! pipenv run python3 yacg.py --models \
    resources/models/json/yacg_config_schema.json \
    --singleFileTemplates pythonBeans=${scriptPos}/../yacg/model/config.py \
                pythonBeansTests=${scriptPos}/../tests/model/test_config.py \
                plantUml=${scriptPos}/../docs/puml/yacg_config_schema.puml \
    --protocolFile logs/gen_config_model.log \
    --skipCodeGenIfVersionUnchanged $*\
    --templateParameters baseModelDomain=yacg.model.config \
                         title="yacg configuration model"; then
    echo "    ERROR while create config model classes"
    exit 1
fi

echo "create openapi model classes ..."
if ! pipenv run python3 yacg.py --models \
    resources/models/json/yacg_openapi_paths.json \
    --singleFileTemplates pythonBeans=${scriptPos}/../yacg/model/openapi.py \
                pythonBeansTests=${scriptPos}/../tests/model/test_openapi.py \
                plantUml=${scriptPos}/../docs/puml/yacg_openapi.puml \
    --blackListed yacg.model.model=domain \
    --protocolFile logs/gen_openapi_model.log \
    --skipCodeGenIfVersionUnchanged $* \
    --templateParameters baseModelDomain=yacg.model.openapi \
                         title="yacg openapi model"; then
    echo "    ERROR while create openapi model classes"
    exit 1
fi

echo "create asyncapi model classes ..."
if ! pipenv run python3 yacg.py --models \
    resources/models/json/yacg_asyncapi_types.json \
    --singleFileTemplates pythonBeans=${scriptPos}/../yacg/model/asyncapi.py \
                pythonBeansTests=${scriptPos}/../tests/model/test_asyncapi.py \
                plantUml=${scriptPos}/../docs/puml/yacg_asyncapi.puml \
    --blackListed yacg.model.model=domain \
    --protocolFile logs/gen_asyncapi_model.log \
    --skipCodeGenIfVersionUnchanged $* \
    --templateParameters baseModelDomain=yacg.model.asyncapi \
                         title="yacg asyncapi model"; then
    echo "    ERROR while create asyncapi model classes"
    exit 1
fi


popd > /dev/null