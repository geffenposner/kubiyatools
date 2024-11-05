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
    
curl -LsSf https://astral.sh/uv/install.sh | sh > /dev/null
. $HOME/.cargo/env

uv venv > /dev/null 2>&1
. .venv/bin/activate > /dev/null

if [ -f /tmp/requirements.txt ]; then
    uv pip install -r /tmp/requirements.txt > /dev/null
fi
""",
    content="""
source .venv/bin/activate
python /tmp/main.py "{{ .name }}" "{{ .description }}" "{{ .tags }}" "{{ .content }}" "{{ .teammates_with_access }}" "{{ .user_groups_with_access }}"
""",
    with_files=[
        FileSpec(
            destination="/tmp/main.py",
            content=inspect.getsource(main),
        ),
        # Add any requirements here if needed
        FileSpec(
            destination="/tmp/requirements.txt",
            content="requests==2.32.3",
        ),
    ],
    secrets=["geff_test"]
)

tool_registry.register(create_knowledge_tool)
