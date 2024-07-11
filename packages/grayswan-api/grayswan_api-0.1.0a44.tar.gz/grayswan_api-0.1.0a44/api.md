# Chat

## Completion

Types:

```python
from gray_swan.types.chat import (
    ChatCompletionChoice,
    ChatCompletionDelta,
    ChatCompletionDeltaToolCall,
    ChatCompletionDeltaToolCallFunction,
    ChatCompletionMessage,
    ChatCompletionStreamChoice,
    ChatCompletionToolCall,
    ChatCompletionToolCallFunction,
    CreateChatCompletionResponse,
    CreateChatCompletionStreamResponse,
    CompletionCreateResponse,
)
```

Methods:

- <code title="post /chat/completion">client.chat.completion.<a href="./src/gray_swan/resources/chat/completion.py">create</a>(\*\*<a href="src/gray_swan/types/chat/completion_create_params.py">params</a>) -> <a href="./src/gray_swan/types/chat/completion_create_response.py">CompletionCreateResponse</a></code>

# Moderation

Types:

```python
from gray_swan.types import CreateModerationResponse
```

Methods:

- <code title="post /moderation">client.moderation.<a href="./src/gray_swan/resources/moderation.py">create</a>(\*\*<a href="src/gray_swan/types/moderation_create_params.py">params</a>) -> <a href="./src/gray_swan/types/create_moderation_response.py">CreateModerationResponse</a></code>
