from typing import Type, Optional, Any

from crewai_tools import BaseTool

from pydantic import Field, BaseModel


class FixedFilesReadToolSchema(BaseModel):
    """Input for FileReadTool."""

    pass


class FilesReadToolSchema(FixedFilesReadToolSchema):
    """Input for FileReadTool."""

    file_paths: list[str] = Field(..., description="Mandatory file full paths to read the files")


class FilesReadTool(BaseTool):
    name: str = "Read files content"
    description: str = "A tool that can be used to read file_paths' contents."
    args_schema: Type[BaseModel] = FilesReadToolSchema
    file_paths: Optional[list[str]] = None

    def __init__(self, file_paths: Optional[list[str]] = None, **kwargs):
        super().__init__(**kwargs)
        if file_paths is not None:
            self.file_paths = file_paths
            self.description = "A tool that can be used to read file_paths' contents."
            self.args_schema = FixedFilesReadToolSchema
            self._generate_description()

    def _run(
            self,
            **kwargs: Any,
    ) -> Any:
        file_paths = self.file_paths or kwargs.get("file_paths", [])
        if not file_paths:
            return "No file paths provided."

        contents = []
        for file_path in file_paths:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    contents.append(file.name + "\n" + file.read())
            except Exception as e:
                return f"Failed to read the file {file_path}. Error: {e}"

        return "\n".join(contents)