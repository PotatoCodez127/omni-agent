# test_foundations.py
from core.schemas import AgentOutput, SuggestedContact
from database.graph_db import org_graph
from database.vector_db import vector_collection

def test_schemas():
    print("\n--- TESTING SCHEMAS ---")
    try:
        # Simulate a valid output from the LLM
        mock_output = AgentOutput(
            conversational_reply="Here is the info.",
            documents_cited=["handbook.pdf"],
            suggested_contacts=[SuggestedContact(name="Sarah", department="Backend", email="sarah@test.com")]
        )
        print("✅ Pydantic Schema Validation Passed!")
    except Exception as e:
        print(f"❌ Schema Validation Failed: {e}")

def test_graph_db():
    print("\n--- TESTING GRAPH DB ---")
    try:
        # Check if Sarah is in the graph and find her department
        if org_graph.has_node("Sarah"):
            edges = org_graph.edges("Sarah", data=True)
            connections = [f"{u} {data['relation']} {v}" for u, v, data in edges]
            print(f"✅ Graph DB Works! Sarah's connections: {connections}")
        else:
            print("❌ Graph DB Failed: Node not found.")
    except Exception as e:
        print(f"❌ Graph DB Error: {e}")

def test_vector_db():
    print("\n--- TESTING VECTOR DB ---")
    try:
        # Search for vacation policy
        results = vector_collection.query(
            query_texts=["How many vacation days do I get?"],
            n_results=1
        )
        document = results['documents'][0][0]
        print(f"✅ Vector DB Works! Found document: {document}")
    except Exception as e:
        print(f"❌ Vector DB Error: {e}")

if __name__ == "__main__":
    print("🚀 Running Foundation Tests...")
    test_schemas()
    test_graph_db()
    test_vector_db()
    print("\n==============================")