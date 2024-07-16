import os
from wrapper import Client
import torch, time
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
print("Libraries imported successfully")

# BASE_URL = "http://vytalgazeapilb-884689726.us-east-1.elb.amazonaws.com/"
BASE_URL = "http://localhost:8000/"



if __name__ == "__main__":
    testVideo1 = "jay1.mp4"

    client = Client(base_url=BASE_URL)
    t0 = time.time()
    result = client.predict_from_video(video_path=testVideo1)
    print(result)
    print("Time taken for prediction: ", time.time()-t0)
    torch.save(result["left"], "resultlb.pt")
    torch.save(result["right"], "resultrb.pt")
    torch.save(result["le_3d"], "resultl3b.pt")
    torch.save(result["re_3d"], "resultr3b.pt")
    torch.save(result["hr"], "resulthrb.pt")

    
    
    
