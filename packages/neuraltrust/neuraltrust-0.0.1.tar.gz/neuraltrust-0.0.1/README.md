# NeuralTrust Python SDK

The NeuralTrust Python SDK provides a convenient way to interact with the NeuralTrust API. It allows you to manage conversations, send messages, and trace interactions asynchronously.

## Installation

To install the SDK, use pip:

```bash
pip install neuraltrust
```

## Usage

### Initialization

First, initialize the `NeuralTrust` client with your API key:

```python
from neuraltrust.client import NeuralTrust

client = NeuralTrust(api_key="your_api_key")
```

You can also set the `base_url`, `timeout`, and `max_workers` if needed:

```python
client = NeuralTrust(
    api_key="your_api_key",
    base_url="https://api.neuraltrust.ai/v1",
    timeout=30.0,
    max_workers=10
)
```

### Conversations

To start a new conversation:

```python
conversation = client.init_conversation()
```

### Messages

To initialize a message within a conversation:

```python
message = conversation.init_message()
```

### Sending Traces

You can send different types of traces (retrieval, generation, router) using the `Message` class:

```python
message.send_retrieval(input="input_text", output="output_text")
message.send_generation(input="input_text", output="output_text")
message.send_router(input="input_text", output="output_text")
```

### Full Example

Here is a full example of how to interact with the SDK:

```python
from neuraltrust import NeuralTrust
import datetime as dt

API_KEY = "your_api_key"
client = NeuralTrust(api_key=API_KEY)

# Initialize a conversation
conversation = client.init_conversation()

# Initialize a message within the conversation
message = conversation.init_message()

# Send different types of traces
message.send_generation("Hello, how are you?", "I'm good, thank you!")
message.send_retrieval("What is my name?", "My name is John Doe.")
message.send_router("What is my name?", "route")

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue on the [GitHub repository](https://github.com/yourusername/neuraltrust).

## Authors and Acknowledgments

- **Your Name** - Initial work

## Project Status

This project is actively maintained. Contributions and feedback are welcome.
