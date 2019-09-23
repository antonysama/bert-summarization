## Implementation of 'Pretraining-Based Natural Language Generation for Text Summarization'
### Versions
* python 2.7;PyTorch: 1.0.1.post2

### Preparing packages, dataset & running 
0. Run: pip2 install -r requirements.txt` (don't make a conda 2.7 env)
1. Downld subset of data from: https://github.com/JafferWilson/Process-Data-of-CNN-DailyMail (first time only )
2. Run: `python data.py` to create pickle files that will be used in my data-loader(first time only)
3. Use smaller parameters as following for debugging purpose. 
`CUDA_VISIBLE_DEVICES=3 python main.py --cuda --batch_size=2 --hop 4 --hidden_dim 100`

### Errors I couldn't fix:
. There are two data loaders: website and the related corpus of text. When I provide load data that is outside the dataset in the repo I get "collecttios must contain at least one sentance."

### Changes I made from original repo:
* In  main.py ln 17 and in  model/transformer.py ln 7, I changed 'utils.data' to 'data' since data was brought up to root. 
* In model/common_layer.py" ln 17, I added 'from pyrouge import Rouge155' since pyrouge is current. I added rouge==0.3.2 to requirements.txt. Installed pyrouge as above.

Paper: https://arxiv.org/pdf/1902.09243.pdf 
