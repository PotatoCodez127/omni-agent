# test_tools.py
from core.tools import search_company_documents, search_org_chart

def test_document_tool():
    print("\n--- TESTING DOCUMENT TOOL ---")
    result = search_company_documents("Rust coding standards")
    print(f"Result:\n{result}")
    assert "eng_handbook_v2.pdf" in result, "Failed to retrieve Rust doc"
    print("✅ Document Tool Passed!")

def test_graph_tool():
    print("\n--- TESTING ORG CHART TOOL ---")
    result = search_org_chart("Rust")
    print(f"Result:\n{result}")
    assert "Sarah" in result, "Failed to traverse Graph to find Sarah"
    print("✅ Org Chart Tool Passed!")

if __name__ == "__main__":
    print("🚀 Running Tool Tests...")
    test_document_tool()
    test_graph_tool()
    print("\n==============================")