from dataclasses import dataclass
from pathlib import Path



@dataclass(frozen=True)
class DataLoaderConfig:
  data_path: Path
  file_types: str

@dataclass(frozen=True)
class SplitterConfig:
  chunk_size: int
  chunk_overlap: int

@dataclass(frozen=True)
class VectorizationConfig:
  model_name: str
  index_name: str
  namespace: str
  encoder_name: str
  encoder_platform: str
  num_of_documnets: int

@dataclass(frozen=True)
class ModelConfig:
    implementation: str
    model_path: Path
    model: str
    model_type: str
    n_gpu_layers: int
    n_batch: int
    n_ctx: int
    f16_kv: bool 
    temperature: int
    max_new_tokens: int