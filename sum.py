# 1. conda activate o
# 2. pip install tensorflow-gpu 

# Run A or B

#A
#python pointer-generator-master/run_summarization.py\
  --mode=decode --data_path=/path/to/your/finished_test_files/chunked/test_* 
  --vocab_path=vocab 
  --log_root=/path/to/pretrained_model 
  --exp_name=pretrained_model_ 
  --coverage=1 
  --single_pass=1 
  --max_enc_steps=500 
  --max_dec_steps=200 
  --min_dec_steps=100
  
#B  
# For expediency I reduced steps down by 1/50
#Before reduction they were: --max_enc_steps=400 --max_dec_steps=120...NEXT TIME reduce epoch size , too.
python run_summarization.py\
  --mode=train 
  --data_path=/home/antony/environments/n/cnn-dailymail/finished_files/chunked/val_* 
  --vocab_path=/home/antony/environments/n/cnn-dailymail/finished_files/vocab 
  --log_root=/home/antony/environments/n/cnn-dailymail/abstracter_model/ 
  --exp_name=abstracter_model 
  --max_enc_steps=8 
  --max_dec_steps=4 
  --coverage=1

# If you want to get the results of the pretrained models, set two arguments in the scripts:  
#    Set the MODE to evalall (i.e., MODE='evalall'). 
#   Set the CKPT_PATH to our pretrained model (e.g., CKPT_PATH="pretrained/bestmodel-xxxx").

