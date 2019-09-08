pip2 install -r requirements.txt  # plus a few others *
pip2 install torch torchvision --user
pip2 install pytorch-pretrained-bert --user
pip2 install python-utils --user

*
pip2 install\
    numpy \
    scipy \
    pandas \
pvlib==0.6.0 \
    cloudpickle \
pickleshare \
    scikit-learn==0.20.0 \
python-dateutil==2.7.5 \
    matplotlib \
PyMySQL==0.9.2 \
mkl-fft \
mkl-random \
windrose==1.6.5 \
    Cython \
tables==3.4.4 \
pyrouge==0.1.3 \

#In folder 'utils', running data.py gives error on line 29 'from config run utils'. Saying "no application named 
utils." Solve by bringing data.py to the root (i.e, n2 in this case) and run it from root. But, since 'from config...' 
looks forthe folder below root, if one modifies 'from config... ' and keep it inside the same folder it should work.
