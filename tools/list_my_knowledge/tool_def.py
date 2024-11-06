import inspect

from kubiya_sdk.tools.models import Arg, Tool, FileSpec
from kubiya_sdk.tools.registry import tool_registry

from . import main

list_my_knowledge_tool = Tool(
    name="list_my_knowledge",
    type="docker",
    image="python:3.12-slim",
    description="Lists all knowldege in the organization",
    args=[],
    on_build="""
apt-get update && apt-get install -y curl > /dev/null
    
curl -LsSf https://astral.sh/uv/install.sh | sh > /dev/null
. $HOME/.cargo/env

uv venv > /dev/null 2>&1
. .venv/bin/activate > /dev/null

uv pip install requests > /dev/null
""",
    content="""
. .venv/bin/activate
python /tmp/main.py
""",
    with_files=[
        FileSpec(
            destination="/tmp/main.py",
            content=inspect.getsource(main),
        ),
        # Add any requirements here if needed
        # FileSpec(
        #     destination="/tmp/requirements.txt",
        #     content="requests==2.32.3",
        # ),
    ],
    secrets=["geff_test"]
)

tool_registry.register(list_my_knowledge_tool)
