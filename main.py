from fastapi import FastAPI, HTTPException
from core.agent import run_autonomous_agent
from core.guardrail import judge_response
from core.schemas import AgentOutput

app = FastAPI(title="Omni-Agent Enterprise Engine")

@app.post("/api/chat", response_model=AgentOutput)
async def chat_endpoint(user_prompt: str):
    
    # 1. & 2. & 3. Run the Agent (Handles Tool Calling, Vector RAG, and GraphRAG)
    # 4. Forces output to match the Pydantic AgentOutput schema
    draft_json_output = run_autonomous_agent(user_prompt) 
    
    # 5. Run the Guardrail Proxy
    is_safe, block_reason = judge_response(user_prompt, draft_json_output.conversational_reply)
    
    if not is_safe:
        # If the judge blocks it, return a safe override and log the breach
        print(f"SECURITY ALERT: {block_reason}")
        raise HTTPException(status_code=403, detail="Response blocked by company safety policies.")
        
    # If safe, return the structured JSON to the frontend
    return draft_json_output