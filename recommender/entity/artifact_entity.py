from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    movies_file_path: str
    credits_file_path: str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_movies_file_path: str
