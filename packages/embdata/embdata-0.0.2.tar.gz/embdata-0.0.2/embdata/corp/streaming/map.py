from datasets import load_dataset, Dataset
from itertools import chain


def update_large_dataset(dataset_name, new_data, batch_size=1000):
    # Stream the existing dataset
    streamed_dataset = load_dataset(dataset_name, streaming=True, split="train")

    # Prepare the new data
    new_dataset = Dataset.from_dict(new_data)

    # Function to yield batches from both datasets
    def data_generator():
        # First, yield all data from the existing dataset
        for batch in streamed_dataset.iter(batch_size=batch_size):
            yield batch

        # Then, yield all new data
        for batch in new_dataset.iter(batch_size=batch_size):
            yield batch

    # Create a new dataset from the combined data
    updated_dataset = Dataset.from_generator(data_generator)

    # Push the updated dataset to the Hub
    updated_dataset.push_to_hub(dataset_name, split="train")


# Usage
new_data = {...}  # Your new data in the same format as the existing dataset
update_large_dataset("your-username/your-dataset-name", new_data)
