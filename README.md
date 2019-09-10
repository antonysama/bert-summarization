## Implementation of 'Pretraining-Based Natural Language Generation for Text Summarization'

Paper: https://arxiv.org/pdf/1902.09243.pdf 

### Versions
* python 2.7
* PyTorch: 1.0.1.post2

### Preparing package/dataset
0. Run: `pip2 install -r requirements.txt` (and more_requirements.txt) to install required packages
1. Download chunk CNN/DailyMail data from: https://github.com/JafferWilson/Process-Data-of-CNN-DailyMail --done
2. Run: `python data.py` to create pickle file that will be used in my data-loader --done

### Running the model
Model is too big for my GPU, so I may use smaller parameters as following for debugging purpose. 
`CUDA_VISIBLE_DEVICES=3 python main.py --cuda --batch_size=2 --hop 4 --hidden_dim 100`

### Notes to reviewer:
* Installing 'requirements.txt' gives error #1. Any idea why ?

### Errors:
1. Could not find a version that satisfies the requirement mkl-fft==1.0.10 (from -r requirements.txt (line 23)) (from versions: 1.0.0.17, 1.0.2, 1.0.6) ... No matching distribution found for mkl-fft==1.0.10 (from -r requirements.txt (line 23)

### Changes made to original script:
* I cahnged 'utils.data' to 'data' in : main.py ln 17;  model/transformer.py ln 7. 
* In model/common_layer.py", ln 17 changed 'from rouge import Rouge' yo 'from pyrouge import Rouge155' 

