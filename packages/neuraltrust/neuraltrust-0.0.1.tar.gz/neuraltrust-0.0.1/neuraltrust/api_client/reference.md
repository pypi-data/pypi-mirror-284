# Reference
<details><summary><code>client.<a href="src/NeuralTrust/client.py">trace</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new trace
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from NeuralTrust.client import NeuralTrustApi

client = NeuralTrustApi(
    api_key="YOUR_API_KEY",
)
client.trace()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Literal["traces"]]` — type of trace
    
</dd>
</dl>

<dl>
<dd>

**task:** `typing.Optional[TraceTask]` — task to perform
    
</dd>
</dl>

<dl>
<dd>

**interaction_id:** `typing.Optional[str]` — interaction id
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[str]` — content to retrieve or generate
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — generated content
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[str]` — conversation id
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `typing.Optional[str]` — message id
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `typing.Optional[dt.datetime]` — timestamp of the trace
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

