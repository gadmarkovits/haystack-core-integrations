# SPDX-FileCopyrightText: 2024-present deepset GmbH <info@deepset.ai>
#
# SPDX-License-Identifier: Apache-2.0
from typing import Any, Dict, List, Optional

from haystack import component, default_from_dict, default_to_dict

from ._opea_backend import OPEABackend
from .backend import GeneratorBackend

_DEFAULT_API_URL = "http://localhost:9000/v1"


@component
class OPEAGenerator:
    """
    A component for generating text using generative models provided by
    [OPEA](https://opea.dev).

    Usage example:
    ```python
    from haystack_integrations.components.generators.nvidia import OPEAGenerator

    generator = OPEAGenerator(
        model_arguments={
            "temperature": 0.2,
            "top_p": 0.7,
            "max_tokens": 1024,
        },
    )
    generator.warm_up()

    result = generator.run(prompt="What is the answer?")
    print(result["replies"])
    print(result["meta"])
    print(result["usage"])
    ```
    """

    def __init__(
        self,
        api_url: str = _DEFAULT_API_URL,
        model_arguments: Optional[Dict[str, Any]] = None,
    ):
        """
        Create a OPEAGenerator component.

        :param api_url:
            Custom API URL for the OPEA model.
        :param model_arguments:
            Additional arguments to pass to the model provider. Different models accept different arguments.
            Search your model in [OPEA](https://opea.dev)
            to know the supported arguments.
        """
        self._api_url = api_url
        self._model_arguments = model_arguments or {}

        self._backend: Optional[GeneratorBackend] = None

    def warm_up(self):
        """
        Initializes the component.
        """
        if self._backend is not None:
            return

        self._backend = OPEABackend(
            api_url=self._api_url,
            model_kwargs=self._model_arguments,
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Serializes the component to a dictionary.

        :returns:
            Dictionary with serialized data.
        """
        return default_to_dict(
            self,
            api_url=self._api_url,
            model_arguments=self._model_arguments,
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OPEAGenerator":
        """
        Deserializes the component from a dictionary.

        :param data:
            Dictionary to deserialize from.
        :returns:
           Deserialized component.
        """
        return default_from_dict(cls, data)

    @component.output_types(replies=List[str], meta=List[Dict[str, Any]])
    def run(self, prompt: str):
        """
        Queries the model with the provided prompt.

        :param prompt:
            Text to be sent to the generative model.
        :returns:
            A dictionary with the following keys:
            - `replies` - Replies generated by the model.
            - `meta` - Metadata for each reply.
        """
        if self._backend is None:
            msg = "The generation model has not been loaded. Call warm_up() before running."
            raise RuntimeError(msg)

        assert self._backend is not None
        replies, meta = self._backend.generate(prompt=prompt)

        return {"replies": replies, "meta": meta}
