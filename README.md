# 🧠 AI Engineer Journey

My self-study path from .NET backend/fullstack developer to **AI Engineer**, starting Python from scratch.

## 📅 Schedule

- **Pace:** 3 hours a day, Monday to Friday (~15 h/week)
- **Saturday:** catch-up on anything that ran long (optional)
- **Sunday:** off
- **Duration:** Week 0 (setup) + 17 weeks
- **Start:** Thursday, Sep 24, 2026 (Week 0) → Week 1 starts Monday, Sep 28, 2026

### Daily structure (3 × ~1 hour chunks)

1. **Learn:** read docs, study the concept (compare it to .NET)
2. **Practice:** small exercises
3. **Build:** work on the week's project, then commit

### Every Friday: code review (last chunk)

- [ ] Type hints everywhere, ruff and mypy pass
- [ ] Tests cover the main paths
- [ ] Errors handled, nothing swallowed silently
- [ ] Logging where it matters
- [ ] Clean structure (no god files, clear layers)
- [ ] `NOTES.md` updated: what I learned, what broke

---

## 📊 Progress

| Week | Phase | Target start | Status |
|---|---|---|---|
| 0 | Setup | Sep 24 | ⬜ |
| 1 | Python fundamentals | Sep 28 | ⬜ |
| 2 | Writing real-world Python | Oct 5 | ⬜ |
| 3 | FastAPI | Oct 12 | ⬜ |
| 4 | Architecture and patterns in Python | Oct 19 | ⬜ |
| 5 | LLM fundamentals | Oct 26 | ⬜ |
| 6 | LLM APIs in depth | Nov 2 | ⬜ |
| 7 | RAG foundations | Nov 9 | ⬜ |
| 8 | RAG advanced | Nov 16 | ⬜ |
| 9 | Agents | Nov 23 | ⬜ |
| 10 | MCP | Nov 30 | ⬜ |
| 11 | Evals and observability | Dec 7 | ⬜ |
| 12 | Local models | Dec 14 | ⬜ |
| 13 | AWS core | Dec 21 | ⬜ |
| 14 | AI on AWS | Dec 28 | ⬜ |
| 15 | TypeScript and UI | Jan 4, 2027 | ⬜ |
| 16 | Capstone build | Jan 11, 2027 | ⬜ |
| 17 | Capstone ship | Jan 18, 2027 | ⬜ |

> Dates are targets, not deadlines. Shift them for holidays or when a phase needs more time. ⬜ Not started · 🟨 In progress · ✅ Done

---

## 🔁 .NET → Python cheat sheet

| .NET | Python |
|---|---|
| ASP.NET Core | FastAPI |
| EF Core + migrations | SQLAlchemy / SQLModel + Alembic |
| Built-in DI | FastAPI `Depends`, dependency-injector |
| Interfaces | `Protocol` / abstract base classes |
| appsettings + Options | pydantic-settings |
| xUnit + Moq | pytest + unittest.mock |
| LINQ | comprehensions, itertools |
| Serilog | structlog |
| Polly | tenacity |
| Hangfire / BackgroundService | Celery or arq |
| MediatR / CQRS | plain command/query handlers |
| NuGet | uv + PyPI |
| Roslyn analyzers | ruff + mypy |

---

## Week 0: Setup (Thu–Fri)

- [x] **Thursday**
  - Learn: install uv, then Python 3.12+ with `uv python install`; verify `python --version`
  - Practice: install VS Code (Python, Pylance, Ruff extensions) and Docker Desktop; run a Postgres container
  - Build: create the `ai-engineer-journey` GitHub repo, clone it, add the folder structure
- [ ] **Friday**
  - Learn: add this README to the repo; upload it to the Claude Project with the Project instructions
  - Practice: create Anthropic and OpenAI API accounts, add small credit, **set spending limits**
  - Build: write and run a Python "hello world" with uv, commit, push

> Leave the AWS account until Week 13 so free-tier time and credits aren't wasted.

---

## Phase 1: Python from scratch

### Week 1: Python fundamentals

- [ ] **D1:** Install check, run scripts → variables, types, strings, f-strings → write 5 tiny scripts
- [ ] **D2:** Lists, tuples, dicts, sets → loops and comprehensions → word-frequency counter
- [ ] **D3:** Functions, `*args` / `**kwargs` → modules and imports → split scripts into modules
- [ ] **D4:** Classes and dataclasses → exceptions (try/except) → model a small bank account
- [ ] **D5:** Files, JSON, pathlib → uv projects and virtual environments → **mini-project:** CLI to-do app saving to JSON

### Week 2: Writing real-world Python

- [ ] **D1:** Type hints → ruff and mypy → add types to the to-do app
- [ ] **D2:** Pydantic models → validation and errors → validate to-do data with Pydantic
- [ ] **D3:** pytest basics → fixtures → write tests for the to-do app
- [ ] **D4:** async/await → httpx → fetch from a public API concurrently
- [ ] **D5:** Decorators, generators, context managers → refactor your code → Friday review

