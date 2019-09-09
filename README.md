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

### Note to reviewer:
* Although I implemented the core-part (2-step summary generation using BERT), I didn't have enough time to implement RL section. 
* The 2nd decoder process is very time-consuming (since it needs to create BERT context vector for each timestamp).
