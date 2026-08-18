# SPECS.md

Decisions on how the app should behave, written before building each feature.
Keep this updated as things change.

## Authentication

- Login: username + password.
- Register a user (via `manage_users.py`): name, email, username, password.
- Passwords are hashed. Never stored as plain text.
- Session dies after 10 min of no activity. User has to log in again.
- Same user can be logged in from more than one place at the same time. No blocking that.
- Wrong login shows a generic error. Don't say if the username exists or not.
- Logout button always visible in the sidebar.

## Reflection step (answer self-check)

- After the chain gives an answer, a second LLM call checks that answer against the context only.
- The check: is this answer really based on the retrieved context, or did it pull from general knowledge or from the chat history?
- If it's not backed by the context, replace the answer with "I don't know" (or fix it).
- If the check itself breaks (LLM error, bad output, etc.), just use the original answer. Reflection is a bonus, not something that should take down the whole response.
- This means 2 LLM calls per question instead of 1 — slower. Document this in the README.
- Plain LCEL, one pass. Not an agent loop, not iterative.

## Error handling

- Ollama down → show a plain message ("The assistant is currently unavailable. Make sure Ollama is running."), not a raw traceback.
- `data/` empty when running ingestion → stop and say so, don't just create an empty KB silently.
- Missing field in `config.yaml` → say exactly which field is missing, not a raw Pydantic error dump.
- Every caught error also gets logged to console, even if the UI shows a friendly message.

## Hybrid retrieval

- Combine semantic search (Chroma) + keyword search (BM25) with `EnsembleRetriever`.
- Default weights: 60% semantic, 40% keyword. Semantic for meaning, keyword to catch exact terms (names, codes) semantic search might miss.
- If one retriever comes back empty, still use whatever the other one found.