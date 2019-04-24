# DEDA

This repo contains all DEDA work. This repo is used to keep files safe in case of
a wild 'rm -rf' appears and to be able to tracking the progress.


## How to prepare the env.

- First Step: Install Anaconda

[Windows Version](https://www.anaconda.com/download/#windows "Anaconda for Windows").

[Linux Version](https://www.anaconda.com/download/#linux "Anaconda for Ubuntu").

- Second Step: Create a conda environment. After Anaconda installation is done. run the following command to create your Anaconda virtualenv named DEDA.

<pre><code> >> conda create -n DEDA python=3.6 anaconda </code></pre>

- Third Step: activate conda environment and install requirements.
<pre><code> >> conda activate DEDA
 >> pip install -r requirements.txt </code></pre>
 
 - Fourth Step: Run Notebook
 
 <pre><code> >> jupyter notebook </code></pre>
 
 ## Dataset directory.
 To be able to run notebook project, you need to put the datasets files that you want to analyse inside the datasets directory.
 
