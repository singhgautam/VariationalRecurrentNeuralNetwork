import torch
print torch.cuda.current_device()
print torch.cuda.device(0)
print torch.cuda.device_count()