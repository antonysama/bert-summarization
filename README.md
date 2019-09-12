## Implementation of 'Pretraining-Based Natural Language Generation for Text Summarization'
### Versions
* python 2.7;PyTorch: 1.0.1.post2

### Preparing packages, dataset & running 
0. Run: conda activate p27;`then run: pip install -r requirements.txt` 
1. Downld subset of data from: https://github.com/JafferWilson/Process-Data-of-CNN-DailyMail(first time only )
2. Run: `python data.py` to create pickle files that will be used in my data-loader(first time only)
3. Use smaller parameters as following for debugging purpose. 
`CUDA_VISIBLE_DEVICES=3 python main.py --cuda --batch_size=2 --hop 4 --hidden_dim 100`

### Errors I couldn't fix:
1. Rouge is not defined...No such file or directory: u'/home/.../.pyrouge/settings.ini' (see error_log above.)

2. Installing 'requirements.txt' gives error "Could not find a version that satisfies the requirement mkl-fft==1.0.10 (from -r requirements.txt (line 23)) (from versions: 1.0.0.17, 1.0.2, 1.0.6) ... No matching distribution found for mkl-fft==1.0.10 (from -r requirements.txt (line 23)"

### Changes I made from original repo:
* In  main.py ln 17 and in  model/transformer.py ln 7, I changed 'utils.data' to 'data' since data was brought up to root. 
* In model/common_layer.py" ln 17, I changed 'from rouge import Rouge' to 'from pyrouge import Rouge155' since pyrouge is current. Ln 578 from Rouge to Rouge 578.

Paper: https://arxiv.org/pdf/1902.09243.pdf 
