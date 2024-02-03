import os
import glob
from transformers import AutoTokenizer, AutoModel
import torch

# Load the pre-trained CodeBERT model and tokenizer
model_name = "microsoft/unixcoder-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = AutoModel.from_pretrained(model_name).to(torch.device(device))

# Specify the directory containing Python files


# Identify files starting with "pascal" prefix
files = glob.glob(os.path.join("SOR*.py"))

# Process each file and generate code embeddings
#data_to_save={}
torch.cuda.empty_cache()
batch_size = 500
file_batches = [files[i:i + batch_size] for i in range(0, len(files), batch_size)]
print("Total batches: ", len(file_batches))
for i, batch in enumerate(file_batches):
    data_to_save = {}
    for file_path in batch:
        with open(file_path, "r") as f:
            code = f.read()
        #print(file_path)
        # Encode the code using the tokenizer
        encoded_inputs = tokenizer(code, return_tensors="pt",padding=True, truncation=True, max_length=4)
        encoded_inputs = encoded_inputs.to(device)
        #print("Keys in encoded_inputs:", encoded_inputs.keys())
        #print("Encoded Inputs Size:", encoded_inputs['input_ids'].size())
        #print("Token Type IDs Size:", encoded_inputs['attention_mask'].size())
        # Pass the encoded inputs to the model
        outputs = model(**encoded_inputs)

        # Get the last hidden state, which represents the code embedding
        embedding = outputs.last_hidden_state[0]
        
        data_to_save[file_path] = embedding
    print("Total batches: ", len(file_batches), " Batch: ",i)
    try:
        torch.save(data_to_save, f'batch_{i}_embeddings.pt')
    except Exception as e:
        print(f"Error occurred while saving batch {i}: {e}")


    # Manually release memory
    del data_to_save
    torch.cuda.empty_cache()
"""torch.save(data_to_save, 'pascal_tensors.pt')
loaded_data = torch.load('pascal_tensors.pt')

print("size of pascal: ",len(loaded_data))
for key in loaded_data:
    print("shape of",key,": ",loaded_data[key].size())"""






