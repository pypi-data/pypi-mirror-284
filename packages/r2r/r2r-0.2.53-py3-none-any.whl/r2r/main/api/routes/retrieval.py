from fastapi.responses import StreamingResponse

from r2r.base import GenerationConfig, KGSearchSettings, VectorSearchSettings

from ...engine import R2REngine
from ..requests import R2REvalRequest, R2RRAGRequest, R2RSearchRequest
from .base_router import BaseRouter


class RetrievalRouter(BaseRouter):
    def __init__(self, engine: R2REngine):
        super().__init__(engine)
        self.setup_routes()

    def setup_routes(self):
        @self.router.post("/search")
        @self.base_endpoint
        async def search_app(request: R2RSearchRequest):
            if "agent_generation_config" in request.kg_search_settings:
                request.kg_search_settings["agent_generation_config"] = (
                    GenerationConfig(
                        **request.kg_search_settings["agent_generation_config"]
                    )
                )

            results = await self.engine.asearch(
                query=request.query,
                vector_search_settings=VectorSearchSettings(
                    **(request.vector_search_settings or {})
                ),
                kg_search_settings=KGSearchSettings(
                    **(request.kg_search_settings or {})
                ),
            )
            return results

        @self.router.post("/rag")
        @self.base_endpoint
        async def rag_app(request: R2RRAGRequest):
            if "agent_generation_config" in request.kg_search_settings:
                request.kg_search_settings["agent_generation_config"] = (
                    GenerationConfig(
                        **(
                            request.kg_search_settings[
                                "agent_generation_config"
                            ]
                            or {}
                        )
                    )
                )
            response = await self.engine.arag(
                query=request.query,
                vector_search_settings=VectorSearchSettings(
                    **(request.vector_search_settings or {})
                ),
                kg_search_settings=KGSearchSettings(
                    **(request.kg_search_settings or {})
                ),
                rag_generation_config=GenerationConfig(
                    **(request.rag_generation_config or {})
                ),
            )
            if (
                request.rag_generation_config
                and request.rag_generation_config.get("stream", False)
            ):

                async def stream_generator():
                    async for chunk in response:
                        yield chunk

                return StreamingResponse(
                    stream_generator(), media_type="application/json"
                )
            else:
                return response

        @self.router.post("/evaluate")
        @self.base_endpoint
        async def evaluate_app(request: R2REvalRequest):
            results = await self.engine.aevaluate(
                query=request.query,
                context=request.context,
                completion=request.completion,
            )
            return results


def create_retrieval_router(engine: R2REngine):
    return RetrievalRouter(engine).router