### Week 3: FastAPI

- [ ] **D1:** First FastAPI app, routes, parameters → explore the auto docs → hello-world API
- [ ] **D2:** Request/response models → in-memory CRUD → turn the to-do app into an API
- [ ] **D3:** Postgres with SQLModel → migrations with Alembic → persist to-dos in Postgres
- [ ] **D4:** Dependency injection, error handling → tests with TestClient → test every endpoint
- [ ] **D5:** Dockerfile and docker compose (API + Postgres) → push to GitHub → Friday review

### Week 4: Architecture and patterns in Python

- [ ] **D1:** Pythonic style (PEP 8), `src` layout → config with pydantic-settings → restructure the to-do API
- [ ] **D2:** SOLID in Python, Protocols as interfaces → DI with `Depends` → put services behind Protocols
- [ ] **D3:** Clean/hexagonal architecture → repository and unit of work with SQLAlchemy → apply to the to-do API
- [ ] **D4:** Logging with structlog, retries with tenacity → background jobs with arq → add both to the API
- [ ] **D5:** CQRS-style handlers, domain events → testing strategy (unit vs integration) → Friday review

---

## Phase 2: LLM fundamentals and APIs

### Week 5: LLM fundamentals

- [ ] **D1:** How LLMs work: tokens, context window, temperature → tokenizer experiments → notes comparing models
- [ ] **D2:** Anthropic SDK first calls → OpenAI SDK first calls → same prompt on both, compare results
- [ ] **D3:** Prompting: system prompts, few-shot, structured prompts → iterate on prompts → prompt-testing script
- [ ] **D4:** Streaming responses → Server-Sent Events in FastAPI → streaming chat endpoint
- [ ] **D5:** Conversation history and context management → token counting → Friday review

### Week 6: LLM APIs in depth

- [ ] **D1:** Structured outputs with Pydantic → extraction exercises → extract data from text into models
- [ ] **D2:** Tool calling concepts → define tools with JSON schema → single-tool assistant
- [ ] **D3:** Multi-tool loop → error handling inside tools → **CLI assistant** with 2–3 tools
- [ ] **D4:** Cost, rate limits, retries, timeouts → provider abstraction with a Protocol → LLM client layer for both providers
- [ ] **D5:** Prompt caching and batching basics → finish the CLI assistant → Friday review

---

## Phase 3: RAG

### Week 7: RAG foundations

- [ ] **D1:** Embeddings and similarity → generate embeddings → compare sentence similarity
- [ ] **D2:** pgvector in Postgres → vector columns with SQLAlchemy → store embeddings
- [ ] **D3:** Chunking strategies → load documents (PDF, Markdown) → ingestion pipeline
- [ ] **D4:** Retrieval → building prompts with context → end-to-end Q&A
- [ ] **D5:** Citations and source tracking → handling "I don't know" → Friday review

### Week 8: RAG advanced

- [ ] **D1:** Hybrid search (Postgres full-text + vector) → reciprocal rank fusion → implement hybrid search
- [ ] **D2:** Reranking concepts → rerank models/APIs → add reranking
- [ ] **D3:** LlamaIndex basics → rebuild the pipeline → compare with your own version
- [ ] **D4:** Metadata filtering, incremental updates → query rewriting → add both
- [ ] **D5:** Clean architecture for a RAG service → refactor → Friday review

---

## Phase 4: Agents and MCP

### Week 9: Agents

- [ ] **D1:** Agent loop from scratch → ReAct pattern → hand-rolled agent, no framework
- [ ] **D2:** Memory and state → short-term vs long-term memory → add memory to your agent
- [ ] **D3:** LangGraph: nodes, edges, state → simple graphs → graph-based agent
- [ ] **D4:** LangGraph branching, checkpoints, human-in-the-loop → multi-step flows → multi-step agent
- [ ] **D5:** Claude Agent SDK or OpenAI Agents SDK → compare with LangGraph → Friday review

### Week 10: MCP (Model Context Protocol)

- [ ] **D1:** MCP concepts: servers, clients, tools, resources, prompts → explore existing servers → connect one to Claude Desktop
- [ ] **D2:** Python MCP SDK → build a server with 2 tools → test with MCP Inspector
- [ ] **D3:** Expose your RAG as an MCP tool → MCP resources → connect it to a client
- [ ] **D4:** Agent consuming your MCP server → auth and security basics → integrate everything
- [ ] **D5:** Guardrails and approval steps → security review → Friday review

---

## Phase 5: Production readiness

### Week 11: Evals and observability

