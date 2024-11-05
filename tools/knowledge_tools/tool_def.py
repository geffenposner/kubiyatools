import inspect

from kubiya_sdk.tools.models import Arg, Tool, FileSpec
from kubiya_sdk.tools.registry import tool_registry

from . import main

create_knowledge_tool = Tool(
    name="create_knowledge",
    type="docker",
    image="python:3.12-slim",
    description="Creates a piece of Kubiya knowldege with {content}!",
    args=[
        Arg(name="title", description="title of the piece of knowledge", required=True),
        Arg(name="description", description="description of the piece of knowledge", required=True),
        Arg(name="tags", description="tags related to the piece of knowledge. multiple tags should be comma separated", required=False),
        Arg(name="content", description="content of the piece of knowledge", required=True),
        Arg(name="teammates_with_access", description="Kubiya teammates with access to the piece of knowledge", required=False),
        Arg(name="user_groups_with_access", description="groups of Kubiya users with access to the piece of knowledge", required=False),
          ],
    on_build="""
apt-get update && apt-get install -y curl > /dev/null
    
curl -LsSf https://astral.sh/uv/install.sh | sh > /dev/null 2>&1
. $HOME/.cargo/env

uv venv > /dev/null 2>&1
. .venv/bin/activate > /dev/null 2>&1

if [ -f /tmp/requirements.txt ]; then
    uv pip install -r /tmp/requirements.txt > /dev/null 2>&1
fi
""",
    content="""
python /tmp/main.py "{{ .name }}"
""",
    with_files=[
        FileSpec(
            destination="/tmp/main.py",
            content=inspect.getsource(main),
        ),
        # Add any requirements here if needed
        # FileSpec(
        #     destination="/tmp/requirements.txt",
        #     content="",
        # ),
    ],
    secrets=["geff_test"]
)

tool_registry.register(create_knowledge_tool)
