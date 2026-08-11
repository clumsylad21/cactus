import sys

from cactus import (
    cactus_init,
    cactus_complete,
    cactus_destroy,
    cactus_reset,
    cactus_set_backend,
)

bundle = sys.argv[1]

cactus_set_backend("cpu")

prompts = [
    "What is 7 * 8? Answer with only the answer.",
    "What is 17 + 26? Answer with only the answer.",
    "Translate 'thank you' to French. Answer with only the translation.",
    "Alice has 12 apples and gives away 5. How many apples remain? Answer with only the answer.",
    "A train travels at 60 miles per hour for 3 hours. How far does it travel? Answer with only the answer.",
]

options = {
    "temperature": 0.0,
    "top_k": 1,
    "max_tokens": 128,
    "auto_handoff": False,
    "enable_thinking_if_supported": False,
}

print("BUNDLE:", bundle)

model = cactus_init(bundle, None, False)

if not model:
    raise RuntimeError("cactus_init failed")

try:
    for i, prompt in enumerate(prompts, 1):
        cactus_reset(model)

        result = cactus_complete(
            model,
            [{"role": "user", "content": prompt}],
            options,
            None,
            None,
        )

        print("\n" + "=" * 60)
        print("TEST", i)
        print("PROMPT:", prompt)
        print("SUCCESS:", result.get("success"))
        print("RESPONSE:", repr(result.get("response")))
        print("DECODE TOKENS:", result.get("decode_tokens"))
        print("DECODE TPS:", result.get("decode_tps"))

finally:
    cactus_destroy(model)