- [ ] **D1:** Why evals, tracing concepts → Langfuse setup (Docker) → trace your RAG app
- [ ] **D2:** Building eval datasets → golden answers → dataset of 20+ questions
- [ ] **D3:** promptfoo or DeepEval → metrics (faithfulness, relevance) → automated eval run
- [ ] **D4:** LLM-as-judge → cost and latency tracking → metrics dashboard
- [ ] **D5:** Evals in GitHub Actions → regression gates → Friday review

### Week 12: Local models

- [ ] **D1:** Ollama → run open models (Llama, Qwen, Mistral) → call them from Python
- [ ] **D2:** Hugging Face Hub, transformers basics → local embeddings with sentence-transformers → swap embeddings in your RAG
- [ ] **D3:** vLLM and OpenAI-compatible APIs → serve a model (use Colab if no GPU) → point your app at it
- [ ] **D4:** Model selection: quality vs cost vs latency → run your evals across models → comparison table
- [ ] **D5:** Provider fallback and routing → Redis caching → Friday review

---

## Phase 6: AWS

### Week 13: AWS core

- [ ] **D1:** IAM, AWS CLI, boto3, **set budget alerts first** → S3 basics → upload/download files with boto3
- [ ] **D2:** Lambda + API Gateway → FastAPI on Lambda with Mangum → deploy one endpoint
- [ ] **D3:** RDS Postgres with pgvector, Secrets Manager → secure connections → move your RAG database to RDS
- [ ] **D4:** ECR + ECS Fargate → containerized deploys → deploy the full API
- [ ] **D5:** AWS CDK in Python → infrastructure as code → rebuild your deployment with CDK

### Week 14: AI on AWS

- [ ] **D1:** Bedrock and the Converse API → call Claude through Bedrock → swap providers in your app
- [ ] **D2:** Bedrock Knowledge Bases → managed RAG → compare with your own RAG
- [ ] **D3:** Bedrock AgentCore → managed agents → compare with your LangGraph agent
- [ ] **D4:** CloudWatch logs and metrics, X-Ray tracing → cost monitoring → instrument your deployed agent
- [ ] **D5:** Bedrock Guardrails, IAM least privilege → security review → Friday review

---

## Phase 7: UI and capstone

### Week 15: TypeScript and UI

- [ ] **D1:** TypeScript essentials → types, async, modules → small exercises
- [ ] **D2:** Next.js App Router basics → pages and API routes → app skeleton
- [ ] **D3:** Vercel AI SDK → `useChat` and streaming → chat UI
- [ ] **D4:** Connect the UI to your FastAPI agent → auth basics → working end-to-end app
- [ ] **D5:** Capstone design: scope, architecture diagram, AWS target → write the design doc → Friday review

### Week 16: Capstone build

- [ ] **D1:** Scaffold the repo and architecture layers → CDK skeleton → CI pipeline
- [ ] **D2:** Domain and data layer → RAG ingestion → tests
- [ ] **D3:** Agent → MCP tools → tests
- [ ] **D4:** API layer → streaming → tests
- [ ] **D5:** UI integration → end-to-end test → Friday review

### Week 17: Capstone ship

- [ ] **D1:** Evals for the capstone → tracing → fix the worst failures
- [ ] **D2:** Deploy to AWS with CDK → smoke tests → monitoring
- [ ] **D3:** Security review → cost review → fixes
- [ ] **D4:** Capstone README → architecture diagram → short demo video
- [ ] **D5:** Retrospective → update this README → plan next steps (PyTorch, LoRA fine-tuning)

---

## 📁 Repo structure

```
ai-engineer-journey/
├── README.md
├── 00-setup/
├── 01-python-fundamentals/
├── 02-real-world-python/
├── 03-fastapi/
├── 04-architecture/
├── 05-llm-fundamentals/
├── 06-llm-apis/
├── 07-rag-foundations/
├── 08-rag-advanced/
├── 09-agents/
├── 10-mcp/
├── 11-evals/
├── 12-local-models/
├── 13-aws-core/
├── 14-ai-on-aws/
├── 15-typescript-ui/
└── capstone/
```

Each week folder has its own `NOTES.md`: what I learned, what broke, what to revisit.

---

## 📚 Main resources

- Python tutorial: https://docs.python.org/3/tutorial/
- uv: https://docs.astral.sh/uv/
- FastAPI: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/
- SQLModel: https://sqlmodel.tiangolo.com/
- Anthropic docs: https://docs.anthropic.com/
- OpenAI docs: https://platform.openai.com/docs
- LangGraph: https://langchain-ai.github.io/langgraph/
- LlamaIndex: https://docs.llamaindex.ai/
- Model Context Protocol: https://modelcontextprotocol.io/
- Langfuse: https://langfuse.com/docs
- Ollama: https://ollama.com/
- AWS docs: https://docs.aws.amazon.com/
- Amazon Bedrock: https://docs.aws.amazon.com/bedrock/
- Next.js: https://nextjs.org/docs
- Vercel AI SDK: https://ai-sdk.dev/
