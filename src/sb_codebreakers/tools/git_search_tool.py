from crewai_tools import tool
from langchain_community.document_loaders import GitLoader


@tool("Git Document Loader")
def my_git_loader_tool(repo_path: str, branch: str = "develop") -> str:
    """Loads documents from a Git repository and lists contents."""
    # Initialize GitLoader
    loader = GitLoader(
        repo_path=repo_path,
        branch=branch
    )

    # Load the documents
    documents = loader.load()

    # Create a list of document file names
    document_list = [doc.page_content for doc in documents]

    # Return formatted list of loaded documents
    joined_documents = "\n".join(document_list) if document_list else "No documents found."
    return f"Loaded Documents:\n{joined_documents}"