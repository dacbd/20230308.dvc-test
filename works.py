import dvc.api

data = dvc.api.read(
    "my_data.txt",
    remote="normal",
    mode="r"
)

