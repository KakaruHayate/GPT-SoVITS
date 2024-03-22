import torch
import torch_musa

ngpu = torch.musa.device_count()
print(ngpu)
if torch.musa.is_available():
    print("musa is available")
print(torch.musa.get_device_properties(0).total_memory)
print(torch.musa.get_device_name(0))
    
